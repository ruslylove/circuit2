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

def generate_s_plane_vary_r():
    """
    Generate s-plane plot showing pole locations for different R values.
    Parameters match plot_vary_r in plot_resonance.py:
    L = 10 mH
    C = 10 uF
    R in [10, 20, 50, 100] Ohms
    """
    L = 10e-3
    C = 10e-6
    Rs = [10, 20, 50, 100]
    
    w0 = 1 / np.sqrt(L*C)
    print(f"w0 = {w0:.2f} rad/s")
    
    plt.figure(figsize=(8, 8))
    
    # Draw axes
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    
    # Draw w0 circle (locus of roots)
    theta = np.linspace(np.pi/2, 3*np.pi/2, 100)
    x_circ = w0 * np.cos(theta)
    y_circ = w0 * np.sin(theta)
    plt.plot(x_circ, y_circ, 'k--', alpha=0.3, label=r'$\omega_0$ Locus')
    
    colors = plt.cm.viridis(np.linspace(0, 1, len(Rs)))
    
    for i, R in enumerate(Rs):
        alpha = 1 / (2 * R * C)
        
        # Parallel RLC Characteristic Equation: s^2 + (1/RC)s + (1/LC) = 0
        # s1,2 = -alpha +/- sqrt(alpha^2 - w0^2)
        
        discriminant = alpha**2 - w0**2
        
        if discriminant > 0:
            # Overdamped (Real roots)
            s1 = -alpha + np.sqrt(discriminant)
            s2 = -alpha - np.sqrt(discriminant)
            plt.plot([s1, s2], [0, 0], 'x', color=colors[i], markersize=10, markeredgewidth=3, label=f'R={R}' + r'$\Omega$ (Overdamped)')
        elif discriminant < 0:
            # Underdamped (Complex conjugate roots)
            wd = np.sqrt(-discriminant)
            plt.plot(-alpha, wd, 'x', color=colors[i], markersize=10, markeredgewidth=3, label=f'R={R}' + r'$\Omega$ (Underdamped)')
            plt.plot(-alpha, -wd, 'x', color=colors[i], markersize=10, markeredgewidth=3)
            # Draw line from origin to pole
            # plt.plot([0, -alpha], [0, wd], '--', color=colors[i], alpha=0.3)
        else:
            # Critically damped
            plt.plot(-alpha, 0, 'o', color=colors[i], markersize=10, label=f'R={R}' + r'$\Omega$ (Critically Damped)')
            
    # Add annotations and labels
    plt.title('S-Plane Pole Locations Varying R')
    plt.xlabel(r'Real Axis ($\sigma$)')
    plt.ylabel(r'Imaginary Axis ($j\omega$)')
    plt.legend(loc='upper left')
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    
    # Set limits to show all poles clearly
    # alpha max is when R is min (10 Ohm). alpha = 1 / (2 * 10 * 10e-6) = 1 / 20e-5 = 5000
    # w0 = 3162
    # So max -5000 on x axis.
    plt.xlim(-6000, 1000)
    plt.ylim(-4000, 4000)
    plt.gca().set_aspect('equal', adjustable='box')
    
    output_path = os.path.join(OUTPUT_DIR, 's_plane_vary_r.png')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_s_plane_vary_r()
