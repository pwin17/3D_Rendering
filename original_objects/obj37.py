'''
in commandline, you can use the following options of argpase to generate 3D model in desired angle.
e.g., python3.6 obj13.py -ry True -a 45

'''

import argparse
parser = argparse.ArgumentParser(description='Options to edit rotations axis, and rotation angle')
parser.add_argument('-rx', type=bool, required=False, default=False, help='Enter True if you want to rotate in x-axis, False if not.')
parser.add_argument('-ry', type=bool, required=False, default=False, help='Enter True if you want to rotate in y-axis, False if not.')
parser.add_argument('-rz', type=bool, required=False, default=False, help='Enter True if you want to rotate in z-axis, False if not.')
parser.add_argument('-a', type=int, required=False, default=0, help='Enter the degree to which you want to rotate the object.')
args = parser.parse_args()

from vpython import *

if args.a:
    angle = args.a
else:
    angle = 0
rotation = vector(0,0,0)
if args.rx:
    rotation.x = 1
if args.ry:
    rotation.y = 1
if args.rz:
    rotation.z = 1

box1 = box(pos=vector(0, 1, 1), size=vector(0.99, 0.99, 0.99))
box2 = box(pos=vector(1, 1, 1), size=vector(0.99, 0.99, 0.99))
box3 = box(pos=vector(2, 1, 1), size=vector(0.99, 0.99, 0.99))
box4 = box(pos=vector(0, 0, 1), size=vector(0.99, 0.99, 0.99))
box5 = box(pos=vector(0, 1, 1), size=vector(0.99, 0.99, 0.99))
box6 = box(pos=vector(0, -1, 1), size=vector(0.99, 0.99, 0.99))
box7 = box(pos=vector(0, -2, 1), size=vector(0.99, 0.99, 0.99))
box8 = box(pos=vector(-1, -2, 1), size=vector(0.99, 0.99, 0.99))
box9 = box(pos=vector(-2, -2, 1), size=vector(0.99, 0.99, 0.99))
box10 = box(pos=vector(-3, -2, 1), size=vector(0.99, 0.99, 0.99))
box11 = box(pos=vector(-3,-2, 0), size=vector(0.99, 0.99, 0.99))
box12 = box(pos=vector(-3,-2, -1), size=vector(0.99, 0.99, 0.99))

obj37 = compound([box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12], pos = vector(0,0,0))

obj37.rotate(angle, axis= rotation, origin= vector(0,0,0))

scene.capture("sample37_"+str(angle))