import plotly.graph_objects as go


def set_max_layout(date, values):
    return go.layout.Shape(
        type="line",
        x0=date,
        y0=values[1],
        x1=date,
        y1=values[2],
        line=dict(color="Red"),
        line_dash="dot",
        line_width=1,
    )


def set_min_layout(date, values):
    return go.layout.Shape(
        type="line",
        x0=date,
        y0=values[1],
        x1=date,
        y1=values[0],
        line=dict(color="Green"),
        line_dash="dot",
        line_width=1,
    )


def generate_chart(
    data: dict, origin: str, destination: str, export_html_file: str = None
) -> None:
    """Generates a Plotly time series chart.

    The chart is displayed in the web browser
    and can be optionally saved to an html file.
    """

    # prepare data and plotly shapes
    max_value_shapes = [
        set_max_layout(date, values) for date, values in data.items()
    ]
    min_value_shapes = [
        set_min_layout(date, values) for date, values in data.items()
    ]
    shapes = [*max_value_shapes, *min_value_shapes]
    data_values = [val for val in zip(*data.values())]

    # add min values
    fig = go.Figure()
    fig.update_layout(shapes=shapes)
    fig.add_trace(
        go.Scatter(
            x=tuple(data.keys()),
            y=data_values[0],
            mode="markers",
            name="min",
            line=dict(color="Green"),
        )
    )
    # add max values
    fig.add_trace(
        go.Scatter(
            x=tuple(data.keys()),
            y=data_values[2],
            mode="markers",
            name="max",
            line=dict(color="Red"),
        )
    )
    # add median values
    fig.add_trace(
        go.Scatter(
            x=tuple(data.keys()),
            y=data_values[1],
            mode="lines+markers",
            name="median",
            line=dict(color="White", width=4, shape="spline"),
            marker=dict(line_width=1, color="#bfc1c2"),
        )
    )

    # style layout
    fig.update_layout(
        title=f"{origin} ✈ {destination} Ryanair flight fares (in the currency of the origin country)",
        yaxis_tickprefix="",
        yaxis_ticksuffix=" ",
        yaxis_tickformat=",.",
    )
    fig.update_xaxes(rangeslider_visible=True, griddash="dot", gridwidth=1)
    fig.update_yaxes(griddash="dot", gridwidth=1)

    # export to html file
    if export_html_file:
        try:
            fig.write_html(export_html_file)
        except FileNotFoundError as e:
            print(e)

    fig.show()
