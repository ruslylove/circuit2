import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'

# Parameters
alpha = 3
wd = 4
w0_sq = alpha**2 + wd**2
w0 = np.sqrt(w0_sq) # 5.0

# Frequency range
freqs = np.linspace(0, 10, 1000)
s = 1j * freqs

# Z(s) normalized factor doesn't matter for shape, but let's be consistent
# Z(s) = s / (s^2 + 2*alpha*s + w0_sq)
# Peak is at w0. 
# At w0, |Z| = w0 / (2*alpha*w0) = 1/(2*alpha)
# Normalized response |V| / |Vmax| = |Z| / |Zmax|
# |Zmax| = 1 / (2*alpha)

Z_vals = s / (s**2 + 2*alpha*s + w0_sq)
Z_mag = np.abs(Z_vals)
Z_max = np.max(Z_mag)

V_norm = Z_mag / Z_max

fig, ax = plt.subplots(figsize=(10, 6))

color = 'tab:blue'
ax.plot(freqs, V_norm, color=color, linewidth=2.5)

# Axis labels
ax.set_xlabel(r'Frequency $\omega$ (rad/s)', fontsize=14)
ax.set_ylabel(r'Normalized Voltage $\frac{|V(j\omega)|}{|I|R}$', fontsize=14)
ax.set_title(r'Resonance Curve and Bandwidth', fontsize=16)

# Mark 1.0 level (Max)
ax.axhline(1.0, color='k', linestyle=':', alpha=0.5)
ax.text(0.5, 1.01, r'$|V|_{max} = |I|R$', fontsize=12)

# Mark 0.707 level
ax.axhline(0.707, color='r', linestyle='--', alpha=0.6)
ax.text(0.2, 0.72, r'$0.707 |I|R$', color='r', fontsize=12)

# Find w1 and w2
# Indices where V_norm crosses 0.707
idx_above = np.where(V_norm >= 0.707)[0]
if len(idx_above) > 0:
    w1 = freqs[idx_above[0]]
    w2 = freqs[idx_above[-1]]
    
    # Drop lines for w1, w2, w0
    ax.vlines(w1, 0, 0.707, colors='r', linestyles='--')
    ax.vlines(w2, 0, 0.707, colors='r', linestyles='--')
    ax.vlines(w0, 0, 1.0, colors='k', linestyles=':')

    # Labels
    ax.text(w1-0.2, -0.05, r'$\omega_1$', color='r', fontsize=14)
    ax.text(w2-0.2, -0.05, r'$\omega_2$', color='r', fontsize=14)
    ax.text(w0-0.2, -0.05, r'$\omega_0$', color='k', fontsize=14)
    
    # Annotate Bandwidth
    ax.annotate('', xy=(w1, 0.3), xytext=(w2, 0.3), arrowprops=dict(arrowstyle='<->', color='brown'))
    ax.text((w1+w2)/2, 0.32, r'$B = \omega_2 - \omega_1$', color='brown', ha='center', fontsize=12)

ax.set_ylim(-0.1, 1.1)
ax.set_xlim(0, 10)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('public/voltage_response.png', dpi=150)
print("Saved public/voltage_response.png")
