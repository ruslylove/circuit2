import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Use LaTeX for text rendering
plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'

# Parameters
alpha = 3
wd = 4
w0_sq = alpha**2 + wd**2
# Y(s) ~ (s^2 + s/RC + 1/LC) / s 
# Normalize C=1. 2alpha = 1/RC, w0^2 = 1/LC
# Y(s) = (s^2 + 2*alpha*s + w0_sq) / s
# Z(s) = s / (s^2 + 2*alpha*s + w0_sq)

def Z_mag(sigma, omega):
    s = np.asarray(sigma + 1j * omega)
    # Avoid division by zero at poles
    denom = s**2 + 2*alpha*s + w0_sq
    # Add small epsilon to avoid infinity for plotting
    denom = np.where(np.abs(denom) < 1e-6, 1e-6, denom)
    Z = s / denom
    return np.abs(Z)

# Grid
sigma = np.linspace(-6, 2, 100)
omega = np.linspace(-6, 6, 100)
Sigma, Omega = np.meshgrid(sigma, omega)

Z_magnitude = Z_mag(Sigma, Omega)
# Cap the magnitude for better visualization
Z_magnitude[Z_magnitude > 5] = 5

fig = plt.figure(figsize=(14, 8))

# -----------------
# 1. 3D Surface Plot (Main)
# -----------------
# Position: [left, bottom, width, height]
# Leave space on the right for the inset
ax1 = fig.add_axes([0.02, 0.1, 0.7, 0.85], projection='3d')
surf = ax1.plot_surface(Sigma, Omega, Z_magnitude, cmap=cm.viridis,
                       linewidth=0.3, edgecolors='k', antialiased=True, alpha=0.9, rcount=40, ccount=40)

ax1.set_xlabel(r'$\sigma$')
ax1.set_ylabel(r'$j\omega$')
ax1.set_zlabel(r'$|Z(s)|$')
ax1.set_title(r'S-Plane Surface of $|Z(s)|$')
ax1.view_init(elev=30, azim=-60)

# Highlight Poles and Zero
ax1.scatter([-alpha, -alpha], [wd, -wd], [5, 5], color='r', s=50, label='Poles', depthshade=False)
ax1.scatter([0], [0], [0], color='b', s=50, label='Zero', depthshade=False)

# Highlight the Cross-section (jw axis, sigma=0)
omega_line = np.linspace(-6, 6, 200)
sigma_line = np.zeros_like(omega_line)
Z_line = Z_mag(sigma_line, omega_line)
Z_line[Z_line > 5] = 5 # Cap it same as surface

ax1.plot(sigma_line, omega_line, Z_line, color='purple', linewidth=3, label=r'$\sigma=0$ (freq resp)')

# -----------------
# 2. Frequency Response (Bottom Right Inset)
# -----------------
# Position: Bottom Right, separated
ax2 = fig.add_axes([0.75, 0.1, 0.22, 0.3]) 
freqs = np.linspace(-8, 8, 400)
Z_freq_resp = Z_mag(0, freqs)

ax2.plot(freqs, Z_freq_resp, linewidth=2, color='purple')
ax2.set_xlabel(r'$\omega$')
ax2.set_ylabel(r'$|Z|$')
ax2.set_title(r'Cross-section ($\sigma=0$)', fontsize=10)
ax2.grid(True, linestyle=':', alpha=0.6)

# Mark resonant frequency w0 and -w0
w0 = np.sqrt(w0_sq)
for w in [w0, -w0]:
    Z_at_w = Z_mag(0, w)
    ax2.plot([w, w], [0, Z_at_w], 'r--', alpha=0.7)
    ax2.scatter([w], [Z_at_w], color='r', s=10)
    
# -----------------
# 3. Heatmap (Top Right Inset)
# -----------------
# Position: Top Right
ax3 = fig.add_axes([0.75, 0.55, 0.22, 0.3])
# Lower dynamic range for heatmap to see low values better
Z_heatmap = Z_magnitude.copy()
Z_heatmap[Z_heatmap > 2.0] = 2.0
c = ax3.contourf(Sigma, Omega, Z_heatmap, levels=50, cmap='viridis', extend='max')
ax3.contour(Sigma, Omega, Z_heatmap, levels=10, colors='white', alpha=0.3, linewidths=0.5)

# Axis markers
ax3.axhline(0, color='white', linestyle=':', alpha=0.5)
ax3.axvline(0, color='white', linestyle='-', linewidth=1)

# Poles(x) and Zero(o) on Heatmap
ax3.scatter([-alpha, -alpha], [wd, -wd], color='red', marker='x', s=20)
ax3.scatter([0], [0], color='cyan', marker='o', s=20, facecolors='none', edgecolors='cyan', linewidth=1)

ax3.set_title(r'Top-down Heatmap', fontsize=10)
ax3.set_xlabel(r'$\sigma$', fontsize=8)
ax3.set_ylabel(r'$j\omega$', fontsize=8)
ax3.tick_params(labelsize=8)

# Mark bandwidth frequencies (70.7% of max) - REMOVED as per request
# max_Z = np.max(Z_freq_resp)
# w_bandwidth = freqs[Z_freq_resp >= 0.707 * max_Z]
# ...

plt.tight_layout()
plt.savefig('public/s_plane_surface.png', dpi=150, bbox_inches='tight')
print("Plot saved to public/s_plane_surface.png")
