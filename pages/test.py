import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
from app import app
import os
import numpy as np
#import pandas as pd
from functions import machines, SQL_Handler


with open('env') as env_data:
    for line in env_data:
        s = str(line).split('=')
        os.environ[s[0]] = s[1][:-1]

sql = SQL_Handler.SQL_Handler()

MP1_OR = machines.Station(*sql.get_state('MP1_OR'))
MP1_IR = machines.Station(*sql.get_state('MP1_IR'))
MP1_RG = machines.Station(*sql.get_state('MP1_RG'))
MP1_CP = machines.Station(*sql.get_state('MP1_CP'))
MP1 = machines.Station(*sql.get_state('MP1'))
AM1_RS = machines.Station(*sql.get_state('AM1_RS'))
AM1 = machines.Station(*sql.get_state('AM1'))
LASER1 = machines.Station(*sql.get_state('LASER1'))
PRESERVATION1 = machines.Station(*sql.get_state('PRESERVATION1'))
WRAP1 = machines.Station(*sql.get_state('WRAP1'))
CONV1 = machines.Station(*sql.get_state('CONV1'))
CARTON1 = machines.Station(*sql.get_state('CARTON1'))
PACK1 = machines.Station(*sql.get_state('PACK1'))

MP2_OR = machines.Station(*sql.get_state('MP2_OR'))
MP2_IR = machines.Station(*sql.get_state('MP2_IR'))
MP2_RG = machines.Station(*sql.get_state('MP2_RG'))
MP2_CP = machines.Station(*sql.get_state('MP2_CP'))
MP2 = machines.Station(*sql.get_state('MP2'))
AM2_RS = machines.Station(*sql.get_state('AM2_RS'))
AM2 = machines.Station(*sql.get_state('AM2'))
LASER2 = machines.Station(*sql.get_state('LASER2'))
PRESERVATION2 = machines.Station(*sql.get_state('PRESERVATION2'))
WRAP2 = machines.Station(*sql.get_state('WRAP2'))
CONV2 = machines.Station(*sql.get_state('CONV2'))
CARTON2 = machines.Station(*sql.get_state('CARTON2'))
PACK2 = machines.Station(*sql.get_state('PACK2'))

BOX = machines.Station(*sql.get_state('BOX'))

DD01 = [MP1_OR, MP1_IR, MP1_RG, MP1_CP, MP1, AM1_RS, AM1, LASER1, PRESERVATION1, WRAP1, CONV1, CARTON1, PACK1]
DD02 = [MP2_OR, MP2_IR, MP2_RG, MP2_CP, MP2, AM2_RS, AM2, LASER2, PRESERVATION2, WRAP2, CONV2, CARTON2, PACK2]

msks = DD01+DD02
msks.append(BOX)

layout = html.Div(className='maachine_pies', children=[
    html.H1('Svarte Petter'),
    html.Div(id='machine_pies'),
    dcc.Interval(id='interval_component',
        interval = 2000,
        n_intervals = 0
        ),
])


@app.callback(
    Output('machine_pies', 'children'),
    [Input('interval_component', 'n_intervals')])
def display_value(value):
    d = sql.refresh()
    if d is not None:
        for i, station in enumerate(d[:, 1]):
            station_stripped = station.rstrip()
            
            if station_stripped == 'MP1_OR':
                MP1_OR.new_status(d[i, :])
            if station_stripped == 'MP1_IR':
                MP1_IR.new_status(d[i, :])
            if station_stripped == 'MP1_RG':
                MP1_RG.new_status(d[i, :])
            if station_stripped == 'MP1_CP':
                MP1_CP.new_status(d[i, :])
            if station_stripped == 'MP1':
                MP1.new_status(d[i, :])
            if station_stripped == 'AM1_RS':
                AM1_RS.new_status(d[i, :])
            if station_stripped == 'AM1':
                AM1.new_status(d[i, :])
            if station_stripped == 'LASER1':
                LASER1.new_status(d[i, :])
            if station_stripped == 'PRESERVATION1':
                PRESERVATION1.new_status(d[i, :])
            if station_stripped == 'WRAP1':
                WRAP1.new_status(d[i, :])
            if station_stripped == 'CONV1':
                CONV1.new_status(d[i, :])
            if station_stripped == 'PACK1':
                PACK1.new_status(d[i, :])
            
            if station_stripped == 'MP2_OR':
                MP2_OR.new_status(d[i, :])
            if station_stripped == 'MP2_IR':
                MP2_IR.new_status(d[i, :])
            if station_stripped == 'MP2_RG':
                MP2_RG.new_status(d[i, :])
            if station_stripped == 'MP2_CP':
                MP2_CP.new_status(d[i, :])
            if station_stripped == 'MP2':
                MP2.new_status(d[i, :])
            if station_stripped == 'AM2_RS':
                AM2_RS.new_status(d[i, :])
            if station_stripped == 'AM2':
                AM2.new_status(d[i, :])
            if station_stripped == 'LASER2':
                LASER2.new_status(d[i, :])
            if station_stripped == 'PRESERVATION2':
                PRESERVATION2.new_status(d[i, :])
            if station_stripped == 'WRAP2':
                WRAP2.new_status(d[i, :])
            if station_stripped == 'CONV2':
                CONV2.new_status(d[i, :])
            if station_stripped == 'PACK2':
                PACK2.new_status(d[i, :])
            
            if station_stripped == 'BOX':
                BOX.new_status(d[i, :])

    data = []
    beacon = []
    layout = []
    b_layout = []
    for i, msk in enumerate(msks):
        data.append([{
            'values': msk.get_portion(),
            'type': 'pie',
            'text': ['alarm', 'producing', 'waiting', 'off'],
            'textposition': 'above',
            'showlegend': False,
            'rotation': 45,
            'hole': .48,
            'sort': False,
            'marker': {'colors': ['#d62728', '#2ca02c','#ff7f0e','#7f7f7f'],
                       'line': {'width': 2}}
            }])
        layout.append({
            'magin': {
                'l': 0,
                'r': 0,
                'b': 0,
                't': 0,
                },
            'padding': {
                'l': 0,
                'r': 0,
                'b': 0,
                't': 0,
                },
            'annotations': [{
                'font': {'size': 30},
                'text': '{}'.format(msk.name),
                'showarrow': False,
                'x': -0.1,
                'y': 1.2,
                },
                {
                'font': {'size': 10},
                'text': '<b>>{}<</b>'.format(msk.state['state']),
                'showarrow': False,
                'x': -0.1,
                'y': 1.1,
                }
                ],
            'height': 500,
            'widht': 500
            })


    return html.Div(className='graph_holder', children=[
            html.Div(className='graph', children=[
                dcc.Graph(id='graph',
                    figure={'data': data[i], 'layout': layout[i]}),
                ])
        for i in range(len(data))])

