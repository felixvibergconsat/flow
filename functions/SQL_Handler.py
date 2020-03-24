import pyodbc
import numpy as np
import os

def exec_sql(env, command):
    conn = pyodbc.connect(
            'DRIVER={};SERVER={};UID={};PWD={}'.format(
                'FreeTDS',
                env['SERVER'],
                env['DB_USER'],
                env['DB_PASSWORD']))
    cursor = conn.cursor()
    sql_result = []
    cursor.execute(command)
    for row in cursor.fetchall():
        sql_result.append(row)
    return np.array(sql_result)


with open('env') as env_data:
    for line in env_data:
        s = str(line).split('=')
        os.environ[s[0]] = s[1][:-1]


class SQL_Handler:
    def __init__(self):
        query = 'SELECT TOP 1 id FROM KEPServer.dbo.Machine_State ORDER BY id DESC'
        self.last_record_id = exec_sql(os.environ, query)[0][0]
    
    def refresh(self):
        query = 'SELECT * FROM KEPServer.dbo.Machine_State WHERE id > {}'.format(self.last_record_id)
        data = exec_sql(os.environ, query)
        if len(data)>0:
            self.last_record_id = data[-1, 0]
            return data

    def get_state(self, machine):
        query = 'EXEC KEPServer.dbo.Get_State {}'.format(machine)
        state = exec_sql(os.environ, query)
        print(state)
        if len(state)>0:
            return machine, {'Alive': state[0][0], 
                    'Producing': state[0][1],
                    'Alarm': state[0][2],
                    'Timestamp': state[0][3]}
        else:
            return machine, {'Alive': 0, 
                    'Producing': 0,
                    'Alarm': 0,
                    'Timestamp': 0}

