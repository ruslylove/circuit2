import numpy as np
import matplotlib.pyplot as plt

# Parameters for Example 16.4
R1 = 2
L = 1
C = 0.125
R2 = 3

# Resonant frequency calculation
w0 = np.sqrt(1/(L*C) - (R1/L)**2)
print(f"Resonant frequency (w0): {w0}")

# Frequency range
w = np.linspace(0.1, 10, 1000)

def calculate_impedance(w):
    Y = 1/R2 + 1j*w*C + 1/(R1 + 1j*w*L)
    Z = 1/Y
    return np.abs(Z)

mag_Z = calculate_impedance(w)

# Find maximum impedance and its frequency (wm)
idx_max = np.argmax(mag_Z)
wm = w[idx_max]
Zmax = mag_Z[idx_max]

# Impedance at resonance (w0)
Z_at_w0 = calculate_impedance(w0)

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(w, mag_Z, 'b-', linewidth=2, label=r'$|Z(\omega)|$')

# Mark w0
plt.axvline(x=w0, color='r', linestyle='--', alpha=0.6)
plt.plot(w0, Z_at_w0, 'ro')
plt.annotate(fr'Resonance: $\omega_0 = {w0:.1f}$' + '\n' + fr'$|Z| = {Z_at_w0:.3f}\Omega$', 
             xy=(w0, Z_at_w0), xytext=(w0-1.8, Z_at_w0+0.5),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))

# Mark wm
plt.axvline(x=wm, color='g', linestyle='--', alpha=0.6)
plt.plot(wm, Zmax, 'go')
plt.annotate(fr'Max: $\omega_m = {wm:.2f}$' + '\n' + fr'$|Z|_{{max}} = {Zmax:.3f}\Omega$', 
             xy=(wm, Zmax), xytext=(wm+1, Zmax-0.4),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))


plt.title('Example 16.4: Impedance Magnitude vs. Frequency')
plt.xlabel(r'Frequency $\omega$ (rad/s)')
plt.ylabel(r'Impedance $|Z|$ ($\Omega$)')

plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.tight_layout()

plt.savefig('public/example_16_4_plot.png', dpi=300)
print(f"Plot saved to public/example_16_4_plot.png")
print(f"wm = {wm}, Zmax = {Zmax}")
