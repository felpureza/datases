## pip install plotly==4.14.3

##### Pacotes externos #####
import plotly.graph_objects as go
import plotly
import plotly.graph_objs
from datetime import date

## Pacotes internos
from data import goias, goiania


### Figura
fig = go.Figure()

### Gráfico da média móvel simples de Goiás
fig.add_trace(go.Scatter(x=goias['notific'], y=goias['media'],
                    mode='lines',
                    name='Goiás',
                    line=dict(color='green', width=4)
                    )
)

### Gráfico da média móvel simples de Goiânia
fig.add_trace(go.Scatter(x=goiania['notific'], y=goiania['media'],
                    mode='lines',
                    name='Goiânia',
                    line=dict(color='purple', width=4)
                    )
)

### Título do gráfico
fig.update_layout(title='',
                   title_font=dict(size=30,
                                   color='black',
                                   family='Trebuchet MS')
)

### Título dos eixos
fig.update_layout(xaxis_title='Dias',
                  yaxis_title='Média de casos',
                  xaxis_title_font=dict(size=24,
                                        color='black',
                                        family='Trebuchet MS'),
                  yaxis_title_font=dict(size=24,
                                        color='black',
                                        family='Trebuchet MS')
)

### Linha do eixo x
fig.update_layout(xaxis=dict(showline=True,
                             showgrid=False,
                             showticklabels=True,
                             linecolor='black',
                             ticks='outside',
                             tickfont=dict(family='Trebuchet MS',
                                           size=16,
                                           color='black')
                             )
                  #xaxis_tickformat = '%-m/%Y'
)

### Linha do eixo y
fig.update_layout(yaxis=dict(showline=False,
                             showgrid=False,
                             showticklabels=False,
                             zeroline=False)
)

fig.update_yaxes(rangemode='tozero') ## A linha do eixo X fica na linha 0

### Legendas
fig.update_layout(legend=dict(yanchor='top',
                              xanchor='right',
                              font=dict(family='Trebuchet MS',
                                        size=16,
                                        color='black'))
)

### Layout do fundo do gráfico
fig.update_layout(plot_bgcolor='white'
)

### Plotando a partir de 01/04/2020
today = date.today()
fig.update_layout(xaxis_range=['2020-04-01',today])

### Gerando o gráfico de forma offline
plotly.offline.plot(fig)