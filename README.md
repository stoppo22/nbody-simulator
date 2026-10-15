# nbody-simulator

N-body gravitational simulation in Python, built from scratch (no physics libraries).

## Stage 1: ball thrown upward

A single body thrown upward under constant gravity, used to understand numerical integration before adding gravity between bodies.

**Initial conditions:** y0 = 0 m, v0 = 10 m/s, a = -9.81 m/s².

**Method:** at every time step `dt`, the velocity is updated from the acceleration, then the position is updated from the new velocity. The loop stops when the ball goes below the ground.

### Results

Exact values from the analytical solution: max height v0²/(2g) ≈ 5.0968 m, flight time 2·v0/g ≈ 2.0387 s.

| dt    | max height (m) | error (m) | flight time (s) |
|-------|----------------|-----------|-----------------|
| 0.1   | 4.6045         | 0.492     | 2.000           |
| 0.01  | 5.0469         | 0.050     | 2.030           |
| 0.001 | 5.0918         | 0.005     | 2.038           |

### Observations

**Effect of dt:** Every time `dt` is divided by 10, the error is also divided by 10, at the cost of 10x more iterations.



## Stage 2: two bodies with Newtonian gravity (2D)

Two bodies in 2D interacting through Newtonian gravity ($F = G \frac{m_1 m_2}{d^2}$), starting from rest and falling toward each other.

**Initial conditions:** 
- $G = 1$
- Body 1: $m_1 = 1$, position $(0, 0)$, $v_1 = (0, 0)$
- Body 2: $m_2 = 3$, position $(3, 4)$, $v_2 = (0, 0)$
- Initial separation: $d_0 = 5$

**Method:** Semi-implicit Euler in 2D. At each time step ($dt = 0.01$):
1. Compute relative displacement $\Delta x, \Delta y$ and distance $d$.
2. Compute acceleration magnitudes ($a_1 = G \frac{m_2}{d^2}$, $a_2 = G \frac{m_1}{d^2}$) and decompose into Cartesian components along the unit vector.
3. Update velocities first, then update positions.
4. Stop when distance $d \le 0.1$ to avoid the numerical singularity at $d = 0$.

### Results

- **Free-fall time:**
  - Analytical solution: $t_{\text{fall}} = \frac{\pi}{2\sqrt{2}} \frac{d_0^{3/2}}{\sqrt{G(m_1 + m_2)}} \approx 6.209\text{ s}$
  - Simulated time: $6.21\text{ s}$
- **Collision position:**
  - Center of mass: $R_{\text{cm}} = \frac{m_1 r_1 + m_2 r_2}{m_1 + m_2} = (2.25, 3.00)$
  - Final positions: $(2.287, 3.050)$ and $(2.238, 2.983)$
- **Velocity ratio:**
  - $v_1 \approx (7.03, 9.37)$, $v_2 \approx (-2.34, -3.12)$
  - $\frac{|v_1|}{|v_2|} = 3.0$, perfectly conserving total linear momentum ($m_1 v_1 + m_2 v_2 = 0$).

### Observations

- **Center of mass:** The center of mass remains stationary throughout the simulation.
- **Overshooting near collision:** Because gravitational acceleration scales as $1/d^2$, the force diverges as $d \to 0$. With a fixed time step ($dt = 0.01$), the acceleration at the final step becomes large enough that the two bodies cross each other (overshoot) in a single step.

## Roadmap

- [x] Stage 1: single body, constant acceleration
- [x] Stage 2: two bodies with Newtonian gravity (2D)
- [ ] Stage 3: visualization
- [ ] Stage 4: Earth-Sun orbit, energy drift, Euler vs Verlet/leapfrog
- [ ] Stage 5: N bodies