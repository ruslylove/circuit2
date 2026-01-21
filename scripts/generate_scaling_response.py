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

def generate_scaling_response():
    """
    Generate impedance magnitude response for the unscaled parallel RLC circuit.
    R = 2.5 Ohm
    L = 0.5 H
    C = 2 F
    w0 = 1/sqrt(LC) = 1/sqrt(1) = 1 rad/s
    """
    R = 2.5
    L = 0.5
    C = 2.0
    
    w0 = 1.0
    
    # Frequency range
    w = np.linspace(0, 3, 1000)
    w = w[1:] # Avoid 0 division
    
    # Admittance Y = 1/R + j(wC - 1/wL)
    Y_mag = np.sqrt( (1/R)**2 + (w*C - 1/(w*L))**2 )
    Z_mag = 1 / Y_mag
    
    plt.figure(figsize=(8, 6))
    plt.plot(w, Z_mag, linewidth=2)
    
    # Mark peak
    plt.plot(w0, R, 'ro')
    plt.annotate(f'Peak: {R}$\Omega$ at {w0} rad/s', 
                 xy=(w0, R), 
                 xytext=(w0+0.5, R), 
                 arrowprops=dict(arrowstyle='->'),
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1, alpha=0.8))
    
    plt.title('Unscaled Circuit Impedance Response')
    plt.xlabel('Frequency $\omega$ (rad/s)')
    plt.ylabel('Impedance Magnitude $|Z|$ ($\Omega$)')
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.xlim(0, 3)
    plt.ylim(0, 3)
    
    output_path = os.path.join(OUTPUT_DIR, 'fig_16_17_response.png')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_scaling_response()
