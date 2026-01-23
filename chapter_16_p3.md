---
theme: seriph
background: https://cover.sli.dev
title: Chapter 16 Part III - Bode Diagrams (2nd Order) and Filters
info: |
  ## Chapter 16 Part III
  Frequency Response: Bode Diagrams and Filters
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
layout: cover
---

# Chapter 16: Frequency Response

## Part III

Presentation slides for Circuit Analysis

<div class="abs-br m-6 flex gap-2">
  <button @click="$slidev.nav.openInEditor()" title="Open in Editor" class="slidev-icon-btn">
    <carbon:edit />
  </button>
  <a href="https://github.com/slidevjs/slidev" target="_blank" class="slidev-icon-btn">
    <carbon:logo-github />
  </a>
</div>

---
transition: fade-out
---

## Outline

- Bode Diagrams (Complex Conjugate Pairs)
- Filters

---
layout: two-cols
---

## Complex Conjugate Pairs

- Consider the standard quadratic form: 

$$H(s) = 1 + 2\zeta(s/\omega_0) + (s/\omega_0)^2$$
- The quantity $\zeta$ is the **damping factor**.
- $\omega_0$ is the **cutoff frequency** of the asymptotic response.
- If $\zeta = 1$, $H(s) = (1 + s/\omega_0)^2$ (Two identical real poles/zeros).
- If $\zeta > 1$, $H(s)$ can be factored into two distinct real poles/zeros.
- If $\zeta < 1$, the roots are complex conjugates.

:: right ::
<img src="/s_plane_damping.svg" class="w-full mx-auto" alt="s-plane damping" />

---

## Magnitude Response (Complex Pairs)

<div class="grid grid-cols-2 gap-4">
<div>

- The magnitude response in dB is given by:

$$
H_{dB} = 20 \log_{10} \left| 1 + j2\zeta\left(\frac{\omega}{\omega_0}\right) - \left(\frac{\omega}{\omega_0}\right)^2 \right|
$$



- Asymptotes:
  - Low frequency ($\omega \ll \omega_0$): $20 \log_{10}(1) = 0 \text{ dB}$
  - High frequency ($\omega \gg \omega_0$): $20 \log_{10} |(j\omega/\omega_0)^2| = 40 \log_{10}(\omega/\omega_0)$. Slope of **+40 dB/decade**.
- Correction near $\omega_0$:
  - The correction at $\omega = \omega_0$ is given by: **$20 \log(2\zeta)$ dB**.

</div>
<div class="text-sm pl-5">
    <img src="/bode_damping_correction.svg" class="h-80 mx-auto" alt="bode damping correction" />

- If $\zeta = 1$: +6 dB correction.
- If $\zeta = 0.5$: No correction (0 dB error).
- If $\zeta = 0.25$: -6 dB correction.
- If $\zeta = 0.1$: -14 dB correction.
</div>
</div>

---
layout: two-cols
---

## Phase Response (Complex Pairs)

- For $H(j\omega) = 1 + j2\zeta(\omega/\omega_0) - (\omega/\omega_0)^2$
- Phase angle $\phi$:

$$
\phi = \tan^{-1}\left( \frac{2\zeta(\omega/\omega_0)}{1 - (\omega/\omega_0)^2} \right)
$$
- Asymptotic approximation:
  - $0^\circ$ for $\omega < 0.1 \omega_0$
  - $180^\circ$ for $\omega > 10 \omega_0$
  - Straight line slope: **$90^\circ$/decade** between $0.1 \omega_0$ and $10 \omega_0$.
- At cutoff frequency $\omega_0$: Phase is **$90^\circ$**.
- Corrections at $0.5\omega_0$ and $2\omega_0$:
  - $\zeta = 0.1$: $\pm 55^\circ$ error from asymptote.
  - $\zeta = 0.5$: $\pm 29^\circ$ error.
  - $\zeta = 1.0$: $\pm 10^\circ$ error.

:: right ::


<img src="/bode_phase_damping.svg" class="h-80 mx-auto" alt="Bode Phase Damping" />

---

## Example 16.10

