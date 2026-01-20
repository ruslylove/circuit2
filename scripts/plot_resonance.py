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

def plot_normalized_q():
    """
    Plot 1: Standardized response for different Q values
    Normalized Magnitude |V|/|V_max| vs Normalized Frequency omega/omega0
    Equation: |V/Vmax| = 1 / sqrt(1 + Q^2 * (omega/omega0 - omega0/omega)^2)
    """
    w_norm = np.logspace(np.log10(0.1), np.log10(10), 1000)
    qs = [0.5, 1, 2, 5, 10, 20]
    
    plt.figure(figsize=(10, 6))
    
    for q in qs:
        # Normalized magnitude response for parallel RLC
        # |Y| = sqrt( (1/R)^2 + (wC - 1/wL)^2 )
        # |Z| = 1/|Y|
        # Normalized: |Z|/R = 1 / sqrt( 1 + R^2(wC - 1/wL)^2 )
        # Substitute Q = R * sqrt(C/L) => R(wC - 1/wL) = Q(w/w0 - w0/w)
        
        mag = 1 / np.sqrt(1 + (q * (w_norm - 1/w_norm))**2)
        plt.semilogx(w_norm, mag, label=f'Q = {q}', linewidth=2)

    plt.title('Normalized Frequency Response for Different Q Values')
    plt.xlabel(r'Normalized Frequency $\omega / \omega_0$')
    plt.ylabel(r'Normalized Magnitude $|V| / V_{max}$')
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'plot_q_normalized.png'), dpi=300)
    plt.close()
    print("Generated plot_q_normalized.png")

def plot_vary_r():
    """
    Plot 2: Effect of varying R (fixed L, C)
    Since L, C are fixed, w0 is fixed.
    Q = w0 * R * C => Q is proportional to R.
    Peak amplitude = I * R. Since I is const, Peak is proportional to R.
    """
    f = np.logspace(2, 4, 1000) # 100 Hz to 10 kHz
    w = 2 * np.pi * f
    
    L = 10e-3 # 10 mH
    C = 10e-6 # 10 uF
    w0 = 1 / np.sqrt(L*C)
    f0 = w0 / (2*np.pi)
    
    Rs = [10, 20, 50, 100] # Ohms
    I_source = 1 # 1 Amp
    
    plt.figure(figsize=(10, 6))
    
    for R in Rs:
        # Y = 1/R + j(wC - 1/wL)
        Y_mag = np.sqrt( (1/R)**2 + (w*C - 1/(w*L))**2 )
        Z_mag = 1 / Y_mag
        V_mag = I_source * Z_mag
        
        Q = R * np.sqrt(C/L)
        bw = w0 / Q
        
        plt.semilogx(f, V_mag, label=f'R = {R}$\Omega$ (Q={Q:.1f})', linewidth=2)

    plt.axvline(f0, color='k', linestyle='--', alpha=0.5, label=f'$f_0$={f0:.0f}Hz')
    plt.title('Effect of Varying Resistance R (Fixed L, C)')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Voltage Magnitude |V| (V)')
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'plot_vary_r.png'), dpi=300)
    plt.close()
    print("Generated plot_vary_r.png")

def plot_vary_lc_ratio():
    """
    Plot 3: Effect of varying L/C ratio (fixed R, fixed LC product)
    Fixed R, Fixed w0.
    Vary L/C.
    Q = R * sqrt(C/L).
    If L/C increases, C/L decreases, so Q decreases.
    If L/C decreases, C/L increases, so Q increases.
    Peak amplitude = I * R (Constant).
    """
    f = np.logspace(2, 4, 1000)
    w = 2 * np.pi * f
    
    R = 10 # 10 Ohms
    w0_target = 2 * np.pi * 1000 # 1 kHz
    LC_product = 1 / w0_target**2
    
    # Ratios of L/C. High L/C means High L, Low C.
    # Q = R * sqrt(C/L). So High L/C -> Low Q.
    # We want to show varying Q with constant peak.
    
    qs = [0.5, 2, 8]
    
    plt.figure(figsize=(10, 6))
    
    for q in qs:
        # Q = R * sqrt(C/L) => Q/R = sqrt(C/L) => (Q/R)^2 = C/L
        # L * C = LC_product
        # L * (Q/R)^2 * L = LC_product => L^2 = LCp / (Q/R)^2
        
        L = np.sqrt(LC_product / (q/R)**2)
        C = LC_product / L
        
        # Verify
        # print(f"Q={q}, L={L}, C={C}, w0={1/np.sqrt(L*C)}")
        
        Y_mag = np.sqrt( (1/R)**2 + (w*C - 1/(w*L))**2 )
        Z_mag = 1 / Y_mag
        V_mag = 1 * Z_mag # I=1
        
        ratio_sci = f"{L/C:.1e}"
        plt.semilogx(f, V_mag, label=f'Q = {q} (L/C $\\approx$ {ratio_sci})', linewidth=2)

    plt.axvline(1000, color='k', linestyle='--', alpha=0.5, label='$f_0$=1kHz')
    plt.title(f'Effect of Varying L/C Ratio (Fixed R={R}$\Omega$, Fixed $\omega_0$)')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Voltage Magnitude |V| (V)')
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'plot_vary_lc.png'), dpi=300)
    plt.close()
    print("Generated plot_vary_lc.png")

