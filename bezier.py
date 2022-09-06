import numpy as np
import matplotlib.pyplot as plt


#QUADRATIC BEZIER CURVE
#defining the points
p1  = [1,1]
p2  = [5,5]
p3  = [3,2]

#line between points
xVal = [p1[0],p2[0],p3[0]]
yVal = [p1[1],p2[1],p3[1]]


t = np.linspace(0,1,50)

#defining the lerp function 
def lerp(xi,xf,yi,yf):
    m = (yf-yi)/(xf-xi) #finds the angular coefficient
    px = (1-t)*xi + t*xf
    py = m*(px-xi)+yi
    return px,py


M1 = lerp(p1[0],p2[0],p1[1],p2[1])
M2 = lerp(p2[0],p3[0],p2[1],p3[1])
B = lerp(M1[0],M2[0],M1[1],M2[1])

plt.plot(p1[0],p1[1],p2[0],p2[1],p3[0],p3[1],marker="o")
plt.plot(xVal,yVal, linewidth=0.5,c='black')
plt.plot(B[0],B[1])
plt.grid()
plt.show()




#CUBIC BEZIER CURVES
#defining the points
p1 = [1,1]
p2 = [5,3]
p3 = [7,2]
p4 = [5,9]

#line between points
xVal = [p1[0],p2[0],p3[0],p4[0]]
yVal = [p1[1],p2[1],p3[1],p4[1]]


M1 = lerp(p1[0],p2[0],p1[1],p2[1])
M2 = lerp(p2[0],p3[0],p2[1],p3[1])
M3 = lerp(p3[0],p4[0],p3[1],p4[1])

M12 = lerp(M1[0],M2[0],M1[1],M2[1])
M23 = lerp(M2[0],M3[0],M2[1],M3[1])
B = lerp(M12[0],M23[0],M12[1],M23[1])

plt.plot(p1[0],p1[1],p2[0],p2[1],p3[0],p3[1],p4[0],p4[1],marker="o")
plt.plot(xVal,yVal, linewidth=0.5,c='black')
plt.plot(B[0],B[1])
plt.grid()
plt.show()