import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'

alpha = 3
wd = 4
w0 = 5

fig, ax = plt.subplots(figsize=(10, 8))

# Poles and Zero
p1 = -alpha + 1j*wd
p2 = -alpha - 1j*wd
z = 0

ax.scatter([p1.real, p2.real], [p1.imag, p2.imag], color='r', marker='x', s=100, label='Poles', zorder=5)
ax.scatter([0], [0], color='b', marker='o', s=100, facecolors='none', edgecolors='b', linewidth=2, label='Zero', zorder=5)

# Axis
ax.axhline(0, color='k', linewidth=0.5)
ax.axvline(0, color='k', linewidth=0.5)

# Function to draw vectors to a test frequency w
def draw_analysis(w, color, offset_x):
    s = 1j * w
    
    # Vector from Zero
    ax.arrow(0, 0, 0, w, head_width=0.2, length_includes_head=True, color=color, linestyle='--', alpha=0.6)
    
    # Vector from P1
    ax.arrow(p1.real, p1.imag, -p1.real, w - p1.imag, head_width=0.2, length_includes_head=True, color=color, alpha=0.8)
    
    # Vector from P2
    ax.arrow(p2.real, p2.imag, -p2.real, w - p2.imag, head_width=0.2, length_includes_head=True, color=color, alpha=0.8)
    
    # Mark test point
    ax.scatter([0], [w], color=color, s=50, zorder=6)
    
    # Calculate lengths
    d_z = w
    d_p1 = np.abs(s - p1)
    d_p2 = np.abs(s - p2)
    mag = d_z / (d_p1 * d_p2)
    
    # Annotation box
    text = (f"Frequency $\omega = {w}$\n"
            f"$|s-z| = {d_z:.1f}$\n"
            f"$|s-p_1| = {d_p1:.1f}$\n"
            f"$|s-p_2| = {d_p2:.1f}$\n"
            f"Result $|Z| \propto {mag:.4f}$")
            
    ax.text(offset_x, w, text, color=color, fontsize=12, 
            bbox=dict(facecolor='white', edgecolor=color, alpha=0.9))

# Draw for wd (4) and w0 (5)
draw_analysis(4, 'green', 1)
draw_analysis(5, 'purple', 1)

# Annotations
ax.set_title(r'Vector contributions at $\omega_d=4$ and $\omega_0=5$')
ax.set_xlabel(r'$\sigma$')
ax.set_ylabel(r'$j\omega$')
ax.grid(True, linestyle=':', alpha=0.6)
ax.set_xlim(-5, 4)
ax.set_ylim(-1, 8)
ax.legend(loc='lower left')

plt.savefig('public/vector_explanation.png', dpi=150, bbox_inches='tight')
print("Saved public/vector_explanation.png")
