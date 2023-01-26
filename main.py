# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input,Output,State,MATCH,ALL
import pandas as pd
import dash_table
import pickle as pkl
import os
from sqlalchemy.types import String
import base64
import plotly.express as px
import plotly.graph_objects as go
from string import digits
import json
from flask import Flask
import math
import page1
import page2
import numpy as np
import json




with open('brazil_geo.json') as f:
    data = json.load(f)
ids=[]
for feature in data['features']:
   # print(feature['id'])
    ids.append(feature['id'])

#print(data['features'][0].keys())
#print(ids)


df=pd.read_csv('banks_data2.csv')
df=df[['id','operation_date','customer_id','customer_size','category_bank','bank_id','bank_name','operation_value','product_name','program_group','market_sector','city_name','city_id','state_id','lack_pyment_deadline','payment_deadline','internal_spread','bank_spread','total_spread']]
df=df.dropna()
df['operation_date']=pd.to_datetime(df['operation_date'],format="%Y-%m-%d")
df['state_id']=df['state_id'].apply(lambda x:x.strip())
df['city_name']=df['city_name'].apply(lambda x:x.strip())

#print(df['state_id'].unique())


#lat=14.2350,  lon=51.9253
#figg.show()










#df.set_index('operation_date', inplace=True)
#graph_data=df[df['bank_name']=='SICREDI']
#graph_data = graph_data['customer_id'].resample('1Y').nunique()
#test=df.groupby("bank_name")['customer_id'].nunique()
#print(graph_data)




#print(df.isnull().sum().sum())
#print(df.shape[0])

#print(bank_df['Operations_Ranges'].value_counts())

######## ranges function
#max_op=int(df['operation_value'].max() )
#min_op=int(df['operation_value'].min() )
#range1=int(max_op/4)
#range2=int(range1*2)
#range3=int(range1*3)
#range4=int(range1*4)
#op_ranges=[min_op,range1,range2,range3,max_op]
#op_labels=['{}-{}'.format(min_op,range1),'{}-{}'.format(range1,range2),'{}-{}'.format(range2,range3),'{}-{}'.format(range3,max_op)]
#df['Operations_Ranges']=pd.cut(df['operation_value'],bins=op_ranges,labels=op_labels)
##################


#print(df.info())
#print(df['operation_value'].max(),df['operation_value'].min())

#df=df['ide;"data_aprovacao";"cliente_cnpj_cpf";"cliente_nome";"cliente_porte_enquadramento";"cliente_tipo_pf_pj";"cliente_natureza_juridica_bndes";"agente_financeiro_categoria";"agente_financeiro_categoria_top5sfn";"agente_financeiro_cnpj";"agente_financeiro_nome_tratado";"produto_nome";"programa_agrupado";"programa_agrupado_alocacao";"investimento_setor_bndes";"investimento_cnae_genero";"investimento_municipio_nome";"ibge";"investimento_uf_sigla";"investimento_regiao_nome";"custo_financeiro_nome";"via_entrada";"valor_operacao";"prazo_carencia";"prazo_amortizacao";"taxa_remuneracao_bndes";"taxa_remuneracao_agente";"taxa_remuneracao_total";"percentual_participacao_bndes"'].str.split(';', expand=True)
#new_df=pd.DataFrame()
#new_df[['id','operation_date','customer_id','customer_name','customer_size','customer_natural_juridical','customer_type','category_bank','category_bank_top5','bank_id','bank_name','product_name','program_group','program_group_2','market_sector','oficial_market','city_name','city_id','state_id','region_name','rate_type','system','operation_value','lack_pyment_deadline','payment_deadline','internal_spread','bank_spread','total_spread','percentual_internal','none']]=df
#print(new_df.head())
#new_df.to_csv('banks_data.csv')

text_font_size='2vh'
navbar_font_size='2vh'
header_font_size='2vh'
main_color='#80d4bd'

#grpby_operations=df.groupby(['id','bank_name']).count().reset_index()
#print(grpby_operations.columns)
#print(grpby_operations['bank_name'].value_counts()[0:10])
#top_operations=df['bank_name'].value_counts()[0:10]
#print(top_operations)

server = Flask(__name__)
app = dash.Dash(
    __name__,server=server,
    meta_tags=[
        {
            'charset': 'utf-8',
        },
        {
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1, shrink-to-fit=no'
        }
    ] ,
)
#external_stylesheets=[dbc.themes.BOOTSTRAP]
app.config.suppress_callback_exceptions = True
encoded = base64.b64encode(open('plotly2.png', 'rb').read())

