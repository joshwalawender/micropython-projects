import pyb
import math

def display_orientation(accel):
    norm = 31./1.5
    (x, y, z) = (accel.x()/norm, accel.y()/norm, accel.z()/norm)
    mag = (x**2 + y**2 + z**2)**0.5
    print(' (x, y, z, mag) = ({:+04.2f}  {:+04.2f}  {:+04.2f}  {:04.2f})'.format(x, y, z, mag))
    alt = y/mag * 180/math.pi
    roll = math.asin(x/z) * 180/math.pi
    print(' alt = {:.1f}'.format(alt))
    print(' roll = {:.1f}'.format(roll))



# import readout_accel
# print('Starting up')
# accel = pyb.Accel()
# while True:
#     readout_accel.display_orientation(accel)
#     pyb.delay(500)
