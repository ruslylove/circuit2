import numpy as np
import matplotlib.pyplot as plt

# Parameters
K = 50
a = 50
omega = np.logspace(0, 4, 1000)

# Magnitude calculations
k_db = 20 * np.log10(K)

# Separate Asymptotes
asymp_k = np.full_like(omega, k_db)
asymp_zero = np.zeros_like(omega)
asymp_zero[omega > a] = 20 * np.log10(omega[omega > a] / a)

# Composite Asymptote
asymp_composite = asymp_k + asymp_zero

# Create plot
plt.figure(figsize=(8, 6))

# Plot components
plt.semilogx(omega, asymp_k, color='gray', linestyle='--', linewidth=1.2, label=f'Gain $K={K}$')
plt.semilogx(omega, asymp_zero, color='darkorange', linestyle='--', linewidth=1.2, label=f'Zero at $\omega={a}$')
plt.semilogx(omega, asymp_composite, color='red', linestyle='-', linewidth=2.5, label='Composite Asymptotic')

# Highlight corner frequency
plt.axvline(x=a, color='gray', linestyle='--', alpha=0.4)
plt.text(a, k_db - 10, fr' $\omega = {a}$', color='gray', ha='left')

# Annotations
plt.text(1.2, k_db + 2, f'{k_db:.1f} dB', color='red', fontweight='bold')
plt.text(a * 4, k_db + 15, r'+20 dB/dec', color='red', fontweight='bold', rotation=30)

# Formatting
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.xlabel(r'Frequency $\omega$ (rad/s)')
plt.ylabel(r'Magnitude $|H(j\omega)|_{dB}$ (dB)')
plt.title(r'Bode Magnitude Plot (Practice 16.11)')
plt.legend(loc='lower right')
plt.ylim(0, 80)

plt.tight_layout()
plt.savefig('public/prac_16_11_bode.svg', format='svg')
print("Successfully generated public/prac_16_11_bode.svg")
