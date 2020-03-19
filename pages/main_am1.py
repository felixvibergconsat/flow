import SQL_Handler
import time
import copy
import matplotlib
matplotlib.use('GTK3Agg')
import matplotlib.pyplot as plt


sql = SQL_Handler.SQL_Handler()

class Station:
    def __init__(self, d, name):
        self.name = name
        self.d = d
        self.labels = [self.d[l][2] for l in self.d]
    
    def new_status(self, attr, status):
        for key in self.d:
            if attr == self.d[key][2]:
                self.d[key][0] = status
        print(self.d)
    
    def update_stats(self):
        for key in self.d:
            self.d[key][1] += self.d[key][0]

    def plot_data(self, ax):
        ax.clear()
        ax.set_title('{}, {}'.format(self.name, self.d['green'][1]))
        self.sizes = [self.d[l][1] for l in self.d]
        ax.pie(self.sizes, labels=self.labels)



class Cell_9(Station):
    def __init__(self, d):
        self.name = 'Cell 9'
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
        super(Cell_9, self).__init__(self.d, self.name)

class AM_1(Station):
    def __init__(self, d):
        self.name = 'Automatisk Montering 1'
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
        super(AM_1, self).__init__(self.d, self.name)


class Laser_1(Station):
    def __init__(self, d):
        self.name = 'Laser DD01'
        self.d = copy.deepcopy(d)
        self.d['blue'][2] =         'LjusfyrBla'
        self.d['green'][2] =        'LjusfyrGron'
        self.d['yellow'][2] =       'LjusfyrGul'
        self.d['white'][2] =        'LjusfyrVit'
        self.d['stop'][2] =         'Laser1_StopCykel'
        self.d['do_blue'][2] =      'LjusfyrBlaBlink'
        self.d['do_green'][2] =     'LjusfyrGronBlink'
        self.d['do_yellow'][2] =    'LjusfyrGulBlink'
        self.d['do_white'][2] =     'LjusfyrVitBlink'
        self.d['do_stop'][2] =      ''
        super(Laser_1, self).__init__(self.d, self.name)


class Preservation_1(Station):
    def __init__(self, d):
        self.name = 'Anoljning DD01'
        self.d = copy.deepcopy(d)
        self.d['blue'][2] =         'LjusfyrBla'
        self.d['green'][2] =        'LjusfyrGron'
        self.d['yellow'][2] =       'LjusfyrGul'
        self.d['white'][2] =        'LjusfyrVit'
        self.d['stop'][2] =         'Preservation1_StopCykel'
        self.d['do_blue'][2] =      'LjusfyrBlaBlink'
        self.d['do_green'][2] =     'LjusfyrGronBlink'
        self.d['do_yellow'][2] =    'LjusfyrGulBlink'
        self.d['do_white'][2] =     'LjusfyrVitBlink'
        self.d['do_stop'][2] =      ''
        super(Preservation_1, self).__init__(self.d, self.name)

class Wrap_1(Station):
    def __init__(self, d):
        self.name = 'Inplastning DD01'
        self.d = copy.deepcopy(d)
        self.d['blue'][2] =         'LjusfyrBla'
        self.d['green'][2] =        'LjusfyrGron'
        self.d['yellow'][2] =       'LjusfyrGul'
        self.d['white'][2] =        'LjusfyrVit'
        self.d['stop'][2] =         'Wrap1_StopCykel'
        self.d['do_blue'][2] =      'LjusfyrBlaBlink'
        self.d['do_green'][2] =     'LjusfyrGronBlink'
        self.d['do_yellow'][2] =    'LjusfyrGulBlink'
        self.d['do_white'][2] =     'LjusfyrVitBlink'
        self.d['do_stop'][2] =      ''
        super(Wrap_1, self).__init__(self.d, self.name)


class Carton_1(Station):
    def __init__(self, d):
        self.name = 'Kartonnering DD01'
        self.d = copy.deepcopy(d)
        self.d['blue'][2] =         'LjusfyrBla'
        self.d['green'][2] =        'LjusfyrGron'
        self.d['yellow'][2] =       'LjusfyrGul'
        self.d['white'][2] =        'LjusfyrVit'
        self.d['stop'][2] =         'Carton1_StopCykel'
        self.d['do_blue'][2] =      'LjusfyrBlaBlink'
        self.d['do_green'][2] =     'LjusfyrGronBlink'
        self.d['do_yellow'][2] =    'LjusfyrGulBlink'
        self.d['do_white'][2] =     'LjusfyrVitBlink'
        self.d['do_stop'][2] =      ''
        super(Carton_1, self).__init__(self.d, self.name)


class Conv_1(Station):
    def __init__(self, d):
        self.name = 'Bansystem DD01'
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
        super(Conv_1, self).__init__(self.d, self.name)



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
Cell_9 = Cell_9(d)
AM_1 = AM_1(d)
Laser_1 = Laser_1(d)
Preservation_1 = Preservation_1(d)
Wrap_1 = Wrap_1(d)
Carton_1 = Carton_1(d)
Conv_1 = Conv_1(d)

plt.ion()
fig, ax = plt.subplots(7,1)

while 1:
    time_resolution = 1
    time.sleep(time_resolution)
    d = sql.refresh()
    if d is not None:
        for i, station in enumerate(d[:, -1]):
            station_stripped = station.rstrip()
            attr = d[i, 1].split('.')[-1]
            status = int(d[i, 3])
            
            if station_stripped == 'Cell_9':
                Cell_9.new_status(attr, status)
            
            if station_stripped == 'AM1':
                AM_1.new_status(attr, status)
            
            if station_stripped == 'Laser1':
                Laser_1.new_status(attr, status)
            
            if station_stripped == 'Preservation1':
                Preservation_1.new_status(attr, status)
            
            if station_stripped == 'Wrap1':
                Wrap_1.new_status(attr, status)
            
            if station_stripped == 'Carton1':
                Carton_1.new_status(attr, status)
                
            if station_stripped == 'Conv1':
                Conv_1.new_status(attr, status)
            
            print(attr)
            
    Cell_9.update_stats()
    AM_1.update_stats()
    Laser_1.update_stats()
    Preservation_1.update_stats()
    Wrap_1.update_stats()
    Carton_1.update_stats()
    Conv_1.update_stats()
    
    Cell_9.plot_data(ax[0])
    AM_1.plot_data(ax[1])
    Laser_1.plot_data(ax[2])
    Preservation_1.plot_data(ax[3])
    Wrap_1.plot_data(ax[4])
    Carton_1.plot_data(ax[5])
    Conv_1.plot_data(ax[6])
    plt.show()
    plt.pause(0.01)
    #plt.clf()

    print('alive')
    