logo_img=html.Img(src='data:image/jpg;base64,{}'.format(encoded.decode()), id='logo_img', height='70vh',
                  style=dict(marginLeft='1vh'))

db_logo_img=dbc.Col([ logo_img] ,
        xs=dict(size=2,offset=0), sm=dict(size=2,offset=0),
        md=dict(size=1,offset=0), lg=dict(size=1,offset=0), xl=dict(size=1,offset=0))

header_text=html.Div('Banks Performance Analysis Dashboard',style=dict(color='white',
                     fontWeight='bold',fontSize='2.8vh',marginTop='1vh',marginLeft='1.5vh'))

db_header_text=  dbc.Col([ header_text] ,
        xs=dict(size=10,offset=0), sm=dict(size=10,offset=0),
        md=dict(size=10,offset=0), lg=dict(size=10,offset=0), xl=dict(size=10,offset=0))

navigation_header=dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Page1", active='exact', href="/Page1",id='Page1',className="page-link",
                                style=dict(fontSize=navbar_font_size))),

        dbc.NavItem(dbc.NavLink("Page2", href="/Page2",active='exact',id='Page2',className="page-link",
                                style=dict(fontSize=navbar_font_size))),

        dbc.NavItem(dbc.NavLink("Page3", href="/Page3", active='exact', id='Page3',className="page-link",
                                style=dict(fontSize=navbar_font_size,color=''))),


    ],
    pills=True,
)
db_navigation_header=dbc.Col([navigation_header],
                             xs=dict(size=12, offset=0), sm=dict(size=12, offset=0),
                             md=dict(size=12, offset=0), lg=dict(size=5, offset=1), xl=dict(size=5, offset=1)
                             )








app.layout=html.Div([ dbc.Row([db_logo_img,db_header_text],style=dict(backgroundColor='#20374c') )

                        , dbc.Row([db_navigation_header]), html.Br(), dbc.Row(id='layout')

                        , dcc.Location(id='url', refresh=True, pathname='/Page1')

                      ])


@app.callback(Output('layout','children'),
               Input('url','pathname'))
def change_page(url):
    if url == '/Page1':
        layout=page1.create_page1_layout(df)
        return layout

    elif url == '/Page2':
        layout=page2.create_page2_layout(df)
        return layout

    else:
        return dash.no_update


@app.callback([Output('bar1','figure'),Output('bar2','figure'),Output('bar3','figure')],
               [Input('page1_city_menu1','value'),Input('page1_state_menu1','value'),Input('page1_product_menu1','value'),
                Input('page1_program_menu1','value'),Input('page1_sector_menu1','value'),Input('page1_customer_menu1','value')]
              )
