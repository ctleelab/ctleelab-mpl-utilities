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
# papers on the package. Check out https://github.com/ctleelab/automembrane/
# for more information.

import importlib.util

MPL_SPEC = importlib.util.find_spec("matplotlib")
MPL_FOUND = MPL_SPEC is not None

SNS_SPEC = importlib.util.find_spec("seaborn")
SNS_FOUND = SNS_SPEC is not None

if not MPL_FOUND:
    raise RuntimeError(f"Plotting requires Matplotlib")
if not SNS_FOUND:
    raise RuntimeError(f"Plotting requires Seaborn")

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import matplotlib.font_manager

import seaborn as sns

# print("Matplotlib Version:", mpl.__version__)

# plt.style.use("seaborn-v0_8-colorblind")  # set plot style
# mpl.rcParams["font.sans-serif"] = "Arial"
# mpl.rcParams["font.family"] = "sans-serif"

DARK_GREY = (0.1, 0.1, 0.1)
THINNER_LINE = 0.5
THIN_LINE = 0.7
NORMAL_LINE = 0.8

SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12
FIG_DPI = 300

plt.rc("font", size=SMALL_SIZE)  # controls default text sizes
plt.rc("axes", titlesize=BIGGER_SIZE)  # fontsize of the axes title
plt.rc("axes", labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
plt.rc("xtick", labelsize=MEDIUM_SIZE)  # fontsize of the tick labels
plt.rc("ytick", labelsize=MEDIUM_SIZE)  # fontsize of the tick labels
plt.rc("legend", fontsize=SMALL_SIZE)  # legend fontsize
plt.rc("figure", titlesize=BIGGER_SIZE)  # fontsize of the figure title
plt.rcParams["figure.figsize"] = [3, 3]  # Default 3x3
plt.rcParams["figure.dpi"] = FIG_DPI
plt.rcParams["savefig.dpi"] = FIG_DPI
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["axes.labelpad"] = 2.5
plt.rcParams["lines.markersize"] = 1

# Force TrueType fonts
plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["ps.fonttype"] = 42

LinearWhiteBlueColormap = mpl.colors.LinearSegmentedColormap.from_list(
    "LinearBlues", ["white", sns.color_palette()[0]], N=256
)
