import time
import datetime
import copy
import numpy as np

class Station:
    def __init__(self, name, state):
        self.name = name
        self.state = {'state': '', 'since': datetime.datetime.now(), 
                'booked': {
                    'Alarm': 0.0,
                    'Producing': 0.0,
                    'Waiting': 0.0,
                    'Off': 0.0
                    }, 
                'current': {
                    'Alarm': 0.0,
                    'Producing': 0.0,
                    'Waiting': 0.0,
                    'Off': 0.0
                        }
                }

        if state['Alarm']:
            self.state['state'] = 'Alarm'
        elif state['Producing']:
            self.state['state'] = 'Producing'
        elif state['Alive']:
            self.state['state'] = 'Waiting'
        else:
            self.state['state'] = 'Off'

    def new_status(self, state):
        elapsed_time = (state[5] - self.state['since']).total_seconds()
        self.book(self.state, elapsed_time)
        if state[4]:
            self.state['state'] = 'Alarm'
        elif state[3]:
            self.state['state'] = 'Producing'
        elif state[2]:
            self.state['state'] = 'Waiting'
        else:
            self.state['state'] = 'Off'
        
        self.state['since'] = state[5]

    def book(self, state, elapsed_time):
        self.state['booked'][self.state['state']] += elapsed_time

    def get_current_duration(self):
        return (datetime.datetime.now() - self.state['since']).total_seconds()

    def get_portion(self):
        self.state['current']['Alarm'] = 0.0
        self.state['current']['Producing'] = 0.0
        self.state['current']['Waiting'] = 0.0
        self.state['current']['Off'] = 0.0

        self.state['current'][self.state['state']] = self.get_current_duration()

        portion = [self.state['booked']['Alarm']+self.state['current']['Alarm'], 
                self.state['booked']['Producing']+self.state['current']['Producing'], 
                self.state['booked']['Waiting']+self.state['current']['Waiting'],
                self.state['booked']['Off']+self.state['current']['Off']
                ]
        print(portion)
        return portion


class Conv_2(Station):
    def __init__(self, d):
        self.name = 'Bansystem DD02'
        self.d = copy.deepcopy(d)
        self.d['blue'][2] =         'LjusfyrBla'
        self.d['green'][2] =        'LjusfyrGron'
        self.d['yellow'][2] =       'LjusfyrGul'
        self.d['white'][2] =        'LjusfyrVit'
        self.d['stop'][2] =         ''
        self.d['do_blue'][2] =      ''
        self.d['do_green'][2] =     'LjusfyrGronBlink'
        self.d['do_yellow'][2] =    'LjusfyrGulBlink'
        self.d['do_white'][2] =     ''
        self.d['do_stop'][2] =      ''
        super(Conv_2, self).__init__(self.d, self.name)