def update_page1_figures(selected_city,selected_state,selected_product,selected_program,selected_sector,selected_customer):
    banks_df=df.copy()

    if selected_city != 'All Cities' :
        banks_df=banks_df[ banks_df['city_name']==selected_city ]

    if selected_state != 'All States' :
        banks_df=banks_df[ banks_df['state_id']==selected_state ]


    if selected_product != 'All Products' :
        banks_df=banks_df[ banks_df['product_name']==selected_product ]



    if selected_program != 'All Programs' :
        banks_df=banks_df[ banks_df['program_group']==selected_program ]



    if selected_sector != 'All Sectors' :
        banks_df=banks_df[ banks_df['market_sector']==selected_sector ]



    if selected_customer != 'All Customers' :
        banks_df=banks_df[ banks_df['customer_size']==selected_customer ]




    bar1_data=banks_df['bank_name'].value_counts()[0:10]
    bar2_data=banks_df.groupby(['bank_name'],sort=False)['operation_value'].mean().nlargest(10)
    bar3_data=banks_df.groupby("bank_name")['customer_id'].nunique().reset_index()

    bar3_data=bar3_data.nlargest(10,'customer_id')

    print(bar3_data)

    bar_fig1 = go.Figure(data=
                         go.Bar(name='Revenue', x=bar1_data.index, y=bar1_data.astype('int64'), marker_color=main_color,
                                text=bar1_data.astype('int64').to_list(),
                                textposition='outside', textfont=dict(
                                 size=12,
                                 color="white"
                             )))

    bar_fig1.update_layout(
        title='Top 10 Banks with number of operations', xaxis_title='Bank', yaxis_title='number of operations',
        font=dict(size=12, family='bold', color='white'), hoverlabel=dict(
            font_size=12, font_family="Rockwell", font_color='white', bgcolor='#20374c'), plot_bgcolor='#20374c',
        paper_bgcolor='#20374c'#,
      #  xaxis=dict(
        #    tickwidth=2, tickcolor='lightsalmon',
        #    ticks="outside",
        #    tickson="boundaries",
        #    rangeslider_visible=False
      #  )
        , margin=dict(l=0, r=0, t=50, b=0)
    )

    bar_fig1.update_xaxes(showgrid=False, showline=True, zeroline=False, tickangle = 90)
    bar_fig1.update_yaxes(showgrid=False, showline=True, zeroline=False)

    bar_fig2 = go.Figure(data=
                         go.Bar(name='Revenue', x=bar2_data.index, y=bar2_data, marker_color=main_color,
                                text=bar2_data.astype('int64').to_list(),
                                textposition='outside', textfont=dict(
                                 size=12,
                                 color="white"
                             )))

    bar_fig2.update_layout(
        title='Top 10 Banks with average operations value', xaxis_title='Bank', yaxis_title='Avg Operation Value',
        font=dict(size=12, family='bold', color='white'), hoverlabel=dict(
            font_size=12, font_family="Rockwell", font_color='white', bgcolor='#20374c'), plot_bgcolor='#20374c',
        paper_bgcolor='#20374c'#,

        , margin=dict(l=0, r=0, t=50, b=0)
    )

    bar_fig2.update_xaxes(showgrid=False, showline=True, zeroline=False,tickangle = 90)
    bar_fig2.update_yaxes(showgrid=False, showline=True, zeroline=False)


    bar_fig3 = go.Figure(data=
                         go.Bar(name='Revenue', x=bar3_data['bank_name'], y=bar3_data['customer_id'].astype('int64'), marker_color=main_color,
                                text=bar3_data['customer_id'].astype('int64').to_list(),
                                textposition='outside', textfont=dict(
                                 size=12,
                                 color="white"
                             )))

    bar_fig3.update_layout(
        title='Top 10 Banks with number of customers', xaxis_title='Bank', yaxis_title='number of customers',
        font=dict(size=12, family='bold', color='white'), hoverlabel=dict(
            font_size=12, font_family="Rockwell", font_color='white', bgcolor='#20374c'), plot_bgcolor='#20374c',
        paper_bgcolor='#20374c'#,
      #  xaxis=dict(
        #    tickwidth=2, tickcolor='lightsalmon',
        #    ticks="outside",
        #    tickson="boundaries",
        #    rangeslider_visible=False
      #  )
        , margin=dict(l=0, r=0, t=50, b=0)
    )

    bar_fig3.update_xaxes(showgrid=False, showline=True, zeroline=False,tickangle = 90)
    bar_fig3.update_yaxes(showgrid=False, showline=True, zeroline=False)


    return (bar_fig1,bar_fig2,bar_fig3)


@app.callback(Output('map_div','children'),
              Input('refresh_map','n_clicks'),
               [State('page1_city_menu1','value'),State('page1_state_menu1','value'),State('page1_product_menu1','value'),
                State('page1_program_menu1','value'),State('page1_sector_menu1','value'),State('page1_customer_menu1','value')]
              )
def update_page1_map(clicks,selected_city,selected_state,selected_product,selected_program,selected_sector,selected_customer):
    banks_df=df.copy()

    if selected_city != 'All Cities' :
        banks_df=banks_df[ banks_df['city_name']==selected_city ]

    if selected_state != 'All States' :
        banks_df=banks_df[ banks_df['state_id']==selected_state ]


    if selected_product != 'All Products' :
        banks_df=banks_df[ banks_df['product_name']==selected_product ]



    if selected_program != 'All Programs' :
        banks_df=banks_df[ banks_df['program_group']==selected_program ]



    if selected_sector != 'All Sectors' :
        banks_df=banks_df[ banks_df['market_sector']==selected_sector ]



    if selected_customer != 'All Customers' :
        banks_df=banks_df[ banks_df['customer_size']==selected_customer ]

    locations = banks_df.groupby(['state_id'])['id'].count()
    #   print(locations)
    figg = go.Figure(go.Choroplethmapbox(z=locations,
                                         locations=locations.index,
                                         colorscale='Tealgrn',
                                         colorbar=dict(thickness=20, ticklen=3, title='Operations Count'),
                                         geojson=data,

                                         hoverinfo='all',
                                         marker_line_width=1, marker_opacity=0.75))

    figg.update_layout(title_text='Number of operations in each brazil state',
                       title_x=0.5,
                       #  width=1200,  height=700,
                       mapbox=dict(center=dict(lat=-15.793889, lon=-47.882778),

                                   style='carto-positron',
                                   zoom=2.35,
                                   ),

                       font=dict(size=12, family='bold', color='white'), hoverlabel=dict(
            font_size=12, font_family="Rockwell", font_color='white', bgcolor='#20374c'), plot_bgcolor='#20374c',
                       paper_bgcolor='#20374c'  # ,

                       , margin=dict(l=20, r=0, t=50, b=0)

                       )

    figg.write_html("map.html")
    map_frame = html.Iframe(srcDoc=open('map.html', 'r').read()
                            , style=dict(width='100%', height='50vh')
                            )
    return map_frame













