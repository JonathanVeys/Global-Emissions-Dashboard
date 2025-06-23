from dash import dcc, html, Input, Output, dash
import plotly.express as px
from utils.get_emissions_data import get_emissions_data

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Graph(
                id='world_emissions_graph',
            )
        ], className='world-map'),

        html.Div([
            dcc.Slider(
                id='slider',
                min=0,
                max=10,
                step=1,
                value=0
            )
        ], className='world-map')
    ], className='container-div'),

    html.Div([

    ], className='container-div')
], className='dashboard-container')


@app.callback(
    Output('world_emissions_graph', 'figure'),
    Input('slider', 'value')
)

def generate_emissions_map(value):
    emissions_data = get_emissions_data(2020)
    fig = px.choropleth(
        emissions_data,
        locations='iso_alpha',
        hover_name='country'
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)



