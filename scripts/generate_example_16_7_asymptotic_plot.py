import numpy as np
import matplotlib.pyplot as plt

# Parameters
K = 20
a = 100
omega = np.logspace(0, 4, 1000)

# Magnitude calculations
k_db = 20 * np.log10(K)

# Separate Asymptotes
asymp_k = np.full_like(omega, k_db)
asymp_zero = np.zeros_like(omega)
asymp_zero[omega > a] = 20 * np.log10(omega[omega > a] / a)

# Composite Asymptote
asymp_composite = asymp_k + asymp_zero

def save_plot(filename, plot_type):
    plt.figure(figsize=(9, 5))
    
    if plot_type == 'asymptotes':
        plt.semilogx(omega, asymp_k, color='gray', linestyle='--', linewidth=1.5, label=f'Constant Gain $K={K}$')
        plt.semilogx(omega, asymp_zero, color='darkorange', linestyle='--', linewidth=1.5, label=f'Zero at $\omega={a}$')
        plt.title(r'Step 1: Individual Asymptotic Terms')
        
        # Annotations for Step 1
        plt.text(1.2, k_db + 2, r'$20 \log 20 \approx 26$ dB', color='gray', fontweight='bold')
        plt.text(a * 5, 20, r'+20 dB/dec', color='darkorange', fontweight='bold', rotation=30)
        
    elif plot_type == 'composite':
        # Muted individual terms in the background for context
        plt.semilogx(omega, asymp_k, color='gray', linestyle='--', linewidth=1, alpha=0.3)
        plt.semilogx(omega, asymp_zero, color='darkorange', linestyle='--', linewidth=1, alpha=0.3)
        plt.semilogx(omega, asymp_composite, color='red', linestyle='-', linewidth=3.0, label='Composite Asymptotic (Summed)')
        plt.title(r'Step 2: Composite Asymptotic (Summed)')
        
        # Annotations for Step 2
        plt.text(1.2, k_db + 2, r'26 dB', color='red', fontweight='bold')
        plt.text(a * 5, k_db + 20, r'+20 dB/dec', color='red', fontweight='bold', rotation=30)

    # Highlight corner frequency
    plt.axvline(x=a, color='gray', linestyle='--', alpha=0.4)
    plt.text(a, -5, fr' $\omega = {a}$', color='gray', ha='left')

    # Formatting
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.xlabel(r'Frequency $\omega$ (rad/s)')
    plt.ylabel(r'Magnitude $|H(j\omega)|_{dB}$ (dB)')
    plt.legend(loc='lower right')
    
    # Consistent Y limits
    plt.ylim(-10, 50) 
    
    plt.tight_layout()
    plt.savefig(f'public/{filename}', format='svg')
    plt.close()
    print(f"Successfully generated public/{filename}")

# Generate both plots
save_plot('example_16_7_asymptotes.svg', 'asymptotes')
save_plot('example_16_7_composite.svg', 'composite')
