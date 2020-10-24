#!/usr/bin/env python
# coding: utf-8

# # Generating 3D Shapes 

# In[40]:


from vpython import *
import random as rd


# ### Rendering a Figure from a 3D List

# In[81]:


"""
def drawFig(shape):
    for block in shape:
        for row in block:
            for cube in row:
                if(cube>0):
                    x = shape.index(block)
                    y = block.index(row)
                    z = row.index(cube)
                    box1 = box(pos=vector(x, y, z))
    return True
"""

def drawFig(shape):
    for x in range(len(shape)):
        for y in range(len(shape[0])):
            for z in range(len(shape[0][0])):
                if(shape[x][y][z] != 0):
                    box1 = box(pos=vector(x, y, z), size=vector(0.99, 0.99, 0.99))
    return True
        


# In[99]:


# Example object
shape7 =[[[1,0,0,0],
         [0,0,0,0],
         [0,0,0,0]],
         
        [[1,0,0,0],
         [1,0,0,2],
         [1,2,3,4]]]
scene = canvas()
drawFig(shape7)


# ### Generating New 3D Figures By a 3D Path

# In[102]:


def generateFig(a, b, c):
    # Empty 3D list of 0s
    fig = [[[0 for col in range(a)] for col in range(b)] for row in range(c)]
    
    # Position, leg count
    x = 0
    y = 0
    z = 0
    count = 0
    blockCount = 0
    direction = rd.randint(1,3)
    
    fig[x][y][z] = 9
    try:
        # Max 4 segments
        while(blockCount < 8 or count < 4 or x == a-1 or y == b-1 or z == c-1):
            d = direction
        
            # Inner 
            if(d == 1):
                r = rd.randint(1, min(int(a/2), a-x))
                for i in range(r):
                    x+=1
                    blockCount +=1
                    fig[x][y][z] = i+1
            # Middle 
            elif(d == 2):
                r = rd.randint(1, min(int(b/2),b-y))
                for i in range(r):
                    blockCount +=1
                    y+=1
                    fig[x][y][z] = i+1
            # Outer
            elif(d == 3):
                r = rd.randint(1, min(int(c/2),c-z))
                for i in range(r):
                    blockCount +=1
                    z+=1
                    fig[x][y][z] = i+1
            count += 1
            
            direction = rd.randint(1,3)
            while(d == direction):
                direction = rd.randint(1,3)
    finally:
        return fig  
    


# In[101]:


scene = canvas()
drawFig(generateFig(5, 5, 5))

