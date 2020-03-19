import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
from app import app
import os
import numpy as np
import pandas as pd
from functions import machines, SQL_Handler


with open('env') as env_data:
    for line in env_data:
        s = str(line).split('=')
        os.environ[s[0]] = s[1][:-1]

d = {'blue':[0, 0, ''],
        'green':[1, 0, ''],
        'yellow':[0, 0, ''],
        'white':[0, 0, ''],
        'stop':[0, 0, ''],
        'do_blue':[0, 0, ''],
        'do_green':[0, 0, ''],
        'do_yellow':[0, 0, ''],
        'do_white':[0, 0, ''],
        'do_stop':[0, 0, '']}

sql = SQL_Handler.SQL_Handler()

Cell_10 = machines.Cell_10(d)
AM_2 = machines.AM_2(d)
Laser_2 = machines.Laser_2(d)
Preservation_2 = machines.Preservation_2(d)
Wrap_2 = machines.Wrap_2(d)
Carton_2 = machines.Carton_2(d)
Conv_2 = machines.Conv_2(d)
msks = [Carton_2, Conv_2, Wrap_2, Preservation_2, Laser_2, AM_2, Cell_10]
svarte_petter_arr = np.zeros(len(msks))

layout = html.Div([
    html.H3('Svarte Petter'),
    html.Div(className='maachine_pies', id='machine_pies'),
    dcc.Interval(id='interval_component',
        interval = 2000,
        n_intervals = 0
        ),
    html.Div(className='svarte_petter_pie', id='svarte_petter_pie'),
    #dcc.Link('Go to App 2', href='/apps/app2')
])


@app.callback(
    Output('machine_pies', 'children'),
    [Input('interval_component', 'n_intervals')])
def display_value(value):
    d = sql.refresh()
    if d is not None:
        for i, station in enumerate(d[:, -1]):
            station_stripped = station.rstrip()
            attr = d[i, 1].split('.')[-1]
            status = int(d[i, 3])

            if station_stripped == 'Cell_10':
                Cell_10.new_status(attr, status)

            if station_stripped == 'AM2':
                AM_2.new_status(attr, status)

            if station_stripped == 'Laser2':
                Laser_2.new_status(attr, status)

            if station_stripped == 'Preservation2':
                Preservation_2.new_status(attr, status)

            if station_stripped == 'Wrap2':
                Wrap_2.new_status(attr, status)

            if station_stripped == 'Carton2':
                Carton_2.new_status(attr, status)
                
            if station_stripped == 'Conv2':
                Conv_2.new_status(attr, status)

    data = []
    beacon = []
    layout = []
    b_layout = []
    for i, msk in enumerate(msks):
        data.append([{
            'values': msk.get_portion(),
            'type': 'pie',
            'text': ['running', 'stopped'],
            'textposition': 'above',
            'showlegend': False,
            'hole': .48,
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
            'title': msk.name,
            'height': 300,
            'widht': 300
            })
        beacon.append([{
            'type': 'heatmap',
            'x': ['solid', 'blinking'],
            'y': ['green','blue','yellow','white','stop'],
            'z': msk.get_beacon(),
            'zmax': 2,
            'zmin': -1,
            'showscale': False,
            'colorscale': 'Greys'
            }])
        b_layout.append({
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
            'height': 300
            })


    return html.Div(className='graph_holder', children=[
            html.Div(className='graph', children=[
                dcc.Graph(id='graph',
                    figure={'data': data[0], 'layout': layout[0]}),
                dcc.Graph(id='map',
                    figure={'data': beacon[0], 'layout': b_layout[0]})
                ]),
            html.Div(className='graph', children=[
                dcc.Graph(id='graph',
                    figure={'data': data[1], 'layout': layout[1]}),
                dcc.Graph(id='map',
                    figure={'data': beacon[1], 'layout': b_layout[0]})
                
                ]),
            html.Div(className='graph', children=[
                dcc.Graph(id='graph',
                    figure={'data': data[2], 'layout': layout[2]}),
                dcc.Graph(id='map',
                    figure={'data': beacon[2], 'layout': b_layout[0]})
                
                ]),
            html.Div(className='graph', children=[
                dcc.Graph(id='graph',
                    figure={'data': data[3], 'layout': layout[3]}),
                dcc.Graph(id='map',
                    figure={'data': beacon[3], 'layout': b_layout[0]})
                
                ]),
            html.Div(className='graph', children=[
                dcc.Graph(id='graph',
                    figure={'data': data[4], 'layout': layout[4]}),
                dcc.Graph(id='map',
                    figure={'data': beacon[4], 'layout': b_layout[0]})
                
                ]),
            html.Div(className='graph', children=[
                dcc.Graph(id='graph',
                    figure={'data': data[5], 'layout': layout[5]}),
                dcc.Graph(id='map',
                    figure={'data': beacon[5], 'layout': b_layout[0]})
                
                ]),
            html.Div(className='graph', children=[
                dcc.Graph(id='graph',
                    figure={'data': data[6], 'layout': layout[6]}),
                dcc.Graph(id='map',
                    figure={'data': beacon[6], 'layout': b_layout[0]})
                
                ]),
        ])

    
@app.callback(
    Output('svarte_petter_pie', 'children'),
    [Input('interval_component', 'n_intervals')])
def display_value(value):
    for i, msk in enumerate(msks):
        msk.update_stats()

    for i, msk in enumerate(msks):
        if msk.running == 0:
            if sum(svarte_petter_arr) == 0:
                svarte_petter_arr[i] = 1
            if svarte_petter_arr[i] == 1:
                msk.svarte_petter_time += 1
        else:
            svarte_petter_arr[i] = 0
    
    portions = [msk.svarte_petter_time for msk in msks]
    texts = [msk.name for msk in msks]
    data = [{
        'values': portions,
        'type': 'pie',
        'text': texts,
        'textposition': 'above',
        'showlegend': False,
        'domain': {'y': [0.3, 0.7]},
        'hole': .48
        }]
    v_layout = {
        'magin': {
            'l': 100,
            'r': 100,
            'b': 100,
            't': 100,
            },
        'height': 800,
        }
    

    return html.Div([
        dcc.Graph(id='graph',
            figure={'data': data, 'layout': v_layout}
            )
        ])
