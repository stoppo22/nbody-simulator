#CONSTANT_G = 6.67 * 10**-11

y=0
v=10
a= -9.81
dt=0.001
max_y= 0
t=0

while y>=0:
    v= v+ (a*dt)
    y = y + (v*dt)
    if y >max_y:
        max_y = y 
    t+=dt

print("max height: ",max_y)
print("flight time: ", t)
