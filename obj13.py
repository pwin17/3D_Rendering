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

box_size = vector(0.99,0.99,0.99)
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

box0 = box(pos=vector(0,0,0), size=box_size)#, axis=vector(50,0,0))
box1 = box(pos=vec(1,0,0), size=box_size)
box2 = box(pos=vector(-1,0,0), size=box_size)
box3 = box(pos=vector(-1,1,0), size=box_size)
box4 = box(pos=vector(1,1,0), size=box_size)
box5 = box(pos=vector(1,2,0), size=box_size)
box6 = box(pos=vector(1,3,0), size=box_size)
box7 = box(pos=vector(1,3,1), size= box_size)
obj13 = compound([box0,box1,box2,box3,box4,box5,box6,box7], pos = vector(0,0,0))

obj13.rotate(angle, axis= rotation, origin= vector(0,0,0))

