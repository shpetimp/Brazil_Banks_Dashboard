import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input,Output,State,MATCH,ALL
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

text_font_size='1.8vh'
navbar_font_size='2vh'
header_font_size='2vh'
main_color='#80d4bd'

line_fig1=go.Figure()
line_fig2=go.Figure()
line_fig3=go.Figure()


line_div1=html.Div([
            dcc.Graph(id='line1', config={'displayModeBar': True, 'scrollZoom': True,'displaylogo': False},
                style=dict(height='40vh',backgroundColor='#20374c') ,figure=line_fig1
            ) ] ,id='bar_div1'
        )

line_div2=html.Div([
            dcc.Graph(id='line2', config={'displayModeBar': True, 'scrollZoom': True,'displaylogo': False},
                style=dict(height='40vh',backgroundColor='#20374c') ,figure=line_fig2
            ) ] ,id='bar_div2'
        )

line_div3=html.Div([
            dcc.Graph(id='line3', config={'displayModeBar': True, 'scrollZoom': True,'displaylogo': False},
                style=dict(height='40vh',backgroundColor='#20374c') ,figure=line_fig3
            ) ] ,id='bar_div3'
        )

def create_page2_layout(df):
    banks=list(df['bank_name'].unique() )

    banks_menu = dcc.Dropdown(className="custom-dropdown",
                             id='page2_banks_menu',

                             options=[{'label': bank, 'value': bank} for bank in banks]
                             ,
                             value=banks[0],
                             style=dict(color='#0f2537', fontWeight='bold', textAlign='center',
                                        width='18vh', backgroundColor='#0f2537',
                                        border='1px solid {}'.format(main_color))
                             )
    # display='inline-block',border='2px solid #082255'
    banks_text = html.Div(html.H1('Bank Name',
                                 style=dict(fontSize=text_font_size, fontWeight='bold', color='white',
                                            marginTop='')),
                         style=dict(display='inline-block', marginLeft='', textAlign="center", width='100%'))
    banks_menu_div = html.Div([banks_text, banks_menu],
                             style=dict(fontSize=text_font_size,
                                        marginLeft='', marginBottom='', display='inline-block'))

    resolution_menu = dcc.Dropdown(className="custom-dropdown",
                             id='page2_resolution_menu',

                             options=[dict(label='Yearly', value='1Y'),dict(label='Quarterly', value='3M'),
                                      dict(label='Monthly', value='1M'),dict(label='Weekly', value='1W'),
                                      dict(label='Daily', value='1D')
                                   ]

                             ,
                             value='3M',
                             style=dict(color='#0f2537', fontWeight='bold', textAlign='center',
                                        width='18vh', backgroundColor='#0f2537',
                                        border='1px solid {}'.format(main_color))
                             )
    # display='inline-block',border='2px solid #082255'
    resolution_text = html.Div(html.H1('Data Resolution',
                                 style=dict(fontSize=text_font_size, fontWeight='bold', color='white',
                                            marginTop='')),
                         style=dict(display='inline-block', marginLeft='', textAlign="center", width='100%'))
    resolution_menu_div = html.Div([resolution_text, resolution_menu],
                             style=dict(fontSize=text_font_size,
                                        marginLeft='2vh', marginBottom='', display='inline-block'))

    filters_text = html.Div(html.H1('Filters',
                                      style=dict(fontSize=header_font_size, fontWeight='bold', color='white',
                                                 marginTop='')),
                              style=dict(display='inline-block', marginLeft='', textAlign="center", width='100%'))



    layout = [dbc.Col([dbc.Card(dbc.CardBody([line_div1])
                                , style=dict(backgroundColor='#20374c')) , html.Br()
                       ], xl=dict(size=4, offset=0), lg=dict(size=4, offset=0),
                      md=dict(size=10, offset=1), sm=dict(size=10, offset=1), xs=dict(size=10, offset=1)),

              dbc.Col([dbc.Card(dbc.CardBody([line_div2])
                                , style=dict(backgroundColor='#20374c')) ,html.Br()
                       ], xl=dict(size=4, offset=0), lg=dict(size=4, offset=0),
                      md=dict(size=10, offset=1), sm=dict(size=10, offset=1), xs=dict(size=10, offset=1)) ,

              dbc.Col([dbc.Card(dbc.CardBody([line_div3])
                                , style=dict(backgroundColor='#20374c')) ,html.Br()
                       ], xl=dict(size=4, offset=0), lg=dict(size=4, offset=0),
                      md=dict(size=10, offset=1), sm=dict(size=10, offset=1), xs=dict(size=10, offset=1)) ,

              dbc.Col([dbc.Card(dbc.CardBody([filters_text   ,

                    html.Div([banks_menu_div,resolution_menu_div],

                             style={'width': '100%','display': 'flex',
                    'align-items': 'center','justify-content': 'center'})


              ])
                                , style=dict(backgroundColor='#20374c')), html.Br()
                       ], xl=dict(size=4, offset=4), lg=dict(size=4, offset=4),
                      md=dict(size=10, offset=1), sm=dict(size=10, offset=1), xs=dict(size=10, offset=1))


              ]

    return layout