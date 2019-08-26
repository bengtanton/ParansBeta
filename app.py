import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import matplotlib.pyplot as plotter ## added this line to test Pandas

########### Get Data

#pd.read_csv('X&Y.csv')                        #this was the original on this line  df_test = pd.read_csv('testspektra.csv')

serieA = pd.Series([1,2,3,4,5,7,8])
'''

########### Set up the chart


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


########### Display the chart

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div(children=[
    html.H1('Header'),



    html.Label('Choose Lightsource'),

    dcc.Dropdown(
        id='droplista',
        options=[
            {'label': 'Unfiltered daylight', 'value': 'Unfiltered Daylight'},
            {'label': u'Daylight through Parans 50m', 'value': 'Parans 50 m'},
            {'label': 'Daylight through 2-pane thermal glass', 'value': 'Thermal Glass'},
            {'label': 'Daylight through 2-pane solar protection glass', 'value': 'Solar Protection Glass'},
            {'label': 'Cool white LED', 'value': 'Cool White LED'},
            {'label': 'Warm white LED', 'value': 'Warm White LED'}
        ],
        value=['Unfiltered Daylight'],
        multi=True
    ),

    html.Div(id='my-div'),


    dcc.Graph(
        id='spektra'
    ),



]
)

########### Callbacks!

@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='droplista', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)


@app.callback(
    dash.dependencies.Output('spektra', 'figure'),
    [dash.dependencies.Input('droplista', 'value')])
def update_graph(valda_serier):

    cols=valda_serier.copy()
    cols.extend(['Wavelength_nm'])
    df_vald = df_test[cols]

    trace=[]

    for serie in valda_serier:
        trace=trace+[go.Scatter(
            x=df_vald['Wavelength_nm'],
            y=df_vald[serie],
            mode='lines',
            name=serie
        )]

    trace_text=go.Scatter(
    x=[550],
    y=[-0.15],
    text=['Visible spectra'],
    mode='text',
    showlegend=False
    )

    trace.extend([trace_text])

    return {
        'data': trace,


        'layout': go.Layout(
            title="Daylight specrum through filters",
            xaxis={'title': 'Frequency [nm]'},
            yaxis={'title': 'Relative energy intensity [%]'},
            showlegend=True,
            shapes=[dict(type='rect',
                    layer='below',
                    xref='x',
                    yref='paper',
                    x0=380,
                    y0=0,
                    x1=740,
                    y1=1,
                    opacity=0.3,
                    fillcolor='#d3d3d3',
                    line=dict(width=0)
                )]


        )
    }


########### Run app!


if __name__ == '__main__':
    app.run_server()
'''
