import pyb

class BMP085(object):
    def __init__(self, i2c, address=0x77):
        self.i2c = i2c
        self.address = address
        self.delay = 50
        self.reg = {'CAL_AC1': 0xAA,
                    'CAL_AC2': 0xAC,
                    'CAL_AC3': 0xAE,
                    'CAL_AC4': 0xB0,
                    'CAL_AC5': 0xB2,
                    'CAL_AC6': 0xB4,
                    'CAL_B1': 0xB6, 
                    'CAL_B2': 0xB8, 
                    'CAL_MB': 0xBA, 
                    'CAL_MC': 0xBC, 
                    'CAL_MD': 0xBE, 
                    'CHIPID': 0xD0,
                    'VERSION': 0xD1,
                    'SOFTRESET': 0xE0,
                    'CONTROL': 0xF4,
                    'TEMPDATA': 0xF6,
                    'PRESSUREDATA': 0xF6,
                    'READTEMPCMD': 0x2E,
                    'READPRESSURECMD': 0x34,
                    }
        self.cals = {}

    def read_cals(self):
        for cal in ['CAL_AC1', 'CAL_AC2', 'CAL_AC3', 'CAL_AC4', 'CAL_AC5',
                   'CAL_AC6', 'CAL_B1', 'CAL_B2', 'CAL_MB', 'CAL_MC', 'CAL_MD']:
            self.i2c.send(self.reg[cal], self.address)
            pyb.delay(self.delay)
            response = self.i2c.recv(2, self.address)
            result = int((response[0] << 8) | response[1])
            print(cal, response[0], response[1], result)
