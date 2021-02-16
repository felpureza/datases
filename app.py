#Pacotes externos
import dash
import dash_core_components as dcc
import dash_html_components as html

## Pacotes internos
from plot import fig
from data import sum_go, sum_gyn

app = dash.Dash(__name__,
                meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)

server = app.server
app.title = 'Covid-19 em Goiás'


app.layout = html.H1(
    children = [
    html.Div(className = 'header__text',
             children=[
                 html.H2("Média móvel de casos da Covid-19 em Goiás e em Goiânia",
                         className="header__text",
                         style = {'textAlign': 'center'
                                  }
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
                             className='mini_container'),
                    html.Div(children = ['Casos em Goiânia',
                                         html.Br(),
                                         sum_gyn],
                             id='sum_gyn',
                             className='mini_container'),            
                    ],
                ),
            html.Br(),
            html.Div(
                id='linha2',
                children = [
                    dcc.Graph(id='grafico', 
                              figure=fig),         
                    ],
                ),
            html.Br(),
    
    ])
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)



