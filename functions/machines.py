import time
import copy
import numpy as np

class Station:
    def __init__(self, d, name):
        self.name = name
        self.d = d
        self.labels = [self.d[l][2] for l in self.d]
        self.running_time = 0
        self.stopped_time = 1
        self.svarte_petter_time = 0
        self.running = False
    
    def new_status(self, attr, status):
        for key in self.d:
            if attr == self.d[key][2]:
                self.d[key][0] = status
                print(self.d[key][2], self.name, status)
    
    def update_stats(self):
        for key in self.d:
            self.d[key][1] += self.d[key][0]

    def get_portion(self):
        self.decide_portions(self)
        return [self.running_time, self.stopped_time]

    def get_beacon(self):
        state_matrix = np.zeros((5, 2))
        state_matrix[0, 0] = self.d['green'][0] and not self.d['do_green'][0]
        state_matrix[0, 1] = self.d['green'][0] and self.d['do_green'][0]
        state_matrix[1, 0] = self.d['blue'][0] and not self.d['do_blue'][0]
        state_matrix[1, 1] = self.d['blue'][0] and self.d['do_blue'][0]
        state_matrix[2, 0] = self.d['yellow'][0] and not self.d['do_yellow'][0]
        state_matrix[2, 1] = self.d['yellow'][0] and self.d['do_yellow'][0]
        state_matrix[3, 0] = self.d['white'][0] and not self.d['do_white'][0]
        state_matrix[3, 1] = self.d['white'][0] and self.d['do_white'][0]
        state_matrix[4, 0] = self.d['stop'][0] and not self.d['do_stop'][0]
        state_matrix[4, 1] = self.d['stop'][0] and self.d['do_stop'][0]
        return state_matrix

    def decide_portions(self, ax):
        self.running = (self.d['green'][0] and not 
                self.d['do_green'][0] and not 
                self.d['yellow'][0] and not 
                self.d['do_yellow'][0] and not
                (self.d['blue'][0] and not self.d['do_blue']) and not
                self.d['white'][0] and not
                self.d['do_white'][0] and not
                self.d['stop'][0] and not
                self.d['do_stop'][0])
        self.running_time += int(self.running)
        self.stopped_time += int(not self.running)


class Cell_10(Station):
    def __init__(self, d):
        self.name = 'Cell 10'
        self.d = copy.deepcopy(d)
        self.d['blue'][2] =         'LjusfyrStatusBla'
        self.d['green'][2] =        'LjusfyrStatusGron'
        self.d['yellow'][2] =       'LjusfyrStatusGul'
        self.d['white'][2] =        ''
        self.d['stop'][2] =         'StoppCykel'
        self.d['do_blue'][2] =      'HMI_BlueLightBlink'
        self.d['do_green'][2] =     'HMI_GreenLightBlink'
        self.d['do_yellow'][2] =    'HMI_YellowLightBlink'
        self.d['do_white'][2] =     ''
        self.d['do_stop'][2] =      ''
        super(Cell_10, self).__init__(self.d, self.name)

class AM_2(Station):
    def __init__(self, d):
        self.name = 'Automatisk Montering 2'
        self.d = copy.deepcopy(d)
        self.d['blue'][2] =         'LjusfyrStatusBla'
        self.d['green'][2] =        'LjusfyrStatusGron'
        self.d['yellow'][2] =       'LjusfyrStatusGul'
        self.d['white'][2] =        'LjusfyrStatusVit'
        self.d['stop'][2] =         'StoppCykel'
        self.d['do_blue'][2] =      'Do_LjusfyrBla_Blink'
        self.d['do_green'][2] =     'Do_LjusfyrGron_Blink'
        self.d['do_yellow'][2] =    'Do_LjusfyrGul_Blink'
        self.d['do_white'][2] =     'Do_LjusfyrVit_Blink'
        self.d['do_stop'][2] =      ''
        super(AM_2, self).__init__(self.d, self.name)

        

class Laser_2(Station):
    def __init__(self, d):
        self.name = 'Laser DD02'
        self.d = copy.deepcopy(d)
        self.d['blue'][2] =         'LjusfyrBla'
        self.d['green'][2] =        'LjusfyrGron'
        self.d['yellow'][2] =       'LjusfyrGul'
        self.d['white'][2] =        'LjusfyrVit'
        self.d['stop'][2] =         'Laser2_StopCykel'
        self.d['do_blue'][2] =      'LjusfyrBlaBlink'
        self.d['do_green'][2] =     'LjusfyrGronBlink'
        self.d['do_yellow'][2] =    'LjusfyrGulBlink'
        self.d['do_white'][2] =     'LjusfyrVitBlink'
        self.d['do_stop'][2] =      ''
        super(Laser_2, self).__init__(self.d, self.name)


class Preservation_2(Station):
    def __init__(self, d):
        self.name = 'Anoljning DD02'
        self.d = copy.deepcopy(d)
        self.d['blue'][2] =         'LjusfyrBla'
        self.d['green'][2] =        'LjusfyrGron'
        self.d['yellow'][2] =       'LjusfyrGul'
        self.d['white'][2] =        'LjusfyrVit'
        self.d['stop'][2] =         'Preservation2_StopCykel'
        self.d['do_blue'][2] =      'LjusfyrBlaBlink'
        self.d['do_green'][2] =     'LjusfyrGronBlink'
        self.d['do_yellow'][2] =    'LjusfyrGulBlink'
        self.d['do_white'][2] =     'LjusfyrVitBlink'
        self.d['do_stop'][2] =      ''
        super(Preservation_2, self).__init__(self.d, self.name)

class Wrap_2(Station):
    def __init__(self, d):
        self.name = 'Inplastning DD02'
        self.d = copy.deepcopy(d)
        self.d['blue'][2] =         'LjusfyrBla'
        self.d['green'][2] =        'LjusfyrGron'
        self.d['yellow'][2] =       'LjusfyrGul'
        self.d['white'][2] =        'LjusfyrVit'
        self.d['stop'][2] =         'Wrap2_StopCykel'
        self.d['do_blue'][2] =      'LjusfyrBlaBlink'
        self.d['do_green'][2] =     'LjusfyrGronBlink'
        self.d['do_yellow'][2] =    'LjusfyrGulBlink'
        self.d['do_white'][2] =     'LjusfyrVitBlink'
        self.d['do_stop'][2] =      ''
        super(Wrap_2, self).__init__(self.d, self.name)


class Carton_2(Station):
    def __init__(self, d):
        self.name = 'Kartonnering DD02'
        self.d = copy.deepcopy(d)
        self.d['blue'][2] =         'LjusfyrBla'
        self.d['green'][2] =        'LjusfyrGron'
        self.d['yellow'][2] =       'LjusfyrGul'
        self.d['white'][2] =        'LjusfyrVit'
        self.d['stop'][2] =         'Carton2_StopCykel'
        self.d['do_blue'][2] =      'LjusfyrBlaBlink'
        self.d['do_green'][2] =     'LjusfyrGronBlink'
        self.d['do_yellow'][2] =    'LjusfyrGulBlink'
        self.d['do_white'][2] =     'LjusfyrVitBlink'
        self.d['do_stop'][2] =      ''
        super(Carton_2, self).__init__(self.d, self.name)


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
