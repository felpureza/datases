#Pacotes externos
import dash
import dash_core_components as dcc
import dash_html_components as html

## Pacotes internos
from plot import fig
from data import sum_go, sum_gyn

app = dash.Dash(__name__)

server = app.server
app.title = 'Covid-19 em Goiás'


app.layout = html.Div(
    children = [
    html.Div(className = 'app-header',
             children=[
                 html.H2("Média móvel de casos de Covid-19 em Goiás e em Goiânia",
                         className="app-title",
                         )
                 ]),

    html.Section([
            html.Div(
                id='linha1',
                children = [ 
                    html.Div(children = ['Casos em Goiás',
                                         html.Br(),
                                         sum_go],
                             id='sum_go',
                             className='box1'),
                    html.Div(children = ['Casos em Goiânia',
                                         html.Br(),
                                         sum_gyn],
                             id='sum_gyn',
                             className='box2'),            
                    ],
                className='box_org'
                ),
            html.Br(),
            html.Div(
                id='linha2',
                children = [
                    dcc.Graph(id='grafico', 
                              figure=fig),         
                    ],
                className='grafico'
                ),
    
    ])
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)



