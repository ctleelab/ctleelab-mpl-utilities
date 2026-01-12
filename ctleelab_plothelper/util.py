#
# ctleelab-mpl-utilities: A collection of utilities for plotting with matplotlib
#
# Copyright 2025- ctleelab
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Please help us support development by citing the research
# papers on the package. Check out https://github.com/ctleelab/ctleelab-mpl-utilities/
# for more information.

import numpy as np

import matplotlib as mpl
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.colorbar import Colorbar, ColorbarBase
from matplotlib.colors import BoundaryNorm, LinearSegmentedColormap, Colormap
from matplotlib.image import AxesImage
from matplotlib.backend_bases import RendererBase

import matplotlib.pyplot as plt
import matplotlib.cm as cm


from mpl_toolkits import axes_grid1
from mpl_toolkits.axes_grid1 import Divider, Size

from .dividers import FixedSizeDivider

from operator import sub

import datetime

import numpy.typing as npt
from typing import Tuple, Union


def get_renderer(fig: Figure) -> RendererBase:
    """Helper function to get the renderer depending on the context.

    Args:
        fig (Figure): Figure of interest

    Raises:
        AttributeError: If no renderer can be found for the current backend.

    Returns:
        RendererBase: Renderer instance
    """
    if hasattr(fig.canvas, "get_renderer"):
        return fig.canvas.get_renderer()
    elif hasattr(fig, "_get_renderer"):
        return fig._get_renderer()
    backend = mpl.get_backend()
    raise AttributeError(f"Could not find a renderer for the '{backend}' backend.")


def get_aspect(ax: Axes) -> float:
    """Get the aspect ratio of a particular axis.

    https://stackoverflow.com/questions/41597177/get-aspect-ratio-of-axes

    Args:
        ax (Axes): Axis of interest

    Returns:
        float: Aspect ratio of the figure
    """
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
