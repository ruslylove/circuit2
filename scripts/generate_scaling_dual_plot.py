import numpy as np
import matplotlib.pyplot as plt
import os

# Set style
plt.style.use('bmh')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.titlesize'] = 16

OUTPUT_DIR = 'public'
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def generate_scaling_response_subplots():
    """
    Generate impedance magnitude response as two subplots: Original and Scaled.
    Original: R=2.5, w0=1.
    Scaled: Km=2000 (R=5000), Kf=5e6 (w0=5e6).
    """
    R = 2.5
    L = 0.5
    C = 2.0
    w0 = 1.0
    
    Km = 2000.0
    Kf = 5.0e6
    
    # Original Data
    w = np.linspace(0, 3, 1000)
    w = w[1:] 
    Y_mag = np.sqrt( (1/R)**2 + (w*C - 1/(w*L))**2 )
    Z_mag = 1 / Y_mag

    # Scaled Data
    w_scaled = w * Kf
    Z_scaled = Z_mag * Km
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
    
    # Plot 1: Original
    ax1.plot(w, Z_mag, linewidth=2, color='#3498db')
    ax1.plot(w0, R, 'ro')
    ax1.annotate(f'Peak: {R} $\Omega$ @ {w0} rad/s', 
                 xy=(w0, R), 
                 xytext=(w0+0.5, R), 
                 arrowprops=dict(arrowstyle='->', color='black'),
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1, alpha=0.9))
    
    ax1.set_title('(a) Original Response')
    ax1.set_xlabel('Frequency $\omega$ (rad/s)')
    ax1.set_ylabel('Impedance $|Z|$ ($\Omega$)')
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.set_xlim(0, 3)
    ax1.set_ylim(0, 3)

    # Plot 2: Scaled
    # Convert ticks to readable units (Mrad/s and kOhm)
    ax2.plot(w_scaled / 1e6, Z_scaled / 1000, linewidth=2, color='#e74c3c')
    w0_scaled = w0 * Kf
    R_scaled = R * Km
    
    ax2.plot(w0_scaled/1e6, R_scaled/1000, 'bo')
    ax2.annotate(f'Peak: {R_scaled/1000:.1f} k$\Omega$ @ {w0_scaled/1e6:.1f} Mrad/s', 
                 xy=(w0_scaled/1e6, R_scaled/1000), 
                 xytext=(w0_scaled/1e6 + 0.5 * (3/3), R_scaled/1000), # Approx scale spacing
                 arrowprops=dict(arrowstyle='->', color='black'),
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1, alpha=0.9))

    ax2.set_title(r'(b) Scaled Response ($K_m=2000, K_f=5 \times 10^6$)')
    ax2.set_xlabel('Frequency $\omega\'$ (Mrad/s)')
    ax2.set_ylabel('Impedance $|Z|\'$ (k$\Omega$)')
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.set_xlim(0, 3 * Kf / 1e6)
    ax2.set_ylim(0, 3 * Km / 1000)
    
    plt.tight_layout()
    
    output_path = os.path.join(OUTPUT_DIR, 'fig_scaling_comparison.png')
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_scaling_response_subplots()
