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

def generate_zero_asymptote():
    w = np.logspace(-1, 5, 2000) # Wider range for logspace
    a = 10
    
    # Exact Magnitude
    mag_exact = 20 * np.log10(np.sqrt(1 + (w/a)**2))
    
    # Asymptotic Magnitude
    mag_async = np.zeros_like(w)
    mag_async[w > a] = 20 * np.log10(w[w > a] / a)
    
    plt.figure(figsize=(11, 6)) # Slightly wider for more labels
    
    # Plot exact vs asymptotic
    plt.semilogx(w, mag_exact, label='Exact Magnitude $|H(j\omega)|$', linewidth=3, color='#3498db')
    plt.semilogx(w, mag_async, '--', label='Asymptotic Approximation', linewidth=2, color='#e74c3c')
    
    # Annotations
    plt.axvline(a, color='gray', linestyle=':', alpha=0.7)
    plt.annotate('Corner Frequency\n$\omega = a$', 
                 xy=(a, 0), xytext=(a*0.05, 10),
                 arrowprops=dict(arrowstyle='->', color='black'),
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1, alpha=0.8))
    
    # Slope Annotation
    plt.annotate('+20 dB/decade', xy=(a*10, 20), xytext=(a*3, 25),
                 color='#e74c3c', fontweight='bold')

    # Error Annotation
    plt.annotate('Max error: +3 dB', xy=(a, 3), xytext=(a*2, 1),
                 arrowprops=dict(arrowstyle='->', color='gray'),
                 fontsize=10)

    plt.xlabel('Frequency $\omega$ (rad/s)')
    plt.ylabel('Magnitude (dB)')
    plt.title('Bode Magnitude Plot: $H(s) = 1 + s/a$ (Single Zero)')
    plt.legend()
    
    # Generic Axis Labels (Enhanced Range)
    ticks = [0.01*a, 0.1*a, a, 10*a, 100*a, 1000*a]
    labels = ['$0.01a$', '$0.1a$', '$a$', '$10a$', '$100a$', '$1000a$']
    plt.xticks(ticks, labels)
    plt.grid(True, which="major", ls="-", alpha=0.5)
    plt.ylim(-5, 65)
    plt.xlim(0.01*a, 1000*a)

    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, 'zero_asymptote_plot.png')
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_zero_asymptote()
