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

bar_fig1=go.Figure()
bar_fig2=go.Figure()
bar_fig3=go.Figure()



map_fig=go.Figure(go.Choroplethmapbox())




bar_div1=html.Div([
            dcc.Graph(id='bar1', config={'displayModeBar': False, 'scrollZoom': True,'displaylogo': False},
                style=dict(height='40vh',backgroundColor='#20374c') ,figure=bar_fig1
            ) ] ,id='bar_div1'
        )

bar_div2=html.Div([
            dcc.Graph(id='bar2', config={'displayModeBar': False, 'scrollZoom': True,'displaylogo': False},
                style=dict(height='40vh',backgroundColor='#20374c') ,figure=bar_fig1
            ) ] ,id='bar_div2'
        )

bar_div3=html.Div([
            dcc.Graph(id='bar3', config={'displayModeBar': False, 'scrollZoom': True,'displaylogo': False},
                style=dict(height='40vh',backgroundColor='#20374c') ,figure=bar_fig1
            ) ] ,id='bar_div3'
        )

map_div=html.Div(id='map_div',style={'height':'','backgroundColor':'#20374c','width': '100%','display': 'flex', 'align-items': 'center','justify-content': 'center'} )



def create_page1_layout(df):
    cities=list(df['city_name'].unique() )
    cities.append('All Cities')
    states=list(df['state_id'].unique() )
    states.append('All States')
    products=list(df['product_name'].unique()   )
    products.append('All Products')
    programs=list(df['program_group'].unique()    )
    programs.append('All Programs')
    market_sectors=list(df['market_sector'].unique()      )
    market_sectors.append('All Sectors')
    customer_size=list(df['customer_size'].unique()       )
    customer_size.append('All Customers')

    city_menu = dcc.Dropdown(className="custom-dropdown",
                            id='page1_city_menu1',

                            options=[{'label': city, 'value': city} for city in cities]
                            ,
                            value=cities[-1],
                            style=dict(color='#0f2537', fontWeight='bold', textAlign='center',
                                       width='18vh', backgroundColor='#0f2537', border='1px solid {}'.format(main_color))
                            )