def plot_zeta_effect():
    """
    Plot 4: Effect of different Zeta values
    Show normalized magnitude response.
    Magnitude |H(jw)| = 1 / sqrt( (1 - (w/w0)^2)^2 + (2*zeta*w/w0)^2 )
    We will plot for various zeta values.
    """
    u = np.logspace(np.log10(0.1), np.log10(10), 1000) # Normalized frequency w/w0
    
    zetas = [0.1, 0.3, 0.5, 0.707, 1.0]
    
    plt.figure(figsize=(10, 6))
    
    for zeta in zetas:
        # Standard 2nd order lowpass magnitude shape (or bandpass? resonance usually bandpass)
        # Parallel RLC impedance Z(s) has bandpass shape!
        # Y(s) = C(s^2 + s/RC + 1/LC)/s
        # Z(s) = (1/C) * s / (s^2 + 2*zeta*w0*s + w0^2)
        # |Z(jw)| = (w/C) / sqrt( (w0^2 - w^2)^2 + (2*zeta*w0*w)^2 )
        # Normalize to max value?
        # At w=w0, |Z(jw0)| = (w0/C) / (2*zeta*w0^2) = 1 / (2*zeta*w0*C) = R ? (since 2*zeta*w0 = 1/RC)
        # Yes, Z(jw0) = R.
        # Let's plot |Z(jw)| / R = |Z(jw)| * 2*zeta*w0*C
        # Normalized Magnitude = (2*zeta*u) / sqrt( (1-u^2)^2 + (2*zeta*u)^2 )
        
        mag_norm = (2 * zeta * u) / np.sqrt((1 - u**2)**2 + (2 * zeta * u)**2)
        
        plt.semilogx(u, mag_norm, label=f'$\zeta$ = {zeta}', linewidth=2)

    plt.axvline(1.0, color='k', linestyle='--', alpha=0.5)
    plt.title(r'Normalized Response for Different Damping Factors $\zeta$')
    plt.xlabel(r'Normalized Frequency $\omega / \omega_0$')
    plt.ylabel(r'Normalized Magnitude $|V| / V_{max}$')
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'plot_zeta_effect.png'), dpi=300)
    plt.close()
    print("Generated plot_zeta_effect.png")

def plot_example_16_1_admittance():
    """
    Plot for Example 16.1: Admittance magnitude |Y| vs Frequency
    Points at 0.1*w0, w0, 1.1*w0
    """
    L = 2e-3
    C = 10e-9
    Q0 = 5
    
    # R = Q0 * sqrt(L/C)
    R = Q0 * np.sqrt(L/C)
    
    w0 = 1 / np.sqrt(L*C)
    
    # Frequency range: 0 to 1.5*w0 (approximating 0 for log scale or just linear?)
    # The snippet used linear scale for points, maybe linear is better here to see the points clearly?
    # Or narrow range.
    w = np.linspace(0.0, 1.5 * w0, 1000)
    w = w[1:] # Avoid 0 division
    
    # Admittance |Y|
    # Y = 1/R + j(wC - 1/wL)
    Y_mag = np.sqrt( (1/R)**2 + (w*C - 1/(w*L))**2 )
    
    plt.figure(figsize=(10, 6))
    plt.plot(w/1000, Y_mag * 1000, label='Admittance |Y|', linewidth=2)
    
    # Specific points
    w_points = np.array([0.9, 1.0, 1.1]) * w0
    Y_points = np.sqrt( (1/R)**2 + (w_points*C - 1/(w_points*L))**2 )
    
    points_labels = ['0.9$\omega_0$', '$\omega_0$', '1.1$\omega_0$']
    colors = ['r', 'g', 'r']
    
    for wp, Yp, label, color in zip(w_points, Y_points, points_labels, colors):
        plt.plot(wp/1000, Yp*1000, 'o', color=color, markersize=8)
        # Annotate
        # Yp is in mS
        xy_text = (10, 10)
        if label == '$\omega_0$':
            xy_text = (10, -30)
        
        plt.annotate(f'{label}\n{Yp*1000:.3f} mS', 
                     xy=(wp/1000, Yp*1000), 
                     xytext=xy_text, 
                     textcoords='offset points',
                     arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'),
                     fontsize=10,
                     bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1, alpha=0.8))

    plt.axvline(w0/1000, color='k', linestyle='--', alpha=0.3, label='$\omega_0$')
    
    plt.title('Admittance |Y| Magnitude for Example 16.1')
    plt.xlabel('Frequency $\omega$ (krad/s)')
    plt.ylabel('Admittance Magnitude |Y| (mS)')
    
    # Limit y-axis to see the minima clearly. The max point of interest is ~0.65 mS.
    # Asymptotes go to infinity, compressing the view.
    plt.ylim(0, 1.0) 
    
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'example_16_1_admittance.png'), dpi=300)
    plt.close()
    print("Generated example_16_1_admittance.png")

if __name__ == "__main__":
    plot_normalized_q()
    plot_vary_r()
    plot_vary_lc_ratio()
    plot_zeta_effect()
    plot_example_16_1_admittance()
