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

def generate_pole_magnitude():
    w = np.logspace(-1, 5, 2000)
    a = 10
    
    # Exact Magnitude: 20 log10(1 / sqrt(1 + (w/a)^2)) = -20 log10(sqrt(1 + (w/a)^2))
    mag_exact = -20 * np.log10(np.sqrt(1 + (w/a)**2))
    
    # Asymptotic Magnitude
    mag_async = np.zeros_like(w)
    mag_async[w > a] = -20 * np.log10(w[w > a] / a)
    
    plt.figure(figsize=(10, 6))
    
    # Plot exact vs asymptotic
    plt.semilogx(w, mag_exact, label='Exact Magnitude $|H(j\omega)|$', linewidth=3, color='#3498db')
    plt.semilogx(w, mag_async, '--', label='Asymptotic Approximation', linewidth=2, color='#e74c3c')
    
    # Annotations
    plt.axvline(a, color='gray', linestyle=':', alpha=0.7)
    plt.annotate('Corner Frequency\n$\omega = a$', 
                 xy=(a, 0), xytext=(a*0.05, -15),
                 arrowprops=dict(arrowstyle='->', color='black'),
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1, alpha=0.8))
    
    # Slope Annotation
    plt.annotate('-20 dB/decade', xy=(a*10, -20), xytext=(a*3, -25),
                 color='#e74c3c', fontweight='bold')

    # Error Annotation
    plt.annotate('Max error: -3 dB', xy=(a, -3), xytext=(a*2, -1),
                 arrowprops=dict(arrowstyle='->', color='gray'),
                 fontsize=10)

    plt.xlabel('Frequency $\omega$ (rad/s)')
    plt.ylabel('Magnitude (dB)')
    plt.title('Bode Magnitude Plot: $H(s) = 1 / (1 + s/a)$ (Simple Pole)')
    plt.legend()
    
    # Generic Axis Labels
    ticks = [0.01*a, 0.1*a, a, 10*a, 100*a, 1000*a]
    labels = ['$0.01a$', '$0.1a$', '$a$', '$10a$', '$100a$', '$1000a$']
    plt.xticks(ticks, labels)
    plt.grid(True, which="major", ls="-", alpha=0.5)
    plt.ylim(-65, 5)
    plt.xlim(0.01*a, 1000*a)

    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, 'pole_magnitude_asymptote.svg')
    plt.savefig(output_path, format='svg')
    plt.close()
    print(f"Generated {output_path}")

def generate_pole_phase():
    w = np.logspace(-1, 5, 2000)
    a = 10
    
    # Exact Phase: arg(1 / (1 + jw/a)) = -arctan(w/a)
    phase_exact = -np.arctan(w/a) * 180 / np.pi
    
    # Asymptotic Phase
    # 0 for w < 0.1a
    # -90 for w > 10a
    # linear in log-scale between
    phase_async = np.zeros_like(w)
    mask_slope = (w >= 0.1*a) & (w <= 10*a)
    phase_async[mask_slope] = -45 * np.log10(w[mask_slope] / (0.1*a))
    phase_async[w > 10*a] = -90
    
    plt.figure(figsize=(10, 6))
    
    # Plot exact vs asymptotic
    plt.semilogx(w, phase_exact, label=r'Exact Phase $\angle H(j\omega)$', linewidth=3, color='#3498db')
    plt.semilogx(w, phase_async, '--', label='Asymptotic Approximation', linewidth=2, color='#e74c3c')
    
    # Highlight key points
    key_omegas = [0.1*a, a, 10*a]
    key_vals = [0, -45, -90]
    for om, val in zip(key_omegas, key_vals):
        plt.plot(om, val, 'ro', markersize=6)
        plt.axvline(x=om, color='gray', linestyle=':', alpha=0.5)

    # Annotations
    plt.annotate(r'slope = $-45^\circ$/dec', xy=(a, -45), xytext=(a*2, -20),
                 arrowprops=dict(arrowstyle='->', color='#e74c3c'), 
                 color='#e74c3c', fontweight='bold')
    
    plt.text(a * 1.1, -50, r'$-45^\circ$', color='#e74c3c', fontweight='bold')

    plt.xlabel('Frequency $\omega$ (rad/s)')
    plt.ylabel('Phase (degrees)')
    plt.title('Bode Phase Plot: $H(s) = 1 / (1 + s/a)$ (Simple Pole)')
    plt.legend(loc='lower left')
    
    # Generic Axis Labels
    ticks = [0.01*a, 0.1*a, a, 10*a, 100*a, 1000*a]
    labels = ['$0.01a$', '$0.1a$', '$a$', '$10a$', '$100a$', '$1000a$']
    plt.xticks(ticks, labels)
    plt.yticks([0, -15, -30, -45, -60, -75, -90])
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.ylim(-100, 10)
    plt.xlim(0.01*a, 1000*a)

    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, 'pole_phase_asymptote.svg')
    plt.savefig(output_path, format='svg')
    plt.close()
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_pole_magnitude()
    generate_pole_phase()
