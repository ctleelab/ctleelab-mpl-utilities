#
# ctleelab-mpl-utilities: A collection of utilities for plotting with matplotlib
#
# Copyright 2025- ctleelab
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Please help us support development by citing the research
# papers on the package. Check out https://github.com/ctleelab/ctleelab-mpl-utilities/
# for more information.

import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# import matplotlib.lines as mlines
# import matplotlib.patches as mpatches
# import matplotlib.transforms as mtransforms
# import matplotlib.font_manager

from mpl_toolkits import axes_grid1
from mpl_toolkits.axes_grid1 import Divider, Size

from .dividers import FixedSizeDivider

from operator import sub

import datetime

import numpy.typing as npt
from typing import Tuple


def fixed_size_subplots(
    nrows: int = 1,
    ncols: int = 1,
    wmargin: float = 0.7,
    hmargin: float = 0.7,
    colsep: float = 0,
    rowsep: float = 0,
    subheight: float = 2,
    subwidth: float = 2,
    rmargin_scale: float = 0.6,
    tmargin_scale: float = 0.6,
    **fig_kw,
) -> Tuple[plt.Figure, Tuple[mpl.axes.Axes, npt.NDArray[mpl.axes.Axes]]]:
    """Utility wrapper for creating a figure with subplots of specific axes sizes.

    All sizes are in inches. wmargin and hmargin are the width and height margins on the left and bottom sides.
    The right and top margins are `wmargin` and `hmargin` scaled by `rmargin_scale` and `tmargin_scale`, respectively.
    The spacing between subplots is given by `wmargin` and `hmargin` plus `rowsep` and `colsep`. For example, "| wmargin | subwidth | wmargin + colsep | subwidth | wmargin*rmargin_scale |"


    Args:
        nrows (int, optional): number of rows for subplot grid. Defaults to 1.
        ncols (int, optional): number of columns for subplot grid. Defaults to 1.
        wmargin (float, optional): size of width margins. Defaults to 0.7.
        hmargin (float, optional): size of height margins. Defaults to 0.7.
        colsep (float, optional): padding for column separation (width). Defaults to 0.
        rowsep (float, optional): padding for row separation (height). Defaults to 0.
        subheight (float, optional): subaxes height. Defaults to 2.
        subwidth (float, optional): subaxes width. Defaults to 2.
        rmargin_scale (float, optional): right margin scale factor. Defaults to 0.6.
        tmargin_scale (float, optional): top margin scale factor. Defaults to 0.6.
        **fig_kw: Additional keyword arguments passed to plt.figure()

    Returns:
        fig, axs (Tuple[plt.Figure, Tuple[mpl.axes.Axes, npt.NDArray[mpl.axes.Axes]]]):
        *axs* can be either a single `mpl.axes.Axes` object, or an array of Axes
        objects if more than one subplot was created.
    """
    width = ncols * (wmargin + colsep + subwidth) + wmargin * rmargin_scale
    height = nrows * (hmargin + rowsep + subheight) + hmargin * tmargin_scale

    axs = np.empty((nrows, ncols), dtype=object)

    fig = plt.figure(figsize=(width, height), **fig_kw)
    # renderer = get_renderer(fig)

    # Initialize vertical divider locations
    v = list()
    for i in range(1, nrows + 1):
        if i == 1:
            v.append(Size.Fixed(hmargin))
        else:
            v.append(Size.Fixed(hmargin + rowsep))
        v.append(Size.Fixed(subheight))

    # Initialize horizontal divider locations
    h = list()
    for i in range(1, ncols + 1):
        if i == 1:
            h.append(Size.Fixed(wmargin))
        else:
            h.append(Size.Fixed(wmargin + colsep))
        h.append(Size.Fixed(subwidth))

    divider = Divider(fig, (0, 0, 1, 1), h, v, aspect=False)

    for row in range(nrows):
        for col in range(ncols):
            axs[row, col] = fig.add_axes(
                divider.get_position(),
                axes_locator=divider.new_locator(nx=2 * col + 1, ny=2 * row + 1),
            )
    if axs.size == 1:
        return fig, axs[0, 0]
    return fig, np.squeeze(axs)


