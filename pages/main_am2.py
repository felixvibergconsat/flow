import SQL_Handler
import time
import copy
import matplotlib
matplotlib.use('GTK3Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
sql = SQL_Handler.SQL_Handler()

class Station:
    def __init__(self, d, name):
        self.name = name
        self.d = d
        self.labels = [self.d[l][2] for l in self.d]
        self.running = 0
        self.stopped = 1
        self.svarte_petter_time = 0
    
    def new_status(self, attr, status):
        for key in self.d:
            if attr == self.d[key][2]:
                self.d[key][0] = status
                print(self.d[key][2], self.name, status)
    
    def update_stats(self):
        for key in self.d:
            self.d[key][1] += self.d[key][0]

    def plot_data(self, ax):
        self.decide_state(self)
        ax.clear()
        ax.set_title('{}, {}'.format(self.name, self.running))
        self.sizes = [self.d[l][1] for l in self.d]
        #ax.bar(self.labels, self.sizes)
        #ax.set_xticklabels(self.labels, rotation=45)
        ax.pie([self.running, self.stopped], labels=['running', 'stopped'])

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

    def decide_state(self, ax):
        self.state = (self.d['green'][0] and not 
                self.d['do_green'][0] and not 
                self.d['yellow'][0] and not 
                self.d['do_yellow'][0] and not
                (self.d['blue'][0] and self.d['do_blue']) and not
                self.d['white'][0] and not
                self.d['do_white'][0] and not
                self.d['stop'][0] and not
                self.d['do_stop'][0])
        self.running += int(self.state)
        self.stopped += int(not self.state)


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
Cell_10 = Cell_10(d)
AM_2 = AM_2(d)
Laser_2 = Laser_2(d)
Preservation_2 = Preservation_2(d)
Wrap_2 = Wrap_2(d)
Carton_2 = Carton_2(d)
Conv_2 = Conv_2(d)

plt.ion()
fig, ax = plt.subplots(7,3)
svarte_petter_arr = np.zeros(7)

while 1:
    t1 = time.time()
    time_resolution = 1
    time.sleep(time_resolution)
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
            
            print(attr)
    msks = [Carton_2, Conv_2, Wrap_2, Preservation_2, Laser_2, AM_2, Cell_10]
    for i, msk in enumerate(msks):
        msk.update_stats()
        msk.plot_data(ax[i, 0])
        msk.plot_state(ax[i, 1])
    
    for i, msk in enumerate(msks):
        if msk.state == 0:
            if sum(svarte_petter_arr) == 0:
                svarte_petter_arr[i] = 1
            if svarte_petter_arr[i] == 1:
                msk.svarte_petter_time += 1
        else:
            svarte_petter_arr[i] = 0

    svarte_petter_ind = np.where(svarte_petter_arr == 1)[0]
    if len(svarte_petter_ind) == 0:
        plt.suptitle('all is well')
    else:
        plt.suptitle(msks[svarte_petter_ind[0]].name)
    

    ax[3, 2].clear()
    ax[3, 2].pie([msk.svarte_petter_time for msk in msks], labels=[msk.name for msk in msks])
   
    print([msk.svarte_petter_time for msk in msks])
    #plt.tight_layout()
    plt.show()
    plt.pause(0.01)
    t2 = time.time()
    #plt.clf()
    print('alive, {}'.format(t2-t1))
    
