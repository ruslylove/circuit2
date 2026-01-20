import numpy as np
import matplotlib.pyplot as plt
import os

# Set style
plt.style.use('bmh')
plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.titlesize'] = 16

OUTPUT_DIR = 'public'
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def generate_plot():
    # Setup subplots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Cases: Low Q and High Q
    cases = [
        {'Q': 1, 'ax': axes[0], 'title': r'Low Q ($Q_0=1$)'},
        {'Q': 10, 'ax': axes[1], 'title': r'High Q ($Q_0=10$)'}
    ]
    
    w0 = 1000 # rad/s
    
    for case in cases:
        Q = case['Q']
        ax = case['ax']
        
        # Bandwidth
        B = w0 / Q
        
        # Exact half-power frequencies
        # derived from standard RLC equations
        # w1,2 = w0 * ( sqrt(1 + (1/2Q)^2) +/- 1/2Q )
        term1 = np.sqrt(1 + (1/(2*Q))**2)
        term2 = 1/(2*Q)
        
        w1_exact = w0 * (term1 - term2)
        w2_exact = w0 * (term1 + term2)
        
        # Approximate half-power frequencies
        w1_approx = w0 - B/2
        w2_approx = w0 + B/2
        
        # Generate Frequency Response Curve
        # Normalized admittance magnitude for parallel RLC:
        # |V| = I * R / sqrt(1 + Q^2(w/w0 - w0/w)^2)
        # Since R is proportional to Q (for fixed L, C), Peak |V| is proportional to Q.
        # We plot proportional magnitude.
        span = 1.5 * B # show range around w0
        w_min = w0 - span
        w_max = w0 + span
        w = np.linspace(w_min, w_max, 1000)
        
        # Un-normalized magnitude (Peak = Q)
        mag = Q / np.sqrt(1 + (Q * (w/w0 - w0/w))**2)
        
        # Plot curve
        ax.plot(w, mag, label='Response', linewidth=2)
        
        # Mark Exact
        ax.axvline(w1_exact, color='g', linestyle='-', alpha=0.6, label='Exact ' + r'$\omega_{1,2}$')
        ax.axvline(w2_exact, color='g', linestyle='-', alpha=0.6)
        
        # Mark Approx
        ax.axvline(w1_approx, color='r', linestyle='--', alpha=0.8, label=r'Approx $\omega_0 \pm B/2$')
        ax.axvline(w2_approx, color='r', linestyle='--', alpha=0.8)
        
        # Mark w0
        ax.axvline(w0, color='k', linestyle=':', alpha=0.3)
        
        # 0.707 * Peak line
        peak_val = Q
        half_power_val = 0.707 * peak_val
        ax.axhline(half_power_val, color='k', linestyle=':', alpha=0.3, label=r'$0.707$ Peak')
        
        # Annotate error
        # Calculate error percentage
        err = w1_exact - w1_approx
        err_pct = (abs(err) / w1_exact) * 100
        
        # Use a background box to prevent overlap with lines
        # Position slightly offset if needed, but bbox handles line overlap nicely
        ax.text(w1_exact, 0.2 * peak_val, f'Error\n{err_pct:.2f}\\%', color='r', ha='center', fontsize=10,
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.9, edgecolor='r'))
        
        ax.set_title(case['title'])
        ax.set_xlabel(r'Frequency (rad/s)')
        
        if case == cases[0]:
            ax.set_ylabel(r'Magnitude (Proportional to Q)')
            ax.legend(loc='upper right', fontsize=10)
            
        ax.set_ylim(0, Q * 1.1)
        ax.grid(True, alpha=0.3)
        
        # Stats box
        stats = (
            f"$B = {B:.1f}$\n"
            fr"$\omega_1$ (Ex): {w1_exact:.1f}" + "\n" +
            fr"$\omega_1$ (Ap): {w1_approx:.1f}" + "\n" +
            fr"$\omega_2$ (Ex): {w2_exact:.1f}" + "\n" +
            fr"$\omega_2$ (Ap): {w2_approx:.1f}"
        )
        ax.text(0.05, 0.95, stats, transform=ax.transAxes, verticalalignment='top', 
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    plt.suptitle(r'Comparison of Exact vs Approximate Half-Power Frequencies', fontsize=16)
    plt.tight_layout()
    
    output_path = os.path.join(OUTPUT_DIR, 'high_q_approx.png')
    plt.savefig(output_path, dpi=150)
    print(f"Saved {output_path}")

if __name__ == "__main__":
    generate_plot()
