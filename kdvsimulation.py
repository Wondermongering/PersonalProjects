import numpy as np
import matplotlib.pyplot as plt

def kdv(u, dx):
    # Finite difference approximations
    u_x = np.roll(u, -1) - np.roll(u, 1) / (2*dx)      # Central difference for first derivative
    u_xx = np.roll(u, -1) - 2*u + np.roll(u, 1) / dx**2  # Central difference for second derivative
    u_xxx = np.roll(u, -1) - 3*u + 3*np.roll(u, 1) - np.roll(u, 2) / dx**3  # Central difference for third derivative
    
    # KdV equation
    return -6 * u * u_x + u_xxx

# Spatial domain
L = 100
N = 256
dx = L/N
x = np.linspace(0, L, N, endpoint=False)

# Initial condition
u = np.sin(x/2)**2

# Time settings
dt = 0.001
Tmax = 2
iterations = int(Tmax/dt)
save_every = 10

# The line u += kdv(u, dx) * dt is a discrete approximation of the continuous behavior of the KdV equation over a small time interval dt. It uses the method of lines, where the spatial derivatives are approximated using finite differences (as done in kdv(u, dx)), and the time integration is approximated using a forward Euler method. The new value of u at each spatial point is the old value plus the estimated change over the time step dt.
# Time-stepping loop
plt.figure()
for n in range(iterations):
    u += kdv(u, dx) * dt
    
    # Normalization (can be commented out if not needed)
    u /= np.max(u)

    # Check stability condition
    if np.isnan(u).any():
        print(f"Simulation became unstable at iteration {n}")
        break

    # Plot intermediate steps
    if n % save_every == 0:
        plt.plot(x, u, label=f'T={n*dt:.2f}')

# Plot settings
plt.legend()
plt.title('KdV Equation Simulation')
plt.xlabel('x')
plt.ylabel('u')
plt.grid(True)
plt.show()