Construct the Bode plot for the transfer function:

$$
H(s) = \frac{100,000s}{(s + 1)(10,000 + 20s + s^2)} = \frac{10s}{(1 + s)(1 + 0.002s + 0.0001s^2)}
$$

---

**Solution**:
1.  **Quadratic Factor**: $1 + \frac{20s}{10000} + \frac{s^2}{10000} = 1 + 2\zeta(\frac{s}{\omega_0}) + (\frac{s}{\omega_0})^2$.
2.  **Parameters**:
    - $\omega_0^2 = 10000 \implies \omega_0 = 100$ rad/s.
    - $2\zeta/\omega_0 = 0.002 \implies \zeta = 0.1$.
3.  **Standard Bode Form**:
    $$
    H(s) = \frac{10s}{(1+s)[1 + 2(0.1)(\frac{s}{100}) + (\frac{s}{100})^2]}
    $$
4.  **Asymptotes (Magnitude)**:
    - **Constant**: 10 (20 dB).
    - **Zero at Origin**: +20 dB/dec slope.
    - **Pole at $\omega=1$**: Slope changes by -20 dB/dec.
    - **Double Pole at $\omega=100$**: Slope changes by -40 dB/dec.

---

5.  **Asymptotes (Phase)**:
    - **Zero at Origin**: Constant $+90^\circ$.
    - **Pole at $\omega=1$**: Phase drops by $-45^\circ$/dec between 0.1 and 10. Final shift $-90^\circ$.
    - **Double Pole at $\omega=100$**: Phase drops by $-90^\circ$/dec between 10 and 1000. Final shift $-180^\circ$.
    - **Total Phase**: Starts at $+90^\circ$, passes through $+45^\circ$ (at $\omega=1$), drops to $-90^\circ$ (at $\omega=100$), and approaches $-180^\circ$ as $\omega \to \infty$.

6.  **Resonant Peak**:
    - Since $\zeta = 0.1$, correction at $\omega_0$ is needed.
    - Peak correction $= -20 \log_{10}(2\zeta) = -20 \log_{10}(0.2) \approx \mathbf{+14 \text{ dB}}$.
    - Actual magnitude at $\omega=100$ is $\sim 14 \text{ dB}$ above the asymptote.

---

<img src="/example_16_10_bode.svg" class="p-4 w-full mx-auto" alt="Example 16.10 Bode Plot" />
<div class="text-xs text-center opacity-70">Fig 16.10: Bode Magnitude and Phase Plots</div>

---

## Practice 16.15

If $H(s) = 1000s^2 / (s^2 + 5s + 100)$, sketch the Bode amplitude plot and calculate a value for:

\(a\) $\omega$ when $H_{dB} = 0$;

\(b\) $H_{dB}$ at $\omega = 1$;

\(c\) $H_{dB}$ as $\omega \to \infty$.

**Answers**:
- \(a\) 0.316 rad/s
- \(b\) 20 dB
- \(c\) 60 dB

---

**Solution**:

1.  **Standard Form**:
    $$
    H(s) = \frac{1000s^2}{s^2 + 5s + 100} = \frac{10s^2}{1 + 0.05s + 0.01s^2} = \frac{10s^2}{1 + 2(0.25)(\frac{s}{10}) + (\frac{s}{10})^2}
    $$
2.  **Parameters**:
    - Constant gain $K = 10 \implies 20 \text{ dB}$.
    - Double zero at origin ($s^2 \implies +40 \text{ dB/dec}$).
    - Second-order pole at $\omega_0 = 10$ with $\zeta = 0.25$.
3.  **Calculations**:
    - \(a\) $H_{dB} = 20 \log_{10}(10\omega^2 / 100) = 0 \implies \omega^2 = 10/100 \implies \omega = 0.316 \text{ rad/s}$.
    - \(b\) At $\omega=1$, substitution yields $|H(j1)| = \left| \frac{1000(j1)^2}{(j1)^2 + 5(j1) + 100} \right| = \left| \frac{-1000}{99 + 5j} \right| \approx 10.1 \implies \mathbf{20 \text{ dB}}$.
    - \(c\) As $\omega \to \infty$, $H(s) \approx \frac{1000s^2}{s^2} = 1000 \implies 20 \log_{10}(1000) = \mathbf{60 \text{ dB}}$.

