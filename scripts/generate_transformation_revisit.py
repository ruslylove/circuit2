import numpy as np
import matplotlib.pyplot as plt

def get_low_q_data():
    # Ex 16.4 Parameters
    R1, L = 2, 1
    C, R2 = 0.125, 3
    w0 = 2  # target frequency for transformation
    
    # Transformation (Exact at w0)
    Qs = (w0 * L) / R1 # Qs = 1
    Rp_prime = R1 * (1 + Qs**2) # 4
    Lp = L * (1 + 1/Qs**2) # 2
    Rp_total = (R2 * Rp_prime) / (R2 + Rp_prime) # 1.714
    
    w = np.linspace(0.1, 10, 1000)
    
    # Actual Response
    Y_actual = 1/R2 + 1j*w*C + 1/(R1 + 1j*w*L)
    Z_actual = 1/Y_actual
    
    # Simplified Ideal Model (Fixed components)
    Y_ideal = 1/Rp_total + 1j*w*C + 1/(1j*w*Lp)
    Z_ideal = 1/Y_ideal
    
    return w, np.abs(Z_actual), np.abs(Z_ideal), w0

def get_high_q_data():
    # Practice 16.5 Parameters
    R1 = 1000
    L = 10e-3
    C = 2.533e-12
    w0 = 2 * np.pi * 1e6
    
    # Transformation (Exact at w0)
    Qs = (w0 * L) / R1 # ~62.8
    Rp_total = R1 * (1 + Qs**2) # No R2 in this problem
    Lp = L * (1 + 1/Qs**2)
    
    f = np.linspace(0.95e6, 1.05e6, 1000)
    w = 2 * np.pi * f
    
    # Actual Response
    Y_actual = 1j*w*C + 1/(R1 + 1j*w*L)
    Z_actual = 1/Y_actual
    
    # Simplified Ideal Model
    Y_ideal = 1/Rp_total + 1j*w*C + 1/(1j*w*Lp)
    Z_ideal = 1/Y_ideal
    
    return f, np.abs(Z_actual), np.abs(Z_ideal), 1e6

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot Low-Q
w, za, zi, w0 = get_low_q_data()
ax1.plot(w, za, 'b-', label='Actual Model (Low-Q)')
ax1.plot(w, zi, 'r--', label='Ideal Shortcut')
ax1.axvline(x=w0, color='k', linestyle=':', alpha=0.5, label=r'$\omega_0$')
ax1.set_title(r'Ex 16.4: Low-Q ($Q \approx 1$)')
ax1.set_xlabel(r'Frequency $\omega$ (rad/s)')
ax1.set_ylabel(r'Impedance $|Z|$ ($\Omega$)')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Plot High-Q
f, za, zi, f0 = get_high_q_data()
ax2.plot(f/1e6, za/1e3, 'b-', label='Actual Model (High-Q)')
ax2.plot(f/1e6, zi/1e3, 'r--', label='Ideal Shortcut')
ax2.axvline(x=f0/1e6, color='k', linestyle=':', alpha=0.5, label='$f_0$')
ax2.set_title(r'Prac 16.5: High-Q ($Q \approx 63$)')

ax2.set_xlabel('Frequency $f$ (MHz)')
ax2.set_ylabel(r'Impedance $|Z|$ (k$\Omega$)')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('public/transformation_comparison_plots.png', dpi=300)
print("Comparison plot saved to public/transformation_comparison_plots.png")
