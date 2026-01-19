import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'

# Parameters
alpha = 3
wd = 4
w0_sq = alpha**2 + wd**2
w0 = np.sqrt(w0_sq)

def Z_mag(sigma, omega):
    s = np.asarray(sigma + 1j * omega)
    denom = s**2 + 2*alpha*s + w0_sq
    denom = np.where(np.abs(denom) < 1e-6, 1e-6, denom)
    Z = s / denom
    return np.abs(Z)

fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# 1. Plot Surface (Faint)
sigma = np.linspace(-6, 2, 80)
omega = np.linspace(0, 8, 80) # Focus on top half
Sigma, Omega = np.meshgrid(sigma, omega)
Z_vals = Z_mag(Sigma, Omega)
Z_vals[Z_vals > 5] = 5

ax.plot_surface(Sigma, Omega, Z_vals, cmap=cm.viridis, alpha=0.3, linewidth=0, antialiased=False)

# 2. Draw jw axis line
w_line = np.linspace(0, 8, 100)
z_line = Z_mag(0, w_line)
ax.plot(np.zeros_like(w_line), w_line, z_line, color='purple', linewidth=3, label='Frequency Response')

# 3. Poles and Zero locations
p1_real, p1_imag = -alpha, wd
ax.scatter([p1_real], [p1_imag], [0], color='r', s=100, marker='x', label='Pole')
ax.scatter([0], [0], [0], color='b', s=100, marker='o', label='Zero')

# 4. Helper function to draw vectors for a specific freq w_target
def visualize_at_freq(w_target, color, label_prefix):
    # Target point on jw axis
    target = np.array([0, w_target, 0])
    
    # Pole location
    pole = np.array([p1_real, p1_imag, 0])
    # Zero location
    zero = np.array([0, 0, 0])
    
    # Draw Vector from Pole to Target
    ax.quiver(pole[0], pole[1], pole[2], 
              target[0]-pole[0], target[1]-pole[1], target[2]-pole[2],
              color=color, linestyle='--', arrow_length_ratio=0.05, alpha=0.8)
              
    # Draw Vector from Zero to Target
    ax.quiver(zero[0], zero[1], zero[2], 
              target[0]-zero[0], target[1]-zero[1], target[2]-zero[2],
              color=color, linestyle='-', arrow_length_ratio=0.05, alpha=0.8)

    # Height line
    z_height = Z_mag(0, w_target)
    ax.plot([0, 0], [w_target, w_target], [0, z_height], color=color, linestyle=':', linewidth=2)
    ax.scatter([0], [w_target], [z_height], color=color, s=50)
    
    ax.text(0.5, w_target, z_height, f"{label_prefix}\n$|Z|={z_height:.2f}$", color=color, fontsize=12, fontweight='bold')

# Visualize at wd=4
visualize_at_freq(4, 'red', r'$\omega_d=4$')

# Visualize at w0=5
visualize_at_freq(5, 'green', r'$\omega_0=5$ (Peak)')

ax.set_xlabel(r'$\sigma$')
ax.set_ylabel(r'$j\omega$')
ax.set_zlabel(r'$|Z(s)|$')
ax.set_title(r'3D Visualization of Vectors at $\omega_d$ vs $\omega_0$')
ax.view_init(elev=20, azim=-10)

plt.savefig('public/vector_explanation_3d.png', dpi=150, bbox_inches='tight')
print("Saved public/vector_explanation_3d.png")
