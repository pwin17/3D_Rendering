GlowScript 3.0 VPython
# x coord, y coord, z coord

s = vector(.99,.99,.99)
angles = [0, 45, 90, 135, 180]

#PHOTO 1
box1_location = vector(2,1,0)
box2_location = vector(2,0,0)
box3_location = vector(1,0,0)
box4_location = vector(0,0,0)
box5_location = vector(0,1,0)
box6_location = vector(0,2,0)
box7_location = vector(0,2,1)

box1 = box(pos = box1_location, size = s)
box2 = box(pos = box2_location, size = s)
box3 = box(pos = box3_location, size = s)
box4 = box(pos = box4_location, size = s)
box5 = box(pos = box5_location, size = s)
box6 = box(pos = box6_location, size = s)
box7 = box(pos = box7_location, size = s)
tetris1 = compound([box1,box2,box3,box4,box5,box6,box7])



#Noah's rotation code

#for i in angles:
#    tetris1.rotate(angle=radians(i), axis=vector(0,1,0))
#    scene.capture("tetris1" + str(i))
#    sleep(1)
#    tetris1.rotate(angle=radians(-i), axis=vector(0,1,0))

#for i in angles:
#    tetris1.rotate(angle=radians(i), axis=vector(1,0,0))
#    scene.capture("tetris1" + str(i))
#    sleep(1)
#    tetris1.rotate(angle=radians(-i), axis=vector(1,0,0))
#################################################
#PHOTO 2
box1_location = vector(0,0,0)
box2_location = vector(0,0,1)
box3_location = vector(1,0,0)
box4_location = vector(2,0,0)
box5_location = vector(2,1,0)
box6_location = vector(2,2,0)
box7_location = vector(3,2,0)

box1 = box(pos = box1_location, size = s)
box2 = box(pos = box2_location, size = s)
box3 = box(pos = box3_location, size = s)
box4 = box(pos = box4_location, size = s)
box5 = box(pos = box5_location, size = s)
box6 = box(pos = box6_location, size = s)
box7 = box(pos = box7_location, size = s)

tetris2 = compound([box1,box2,box3,box4,box5,box6,box7])

#################################################
#PHOTO 3
box1_location = vector(0,0,0)
box2_location = vector(0,0,1)
box3_location = vector(0,1,0)
box4_location = vector(0,2,0)
box5_location = vector(1,2,0)
box6_location = vector(2,2,0)
box7_location = vector(2,3,0)

box1 = box(pos = box1_location, size = s)
box2 = box(pos = box2_location, size = s)
box3 = box(pos = box3_location, size = s)
box4 = box(pos = box4_location, size = s)
box5 = box(pos = box5_location, size = s)
box6 = box(pos = box6_location, size = s)
box7 = box(pos = box7_location, size = s)

tetris3 = compound([box1,box2,box3,box4,box5,box6,box7])
#################################################
#PHOTO 4
box1_location = vector(0,0,0)
box2_location = vector(0,1,0)
box3_location = vector(0,2,0)
box4_location = vector(0,2,1)
box5_location = vector(1,0,0)
box6_location = vector(2,0,0)
box7_location = vector(2,0,1)
box8_location = vector(2,0,2)

box1 = box(pos = box1_location, size = s)
box2 = box(pos = box2_location, size = s)
box3 = box(pos = box3_location, size = s)
box4 = box(pos = box4_location, size = s)
box5 = box(pos = box5_location, size = s)
box6 = box(pos = box6_location, size = s)
box7 = box(pos = box7_location, size = s)
box8 = box(pos = box8_location, size = s)
tetris4 = compound([box1,box2,box3,box4,box5,box6,box7,box8])

#################################################
#PHOTO 5
box1_location = vector(0,0,0)
box2_location = vector(0,0,1)
box3_location = vector(0,1,0)
box4_location = vector(0,2,0)
box5_location = vector(1,2,0)
box6_location = vector(2,2,0)
box7_location = vector(2,3,0)
box8_location = vector(2,4,0)

box1 = box(pos = box1_location, size = s)
box2 = box(pos = box2_location, size = s)
box3 = box(pos = box3_location, size = s)
box4 = box(pos = box4_location, size = s)
box5 = box(pos = box5_location, size = s)
box6 = box(pos = box6_location, size = s)
box7 = box(pos = box7_location, size = s)
box8 = box(pos = box8_location, size = s)

tetris5 = compound([box1,box2,box3,box4,box5,box6,box7,box8])

#################################################
#PHOTO 6
box1_location = vector(0,0,2)
box2_location = vector(1,0,2)
box3_location = vector(2,0,2)
box4_location = vector(2,0,1)
box5_location = vector(2,0,0)
box6_location = vector(2,1,0)
box7_location = vector(2,2,0)
box8_location = vector(3,2,0)

box1 = box(pos = box1_location, size = s)
box2 = box(pos = box2_location, size = s)
box3 = box(pos = box3_location, size = s)
box4 = box(pos = box4_location, size = s)
box5 = box(pos = box5_location, size = s)
box6 = box(pos = box6_location, size = s)
box7 = box(pos = box7_location, size = s)
box8 = box(pos = box8_location, size = s)

tetris6 = compound([box1,box2,box3,box4,box5,box6,box7,box8])
