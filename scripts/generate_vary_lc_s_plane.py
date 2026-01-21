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

def generate_s_plane_vary_lc():
    """
    Generate s-plane plot showing pole locations for different Q values
    (varying L/C ratio, fixed w0).
    Parameters:
    w0 = 2*pi*1000 rad/s
    Q in [0.5, 2, 8]
    """
    w0 = 2 * np.pi * 1000
    qs = [0.5, 2, 8]
    
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
    
    colors = plt.cm.plasma(np.linspace(0, 1, len(qs)))
    
    for i, Q in enumerate(qs):
        alpha = w0 / (2 * Q)
        
        # Characteristic Equation: s^2 + 2*alpha*s + w0^2 = 0
        discriminant = alpha**2 - w0**2
        
        if discriminant > 0:
            # Overdamped
            s1 = -alpha + np.sqrt(discriminant)
            s2 = -alpha - np.sqrt(discriminant)
            plt.plot([s1, s2], [0, 0], 'x', color=colors[i], markersize=10, markeredgewidth=3, label=f'Q={Q}')
        elif discriminant < 0:
            # Underdamped
            wd = np.sqrt(-discriminant)
            plt.plot(-alpha, wd, 'x', color=colors[i], markersize=10, markeredgewidth=3, label=f'Q={Q}')
            plt.plot(-alpha, -wd, 'x', color=colors[i], markersize=10, markeredgewidth=3)
            # Draw line from origin?
        else:
            # Critically damped (Q=0.5)
            plt.plot(-alpha, 0, 'o', color=colors[i], markersize=10, label=f'Q={Q}')
            
    # Add annotations and labels
    plt.title('S-Plane Pole Locations Varying L/C')
    plt.xlabel(r'Real Axis ($\sigma$)')
    plt.ylabel(r'Imaginary Axis ($j\omega$)')
    plt.legend(loc='upper left')
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    
    # Set limits
    # Max alpha when Q=0.5 -> alpha = w0. s = -w0.
    # w0 approx 6283.
    plt.xlim(-8000, 2000)
    plt.ylim(-7000, 7000)
    plt.gca().set_aspect('equal', adjustable='box')
    
    output_path = os.path.join(OUTPUT_DIR, 's_plane_vary_lc.png')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_s_plane_vary_lc()