---

**Bode Plot**:

<img src="/practice_16_15_bode.svg" class="p-4 w-full mx-auto" alt="Practice 16.15 Bode Plot" />
<div class="text-xs text-center opacity-70">Fig 16.15: Bode Magnitude and Phase Plots for Practice 16.15</div>

---

## 16.7 Filters

<div class="grid grid-cols-2 gap-4">
<div>

- Filters are used in modern electronics to obtain DC voltages, eliminate noise, separate channels, etc.
- A filter selects the frequencies that may pass through a network.
- **Low-pass filter**: Passes frequencies below a cutoff, attenuates above.
- **High-pass filter**: Passes frequencies above a cutoff, attenuates below.
- **Bandpass filter**: Passes a specific range (passband), attenuates outside (stopband).
- **Bandstop/Notch filter**: Blocks a specific range of frequencies.
</div>
<div>
    <img src="/filter_types_ideal.svg" class="w-full mx-auto" alt="ideal filter types" />
</div>
</div>

---
layout: two-cols-header
---

## Passive Low-Pass and High-Pass Filters



- Can be constructed using a single capacitor and resistor (RC circuit).

::left::

- **Low-Pass**: Output across Capacitor.
  - Using voltage division: $V_{out} = V_{in} \frac{1/sC}{R + 1/sC}$
  - Multiplying numerator and denominator by $sC$:
    $$H(s) = \frac{V_{out}}{V_{in}} = \frac{1}{1 + sRC}$$
  - Cutoff (Break) frequency $\omega_c = 1/RC$.
  - Low freq gain $\approx 1$, High freq gain $\to 0$.

::right::

<img src="/rc_low_pass_filter.svg" class="h-70 mx-auto" alt="RC low-pass filter" />


---

- **High-Pass**: Output across Resistor (swap R and C).
  - Using voltage division: $V_{out} = V_{in} \frac{R}{R + 1/sC}$
  - Multiplying numerator and denominator by $sC$:
    $$H(s) = \frac{V_{out}}{V_{in}} = \frac{sRC}{1 + sRC}$$
  - Passes high frequencies.

<img src="/rc_high_pass_filter.svg" class="h-70 mx-auto" alt="RC high-pass filter" />

---

## Example 16.14

Design a high-pass filter with a cutoff frequency of 3 kHz.

---

**Solution (Practical Approach)**:

1.  **Identify Parameters**:
    - $f_c = 3 \text{ kHz} \implies \omega_c = 2\pi(3000) = 6000 \pi \text{ rad/s}$

2.  **Select Component**:
    - Engineering Tip: Select **Capacitor first**, as standard capacitor values are more limited than resistors.
    - Let **$C = 10 \text{ nF}$** (a common standard value).

3.  **Calculate Resistor**:
    - Since $\omega_c = 1/RC \implies R = \frac{1}{\omega_c C}$
    - $R = \frac{1}{(6000\pi)(10 \times 10^{-9})} \approx 5305 \Omega$
    - Use a standard **$5.1 \text{ k}\Omega$** resistor for a close approximation ($f_c \approx 3.12 \text{ kHz}$) or a **$5.36 \text{ k}\Omega$** precision resistor for exactness.

---

4.  **Comparison: R-first ($4.7 \text{ k}\Omega$) vs. C-first ($10 \text{ nF}$)**

| Approach | Initial Selection | Calculated Requirement | Practical Result |
| :--- | :--- | :--- | :--- |
| **Resistor First** | $R = 4.7 \text{ k}\Omega$ | $C = \mathbf{11.3 \text{ nF}}$ | Hard to find non-standard $C$. Need to parallel $10\text{nF} + 1.2\text{nF} + \dots$ |
| **Capacitor First** | $C = \mathbf{10 \text{ nF}}$ | $R = \mathbf{5.3 \text{ k}\Omega}$ | Easy to find $5.1\text{k}\Omega$ or use $10\text{k}\Omega$ trimmer for precision. |

