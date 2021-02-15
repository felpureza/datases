#Pacotes externos
import dash
import dash_core_components as dcc
import dash_html_components as html

## Pacotes internos
from plot import fig
from data import sum_go, sum_gyn


app = dash.Dash()

colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Média móvel de casos da Covid-19 em Goiás e em Goiânia',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    dcc.Graph(
        id='Graph1',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

