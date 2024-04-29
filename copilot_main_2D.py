import numpy as np
import matplotlib.pyplot as plt

def z(x, y, B, λ):
    return B * (np.cos(np.pi * 2 * x / λ) * np.cos(np.pi * 2 * y / λ))

atom_lattice = 2
tip_lattice = 3
atom_limit = 1000
radius_multiple = np.linspace(1, 30, 30)

max_min_potentials = []

B = 0.01
λ = atom_lattice

tip_base = [(x, y) for s in (1, -1) for x in np.arange(tip_lattice, atom_limit, tip_lattice) for y in np.arange(tip_lattice, atom_limit, tip_lattice)]
tip_base.insert(0, (0.0, 0.0))

for radius_multiplier in radius_multiple:
    radius = tip_lattice * radius_multiplier
    z_values = []

    for x_start in np.arange(0, atom_lattice, 0.1):
        for y_start in np.arange(0, atom_lattice, 0.1):
            z_values_sum = sum([z(x_start + x, y_start + y, B, λ) for x, y in tip_base if np.sqrt((x_start + x) ** 2 + (y_start + y) ** 2) <= radius])
            z_values.append(z_values_sum)

    max_min_potentials.append(max(z_values) - min(z_values))

plt.figure(figsize=(10, 6))
plt.plot(radius_multiple * tip_lattice, max_min_potentials, marker='o')
plt.xlabel('Radius')
plt.ylabel('Max-Min Potential')
plt.title('Radius vs. Max-Min Potential')
plt.grid(True)
plt.show()
