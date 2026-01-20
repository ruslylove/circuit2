import numpy as np
import matplotlib.pyplot as plt

# Parameters for Example 16.5
Rs = 5
Ls = 0.1
w_trans = 1000  # Transformation frequency

# Calculated Parallel Equivalent (at 1000 rad/s)
# Q = 1000 * 0.1 / 5 = 20
# Rp = 5 * (1 + 20^2) = 2005 (Exact)
# Lp = 0.1 * (1 + 1/20^2) = 0.10025 (Exact)
Rp = 2005
Lp = 0.10025

# Frequency range
w = np.linspace(500, 1500, 500)

# Actual Series Impedance
Zs = Rs + 1j * w * Ls
mag_Zs = np.abs(Zs)

# Fixed Parallel Equivalent Impedance (computed at w_trans)
Zp = 1 / (1/Rp + 1/(1j * w * Lp))
mag_Zp = np.abs(Zp)

# Error percentage
error = np.abs(mag_Zs - mag_Zp) / mag_Zs * 100

# Plotting
fig, ax1 = plt.subplots(figsize=(8, 5))

# Magnitude Plot
color = 'tab:blue'
ax1.set_xlabel(r'Frequency $\omega$ (rad/s)')
ax1.set_ylabel(r'Impedance Magnitude $|Z|$ ($\Omega$)', color=color)

ax1.plot(w, mag_Zs, 'b-', label='Actual Series ($Z_s$)')
ax1.plot(w, mag_Zp, 'r--', label='Fixed Equiv Parallel ($Z_p$)')
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend(loc='upper left')

# Error Plot
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Magnitude Error (%)', color=color)
ax2.plot(w, error, color=color, alpha=0.3, label='Error (%)')
ax2.tick_params(axis='y', labelcolor=color)

# Mark transformation frequency
ax1.axvline(x=w_trans, color='k', linestyle=':', alpha=0.5)
ax1.text(w_trans+20, 10, 'Transformation Frequency', rotation=90, verticalalignment='bottom')

plt.title('Transformation Error vs. Frequency (Ex 16.5)')
fig.tight_layout()

plt.savefig('public/transformation_sensitivity.png', dpi=300)
print(f"Plot saved to public/transformation_sensitivity.png")
print(f"Error at 1000 rad/s: {error[np.argmin(np.abs(w-1000))]:.4f}%")
print(f"Error at 500 rad/s: {error[0]:.4f}%")
print(f"Error at 1500 rad/s: {error[-1]:.4f}%")
