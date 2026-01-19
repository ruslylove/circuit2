import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'

# Parameters
alpha = 3
wd = 4
w0_sq = alpha**2 + wd**2

def Z_mag(sigma, omega):
    s = np.asarray(sigma + 1j * omega)
    # Avoid division by zero at poles
    denom = s**2 + 2*alpha*s + w0_sq
    denom = np.where(np.abs(denom) < 1e-6, 1e-6, denom)
    Z = s / denom
    return np.abs(Z)

# Grid
sigma = np.linspace(-6, 2, 200)
omega = np.linspace(-8, 8, 200)
Sigma, Omega = np.meshgrid(sigma, omega)
Z_vals = Z_mag(Sigma, Omega)

# Cap for better color resolution near peaks
Z_vals[Z_vals > 5] = 5

fig, ax = plt.subplots(figsize=(10, 8))

# Heatmap
# levels = np.linspace(0, 5, 20)
c = ax.contourf(Sigma, Omega, Z_vals, levels=50, cmap='viridis', extend='max')
fig.colorbar(c, ax=ax, label=r'$|Z(s)|$')

# Contours
ax.contour(Sigma, Omega, Z_vals, levels=10, colors='white', alpha=0.3, linewidths=0.5)

# Axis markers
ax.axhline(0, color='white', linestyle=':', alpha=0.5)
ax.axvline(0, color='white', linestyle='-', linewidth=1.5) # jw axis

# Poles and Zeros
ax.scatter([-alpha, -alpha], [wd, -wd], color='red', marker='x', s=100, label='Poles', zorder=5)
ax.scatter([0], [0], color='cyan', marker='o', s=100, facecolors='none', edgecolors='cyan', linewidth=2, label='Zero', zorder=5)

# Annotate wd and w0
ax.scatter([0], [wd], color='orange', marker='s', s=30, zorder=5)
ax.text(0.2, wd, r'$j\omega_d$', color='orange', fontsize=12)

ax.scatter([0], [np.sqrt(w0_sq)], color='magenta', marker='^', s=50, zorder=5)
ax.text(0.2, np.sqrt(w0_sq), r'$j\omega_0$ (Peak)', color='magenta', fontsize=12, fontweight='bold')

ax.set_xlabel(r'$\sigma$')
ax.set_ylabel(r'$j\omega$')
ax.set_title(r'S-Plane Heatmap of $|Z(s)|$')
ax.legend(loc='upper right', framealpha=0.9)

plt.savefig('public/s_plane_heatmap.png', dpi=150, bbox_inches='tight')
print("Saved public/s_plane_heatmap.png")
