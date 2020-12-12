from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations
from numpy import sin, cos

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("auto")
ax.set_autoscale_on(True)


d = [-2, 2]
for s, e in combinations(np.array(list(product(d,d,d))), 2):
    if np.sum(np.abs(s-e)) == d[1]-d[0]:
        ax.plot3D(*zip(s,e), color="g")


print("1. Translation\n2. Rotation\n3. Scaling\n")
choiceTransform = int(input("Enter your choice of transformation: "))


if choiceTransform == 1:
    
    tx, ty, tz = [int(x) for x in input("Enter tx, ty and tz: ").split()]

    for s, e in combinations(np.array(list(product(d,d,d))), 2):
        if np.sum(np.abs(s-e)) == d[1]-d[0]:
            s_rotated = [s[0] + tx, 
                        s[1] + ty,
                        s[2] + tz]
            e_rotated = [e[0] + tx, 
                        e[1] + ty,
                        e[2] + tz]      
            ax.plot3D(*zip(s_rotated,e_rotated), color="r")


elif choiceTransform == 2:
    
    angle = float(input("Enter angle to rotate: "))

    theta = np.radians(angle)

    for s, e in combinations(np.array(list(product(d,d,d))), 2):
        if np.sum(np.abs(s-e)) == d[1]-d[0]:
            s_rotated = [s[0] * cos(theta) - s[1] * sin(theta), 
                        s[0] * sin(theta) + s[1] * cos(theta),
                        s[2]]
            e_rotated = [e[0] * cos(theta) - e[1] * sin(theta), 
                        e[0] * sin(theta) + e[1] * cos(theta),
                        e[2]]      
            ax.plot3D(*zip(s_rotated,e_rotated), color="r")

elif choiceTransform == 3:
    
    sx, sy, sz = [int(x) for x in input("Enter scaling factors Sx, Sy and Sz: ").split()]

    for s, e in combinations(np.array(list(product(d,d,d))), 2):
        if np.sum(np.abs(s-e)) == d[1]-d[0]:
            s_rotated = [s[0] * sx, 
                        s[1] * sy,
                        s[2] * sz]
            e_rotated = [e[0] * sx, 
                        e[1] * sy,
                        e[2] * sz]      
            ax.plot3D(*zip(s_rotated,e_rotated), color="r")


plt.legend(["Orginal"], loc ="lower right") 

plt.show()