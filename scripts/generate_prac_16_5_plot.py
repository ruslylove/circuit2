import numpy as np
import matplotlib.pyplot as plt

# Parameters for Practice 16.5
R1 = 1000       # 1 kOhm
C = 2.533e-12   # 2.533 pF
L = 10e-3       # 10 mH
f0_target = 1e6 # 1 MHz

# Exact calculations
w0 = np.sqrt(1/(L*C) - (R1/L)**2)
f0 = w0 / (2*np.pi)

# Frequency range around 1 MHz (narrow range because Q is high)
f = np.linspace(0.95e6, 1.05e6, 2000)
w = 2 * np.pi * f

def calculate_impedance(w):
    # Practice 16.5 has no R2 mentioned, assuming parallel R is infinite or just R1+L in parallel with C
    # The wording "RLC Parallel circuit" and "R1 = 1k" implies the practical model Fig 16.9a
    # where R1 is in series with L, and that whole branch is in parallel with C.
    Y = 1j*w*C + 1/(R1 + 1j*w*L)
    Z = 1/Y
    return np.abs(Z)

mag_Z = calculate_impedance(w)

# Find maximum impedance and its frequency (fm)
idx_max = np.argmax(mag_Z)
fm = f[idx_max]
Zmax = mag_Z[idx_max]

# Impedance at resonance (f0)
Z_at_f0 = calculate_impedance(w0)

# Calculate Q0
Q0 = (w0 * L) / R1

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(f/1e6, mag_Z/1e3, 'b-', linewidth=2, label=r'$|Z(f)|$')

# Mark f0
plt.axvline(x=f0/1e6, color='r', linestyle='--', alpha=0.6)
plt.plot(f0/1e6, Z_at_f0/1e3, 'ro')

# Mark fm
plt.plot(fm/1e6, Zmax/1e3, 'g.', alpha=0.5)

# Annotate
plt.annotate(fr'Resonance: $f_0 \approx {f0/1e6:.4f}$ MHz' + '\n' + fr'Max Resp: $f_m \approx {fm/1e6:.4f}$ MHz' + '\n' + fr'$Q_0 \approx {Q0:.1f}$', 
             xy=(f0/1e6, Z_at_f0/1e3), xytext=(f0/1e6 + 0.015, Z_at_f0/1e3 * 0.8),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))

plt.title(r'Practice 16.5: Impedance Magnitude (High-Q, $Q_0 \approx 63$)')
plt.xlabel('Frequency $f$ (MHz)')
plt.ylabel(r'Impedance $|Z|$ (k$\Omega$)')
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()

plt.savefig('public/practice_16_5_plot.png', dpi=300)
print(f"Plot saved to public/practice_16_5_plot.png")
print(f"f0 = {f0/1e6} MHz, fm = {fm/1e6} MHz, Q0 = {Q0}")
