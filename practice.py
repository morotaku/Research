#### Circular geometrical mode
from math import *
import numpy as np
from scipy.special import *
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

N2=10 #Number of arrow
L2=10 #Display range
U=np.linspace(-L2,L2,N2)
V=np.linspace(-L2,L2,N2)
u,v=np.meshgrid(U,V)
print(u)
for i in range(N2):
    for j in range(N2):
        if u[i,j]<5:
            u[i,j]=0
        else:
            u[i,j]=1

print(u)
