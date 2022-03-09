from shiny import *
import matplotlib.pyplot as plt
import numpy as np

app_ui = ui.page_fluid(
    ui.row(
        ui.column(4, ui.input_slider("n", "N", 0, 100, 20)),
        ui.column(8, ui.output_plot("plot")),
    )
)


def server(input: Inputs, output: Outputs, session: Session):
    @output()
    @render_plot(alt="A histogram")
    def plot() -> object:
        np.random.seed(19680801)
        x = 100 + 15 * np.random.randn(437)

        fig, ax = plt.subplots()
        ax.hist(x, input.n(), density=True)
        return fig


app = App(app_ui, server)