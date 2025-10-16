import ctleelab_plothelper.plothelpers as ph

import matplotlib
import matplotlib.pyplot as plt

import numpy as np

from mpl_toolkits import axes_grid1


def label_axes(ax, text):
    """Place a label at the center of an Axes, and remove the axis ticks."""
    ax.text(
        0.5,
        0.5,
        text,
        transform=ax.transAxes,
        horizontalalignment="center",
        verticalalignment="center",
    )
    ax.tick_params(bottom=False, labelbottom=False, left=False, labelleft=False)


print(matplotlib.__version__)

# Options for backend: ['gtk3agg', 'gtk3cairo', 'gtk4agg', 'gtk4cairo', 'macosx', 'nbagg', 'notebook', 'qtagg', 'qtcairo', 'qt5agg', 'qt5cairo', 'tkagg', 'tkcairo', 'webagg', 'wx', 'wxagg', 'wxcairo', 'agg', 'cairo', 'pdf', 'pgf', 'ps', 'svg', 'template']
# matplotlib.use("svg")

plot_styles = [
    ("ctleelab_plothelper.light", ""),
    ("ctleelab_plothelper.dark", "_dark"),
]

for i, (style, style_ext) in enumerate(plot_styles):

    # Style sheets can be combined with settings from the right-most having the highest priority.
    with plt.style.context(
        ["ctleelab_plothelper.base", style, "ctleelab_plothelper.transparent"]
    ):

        fig, axs = ph.fixed_size_subplots(3, 3, subwidth=1.5, subheight=1.5)

        x = np.arange(-100, 100)
        y = np.sin(x)

        ax = axs[0, 0]

        ax.plot(x, y)
        ax.minorticks_on()
        ax.set_title("Demo Plot")
        ax.set_xlabel("X Axis")
        ax.set_ylabel(r"Y Axis γ")

        r = np.random.random((100, 100))

        ax = axs[0, 2]
        im = ax.imshow(r, cmap="viridis")
        ph.add_fixed_colorbar(im, aspect=20, pad=0.05)

        fig.savefig(f"demo{style_ext}")
        fig.savefig(f"demo{style_ext}.svg", format="svg")
        fig.savefig(f"demo{style_ext}.pdf", format="pdf")

        # Uncomment to test font sizes

        # t = ax.text(0.5, 0.5, "Text")

        # fonts = ['xx-small', 'x-small', 'small', 'medium', 'large',
        #         'x-large', 'xx-large', 'larger', 'smaller']

        # for font in fonts:
        #     t.set_fontsize(font)
        #     print (font, round(t.get_fontsize(), 2))