**Practical Tip**: In filter design, always try to **fix the component with fewer standard values (Capacitor)** first. Resistors are inexpensive and available in much finer increments (E24/E96 series).

---

## Practice 16.16

Design a high-pass filter with a cutoff frequency of 13.56 MHz, a common RF power supply frequency. Verify your design using PSpice.

---

**Solution (Practical Approach)**:

1.  **Identify Parameters**:
    - $f_c = 13.56 \text{ MHz} \implies \omega_c = 2\pi(13.56 \times 10^6) \approx 8.52 \times 10^7 \text{ rad/s}$

2.  **Select Component**:
    - Following the engineering workflow, we select **Capacitor first**.
    - For high-frequency RF circuits, a small standard capacitor is appropriate.
    - Let **$C = 100 \text{ pF} = 100 \times 10^{-12} \text{ F}$**.

3.  **Calculate Resistor**:
    - $R = \frac{1}{\omega_c C} = \frac{1}{(8.52 \times 10^7)(100 \times 10^{-12})} \approx 117.4 \Omega$
    - A standard **$120 \Omega$** (5% tolerance) or **$118 \Omega$** (1% tolerance) resistor would be used.

---

4.  **Verification**:
    - If we use $C = 100 \text{ pF}$ and $R = 120 \Omega$:
    - $f_c = \frac{1}{2\pi (120)(100 \times 10^{-12})} \approx 13.26 \text{ MHz}$ (within 2.2% of target).

---

## Bandpass Filters

<div class="grid grid-cols-2 gap-4">
<div>

- Combining low-pass and high-pass characteristics.



- Consider a series $LCR$ circuit with $V_i$ and $V_o$ across $R$.
- **Transfer Function $A_v$**:
  $$A_v(j\omega) = \frac{V_o}{V_i} = \frac{R}{R + j\omega L + 1/j\omega C}$$
  Multiply num/den by $j\omega C$:
  $$A_v(j\omega) = \frac{j\omega RC}{1 - \omega^2 LC + j\omega RC}$$
- **Magnitude $|A_v|$**:
  $$|A_v(j\omega)| = \frac{\omega RC}{\sqrt{(1 - \omega^2 LC)^2 + (\omega RC)^2}}$$

</div>
<div>

<img src="/rlc_bandpass_filter.svg" class="h-70 mx-auto" alt="RLC bandpass filter" />

- **Frequency Limits**:
  - As $\omega \to 0$: $|A_v| \to \frac{0}{1} = \mathbf{0}$
  - As $\omega \to \infty$: $|A_v| \to \frac{\omega RC}{\omega^2 LC} = \mathbf{0}$
- The circuit acts as a **bandpass filter**, passing frequencies near $\omega_0 = 1/\sqrt{LC}$ where the denominator is minimum ($|A_v|=1$).

</div>
</div>

---

## Bandpass Filter (Continued)

- **Transfer Function (s-domain)**:
  - Substitute $j\omega \to s$:
    $$H(s) = \frac{sRC}{LCs^2 + sRC + 1}$$
  - Divide numerator and denominator by $LC$:
    $$H(s) = \frac{s(R/L)}{s^2 + s(R/L) + 1/LC}$$

- Comparing to $H(s) = \frac{K s}{s^2 + 2\zeta\omega_0 s + \omega_0^2}$
  - **Resonant Frequency**: $\omega_0 = \frac{1}{\sqrt{LC}}$
  - **Bandwidth**: $\beta = \frac{R}{L}$
  - **Quality Factor**: $Q = \frac{\omega_0}{\beta} = \frac{1}{R}\sqrt{\frac{L}{C}}$

---

- **Cutoff Frequencies ($\omega_L, \omega_H$)**:
  - Occur at half-power points where $|H(j\omega)| = \frac{1}{\sqrt{2}}$.
  - Solving $\frac{\omega RC}{\sqrt{(1-\omega^2 LC)^2 + (\omega RC)^2}} = \frac{1}{\sqrt{2}} \implies \omega_{L,H} = \mp \frac{R}{2L} + \sqrt{\left(\frac{R}{2L}\right)^2 + \frac{1}{LC}}$
  - Bandwidth $\beta = \omega_H - \omega_L = \frac{R}{L}$.
  - Resonant frequency is the geometric mean: $\omega_0 = \sqrt{\omega_L \omega_H}$.