# display='inline-block',border='2px solid #082255'
    city_text = html.Div(html.H1('City',
                                style=dict(fontSize=text_font_size, fontWeight='bold', color='white',
                                           marginTop='')),
                        style=dict(display='inline-block', marginLeft='', textAlign="center", width='100%'))
    city_menu_div = html.Div([city_text, city_menu],
                            style=dict(fontSize=text_font_size,
                                       marginLeft='', marginBottom='', display='inline-block'))

    state_menu = dcc.Dropdown(className="custom-dropdown",
                             id='page1_state_menu1',

                             options=[{'label': state, 'value': state} for state in states]
                             ,
                             value=states[-1],
                             style=dict(color='#0f2537', fontWeight='bold', textAlign='center',
                                        width='18vh', backgroundColor='#0f2537',
                                        border='1px solid {}'.format(main_color))
                             )
    # display='inline-block',border='2px solid #082255'
    state_text = html.Div(html.H1('State ID',
                                 style=dict(fontSize=text_font_size, fontWeight='bold', color='white',
                                            marginTop='')),
                         style=dict(display='inline-block', marginLeft='', textAlign="center", width='100%'))
    state_menu_div = html.Div([state_text, state_menu],
                             style=dict(fontSize=text_font_size,
                                        marginLeft='2vh', marginBottom='', display='inline-block'))

    product_menu = dcc.Dropdown(className="custom-dropdown",
                             id='page1_product_menu1',

                             options=[{'label': product, 'value': product} for product in products]
                             ,
                             value=products[-1],
                             style=dict(color='#0f2537', fontWeight='bold', textAlign='center',
                                        width='18vh', backgroundColor='#0f2537',
                                        border='1px solid {}'.format(main_color))
                             )
    # display='inline-block',border='2px solid #082255'
    product_text = html.Div(html.H1('Product',
                                 style=dict(fontSize=text_font_size, fontWeight='bold', color='white',
                                            marginTop='')),
                         style=dict(display='inline-block', marginLeft='', textAlign="center", width='100%'))
    product_menu_div = html.Div([product_text, product_menu],
                             style=dict(fontSize=text_font_size,
                                        marginLeft='2vh', marginBottom='', display='inline-block'))

    program_menu = dcc.Dropdown(className="custom-dropdown",
                             id='page1_program_menu1',

                             options=[{'label': program, 'value': program} for program in programs]
                             ,
                             value=programs[-1],
                             style=dict(color='#0f2537', fontWeight='bold', textAlign='center',
                                        width='18vh', backgroundColor='#0f2537',
                                        border='1px solid {}'.format(main_color))
                             )
    # display='inline-block',border='2px solid #082255'
    program_text = html.Div(html.H1('Program',
                                 style=dict(fontSize=text_font_size, fontWeight='bold', color='white',
                                            marginTop='')),
                         style=dict(display='inline-block', marginLeft='', textAlign="center", width='100%'))
    program_menu_div = html.Div([program_text, program_menu],
                             style=dict(fontSize=text_font_size,
                                        marginLeft='2vh', marginBottom='', display='inline-block'))

    sector_menu = dcc.Dropdown(className="custom-dropdown",
                             id='page1_sector_menu1',

                             options=[{'label': sector, 'value': sector} for sector in market_sectors]
                             ,
                             value=market_sectors[-1],
                             style=dict(color='#0f2537', fontWeight='bold', textAlign='center',
                                        width='18vh', backgroundColor='#0f2537',
                                        border='1px solid {}'.format(main_color))
                             )
    # display='inline-block',border='2px solid #082255'
    sector_text = html.Div(html.H1('Market Sector',
                                 style=dict(fontSize=text_font_size, fontWeight='bold', color='white',
                                            marginTop='')),
                         style=dict(display='inline-block', marginLeft='', textAlign="center", width='100%'))
    sector_menu_div = html.Div([sector_text, sector_menu],
                             style=dict(fontSize=text_font_size,
                                        marginLeft='2vh', marginBottom='', display='inline-block'))

    customer_menu = dcc.Dropdown(className="custom-dropdown",
                             id='page1_customer_menu1',

                             options=[{'label': customer, 'value': customer} for customer in customer_size]
                             ,
                             value=customer_size[-1],
                             style=dict(color='#0f2537', fontWeight='bold', textAlign='center',
                                        width='18vh', backgroundColor='#0f2537',
                                        border='1px solid {}'.format(main_color))
                             )
    # display='inline-block',border='2px solid #082255'
    customer_text = html.Div(html.H1('Customer Size',
                                 style=dict(fontSize=text_font_size, fontWeight='bold', color='white',
                                            marginTop='')),
                         style=dict(display='inline-block', marginLeft='', textAlign="center", width='100%'))
    customer_menu_div = html.Div([customer_text, customer_menu],
                             style=dict(fontSize=text_font_size,
                                        marginLeft='2vh', marginBottom='', display='inline-block'))

    filters_text = html.Div(html.H1('Filters',
                                      style=dict(fontSize=header_font_size, fontWeight='bold', color='white',
                                                 marginTop='')),
                              style=dict(display='inline-block', marginLeft='', textAlign="center", width='100%'))

    filters_list = dbc.Checklist(
        inline=True,
        options=[{'label': 'Graph1', 'value': 'Graph1'},{'label': 'Graph2', 'value': 'Graph2'},{'label': 'Graph3', 'value': 'Graph3'} ]
        ,
        value=['Graph1'],
        id="filters_list", style=dict(fontSize='2vh', marginLeft='0', color='white'),
        input_checked_style={
            "backgroundColor": "{}".format(main_color),
          #  "borderColor": "#ea6258",
        }
    )

    filters_list_div=html.Div([filters_list],style={'width': '100%','display': 'flex',
                    'align-items': 'center','justify-content': 'center'} )

    refresh_map = html.Div([dbc.Button("Refresh Map", color="success", size='lg', n_clicks=0, id="refresh_map",outline=True
                                          , style=dict(fontSize=text_font_size)
                                          )],style={'width': '100%','display': 'flex','align-items': 'center','justify-content': 'center'})

    layout = [dbc.Col([dbc.Card(dbc.CardBody([bar_div1])
                                , style=dict(backgroundColor='#20374c')) , html.Br()
                       ], xl=dict(size=4, offset=0), lg=dict(size=4, offset=0),
                      md=dict(size=10, offset=1), sm=dict(size=10, offset=1), xs=dict(size=10, offset=1)),

              dbc.Col([dbc.Card(dbc.CardBody([bar_div2])
                                , style=dict(backgroundColor='#20374c')) ,html.Br()
                       ], xl=dict(size=4, offset=0), lg=dict(size=4, offset=0),
                      md=dict(size=10, offset=1), sm=dict(size=10, offset=1), xs=dict(size=10, offset=1)) ,

              dbc.Col([dbc.Card(dbc.CardBody([bar_div3])
                                , style=dict(backgroundColor='#20374c')) ,html.Br()
                       ], xl=dict(size=4, offset=0), lg=dict(size=4, offset=0),
                      md=dict(size=10, offset=1), sm=dict(size=10, offset=1), xs=dict(size=10, offset=1)) ,

              dbc.Col([dbc.Card(dbc.CardBody([filters_text   ,

                    html.Div([city_menu_div,state_menu_div,sector_menu_div,program_menu_div,product_menu_div,customer_menu_div],

                             style={'width': '100%','display': 'flex',
                    'align-items': 'center','justify-content': 'center'})

#flex
              ])
                                , style=dict(backgroundColor='#20374c')), html.Br()
                       ], xl=dict(size=10, offset=1), lg=dict(size=10, offset=1),
                      md=dict(size=10, offset=1), sm=dict(size=10, offset=1), xs=dict(size=10, offset=1)),

              dbc.Col([dbc.Card(dbc.CardBody([map_div,html.Br(),refresh_map])
                                , style=dict(backgroundColor='#20374c')), html.Br()
                       ], xl=dict(size=6, offset=3), lg=dict(size=6, offset=3),
                      md=dict(size=10, offset=1), sm=dict(size=10, offset=1), xs=dict(size=10, offset=1))


              ]

    return layout

