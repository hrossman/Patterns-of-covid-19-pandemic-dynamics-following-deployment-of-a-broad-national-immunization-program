import os

ROOT_DIR = os.path.join(os.path.dirname(__file__))
DATA_DIR = os.path.join(ROOT_DIR, 'data')

VAX_NATIONAL_FILENAME = 'vaccinated-per-day.csv'
VAX_DATA_DIR = DATA_DIR

VAX_BINS = [0, 19, 29, 39, 49, 59, 69, 79, 89, 150]
VAX_LABELS = ['0-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90+']
DEFAULT_REGROUP_DICT = dict(zip(VAX_LABELS, VAX_LABELS))