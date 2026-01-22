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

def generate_bode_intro():
    w = np.logspace(0, 4, 1000)
    w_break = 100
    
    # Exact Magnitude
    mag_exact = 20 * np.log10(1 / np.sqrt(1 + (w/w_break)**2))
    
    # Asymptotic Magnitude
    mag_async = np.zeros_like(w)
    mag_async[w > w_break] = -20 * np.log10(w[w > w_break] / w_break)
    
    # Exact Phase
    phase_exact = -np.rad2deg(np.arctan(w / w_break))
    
    # Asymptotic Phase
    phase_async = np.zeros_like(w)
    mask_mid = (w >= 10) & (w <= 1000)
    mask_high = (w > 1000)
    phase_async[mask_mid] = -45 * np.log10(w[mask_mid] / 10)
    phase_async[mask_high] = -90
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    
    # Magnitude Plot
    ax1.semilogx(w, mag_exact, label='Exact Response', linewidth=3, color='#3498db')
    ax1.semilogx(w, mag_async, '--', label='Asymptotic (Bode)', linewidth=2, color='#e74c3c')
    ax1.axvline(w_break, color='gray', linestyle=':', alpha=0.7)
    ax1.annotate('Break Frequency\n$\omega = 100$ rad/s', xy=(w_break, -3), xytext=(w_break*2, 10),
                 arrowprops=dict(arrowstyle='->', color='black'))
    ax1.set_ylabel('Magnitude (dB)')
    ax1.set_title('Bode Magnitude Plot: $H(s) = \\frac{1}{1 + s/100}$')
    ax1.legend()
    ax1.grid(True, which="both", ls="-", alpha=0.5)
    ax1.set_ylim(-45, 15)

    # Phase Plot
    ax2.semilogx(w, phase_exact, label='Exact Response', linewidth=3, color='#3498db')
    ax2.semilogx(w, phase_async, '--', label='Asymptotic (Bode)', linewidth=2, color='#e74c3c')
    ax2.axvline(w_break, color='gray', linestyle=':', alpha=0.7)
    ax2.set_xlabel('Frequency $\omega$ (rad/s)')
    ax2.set_ylabel('Phase (degrees)')
    ax2.set_title('Bode Phase Plot')
    ax2.legend()
    ax2.grid(True, which="both", ls="-", alpha=0.5)
    ax2.set_yticks([0, -45, -90])
    ax2.set_ylim(-110, 10)

    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, 'bode_intro_plot.png')
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_bode_intro()
