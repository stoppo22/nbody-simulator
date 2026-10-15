import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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

listx1 = [x1]
listy1 = [y1]
listx2 = [x2]
listy2 = [y2]

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

    listx1.append(x1)
    listy1.append(y1)
    listx2.append(x2)
    listy2.append(y2)
    
print(f"Final Velocities: ({vx1}, {vy1}) and ({vx2}, {vy2})")
print(f"Final Position: ({x1}, {y1}) and ({x2}, {y2})")
print(f" Final Distance: {d}")
print(f" Final Time: {t}")
    
    

fig, ax = plt.subplots()
trail1, = ax.plot([], [], 'b-', alpha=0.5)
trail2, = ax.plot([], [], 'r-', alpha=0.5)
p1, = ax.plot([], [], 'bo', label=f'Mass 1 (m1={m1})', markersize=8*m1)
p2, = ax.plot([], [], 'ro', label=f'Mass 2 (m2={m2})', markersize=8*m2)
ax.set_xlim(-0.5, 4.5)                                                                                                                      
ax.set_ylim(-0.5, 4.5)                                                                                                                      
ax.set_aspect('equal')                                                                                                                      
ax.grid(True)                                                                                                                               
leg = ax.legend()
for handle in leg.legend_handles:
    handle.set_markersize(6)


def update(frame):
    p1.set_data([listx1[frame]], [listy1[frame]])
    p2.set_data([listx2[frame]], [listy2[frame]])
    trail1.set_data(listx1[:frame], listy1[:frame])
    trail2.set_data(listx2[:frame], listy2[:frame])
    
    return p1, p2, trail1, trail2

animation = FuncAnimation(fig, update, frames=range(0,len(listx1),6), interval=20, blit=True)
animation.save('outputs/2body_simulation.gif', writer='pillow', fps=30)
plt.show()