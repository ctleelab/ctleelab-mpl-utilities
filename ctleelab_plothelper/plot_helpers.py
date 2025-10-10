def matplotlibStyle(small: float = 6, medium: float = 8, large: float = 10):
    """Set matplotlib plotting style

    Args:
        s (int, optional): Small size. Defaults to 6.
        m (int, optional): Medium size. Defaults to 8.
        l (int, optional): Large size. Defaults to 10.
    """
    plt.rcParams["font.sans-serif"] = "Arial"
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["lines.linewidth"] = 2
    plt.rcParams["savefig.dpi"] = 600
    # mpl.rcParams.update({'font.size': 8})
    plt.rc("font", size=large)  # controls default text sizes
    plt.rc("axes", titlesize=large)  # fontsize of the axes title
    plt.rc("axes", labelsize=medium)  # fontsize of the x and y labels
    plt.rc("xtick", labelsize=medium)  # fontsize of the tick labels
    plt.rc("ytick", labelsize=medium)  # fontsize of the tick labels
    plt.rc("legend", fontsize=small, frameon=False)  # legend fontsize
    plt.rc("figure", titlesize=large)  # fontsize of the figure title
    plt.rc("pdf", fonttype=42)


from mpl_toolkits import axes_grid1

from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset # InsetPosition, mark_inset


def add_colorbar(im, ax=None, aspect=20, pad_fraction=0.5, **kwargs):
    """Add a vertical color bar to an image plot."""
    if ax is None:
        ax = plt.gca()
    divider = axes_grid1.make_axes_locatable(im.axes)
    width = axes_grid1.axes_size.AxesY(im.axes, aspect=1.0 / aspect)
    pad = axes_grid1.axes_size.Fraction(pad_fraction, width)
    cax = divider.append_axes("right", size=width, pad=pad)
    plt.sca(ax)
    return im.axes.figure.colorbar(im, cax=cax, **kwargs)


from operator import sub


def get_aspect(ax):
    # Total figure size
    figW, figH = ax.get_figure().get_size_inches()
    # Axis size on figure
    _, _, w, h = ax.get_position().bounds
    # Ratio of display units
    disp_ratio = (figH * h) / (figW * w)
    # Ratio of data units
    # Negative over negative because of the order of subtraction
    data_ratio = sub(*ax.get_ylim()) / sub(*ax.get_xlim())

    return disp_ratio / data_ratio


def plot_errorbar(means, stds, c, label):

    plt.figure(figsize=(6, 4))
    #     plt.rc('font', size=20)
    #     plt.rc('xtick', labelsize=20)
    #     plt.rc('ytick', labelsize=20)

    color = c

    plt.plot(means.index, means, c=color)
    times_cur = means.index
    yminus = means - stds
    yplus = means + stds

    plt.fill_between(
        times_cur,
        np.asarray(yminus),
        np.asarray(yplus),
        alpha=0.25,
        edgecolor=color,
        facecolor=color,
        linewidth=1,
        antialiased=True,
    )

    plt.xlabel("Time (s)")
    plt.ylabel(label)

    plt.tick_params(reset=True, color="black", direction="in", length=4)
    plt.grid(False)

    plt.tight_layout()


#  to plot multiple
def plot_multiple_errorbars(means, stds, c, label):

    # You can call this multiple times to make several plots on top of each other.
    #     plt.figure(figsize=(6,4))
    #     plt.rc('font', size=20)
    #     plt.rc('xtick', labelsize=20)
    #     plt.rc('ytick', labelsize=20)

    color = c

    plt.plot(means.index, means, c=color)
    times_cur = means.index
    yminus = means - stds
    yplus = means + stds

    plt.fill_between(
        times_cur,
        np.asarray(yminus),
        np.asarray(yplus),
        alpha=0.25,
        edgecolor=color,
        facecolor=color,
        linewidth=1,
        antialiased=True,
    )

    plt.xlabel("Time (s)")
    plt.ylabel(label)

    plt.tick_params(reset=True, color="black", direction="in", length=4)
    plt.grid(False)


#     plt.tight_layout()
# auto_fit the plot dimensions using plot tight layout
def plot_multiple_errorbars_tight(means, stds, c, label):

    # You can call this multiple times to make several plots on top of each other.

    #     plt.figure(figsize=(6,4))
    #     plt.rc('font', size=20)
    #     plt.rc('xtick', labelsize=20)
    #     plt.rc('ytick', labelsize=20)

    color = c

    plt.plot(means.index, means, c=color)
    times_cur = means.index
    yminus = means - stds
    yplus = means + stds

    plt.fill_between(
        times_cur,
        np.asarray(yminus),
        np.asarray(yplus),
        alpha=0.25,
        edgecolor=color,
        facecolor=color,
        linewidth=1,
        antialiased=True,
    )

    plt.xlabel("Time (s)")
    plt.ylabel(label)

    plt.tick_params(reset=True, color="black", direction="in", length=4)
    plt.grid(False)

    plt.tight_layout()


def custom_cmap(size, label, ticklabels, cmap=cm.RdPu):
    """
    Function to define colormap
    """
    cmap = cm.RdPu  # define the colormap
    cmaplist = [cmap(i) for i in range(cmap.N)]
    cmap = mplt.colors.LinearSegmentedColormap.from_list(
        "Custom cmap", cmaplist, cmap.N
    )
    bounds = np.linspace(0, 1, size)
    norm = mplt.colors.BoundaryNorm(bounds, cmap.N)
    val = (float(bounds[1]) - float(bounds[0])) / 2
    ticks = np.linspace(val, 1 - val, size - 1)

    cax = fig.add_axes([0.92, 0.25, 0.02, 0.5])
    cb = mplt.colorbar.ColorbarBase(
        cax,
        cmap=cmap,
        norm=norm,
        spacing="proportional",
        ticks=ticks,
        boundaries=bounds,
        format="%1i",
        label=label,
    )
    cb.ax.set_yticklabels(ticklabels)  # vertically oriented colorbar


import datetime

now = datetime.datetime.now()
date = now.strftime("%Y%m%d")


def save_fig(fig, basename: str):
    fig.savefig(f"{basename}.png", format="png")
    fig.savefig(f"{basename}.pdf", format="pdf")