@app.callback([Output('line1','figure'),Output('line2','figure'),Output('line3','figure')],
               [Input('page2_banks_menu','value'),Input('page2_resolution_menu','value')]
              )
def update_page2_figures(selected_bank,selected_resolution):
    banks_df2=df.copy()
    banks_df2=banks_df2[banks_df2['bank_name']==selected_bank]
    banks_df2.set_index('operation_date', inplace=True)
    line1_data=banks_df2['id'].resample(selected_resolution).count()
    line3_data=banks_df2['customer_id'].resample(selected_resolution).nunique()
    line2_data=banks_df2['operation_value'].resample(selected_resolution).mean()

    line_fig1 = go.Figure(data=
                         go.Scatter(x=line1_data.index, y=line1_data, mode='lines',
                             marker_color=main_color
                             ))

    line_fig1.update_layout(
        title='Number of operations over the years', xaxis_title='Date', yaxis_title='Number of operations',
        font=dict(size=12, family='Arial', color='white'), hoverlabel=dict(
            font_size=12, font_family="Rockwell", font_color='white', bgcolor='#20374c'), plot_bgcolor='#20374c',
        paper_bgcolor='#20374c',
        xaxis=dict(

            tickwidth=2, tickcolor=main_color,
            ticks="outside",
            tickson="labels",
            rangeslider_visible=False
        )
    )

    line_fig1.update_xaxes(showgrid=False, showline=True, zeroline=False)
    line_fig1.update_yaxes(showgrid=False, showline=True, zeroline=False)

    line_fig2 = go.Figure(data=
                          go.Scatter(x=line2_data.index, y=line2_data, mode='lines',
                                     marker_color=main_color
                                     ))

    line_fig2.update_layout(
        title='average operations value over the years', xaxis_title='Date', yaxis_title='average operations value',
        font=dict(size=12, family='Arial', color='white'), hoverlabel=dict(
            font_size=12, font_family="Rockwell", font_color='white', bgcolor='#20374c'), plot_bgcolor='#20374c',
        paper_bgcolor='#20374c',
        xaxis=dict(

            tickwidth=2, tickcolor=main_color,
            ticks="outside",
            tickson="labels",
            rangeslider_visible=False
        )
    )

    line_fig2.update_xaxes(showgrid=False, showline=True, zeroline=False)
    line_fig2.update_yaxes(showgrid=False, showline=True, zeroline=False)

    line_fig3 = go.Figure(data=
                          go.Scatter(x=line3_data.index, y=line3_data, mode='lines',
                                     marker_color=main_color
                                     ))

    line_fig3.update_layout(
        title='Number of customers over the years', xaxis_title='Date', yaxis_title='Number of customers',
        font=dict(size=12, family='Arial', color='white'), hoverlabel=dict(
            font_size=12, font_family="Rockwell", font_color='white', bgcolor='#20374c'), plot_bgcolor='#20374c',
        paper_bgcolor='#20374c',
        xaxis=dict(

            tickwidth=2, tickcolor=main_color,
            ticks="outside",
            tickson="labels",
            rangeslider_visible=False
        )
    )

    line_fig3.update_xaxes(showgrid=False, showline=True, zeroline=False)
    line_fig3.update_yaxes(showgrid=False, showline=True, zeroline=False)
    # df.set_index('operation_date', inplace=True)
    # graph_data=df[df['bank_name']=='BRADESCO']
    # line1 graph_data['id'].resample('1Y').count()
    # line2 graph_data['customer_id'].resample('1Y').nunique()
    # line_3 graph_data['operation_value'].resample('1Y').mean()



    return (line_fig1,line_fig2,line_fig3)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port=8500,debug=False,dev_tools_silence_routes_logging=True)