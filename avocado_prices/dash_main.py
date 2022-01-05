import dash
from dash import html
from dash import dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

path = "C:/Users/irfan/OneDrive/Desktop/MO TECH/avocado-updated-2020.csv" 
avo = pd.read_csv(path)

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Avocado Prices Dashboard'),
    dcc.Dropdown(id='geo-drop', options=[{'label':i, 'value': i}
                                         for i in avo['geography'].unique()],
                 value='New York'),
    dcc.Graph(id='Price-Graph')
])

@app.callback(
    Output(component_id='Price-Graph', component_property='figure'),
    Input(component_id='geo-drop', component_property='value')
)
def update_graph(selected_geography):
    filtered_avo = avo[avo['geography'] == selected_geography]
    line_fig= px.line(filtered_avo, x='date', y='average_price', color='type', title=f'Avocado Prices in {selected_geography}')
    return line_fig

if __name__ == '__main__':
    app.run_server(debug=True)
