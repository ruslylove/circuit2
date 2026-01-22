import numpy as np
import matplotlib.pyplot as plt

# Parameters
a = 100
omega = np.logspace(0, 4, 1000)

# Phase calculation (Exact)
# H(s) = 20(1 + s/100) -> Phase is just arg(1 + jw/100)
phase_exact = np.arctan(omega / a) * 180 / np.pi

# Asymptotic construction
omega_asymp = [omega[0], 0.1 * a, 10 * a, omega[-1]]
phase_asymp = [0, 0, 90, 90]

# Create plot
plt.figure(figsize=(8, 6))

# Plot components
plt.semilogx(omega, phase_exact, 'b-', linewidth=2, label=r'Exact Phase $\arg(1 + j\omega/100)$')
plt.semilogx(omega_asymp, phase_asymp, 'r--', linewidth=2.5, label='Asymptotic Approximation')

# Highlight key points
key_omegas = [0.1 * a, a, 10 * a]
key_vals = [0, 45, 90]
for om, val in zip(key_omegas, key_vals):
    plt.plot(om, val, 'ro', markersize=6)
    plt.axvline(x=om, color='gray', linestyle=':', alpha=0.5)

# Marking 45 degrees
plt.axhline(y=45, color='gray', linestyle=':', alpha=0.5)
plt.yticks([0, 15, 30, 45, 60, 75, 90])

# Annotations
plt.text(a * 1.1, 40, r'$45^\circ$', color='red', fontweight='bold')
plt.annotate(r'slope = $45^\circ$/dec', xy=(a, 45), xytext=(a*2, 20),
             arrowprops=dict(arrowstyle='->', color='red'), color='red', fontweight='bold')

# Formatting
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.xlabel(r'Frequency $\omega$ (rad/s)')
plt.ylabel(r'Phase $\angle H(j\omega)$ (degrees)')
plt.title(r'Bode Phase Plot (Practice 16.12)')
plt.legend(loc='upper left')

plt.tight_layout()
plt.savefig('public/prac_16_12_phase.svg', format='svg')
print("Successfully generated public/prac_16_12_phase.svg")
