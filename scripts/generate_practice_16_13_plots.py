import numpy as np
import matplotlib.pyplot as plt

def setup_plot(title):
    plt.figure(figsize=(8, 6))
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.xlabel(r'Frequency $\omega$ (rad/s)')
    plt.ylabel(r'Magnitude $|H(j\omega)|_{dB}$ (dB)')
    plt.title(title)

def save_plot(filename):
    plt.legend(loc='best')
    plt.tight_layout()
    plt.savefig(f'public/{filename}', format='svg')
    print(f"Generated public/{filename}")
    plt.close()

omega = np.logspace(0, 4, 1000)

# (a) H(s) = 50 / (s + 100)
# K = 50/100 = 0.5 => -6 dB
# Pole at 100
setup_plot(r'Practice 16.13(a): $H(s) = 50/(s+100)$')
k_db_a = 20 * np.log10(0.5)
asymp_a = np.zeros_like(omega)
asymp_a[omega <= 100] = k_db_a
asymp_a[omega > 100] = k_db_a - 20 * np.log10(omega[omega > 100] / 100)
exact_a = 20 * np.log10(50 / np.sqrt(omega**2 + 100**2))

plt.semilogx(omega, asymp_a, 'r--', linewidth=2, label='Asymptotic')
plt.semilogx(omega, exact_a, 'b-', linewidth=2, label='Exact')
plt.ylim(-60, 10)
save_plot('practice_16_13_a.svg')

# (b) H(s) = (s + 10) / (s + 100)
# K = 10/100 = 0.1 => -20 dB
# Zero at 10, Pole at 100
setup_plot(r'Practice 16.13(b): $H(s) = (s+10)/(s+100)$')
k_db_b = 20 * np.log10(0.1)
asymp_b = np.zeros_like(omega)
asymp_b[omega <= 10] = k_db_b
mask_mid = (omega > 10) & (omega <= 100)
asymp_b[mask_mid] = k_db_b + 20 * np.log10(omega[mask_mid] / 10)
asymp_b[omega > 100] = k_db_b + 20 * np.log10(100/10) # 0 dB
exact_b = 20 * np.log10(np.sqrt(omega**2 + 10**2) / np.sqrt(omega**2 + 100**2))

plt.semilogx(omega, asymp_b, 'r--', linewidth=2, label='Asymptotic')
plt.semilogx(omega, exact_b, 'b-', linewidth=2, label='Exact')
plt.ylim(-30, 10)
save_plot('practice_16_13_b.svg')

# (c) H(s) = (s + 10) / s
# Zero at 10, Pole at 0 (Integrator)
# Low freq: 10/s => slope -20dB/dec. At w=1, |H|=10 => 20dB
# High freq: 1 => 0 dB
setup_plot(r'Practice 16.13(c): $H(s) = (s+10)/s$')
asymp_c = np.zeros_like(omega)
asymp_c[omega <= 10] = 20 * np.log10(10/omega[omega <= 10])
asymp_c[omega > 10] = 0
exact_c = 20 * np.log10(np.sqrt(omega**2 + 10**2) / omega)

plt.semilogx(omega, asymp_c, 'r--', linewidth=2, label='Asymptotic')
plt.semilogx(omega, exact_c, 'b-', linewidth=2, label='Exact')
plt.ylim(-10, 40)
save_plot('practice_16_13_c.svg')
