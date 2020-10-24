from vpython import *

# This code renders shape 48 of the sample group with the segments in different colors

shape1 = box(pos=vector(0,1,0), size=vector(4,1,1), color=color.white)
shape2 = box(pos=vector(-1.5,-1,0), size=vector(1,3,1), color=color.blue)
shape3 = box(pos=vector(-1.5,-2,1.5), size=vector(1,1,2), color=color.red)
shape4 = box(pos=vector(1.5,2.5,0), size=vector(1,2,1), color=color.green)

sample48 = compound([shape1, shape2, shape3, shape4])


#rotational = cylinder(pos=vector(0,-5,.5), axis=vector(0,10,0), radius=.1)
#sample48.rotate(angle=45, axis=vec(1,1,1))
#sample48.rotate(angle=45, axis=vector(0,10,0))

# while True:
# 	sleep(.1)
# 	sample48.rotate(angle=radians(10), axis=vector(0,1,0))

angles = [0, 45, 90, 135, 180]
for i in angles:
	sample48.rotate(angle=radians(i), axis=vector(0,1,0))
	scene.capture("sample48_" + str(i))
	sleep(1)
	sample48.rotate(angle=radians(-i), axis=vector(0,1,0))