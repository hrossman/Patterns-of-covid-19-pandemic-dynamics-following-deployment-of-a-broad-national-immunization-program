import os
import pandas as pd
from config import *


def load_national_vax_df(vax_data_dir=VAX_DATA_DIR, national_filename=VAX_NATIONAL_FILENAME):
    national_vax_df = pd.read_csv(os.path.join(vax_data_dir, national_filename), parse_dates=['VaccinationDate'])
    national_vax_df['first_dose'] = pd.to_numeric(national_vax_df['first_dose'], errors='coerce').fillna(0)
    national_vax_df['second_dose'] = pd.to_numeric(national_vax_df['second_dose'], errors='coerce').fillna(0)
    national_vax_df = national_vax_df.groupby(['VaccinationDate', 'age_group'], as_index=False).sum()
    cumulatives = national_vax_df.set_index(['VaccinationDate', 'age_group']).unstack('age_group').cumsum().stack().reset_index()
    national_vax_df = national_vax_df.merge(cumulatives.rename({'first_dose': 'cumulative_first_dose',
                                        'second_dose': 'cumulative_second_dose'}, axis=1), on=['VaccinationDate', 'age_group'])
    return national_vax_df.rename({'VaccinationDate': 'date'}, axis=1)


def get_pop_size(minimal_age=0):
    if minimal_age == 0:
        return pd.read_csv(os.path.join(DATA_DIR, 'pop_tot.csv'), index_col=[0])
    elif minimal_age == 16:
        return pd.read_csv(os.path.join(DATA_DIR, 'pop_tot_16+.csv'), index_col=[0])
    else:
        raise ValueError


def add_vax_perc(national_vax_df):
    national_vax_df['first_dose_perc'] = 100 * (national_vax_df['cumulative_first_dose'] / national_vax_df['pop_tot'])
    national_vax_df['second_dose_perc'] = 100 * (national_vax_df['cumulative_second_dose'] / national_vax_df['pop_tot'])
    return national_vax_df


def get_national_vax_df(minimal_age=0, regroup_dict=DEFAULT_REGROUP_DICT, vax_total_pop_file=True):
    assert (minimal_age in [0, 16])
    national_vax_df = load_national_vax_df()

    pop_tot = get_pop_size(minimal_age=minimal_age)
    national_vax_df = national_vax_df.merge(pop_tot['all'], on='age_group', how='outer').rename({'all': 'pop_tot'}, axis=1)

    national_vax_df['age_group'] = national_vax_df['age_group'].replace(regroup_dict)
    national_vax_df = national_vax_df.groupby(['date', 'age_group']).sum()

    national_vax_df = add_vax_perc(national_vax_df)

    return national_vax_df
