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

def generate_origin_plots():
    w = np.logspace(-2, 2, 1000)
    
    # H(s) = s
    mag_zero = 20 * np.log10(w)
    phase_zero = np.full_like(w, 90)
    
    # H(s) = 1/s
    mag_pole = -20 * np.log10(w)
    phase_pole = np.full_like(w, -90)
    
    # Magnitude Plot
    plt.figure(figsize=(10, 6))
    plt.semilogx(w, mag_zero, label='$H(s) = s$ (+20 dB/dec)', linewidth=3, color='#3498db')
    plt.semilogx(w, mag_pole, label='$H(s) = 1/s$ (-20 dB/dec)', linewidth=3, color='#e74c3c')
    
    plt.axvline(1, color='gray', linestyle=':', alpha=0.7)
    plt.axhline(0, color='gray', linestyle=':', alpha=0.7)
    plt.annotate('0 dB at $\omega = 1$', xy=(1, 0), xytext=(2, 5),
                 arrowprops=dict(arrowstyle='->', color='black'))

    plt.xlabel('Frequency $\omega$ (rad/s)')
    plt.ylabel('Magnitude (dB)')
    plt.title('Bode Magnitude: Pole/Zero at Origin')
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.ylim(-45, 45)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'origin_magnitude.svg'), format='svg')
    plt.close()

    # Phase Plot
    plt.figure(figsize=(10, 5))
    plt.semilogx(w, phase_zero, label='$H(s) = s$ ($+90^\circ$)', linewidth=3, color='#3498db')
    plt.semilogx(w, phase_pole, label='$H(s) = 1/s$ ($-90^\circ$)', linewidth=3, color='#e74c3c')
    
    plt.xlabel('Frequency $\omega$ (rad/s)')
    plt.ylabel('Phase (degrees)')
    plt.title('Bode Phase: Pole/Zero at Origin')
    plt.legend(loc='center right')
    plt.yticks([-90, -45, 0, 45, 90])
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.ylim(-110, 110)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'origin_phase.svg'), format='svg')
    plt.close()

if __name__ == "__main__":
    generate_origin_plots()
    print("Generated public/origin_magnitude.svg and public/origin_phase.svg")
