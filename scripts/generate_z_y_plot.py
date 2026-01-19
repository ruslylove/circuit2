import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'

alpha = 3
wd = 4
w0_sq = alpha**2 + wd**2
w0 = np.sqrt(w0_sq) # 5.0

# Avoid 0 to avoid division by zero
freqs = np.linspace(0.1, 10, 500)
s = 1j * freqs

# Z(s) = s / (s^2 + 2*alpha*s + w0_sq)  (Assuming C=1, normalized)
# Y(s) = 1/Z(s)

Z_vals = s / (s**2 + 2*alpha*s + w0_sq)
Z_mag = np.abs(Z_vals)

Y_vals = 1/Z_vals
Y_mag = np.abs(Y_vals)

fig, ax1 = plt.subplots(figsize=(8, 5))

# Plot Z (Impedance)
color = 'tab:blue'
ax1.set_xlabel(r'Frequency $\omega$ (rad/s)')
ax1.set_ylabel(r'$|Z(j\omega)|$ ($\Omega$)', color=color)
ax1.plot(freqs, Z_mag, color=color, linewidth=2.5, label=r'$|Z(j\omega)|$')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(0, np.max(Z_mag)*1.2)
ax1.grid(True, linestyle=':', alpha=0.6)

# Annotate Peak Z
peak_Z = np.max(Z_mag)
ax1.plot([w0, w0], [0, peak_Z], color='k', linestyle='--', alpha=0.5)
ax1.scatter([w0], [peak_Z], color=color, zorder=5, s=50)
ax1.text(w0+0.2, peak_Z, r'Max $|Z| = R$', color=color, fontsize=12, fontweight='bold')

# Plot Y (Admittance) on secondary axis
ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel(r'$|Y(j\omega)|$ (S)', color=color)
ax2.plot(freqs, Y_mag, color=color, linewidth=2.5, linestyle='-.', label=r'$|Y(j\omega)|$')
ax2.tick_params(axis='y', labelcolor=color)
# Set ylim to show the "valley" clearly. High values at edges are large.
ax2.set_ylim(0, np.max(Y_mag[freqs>1])*1.5) 

# Annotate Min Y
min_Y = 2*alpha # |Y(w0)| = 2*alpha
ax2.scatter([w0], [min_Y], color=color, zorder=5, s=50)
# Offset text slightly to avoid overlap if close
ax2.text(w0+0.2, min_Y + 1, r'Min $|Y| = 1/R$', color=color, fontsize=12, fontweight='bold')

ax1.set_title(r'Impedance $|Z|$ vs Admittance $|Y|$ Resonance Characteristics')
ax1.set_xlim(0, 10)

plt.tight_layout()
plt.savefig('public/z_y_plot.png', dpi=150)
print("Saved public/z_y_plot.png")
