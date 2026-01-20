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
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Parameters
    w0 = 1000  # rad/s
    Q = 10     # High Q
    R = 1000   # Ohms
    C = Q / (w0 * R)
    L = 1 / (w0**2 * C)
    
    # Frequency range: +/- 20% around w0
    w = np.linspace(0.8*w0, 1.2*w0, 1000)
    
    # Exact Admittance Magnitude
    # Y = 1/R + j(wC - 1/wL)
    Y_exact = (1/R) + 1j * (w*C - 1/(w*L))
    mag_Y_exact = np.abs(Y_exact) * R # Normalized to 1/R scale (i.e., |Y|*R)
    
    # Approximate Admittance Magnitude
    # Y ~ (1/R)(1 + jN), N = 2Q(w-w0)/w0
    N = 2 * Q * (w - w0) / w0
    Y_approx = (1/R) * (1 + 1j*N)
    mag_Y_approx = np.abs(Y_approx) * R
    
    # Plot curves
    ax.plot(w, mag_Y_exact, label=r'Exact $|Y| \cdot R$', linewidth=2.5, color='tab:blue')
    ax.plot(w, mag_Y_approx, label=r'Approx $|Y| \cdot R$', linewidth=2.5, color='tab:red', linestyle='--')
    
    # Highlight +/- 10% region
    w_lower = 0.9 * w0
    w_upper = 1.1 * w0
    ax.axvspan(w_lower, w_upper, color='green', alpha=0.1, label=r'Valid Range $\pm 10\% \omega_0$')
    
    # Mark boundaries
    ax.axvline(w_lower, color='green', linestyle=':', alpha=0.5)
    ax.axvline(w_upper, color='green', linestyle=':', alpha=0.5)
    ax.axvline(w0, color='k', linestyle='-.', alpha=0.3)
    
    # Calculate max error in range
    mask = (w >= w_lower) & (w <= w_upper)
    w_range = w[mask]
    exact_range = mag_Y_exact[mask]
    approx_range = mag_Y_approx[mask]
    
    # Max error calculation
    error = np.abs(exact_range - approx_range)
    # Be careful with division by zero/small numbers if exact is 0 (it's not here, min is 1)
    pct_error = (error / exact_range) * 100
    max_pct_error = np.max(pct_error)
    
    # Annotate Max Error
    # Place text in the middle of the shaded region
    text_x = w0
    text_y = np.max(mag_Y_exact) * 0.8
    
    msg = f"Max Error within $\\pm 10\\%$: {max_pct_error:.2f}\\%" + "\n" + r"Approximation holds well in green region"
    
    ax.text(text_x, text_y, msg, ha='center', va='center', 
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.9, edgecolor='g'))

    ax.set_title(r'Admittance Approximation: Exact vs Approx ($Q=10$)')
    ax.set_xlabel(r'Frequency $\omega$ (rad/s)')
    ax.set_ylabel(r'Normalized Admittance Magnitude $|Y| \cdot R$')
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, 'admittance_approx.png')
    plt.savefig(output_path, dpi=150)
    print(f"Saved {output_path}")

if __name__ == "__main__":
    generate_plot()