---

## Derivation of Cutoff Frequencies

**Condition**: Magnitude is $1/\sqrt{2}$ of max value (1).
$$ \frac{\omega RC}{\sqrt{(1-\omega^2 LC)^2 + (\omega RC)^2}} = \frac{1}{\sqrt{2}} $$
**Square both sides**:
$$ \frac{(\omega RC)^2}{(1-\omega^2 LC)^2 + (\omega RC)^2} = \frac{1}{2} \implies 2(\omega RC)^2 = (1-\omega^2 LC)^2 + (\omega RC)^2 $$
**Simplify**:
$$ (\omega RC)^2 = (1-\omega^2 LC)^2 \implies \pm \omega RC = 1 - \omega^2 LC $$
**Rearrange into Quadratic Form** ($\omega^2 LC \pm \omega RC - 1 = 0$):
$$ \omega^2 \pm \frac{R}{L}\omega - \frac{1}{LC} = 0 $$

---

**Solving for $\omega$** (Quadratic Formula):
$$ \omega = \frac{\mp \frac{R}{L} + \sqrt{(\frac{R}{L})^2 + \frac{4}{LC}}}{2} = \mp \frac{R}{2L} + \sqrt{\left(\frac{R}{2L}\right)^2 + \frac{1}{LC}} $$








---

## Example 16.12

Design a bandpass filter characterized by a bandwidth of 1 MHz and a high-frequency cutoff of 1.1 MHz.

---

**Solution**:

1.  **Identify Frequencies**:
    - Bandwidth $B = 1 \text{ MHz}$.
    - High-frequency cutoff $f_H = 1.1 \text{ MHz}$.
    - Low-frequency cutoff $f_L = f_H - B = 1.1 - 1.0 = \mathbf{0.1 \text{ MHz} (100 \text{ kHz})}$.

2.  **Calculate Center Frequency ($f_0$)**:
    - $f_0 = \sqrt{f_L f_H} = \sqrt{0.1 \times 1.1} \approx \mathbf{0.3317 \text{ MHz} (331.7 \text{ kHz})}$.

3.  **Select Components**:
    - Let's use a series RLC circuit.
    - Pick a standard inductor, e.g., **$L = 100 \mu\text{H}$**.
    - Calculate **$R$** from bandwidth: $R = 2\pi B L = 2\pi(10^6)(100 \times 10^{-6}) = 200\pi \approx \mathbf{628.3 \Omega}$.
    - Calculate **$C$** from $f_0$: $C = \frac{1}{(2\pi f_0)^2 L} = \frac{1}{(2\pi \cdot 331.7 \cdot 10^3)^2 (100 \cdot 10^{-6})} \approx \mathbf{2.3 \text{ nF}}$.

---


<img src="/example_16_12_plot.svg" class="h-100 mx-auto p-4" alt="Example 16.12 Freq Response" />

- **Geometric Symmetry**: The response depends on $\omega/\omega_0$. Since $\log(\omega/\omega_0) = -\log(\omega_0/\omega)$, the magnitude is symmetric around $\omega_0$ on a logarithmic scale.
---

## Practice 16.17

Design a bandpass filter with $\omega_L = 100 \text{ rad/s}$ and $\omega_H = 10 \text{ krad/s}$.

**Answer**:
- One possible solution: $R = 990 \Omega$, $L = 100 \text{ mH}$, $C = 10 \mu\text{F}$.

---

**Solution**:

1.  **Calculate Parameters**:
    - Center Frequency: $\omega_0 = \sqrt{\omega_L \omega_H} = \sqrt{100 \times 10,000} = \sqrt{1,000,000} = 1000 \text{ rad/s}$.
    - Bandwidth: $\beta = \omega_H - \omega_L = 10,000 - 100 = 9900 \text{ rad/s}$.

