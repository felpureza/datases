## pip install plotly==4.14.3

##### Pacotes externos #####
import plotly.graph_objects as go
import plotly
import plotly.graph_objs

## Pacotes internos
from data import goias, goiania
from data import sum_go, sum_gyn

fig = go.Figure()
fig.add_trace(go.Scatter(x=goias['notific'], y=goias['media'],
                    mode='lines',
                    name='Goiás',
                    line=dict(color='green', width=4)))

fig.add_trace(go.Scatter(x=goiania['notific'], y=goiania['media'],
                    mode='lines',
                    name='Goiânia',
                    line=dict(color='purple', width=4)))

fig.update_layout(title='',
                   xaxis_title='Dias',
                   yaxis_title='Média de casos',
                   title_font=dict(size=30, color='black'),
                   )

fig.update_layout(xaxis_title='Dias',
                  yaxis_title='Média de casos',
                  xaxis_title_font=dict(size=20, color='black'),
                  yaxis_title_font=dict(size=20, color='black')
                  )

fig.update_xaxes(showgrid=False,
                 tickfont=dict(size=15, color='black'),
                 zeroline=True, zerolinewidth=1, zerolinecolor = 'black'
                 )

fig.update_yaxes(showgrid=False,
                 tickfont=dict(size=15, color='black')
                 )


#plotly.offline.plot(fig)