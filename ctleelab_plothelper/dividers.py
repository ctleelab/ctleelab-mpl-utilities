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


import matplotlib as mpl
import matplotlib.transforms as mtransforms
from mpl_toolkits.axes_grid1 import Size
from mpl_toolkits.axes_grid1.axes_divider import AxesDivider

import functools


class FixedSizeDivider(AxesDivider):
    """
    A custom AxesDivider that allows fixed size axes.

    This class extends the AxesDivider to support fixed size axes in inches.
    """

    def __init__(self, axes, xref=None, yref=None):
        super().__init__(axes, xref=xref, yref=yref)

    def new_right_locator(self, pad: float, aspect: float) -> callable:
        """Locate a new axes to the RHS of current axes with explicit padding and width given in aspect to main figure.

        Args:
            pad (_type_): _description_
            aspect (_type_): _description_

        Returns:
            _type_: _description_
        """
        locator = functools.partial(self._locate, pad, aspect)
        locator.get_subplotspec = self.get_subplotspec
        return locator

    def _locate(self, pad: float, aspect: float, axes, renderer):
        """
        Implementation of ``divider.new_locator().__call__``.

        The axes locator callable returned by ``new_locator()`` is created as
        a `functools.partial` of this method with *nx*, *ny*, *nx1*, and *ny1*
        specifying the requested cell.
        """
        fig_w, fig_h = self._fig.bbox.size / self._fig.dpi
        x0, y0, w, h = self.get_position_runtime(axes, renderer)

        x1, w1 = x0 + w + pad / fig_w, w / aspect
        y1, h1 = y0, h

        return mtransforms.Bbox.from_bounds(x1, y1, w1, h1)
