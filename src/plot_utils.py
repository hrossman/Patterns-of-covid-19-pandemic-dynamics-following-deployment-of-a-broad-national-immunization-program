import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def _prettify_ax(ax, x, legend=True, loc='lower right', every_x_axis_ticks=7):
    ax.set_xticks(x[::-every_x_axis_ticks])
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=70, fontsize=12)
#     sns.despine()
    if legend:
        ax.legend(fontsize=15, frameon=True, loc=loc, facecolor='white', edgecolor='white', framealpha=0.8)
    ax.grid()


def add_panel_text(ax,text, SZ=16):
    ax.text(-0.1, 1.15, text, transform=ax.transAxes,
            fontsize=SZ+4, fontweight='bold', va='top', ha='right')