2.  **Design Series RLC**:
    - Relationships: $\omega_0^2 = \frac{1}{LC}$ and $\beta = \frac{R}{L}$.
    - $LC = \frac{1}{\omega_0^2} = \frac{1}{10^6} = 1 \mu\text{s}^2$. 

3.  **Component Selection**:
    - Pick a standard inductor: **$L = 100 \text{ mH} = 0.1 \text{ H}$**.
    - Calculate **$R$**: $R = L\beta = 0.1 \times 9900 = \mathbf{990 \Omega}$.
    - Calculate **$C$**: $C = \frac{1}{\omega_0^2 L} = \frac{10^{-6}}{0.1} = 10^{-5} \text{ F} = \mathbf{10 \mu\text{F}}$.

---

## Active Filters

- Use active elements like Op Amps.
- Overcomes shortcomings of passive filters (loading effects, inductor size/loss).
- Can provide gain.

---

## Example 16.13

Design an active low-pass filter with a cutoff frequency of 10 kHz and a voltage gain of 40 dB.

<img src="/active_lpf_circuit.svg" class="h-60 mx-auto p-5" alt="Active LPF Circuit" />

- **Non-inverting Amplifier Equation**: $K = 1 + \frac{R_f}{R_1}$

---

**Solution**:

1.  **Identify Specifications**:
    - $f_c = 10 \text{ kHz}$
    - Gain $G = 40 \text{ dB} \implies 20 \log_{10}(K) = 40 \implies K = 100 \text{ V/V}$.

2.  **Circuit Topology**:
    - Use a non-inverting op-amp active low-pass filter. 
    - The transfer function is: $H(s) = \left(1 + \frac{R_f}{R_1}\right) \frac{1}{1 + sRC}$.

3.  **Calculate RC (Filter stage)**:
    - Engineering Tip: Select **Capacitor first**.
    - Let **$C = 10 \text{ nF}$**.
    - $R_2 = \frac{1}{2\pi f_c C} = \frac{1}{2\pi(10^4)(10 \times 10^{-9})} \approx \mathbf{1591.5 \Omega}$.
    - Practical value: **$1.6 \text{ k}\Omega$** (1% tolerance).



---

4.  **Calculate $R_f$ and $R_1$ (Gain stage)**:
    - $K = 1 + \frac{R_f}{R_1} = 100 \implies \frac{R_f}{R_1} = 99$.
    - Let **$R_1 = 1 \text{ k}\Omega$**.
    - Then **$R_f = 99 \text{ k}\Omega$**.
    - Practical value: **$100 \text{ k}\Omega$** for $R_f$ gives $K = 101 \approx 40.1 \text{ dB}$.

<img src="/active_lpf_response.svg" class="p-4 h-80 mx-auto" alt="Active LPF Response" />

---

## Practice 16.18

Design a low-pass filter circuit with a gain of 30 dB and a cutoff frequency of 1 kHz.

**Answer**:
- One possible solution: 

$R_1 = 100 \text{ k}\Omega$, $R_f = 3.062 \text{ M}\Omega$, $R_2 = 79.58 \Omega$, $C = 2 \mu\text{F}$.

---
layout: default
---


**Solution**:

**Gain Calculation**:
- $20 \log_{10} K = 30 \implies \log_{10} K = 1.5 \implies K = 10^{1.5} \approx 31.62$.
- $K = 1 + \frac{R_f}{R_1} = 31.62 \implies \frac{R_f}{R_1} = 30.62$.
- Choose **$R_1 = 100 \text{ k}\Omega$**.
- Then **$R_f = 30.62 \times 100 \text{ k}\Omega = 3.062 \text{ M}\Omega$**.

2.  **Filter Component Calculation**:
- $f_c = 1 \text{ kHz}$.
- Choose **$C = 2 \mu\text{F}$**.
- Calculate $R_2$:
  $R_2 = \frac{1}{2\pi f_c C} = \frac{1}{2\pi (1000) (2 \times 10^{-6})} \approx \mathbf{79.58 \Omega}$
