import math
import matplotlib.pyplot as plt

# Gravitational and astronomical constants (AU, M_sun, yr)
G = 4 * math.pi ** 2  # AU^3 / (yr^2 * M_sun)
M_SUN = 1.0           # M_sun

# Initial conditions for Earth (circular orbit at 1 AU)
X0 = 1.0
Y0 = 0.0
VX0 = 0.0
VY0 = 2 * math.pi     # v_circ = sqrt(G * M_sun / r) = 2*pi AU/yr


def compute_acceleration(x, y):
    """Compute gravitational acceleration vector from the Sun at origin."""
    r = math.sqrt(x**2 + y**2)
    a = G * M_SUN / r**2
    ax = -a * (x / r)
    ay = -a * (y / r)
    return ax, ay, r


def compute_energy(x, y, vx, vy):
    """Compute specific mechanical energy E = K + U."""
    r = math.sqrt(x**2 + y**2)
    kinetic = 0.5 * (vx**2 + vy**2)
    potential = -G * M_SUN / r
    return kinetic + potential


def simulate_euler_explicit(dt=0.001, t_max=5.0):
    """
    Standard (Explicit) Euler method:
    x_{n+1} = x_n + v_n * dt
    v_{n+1} = v_n + a_n * dt
    """
    t = 0.0
    x, y = X0, Y0
    vx, vy = VX0, VY0

    t_list = [t]
    x_list = [x]
    y_list = [y]
    e_list = [compute_energy(x, y, vx, vy)]

    while t < t_max:
        ax, ay, _ = compute_acceleration(x, y)

        # Explicit Euler: position updated using OLD velocity
        new_x = x + vx * dt
        new_y = y + vy * dt

        # Velocity updated using OLD acceleration
        new_vx = vx + ax * dt
        new_vy = vy + ay * dt

        x, y = new_x, new_y
        vx, vy = new_vx, new_vy
        t += dt

        t_list.append(t)
        x_list.append(x)
        y_list.append(y)
        e_list.append(compute_energy(x, y, vx, vy))

    return t_list, x_list, y_list, e_list


def simulate_euler_semi_implicit(dt=0.001, t_max=5.0):
    """
    Semi-implicit Euler (Euler-Cromer) method:
    v_{n+1} = v_n + a_n * dt
    x_{n+1} = x_n + v_{n+1} * dt
    """
    t = 0.0
    x, y = X0, Y0
    vx, vy = VX0, VY0

    t_list = [t]
    x_list = [x]
    y_list = [y]
    e_list = [compute_energy(x, y, vx, vy)]

    while t < t_max:
        ax, ay, _ = compute_acceleration(x, y)

        # Semi-implicit Euler: velocity updated FIRST
        vx += ax * dt
        vy += ay * dt

        # Position updated using NEW velocity
        x += vx * dt
        y += vy * dt
        t += dt

        t_list.append(t)
        x_list.append(x)
        y_list.append(y)
        e_list.append(compute_energy(x, y, vx, vy))

    return t_list, x_list, y_list, e_list


if __name__ == "__main__":
    dt = 0.001
    t_max = 5.0

    print("Running Explicit Euler...")
    t_exp, x_exp, y_exp, e_exp = simulate_euler_explicit(dt=dt, t_max=t_max)

    print("Running Semi-Implicit Euler...")
    t_semi, x_semi, y_semi, e_semi = simulate_euler_semi_implicit(dt=dt, t_max=t_max)

    # Print quantitative summary
    exact_energy = -2 * math.pi**2
    print("\n--- Summary after 5 orbits (5 years) ---")
    print(f"Exact Theoretical Energy: {exact_energy:.4f}")
    print(f"Explicit Euler Energy:      initial = {e_exp[0]:.4f}, final = {e_exp[-1]:.4f}, drift = {e_exp[-1] - e_exp[0]:+.4f}")
    print(f"Semi-Implicit Euler Energy: initial = {e_semi[0]:.4f}, final = {e_semi[-1]:.4f}, drift = {e_semi[-1] - e_semi[0]:+.4f}")

    # Plot comparison
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

    # 1. Trajectory comparison
    ax1.plot(0, 0, 'yo', markersize=14, label="Sun")
    ax1.plot(x_exp, y_exp, 'r--', label="Explicit Euler (spirals out)", alpha=0.8)
    ax1.plot(x_semi, y_semi, 'b-', label="Semi-Implicit Euler (stable)", alpha=0.8)
    ax1.set_aspect('equal')
    ax1.grid(True)
    ax1.set_xlabel("X (AU)")
    ax1.set_ylabel("Y (AU)")
    ax1.set_title("Orbital Trajectory (5 years)")
    ax1.legend()

    # 2. Energy drift comparison
    ax2.plot(t_exp, e_exp, 'r--', label="Explicit Euler (energy diverges)")
    ax2.plot(t_semi, e_semi, 'b-', label="Semi-Implicit Euler (oscillating, bounded)")
    ax2.axhline(exact_energy, color='k', linestyle=':', label=f"Exact Energy ({exact_energy:.2f})")
    ax2.grid(True)
    ax2.set_xlabel("Time (years)")
    ax2.set_ylabel("Total Mechanical Energy E")
    ax2.set_title("Energy Drift Comparison")
    ax2.legend()

    plt.tight_layout()
    plt.savefig("outputs/euler_comparison.png", dpi=150)
    print("\nComparison plot saved to outputs/euler_comparison.png")
    plt.show()