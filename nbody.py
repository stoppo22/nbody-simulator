import math
G=1
m1=1
x1=0
y1=0

m2=3
x2=3
y2=4

vx1=0
vx2=0
vy1=0
vy2=0

dt=0.01

delta_x = x2-x1
delta_y = y2-y1

d= math.sqrt(delta_x**2 + delta_y**2)
t=0
while d>0.1:
    delta_x = x2-x1
    delta_y = y2-y1
    t+=dt
    d= math.sqrt(delta_x**2 + delta_y**2)

    a1= G * m2 / d**2
    a2 = G * m1 / d**2

    a1x= a1 *delta_x/ d
    a1y= a1 * delta_y/d

    a2x = -a2 * delta_x/d
    a2y= -a2 * delta_y/d
    
    vx1+= a1x * dt
    vy1+= a1y * dt
    vx2+= a2x * dt
    vy2+= a2y * dt
    
    x1+= vx1 * dt
    y1+= vy1 * dt
    x2+= vx2 * dt
    y2+= vy2 * dt

print(f"Final Velocities: ({vx1}, {vy1}) and ({vx2}, {vy2})")
print(f"Final Position: ({x1}, {y1}) and ({x2}, {y2})")
print(f" Final Distance: {d}")
print(f" Final Time: {t}")
    
    