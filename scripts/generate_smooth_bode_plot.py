import numpy as np
import matplotlib.pyplot as plt

# Parameters
a = 100  # Corner frequency
omega = np.logspace(0, 4, 1000)  # Frequency range from 1 to 10000

# Magnitude calculations
# H(s) = 1 + s/a
h_exact_mag_db = 20 * np.log10(np.sqrt(1 + (omega/a)**2))

# Asymptotic approximation
h_asymp_mag_db = np.zeros_like(omega)
h_asymp_mag_db[omega > a] = 20 * np.log10(omega[omega > a] / a)

# Create plot
plt.figure(figsize=(8, 6))

# Plot exact and asymptotic
plt.semilogx(omega, h_exact_mag_db, 'b-', linewidth=2, label='Exact Response')
plt.semilogx(omega, h_asymp_mag_db, 'r--', linewidth=2, label='Asymptotic Approximation')

# Key frequencies for error marking
freqs = [0.5 * a, a, 2 * a]
colors = ['green', 'purple', 'green']
labels = ['+1 dB Error', '+3 dB Error', '+1 dB Error']

for f, c, l in zip(freqs, colors, labels):
    # Calculate values at these points
    idx = (np.abs(omega - f)).argmin()
    y_exact = h_exact_mag_db[idx]
    y_asymp = h_asymp_mag_db[idx]
    
    # Draw vertical error line
    plt.vlines(f, y_asymp, y_exact, colors=c, linestyles='-', linewidth=2)
    
    # Add text label for the error
    plt.text(f, (y_asymp + y_exact)/2, f'  {l}', color=c, fontweight='bold', ha='left', va='center')
    
    # Mark points separately with color and marker
    plt.plot(f, y_exact, marker='o', color=c, markersize=6)
    plt.plot(f, y_asymp, marker='x', color=c, markersize=6)

# Formatting
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.xlabel(r'Frequency $\omega$ (rad/s)')
plt.ylabel(r'Magnitude $H_{dB}$ (dB)')
plt.title(r'Bode Magnitude Plot: Error vs. Asymptote ($H(s) = 1 + s/a$)')
plt.legend()

# Custom ticks for frequency relative to a
ticks = [1, 10, 50, 100, 200, 1000, 10000]
tick_labels = ['1', '10', '0.5a', 'a', '2a', '10a', '100a']
plt.xticks(ticks, tick_labels)

plt.tight_layout()

# Save the plot
plt.savefig('public/smooth_bode_plot.png', dpi=300)
print("Successfully generated public/smooth_bode_plot.png")
