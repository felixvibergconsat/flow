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



OR1 = machines.Station(*sql.get_state('MP1_OR'))
IR1 = machines.Station(*sql.get_state('MP1_IR'))
RG1 = machines.Station(*sql.get_state('MP1_RG'))
RS1 = machines.Station(*sql.get_state('MP1_RS'))
CP1 = machines.Station(*sql.get_state('MP1_CP'))
MP1 = machines.Station(*sql.get_state('MP1'))
AM1 = machines.Station(*sql.get_state('AM1'))
CONV1 = machines.Station(*sql.get_state('CONV1'))


OR2 = machines.Station(*sql.get_state('MP2_OR'))
IR2 = machines.Station(*sql.get_state('MP2_IR'))
RG2 = machines.Station(*sql.get_state('MP2_RG'))
RS2 = machines.Station(*sql.get_state('MP2_RS'))
CP2 = machines.Station(*sql.get_state('MP2_CP'))
MP2 = machines.Station(*sql.get_state('MP2'))
AM2 = machines.Station(*sql.get_state('AM2'))
CONV2 = machines.Station(*sql.get_state('CONV2'))

msks = [OR1, IR1, RG1, RS1, CP1, MP1, AM1, CONV1, OR2, IR2, RG2, RS2, CP2, MP2, AM2, CONV2]
print(AM1.state)
print(AM2.state)
print(CONV1.state)
print(CONV2.state)

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
            
            if station_stripped == 'OR1':
                OR1.new_status(d[i, :])
            if station_stripped == 'IR1':
                IR1.new_status(d[i, :])
            if station_stripped == 'RG1':
                RG1.new_status(d[i, :])
            if station_stripped == 'RS1':
                RS1.new_status(d[i, :])
            if station_stripped == 'CP1':
                CP1.new_status(d[i, :])
            if station_stripped == 'MP1':
                MP1.new_status(d[i, :])
            if station_stripped == 'AM1':
                AM1.new_status(d[i, :])
            if station_stripped == 'CONV1':
                CONV1.new_status(d[i, :])
            
            
            if station_stripped == 'OR2':
                OR2.new_status(d[i, :])
            if station_stripped == 'IR2':
                IR2.new_status(d[i, :])
            if station_stripped == 'RG2':
                RG2.new_status(d[i, :])
            if station_stripped == 'RS2':
                RS2.new_status(d[i, :])
            if station_stripped == 'CP2':
                CP2.new_status(d[i, :])
            if station_stripped == 'MP2':
                MP2.new_status(d[i, :])
            if station_stripped == 'AM2':
                AM2.new_status(d[i, :])
            if station_stripped == 'CONV2':
                CONV2.new_status(d[i, :])

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

