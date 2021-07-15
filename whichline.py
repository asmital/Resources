#!/usr/bin/env python3
import sys
import os
#import pandas as pd
import numpy as np
import glob
import re

# save numpy array as csv file
from numpy import asarray
from numpy import savetxt


class fluid_data:
    def __init__(self,u=0,v=0):
        self.u=u
        self.v=v

    def set_u(self,u):
        self.u=u

    def set_v(self,v):
        self.v=v

    def __str__(self):
        return f"Fluid u: {self.u} Fluid v:{self.v} \n"

filestr="Test_1__Resolution_40_60/testing_octave-*.txt"
filenames=glob.glob(filestr)
print(len(filenames))
mat=np.array([[[[0.0,0.0] for i in range(63)]for j in range(43)] for k in range(len(filenames))])
for filename in filenames:
    matchObj = re.match(r'Test_1__Resolution_40_60/testing_octave-([0-9]*).txt', filename)
    frame_no=int(matchObj.group(1))
    print(frame_no)
    t=frame_no

    with open(filename, "r") as f:
        content = f.readlines()


    print(len(content))
    #print(content)


    newcontent = content[4:]
    #print("Asmita Content -----------> ",newcontent)
    print("length of content ----> ",len(newcontent))

    k=0
    for i in range(0,43,1):
        for j in range(0, 62, 1):
            u = newcontent[k].strip()
            
            mat[t][i][j][0]=float(u)
            k+=1
    for i in range(0,42,1):
        for j in range(0, 63, 1):
            v = newcontent[k].strip()
            mat[t][i][j][1]=float(v)
            k+=1


    for i in range(0,43,1):
        for j in range(0, 63, 1):
            print(f"t value", t, "i value:", i, "j value:", j, "fluid velocity:", mat[t][i][j])
    
np.save('data',mat)
sys.exit(1)