def get_renderer(fig):
    if hasattr(fig.canvas, "get_renderer"):
        return fig.canvas.get_renderer()
    elif hasattr(fig, "_get_renderer"):
        return fig._get_renderer()
    backend = matplotlib.get_backend()
    raise AttributeError(f"Could not find a renderer for the '{backend}' backend.")


def add_colorbar(
    im: mpl.image.AxesImage,
    ax: mpl.axes.Axes = None,
    aspect: float = 20,
    pad_fraction: float = 0.5,
    **kwargs,
) -> mpl.colorbar.Colorbar:
    """Add a vertical color bar to an image plot.

    Args:
        im (mpl.image.AxesImage): The image to which the colorbar applies.
        aspect (float, optional): Aspect width scaled to current axis. Defaults to 20.
        pad_fraction (float, optional): Padding spacing. Defaults to 0.5.

    Returns:
        -> mpl.colorbar.Colorbar: Colorbar instance
    """
    if ax is None:
        ax = plt.gca()
    divider = axes_grid1.make_axes_locatable(ax)
    width = axes_grid1.axes_size.AxesY(ax, aspect=1.0 / aspect)
    pad = axes_grid1.axes_size.Fraction(pad_fraction, width)
    cax = divider.append_axes("right", size=width, pad=pad)
    plt.sca(ax)
    return im.axes.figure.colorbar(im, cax=cax, **kwargs)


def add_fixed_colorbar(
    im: mpl.image.AxesImage,
    ax: mpl.axes.Axes = None,
    aspect: float = 20,
    pad: float = 0.05,
    **kwargs,
) -> mpl.colorbar.Colorbar:
    """Add a vertical color bar to an axes with fixed non-floating subplots.

    Args:
        im (mpl.image.AxesImage): The image to which the colorbar applies.
        ax (mpl.axes.Axes, optional): The axes to draw the colorbar by. Defaults to None.
        aspect (float, optional): Aspect width in inches. Defaults to 20.
        pad (float, optional): Padding spacing in inches. Defaults to 0.05.
        **kwargs: Additional keyword arguments passed to colorbar().

    Returns:
        mpl.colorbar.Colorbar: Colorbar instance

    """
    if ax is None:
        ax = plt.gca()

    divider = FixedSizeDivider(ax)
    divider.set_locator(ax.get_axes_locator())

    cax = ax.figure.add_axes(
        divider.get_position(),
        axes_locator=divider.new_right_locator(pad, aspect),
    )
    plt.sca(cax)

    # Hard-coded alternative which does not defer final placement until draw time.
    # renderer = get_renderer(fig)

    # divider = axes_grid1.axes_divider.AxesDivider(ax)
    # divider.set_locator(ax.get_axes_locator())

    # fig_w, fig_h = fig.bbox.size / fig.dpi

    # print(divider.get_position())
    # x0, y0, w, h = divider.get_position_runtime(ax, renderer)

    # x1, w1 = x0 + w + pad / fig_w, w / aspect
    # y1, h1 = y0, h

    # bbx = mtransforms.Bbox.from_bounds(x1, y1, w1, h1)
    # cax = fig.add_axes(bbx)
    return im.axes.figure.colorbar(im, cax=cax, **kwargs)


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


def custom_cmap(size, label, ticklabels, cmap=cm.RdPu):
    """
    Function to define colormap
    """
    cmap = cm.RdPu  # define the colormap
    cmaplist = [cmap(i) for i in range(cmap.N)]
    cmap = mpl.colors.LinearSegmentedColormap.from_list("Custom cmap", cmaplist, cmap.N)
    bounds = np.linspace(0, 1, size)
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    val = (float(bounds[1]) - float(bounds[0])) / 2
    ticks = np.linspace(val, 1 - val, size - 1)

    cax = fig.add_axes([0.92, 0.25, 0.02, 0.5])
    cb = mpl.colorbar.ColorbarBase(
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


now = datetime.datetime.now()
date = now.strftime("%Y%m%d")


def save_fig(fig, basename: str):
    fig.savefig(f"{basename}.png", format="png")
    fig.savefig(f"{basename}.svg", format="svg")
    fig.savefig(f"{basename}.pdf", format="pdf")
