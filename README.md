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



## Roadmap

- [x] Stage 1: single body, constant acceleration
- [ ] Stage 2: two bodies with Newtonian gravity (2D)
- [ ] Stage 3: visualization
- [ ] Stage 4: Earth-Sun orbit, energy drift, Euler vs Verlet/leapfrog
- [ ] Stage 5: N bodies