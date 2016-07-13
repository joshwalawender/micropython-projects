import pyb

class HTU21DF(object):
    def __init__(self, i2c, address=0x40):
        self.i2c = i2c
        self.address = address
        self.delay = 100 # ms delay between send and read

    def read_temp(self):
        self.i2c.send(0xE3, self.address)
        pyb.delay(self.delay)
        response = self.i2c.recv(3, self.address)
        result = 256*int(response[0]) + int(response[1])
        t = ((float(result)/ 65536.) * 175.72 ) - 46.85
        return t

    def read_hum(self):
        self.i2c.send(0xE5, self.address)
        pyb.delay(100)
        response = self.i2c.recv(3, self.address)
        result = 256*int(response[0]) + int(response[1])
        h = ((float(result)/ 65536.) * 125. ) - 6.
        return h
