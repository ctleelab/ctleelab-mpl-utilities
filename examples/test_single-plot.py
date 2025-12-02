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

import ctleelab_plothelper.plothelpers as ph
import matplotlib.pyplot as plt
import numpy as np


def test_single_plot():
    plot_styles = [
        ("ctleelab_plothelper.light", ""),
        ("ctleelab_plothelper.dark", "_dark"),
    ]

    for i, (style, style_ext) in enumerate(plot_styles):

        # Style sheets can be combined with settings from the right-most having the highest priority.
        with plt.style.context(["ctleelab_plothelper.base", style]):

            fig, ax = ph.fixed_size_subplots(1, 1, subwidth=1.5, subheight=1.5)

            x = np.arange(-10, 10, 0.1)
            y = np.sin(x)

            ax.plot(x, y)
            ax.minorticks_on()
            ax.set_title("a basic plot")
            ax.set_xlabel("X Axis")
            ax.set_ylabel(r"Y Axis")

            fig.savefig(f"outputs/single-plot{style_ext}")
            # fig.savefig(f"outputs/single-plot{style_ext}.pdf", format="pdf")
    assert True


def test_transparent_background():
    plot_styles = [
        ("ctleelab_plothelper.light", ""),
        ("ctleelab_plothelper.dark", "_dark"),
    ]

    for i, (style, style_ext) in enumerate(plot_styles):

        # Style sheets can be combined with settings from the right-most having the highest priority.
        with plt.style.context(
            ["ctleelab_plothelper.base", style, "ctleelab_plothelper.transparent"]
        ):

            fig, ax = ph.fixed_size_subplots(1, 1, subwidth=1.5, subheight=1.5)

            x = np.arange(-10, 10, 0.1)
            y = np.sin(x)

            ax.plot(x, y)
            ax.minorticks_on()
            ax.set_title("This plot has a transparent background")
            ax.set_xlabel("X Axis")
            ax.set_ylabel("Y Axis")

            fig.savefig(f"outputs/transparent-plot{style_ext}")
            # fig.savefig(f"outputs/transparent-plot{style_ext}.pdf", format="pdf")
    assert True


def test_1x3():
    with plt.style.context(
        [
            "ctleelab_plothelper.base",
            "ctleelab_plothelper.light",
        ]
    ):

        fig, axs = ph.fixed_size_subplots(1, 3, subwidth=1.5, subheight=1.5)

        for i, ax in enumerate(axs):
            j = i + 1
            x = np.arange(-10 * j, 10 * j, 1)
            y = np.sin(x)

            ax.plot(x, y)
            ax.minorticks_on()
            ax.set_title("Plots of the same size")
            ax.set_xlabel("X Axis")
            ax.set_ylabel("Y Axis")

        fig.savefig(f"outputs/1x3-plot")
        # fig.savefig(f"outputs/transparent-plot{style_ext}.pdf", format="pdf")
    assert True


def test_colorbar():
    with plt.style.context(
        [
            "ctleelab_plothelper.base",
            "ctleelab_plothelper.light",
        ]
    ):

        fig, axs = ph.fixed_size_subplots(2, 2, subwidth=1.5, subheight=1.5)

        ax = axs[0, 0]
        x = np.arange(-10, 10, 1)
        y = np.sin(x)

        ax.plot(x, y)
        ax.minorticks_on()
        ax.set_title("Plots of the same size")
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")

        ax = axs[0, 1]
        r = np.random.random((100, 100))
        im = ax.imshow(r, cmap="viridis")
        ph.add_fixed_colorbar(im, ax=ax, aspect=20, pad=0.05)

        ax = axs[1, 0]

        x = np.arange(-1, 1, 0.01)
        y = np.arange(-1, 1, 0.01)

        xx, yy = np.meshgrid(x, y)

        r = np.sin(10 * (xx**2 + yy**2)) / 10

        im = ax.imshow(r, cmap="PRGn")
        ph.add_fixed_colorbar(im, ax=ax, aspect=30, pad=0.02)

        fig.savefig(f"outputs/fixed-size-colorbar")
        # fig.savefig(f"outputs/transparent-plot{style_ext}.pdf", format="pdf")
    assert True
