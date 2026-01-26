---
theme: seriph
background: https://cover.sli.dev
title: Chapter 16 Part II - Scaling and Bode Diagrams (1st Order)
info: |
  ## Chapter 16 Part 2
  Frequency Response: Scaling and Bode Diagrams
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
layout: cover
---

# Chapter 16: Frequency Response

## Part II - Scaling and Bode Diagrams

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

- Scaling
- Bode Diagrams

---

## 16.5 Scaling

- The scaling procedures discussed in this section enable us to analyze networks composed of practical-sized elements by scaling the element values to permit more convenient numerical calculations.
- Let us select the parallel resonant circuit shown in Figure below as our example.
- $R = 2.5 \Omega$, $L = 0.5$ H, $C = 2$ F.
- $\omega_0 = 1/\sqrt{LC} = 1$ rad/s. At resonance, $Z_{in} = R = 2.5 \Omega$.

<div class="grid grid-cols-2 gap-4 items-center mt-4">
  <div class="flex flex-col items-center">
    <img src="/fig_16_17_parallel_rlc.svg" class="w-full bg-white p-2 rounded" />
    <div class="text-xs text-center opacity-70 mt-1">(a) Unscaled Parallel RLC</div>
  </div>
  <div class="flex flex-col items-center">
    <img src="/fig_16_17_response.svg" class="h-55 rounded bg-white p-1" />
    <div class="text-xs text-center opacity-70 mt-1">(b) Impedance Response</div>
  </div>
</div>

---
layout: two-cols
---

## 16.5 Scaling (continued)

- Let us assume that our goal is to scale this network in such a way as to provide an impedance **maximum of 5000 $\Omega$** at a resonant frequency of **$5 \times 10^6$ rad/s**, or 796 kHz.
- We may use the same response curve shown in Figure on the right. If every number on the **ordinate** scale is increased by a factor of 2000 and every number on the **abscissa** scale is increased by a factor of $5 \times 10^6$.
- We will treat this as two problems:
  1.  Scaling in magnitude by a factor of **2000**
  2.  Scaling in frequency by a factor of **$5 \times 10^6$**

:: right ::


  <img src="/fig_scaling_comparison.svg" class="w-full rounded bg-white p-4 mt-20" />

<div class="text-xs text-center opacity-70 mt-1">Comparison of Original vs Scaled Response</div>

---

## Magnitude Scaling

- Magnitude scaling is defined as the process by which the impedance of a two-terminal network is increased by a factor of $K_m$, the frequency remaining constant. The factor $K_m$ is real and positive.
- To increase the input impedance of a network by a factor of $K_m$, it is sufficient to increase the impedance of each element in the network by this same factor.
  $$ R \to K_m R $$
  $$ L \to K_m L $$
  $$ C \to C/K_m $$

---

## Frequency Scaling

- We define frequency scaling as the process by which the frequency at which any impedance occurs is increased by a factor of $K_f$.
- Frequency scaling is accomplished by scaling each passive element in frequency.
  $$ R \to R $$
  $$ L \to L/K_f $$
  $$ C \to C/K_f $$

---

## Example 16.6

**Problem**: Scale the network shown in Fig. 16.20(a) by $K_m = 20$ and $K_f = 50$, and then find $Z_{in}(s)$ for the scaled network.

<div class="flex justify-center my-4">
  <img src="/fig_16_20a_scaling_example.svg" class="w-100 bg-white p-2 rounded" />
</div>
<div class="text-xs text-center opacity-70">Fig 16.20(a): Network for Example 16.6</div>

---

**Solution**:
1.  **Original Values**:
    - $L = 0.5$ H, $C = 0.05$ F.
    - Controlled Source: $I = 0.2 V_1$ (Conductance $g = 0.2$ S).
2.  **Scaled Values** ($K_m = 20, K_f = 50$):
    - **Inductor**: $L' = \frac{K_m L}{K_f} = \frac{20 \times 0.5}{50} = 0.2$ H.
    - **Capacitor**: $C' = \frac{C}{K_m K_f} = \frac{0.05}{20 \times 50} = 50 \mu$F.
    - **VCCS**: $g' = \frac{g}{K_m} = \frac{0.2}{20} = 0.01$ S.
    - The new source is $0.01 V_1$.
3.  **Result**: Determine $Z_{in}(s)$ by applying a 1 A source.
    - $V_1 = I_{in} \frac{1}{sC'} = \frac{1}{s(50 \times 10^{-6})} = \frac{20000}{s}$.
    - KCL at node: $1 = 0.01 V_1 + I_L \implies I_L = 1 - 0.01(\frac{20000}{s}) = 1 - \frac{200}{s}$.
    - $V_L = I_L (sL') = (1 - \frac{200}{s})(0.2s) = 0.2s - 40$.
    - $Z_{in} = \frac{V_{in}}{1} = V_1 + V_L = \frac{20000}{s} + 0.2s - 40 = \frac{0.2s^2 - 40s + 20000}{s}$.

---

## Practice 16.9

A parallel resonant circuit is defined by $C = 0.01 \text{ F}$, $B = 2.5 \text{ rad/s}$, and $\omega_0 = 20 \text{ rad/s}$. Find the values of $R$ and $L$ if the network is scaled in:

(a) magnitude by a factor of 800;
(b) frequency by a factor of $10^4$;
\(c) magnitude by a factor of 800 and frequency by a factor of $10^4$.

**Answers**:
- (a) $32 \text{ k}\Omega, 200 \text{ H}$
- (b) $40 \Omega, 25 \mu\text{H}$
- \(c) $32 \text{ k}\Omega, 20 \text{ mH}$

---
layout: two-cols
---

## Practice 16.9 Solution

**1. Original Parameters**:
- $C = 0.01$ F, $B = 2.5$ rad/s, $\omega_0 = 20$ rad/s.
- $L = \frac{1}{\omega_0^2 C} = \frac{1}{20^2 \times 0.01} = \frac{1}{4} = \mathbf{0.25 \text{ H}}$
- $R = \frac{1}{BC} = \frac{1}{2.5 \times 0.01} = \frac{1}{0.025} = \mathbf{40 \ \Omega}$

:: right ::


**2. Scaled Values**:
- **(a) $K_m = 800, K_f = 1$**:
  - $R' = K_m R = 800 \times 40 = \mathbf{32 \text{ k}\Omega}$
  - $L' = \frac{K_m L}{K_f} = 800 \times 0.25 = \mathbf{200 \text{ H}}$
- **(b) $K_m = 1, K_f = 10^4$**:
  - $R' = R = \mathbf{40 \ \Omega}$
  - $L' = \frac{L}{K_f} = \frac{0.25}{10^4} = \mathbf{25 \ \mu\text{H}}$
- **\(c) $K_m = 800, K_f = 10^4$**:
  - $R' = K_m R = \mathbf{32 \text{ k}\Omega}$
  - $L' = \frac{K_m L}{K_f} = \frac{800 \times 0.25}{10^4} = \mathbf{20 \text{ mH}}$


---
layout: two-cols
---

## 16.6 Bode Diagrams

- To discover a quick method of obtaining an approximate picture of the amplitude and phase variation of a given transfer function as functions of $\omega$.
- We construct an **asymptotic plot** approach, or a **Bode plot**.
- Both magnitude ($|H|$) and phase ($\angle H$) are plotted against a **logarithmic frequency scale**.

:: right ::

<div class="flex flex-col justify-center h-full items-center px-4">
  <img src="/bode_intro_asymptotes.svg" class="w-full rounded bg-white p-1" />
</div>

---

## The Decibel (dB) Scale

- The approximate response curve we construct is called **an asymptotic plot**, or **a Bode plot**, or **a Bode diagram**, after its developer, Hendrik W. Bode.
- Both the magnitude and phase curves are shown using a logarithmic frequency scale for the abscissa.
- The magnitude itself is also shown in logarithmic units called **decibels (dB)**.
- Definition: $H_{dB} = 20 \log_{10} |H(j\omega)|$
- Inverse: $|H(j\omega)| = 10^{H_{dB}/20}$

<div class="grid grid-cols-2 gap-4 mt-6">
<div class="bg-gray-50 p-3 rounded border border-gray-200 text-sm">

**Common dB Values**
- **$0 \text{ dB}$**: $|H| = 1$ (Unity)
- **$6 \text{ dB}$**: $|H| \approx 2$ (Double)
- **$20 \text{ dB}$**: $|H| = 10$ (Tenfold)

</div>
<div class="bg-gray-50 p-3 rounded border border-gray-200 text-sm">

**Quick Check**
- $+20 \text{ dB} \to \times 10$
- $-20 \text{ dB} \to \times 0.1$
- $+40 \text{ dB} \to \times 100$

</div>
</div>

---

## Practice 16.10

Calculate $H_{dB}$ at $\omega = 146 \text{ rad/s}$ if $H(s)$ equals:
(a) $20/(s+100)$
(b) $20(s+100)$
\(c) $20s$

Calculate $|H(j\omega)|$ if $H_{dB}$ equals:
(d) $29.2 \text{ dB}$
(e) $-15.6 \text{ dB}$
(f) $-0.318 \text{ dB}$

**Answers**:
- (a) $-18.94 \text{ dB}$
- (b) $71.0 \text{ dB}$
- \(c) $69.3 \text{ dB}$
- (d) $28.8$
- (e) $0.1660$
- (f) $0.964$

---
layout: two-cols
---

## Practice 16.10 Solution

**Part 1: dB Calculations** ($\omega = 146$)

- **(a)** $H(s) = \frac{20}{s+100}$
  $|H| = \frac{20}{\sqrt{146^2 + 100^2}} \approx 0.1130$
  $H_{dB} = 20 \log_{10}(0.1130) = \mathbf{-18.94 \text{ dB}}$

- **(b)** $H(s) = 20(s+100)$
  $|H| = 20\sqrt{146^2 + 100^2} \approx 3539.2$
  $H_{dB} = 20 \log_{10}(3539.2) = \mathbf{71.0 \text{ dB}}$

- **\(c)** $H(s) = 20s \implies |H| = 20(146) = 2920$
  $H_{dB} = 20 \log_{10}(2920) = \mathbf{69.3 \text{ dB}}$

:: right ::


**Part 2: Inverse Calculations**
$|H| = 10^{H_{dB}/20}$

- **(d)** $29.2 \text{ dB}$
  $|H| = 10^{29.2/20} = 10^{1.46} = \mathbf{28.8}$

- **(e)** $-15.6 \text{ dB}$
  $|H| = 10^{-15.6/20} = 10^{-0.78} = \mathbf{0.1660}$

- **(f)** $-0.318 \text{ dB}$
  $|H| = 10^{-0.318/20} = 10^{-0.0159} = \mathbf{0.964}$


---

## Determination of Asymptotes

- Factor $H(s)$ to display poles/zeros. Consider a zero at $s = -a$:
$$ H(s) = 1 + \frac{s}{a} $$
$$ |H(j\omega)| = \sqrt{1 + \left(\frac{\omega}{a}\right)^2} $$
$$ H_{dB} = 20 \log_{10} \sqrt{1 + \left(\frac{\omega}{a}\right)^2} $$

**Approximations**:
- **$\omega \ll a$**: 
$$H_{dB} \approx 20 \log_{10} 1 = \mathbf{0 \text{ dB}}$$
- **$\omega \gg a$**: 
$$H_{dB} \approx 20 \log_{10} \frac{\omega}{a}$$

---

## Determination of Asymptotes (cont.)

  <img src="/zero_asymptote_plot.svg" class="h-60 rounded bg-white p-1 mx-auto" />


- At $\omega = a$, $H_{dB}$ error is max.
- At $\omega = 10a$, $H_{dB}$ increases by 20 dB.
- Thus, the value of $H_{dB}$ increases **20 dB** for every 10-fold increase in frequency.
- The asymptote therefore has a slope of **20 dB/decade**.
- Since $H_{dB}$ increases by **6 dB** when $\omega$ doubles, an alternate value for the slope is **6 dB/octave**.
- The frequency $\omega = a$ is described as the **corner**, **break**, **3 dB**, or **half-power frequency**.


---
layout: two-cols
---

## Smooth Bode Plots

- The exact magnitude response is a **smooth curve**, not a "broken line" asymptote.
- The **error (deviation)**:
  - **Corner Frequency ($a$):** Error is maximum at $\mathbf{+3 \text{ dB}}$.
  - **One Octave Away ($0.5a$ or $2a$):** Error is approx. $\mathbf{+1 \text{ dB}}$.
- For most engineering applications, the asymptotic plot is sufficient, but these corrections improve accuracy.

<br>

**3 dB Error at $\omega = a$:**
$$ H_{dB}(\omega = a) = 20 \log_{10} \sqrt{1 + (a/a)^2} = 20 \log_{10} \sqrt{2} \approx \mathbf{3.01 \text{ dB}} $$

:: right ::

<div class="flex flex-col justify-center h-full items-center px-4">
  <img src="/smooth_bode_plot.svg" class="w-120 rounded bg-white p-1" />
  <div class="text-xs text-center opacity-70 mt-2">Smooth vs. Asymptotic Magnitude Plot</div>
</div>

---

## Multiple Terms

- Most transfer functions are composed of a constant $K$ and several first-order factors.
- Because we use a **logarithmic scale (dB)**, the total response is simply the **sum** of the individual responses:
$$ H_{dB} = 20 \log_{10} K + \sum 20 \log_{10} \left| 1 + \frac{s}{z_n} \right| - \sum 20 \log_{10} \left| 1 + \frac{s}{p_n} \right| $$

**Example Derivation**:
For $H(s) = K \left( 1 + \frac{s}{z_1} \right) \left( 1 + \frac{s}{z_2} \right)$:
1. Substitute $s = j\omega$ and take the magnitude:
   $|H(j\omega)| = |K| \cdot \left| 1 + \frac{j\omega}{z_1} \right| \cdot \left| 1 + \frac{j\omega}{z_2} \right|$
2. Convert to decibels ($20 \log_{10}$):
   $H_{dB} = 20 \log_{10} |K| + 20 \log_{10} \left| 1 + \frac{j\omega}{z_1} \right| + 20 \log_{10} \left| 1 + \frac{j\omega}{z_2} \right|$

**Procedure**:
1. Draw the asymptotes for each individual term separately.
2. Sum the asymptotes point-by-point to obtain the **composite asymptotic plot**.
3. Apply corrections ($\pm 3 \text{ dB}$ at corners) if a smooth curve is needed.

---

## Example 16.7

**Problem**: Obtain the Bode plot of the input impedance of the network shown in Fig. 16.22 (Series RL with $R=20\Omega$, $L=0.2H$ based on solution).

<div class="flex justify-center my-4">
  <img src="/example_16_7_circuit.svg" class="w-150 rounded bg-white p-2" />
</div>

---
layout: two-cols
---

**Solution**:
1.  **Impedance Function**: $Z_{in}(s) = 20 + 0.2s$.
2.  **Standard Form**:
    - $H(s) = 20(1 + \frac{0.2s}{20}) = 20(1 + \frac{s}{100})$.
3.  **Components**:
    - **DC Gain**: $K = 20 \implies 20 \log 20 = 26 \text{ dB}$.
    - **Zero**: $s = -100$ (Break frequency $\omega = 100$ rad/s).
4.  **Plot Construction**:
    - Start at 26 dB for $\omega < 100$.
    - At $\omega = 100$, slope changes to $+20$ dB/decade.

:: right ::

<img src="/example_16_7_asymptotes.svg" class="h-55 rounded bg-white p-1 mx-auto" />
<div class="text-[10px] text-center opacity-70 mb-2">1. Individual Asymptotic Terms</div>

<img src="/example_16_7_composite.svg" class="h-55 rounded bg-white p-1 mx-auto" />
<div class="text-[10px] text-center opacity-70">2. Composite Asymptotic (Summed)</div>
---

## Practice 16.11

Construct a Bode magnitude plot for $H(s) = 50 + s$.

**Answers**:
- 34 dB, $\omega < 50 \text{ rad/s}$
- slope = +20 dB/decade, $\omega > 50 \text{ rad/s}$

---
layout: two-cols
---

**Solution**:
1.  **Standard Form**:
    - $H(s) = 50(1 + \frac{s}{50})$.
2.  **Components**:
    - **DC Gain**: $K = 50$
    - <span class="text-orange-500">🧠 **Mental Math**</span>: $20 \log 50 = 20 \log (100/2) = 20 \log 100 - 20 \log 2 \approx 40 - 6 = 34 \text{ dB}$.
    - **Zero**: Break frequency at $\omega = 50 \text{ rad/s}$.
3.  **Plot Construction**:
    - Start at **34 dB** for $\omega < 50$.
    - At $\omega = 50$, slope becomes **+20 dB/decade**.
    - <span class="text-orange-500">**Note**</span>: $+20 \text{ dB/dec} \approx +6 \text{ dB/octave}$.

:: right ::

<img src="/prac_16_11_bode.svg" class="w-120 rounded bg-white p-1 mx-auto" />

<div class="text-[10px] text-center opacity-70">

Bode Magnitude Plot: $H(s) = 50 + s$
</div>

---
layout: two-cols
---
## Phase Response

<div class="text-base">

For the factor $H(s) = 1 + s/a$, the phase is:
$$\phi(\omega) = \arg H(j\omega) = \tan^{-1} \left( \frac{\omega}{a} \right)$$

**Key Points**:
- **$\omega \ll a$**: $\phi \approx \tan^{-1}(0) = \mathbf{0^\circ}$
- **$\omega = a$**: $\phi = \tan^{-1}(1) = \mathbf{45^\circ}$
- **$\omega \gg a$**: $\phi \approx \tan^{-1}(\infty) = \mathbf{90^\circ}$

**Asymptotic Construction**:
- We construct a straight-line approximation extending from:
  - $0^\circ$ at $\omega = 0.1a$
  - to $90^\circ$ at $\omega = 10a$.
- This line passes through $45^\circ$ at $\omega = a$ with a slope of **$45^\circ$/decade**.

</div>

:: right ::

<img src="/phase_response_plot.svg" class="w-110 rounded bg-white p-1 mx-auto" />

<div class="text-xs">

**Errors**:
- Max diff $\pm 5.71^\circ$ at $\omega = 0.1a$ and $10a$.
- Errors of $\pm 5.29^\circ$ occur at $\omega = 0.394a$ and $2.54a$.
- Error is zero at $\omega = 0.159a$, $a$, and $6.31a$.

</div>

---

## Practice 16.12

Draw the Bode phase plot for the transfer function of Example 16.7:
$$H(s) = 20 + 0.2s = 20(1 + s/100)$$

**Answers**:
- $0^\circ$, $\omega \le 10$
- $90^\circ$, $\omega \ge 1000$
- $45^\circ$, $\omega = 100$
- $45^\circ$/dec slope, $10 < \omega < 1000$.

---
layout: two-cols
---

**Solution**:
1.  **Transfer Function**:
    - $H(s) = 20(1 + s/100)$.
2.  **Phase Components**:
    - $\arg(20) = 0^\circ$ (Constant).
    - $\arg(1 + j\omega/100) = \tan^{-1}(\omega/100)$.
3.  **Asymptotic Steps**:
    - **$\omega \le 10$**: $0.1a \implies \mathbf{0^\circ}$.
    - **$\omega = 100$**: Break freq $\implies \mathbf{45^\circ}$.
    - **$\omega \ge 1000$**: $10a \implies \mathbf{90^\circ}$.
    - **Slope**: $\frac{90-0}{1} = \mathbf{45^\circ/\text{decade}}$.

:: right ::

<img src="/prac_16_12_phase.svg" class="w-120 rounded bg-white p-1 mx-auto" />
<div class="text-xs text-center opacity-70 mt-2">

Bode Phase Response: $H(s) = 20 + 0.2s$

</div>

---
layout: two-cols
---

## Additional Considerations

- **Simple Pole**:
  $$ H(s) = \frac{1}{1 + s/a} $$
  - Since this is the reciprocal of a zero, the logarithmic operation leads to a Bode plot which is the negative of that obtained previously.
  - Amplitude: 0 dB up to $\omega = a$, then slope is **-20 dB/decade**.
  - Phase: $0^\circ$ for $\omega < 0.1a$, $-90^\circ$ for $\omega > 10a$, slope **$-45^\circ$/decade** in between.

:: right ::


  <img src="/pole_magnitude_asymptote.svg" class="h-60 bg-white p-1 rounded mx-auto" />
  <img src="/pole_phase_asymptote.svg" class="h-60 bg-white p-1 rounded mx-auto mt-5" />


---
layout: two-cols
---

- **Pole/Zero at Origin**:
  - If $H(s) = s$: 
    - Amplitude: Infinite straight line passing through 0 dB at $\omega = 1$ with slope **20 dB/decade**.
    - Phase: Constant at **$+90^\circ$**.
  - If $H(s) = 1/s$: 
    - Amplitude: Straight line passing through 0 dB at $\omega = 1$ with slope **-20 dB/decade**.
    - Phase: Constant at **$-90^\circ$**.

:: right ::

<div class="flex flex-col gap-4 mt-8">
  <img src="/origin_magnitude.svg" class="h-55 bg-white p-1 rounded mx-auto" />
  <img src="/origin_phase.svg" class="h-55 bg-white p-1 rounded mx-auto" />
</div>

---

## Example 16.8

**Problem**: Obtain the Bode plot for the gain of the circuit shown in Fig. 16.26 ($V_{in}$ to $V_{out}$).

<img src="/practice_circuit.svg" class="mx-auto w-full">

---

**Solution**:

- **Stage 1 (Voltage Divider)**:
  $$ V_x = V_{in} \frac{R_2}{R_1 + R_2 + \frac{1}{sC_1}} = V_{in} \frac{sC_1 R_2}{1 + sC_1(R_1 + R_2)} $$
  With values: $V_x = V_{in} \frac{0.08s}{1 + s/10}$.
- **Stage 2 (Output Stage)**:
  $$ I_{src} = \frac{V_x}{200}, \quad Z_p = R_3 \parallel \frac{1}{sC_2} = \frac{R_3}{1 + sC_2 R_3} $$
  $$ V_{out} = -I_{src} Z_p = -\frac{V_x}{200} \frac{R_3}{1 + s/20000} = -25 V_x \frac{1}{1 + s/20000} $$
- **Total Transfer Function**:
  $$ H(s) = \frac{V_{out}}{V_{in}} = (-25)\frac{0.08s}{(1+s/10)(1+s/20000)} = \frac{-2s}{(1 + s/10)(1 + s/20,000)} $$

---
layout: two-cols
---

**Solution (Bode Analysis)**:
- **Transfer Function**: 

$$H(s) = \frac{-2s}{(1 + s/10)(1 + s/20,000)}$$

- **Factors**:
  1.  **Constant**: $6 \text{ dB}$.
  2.  **Zero**: $s$ ($+20$ dB/dec).
  3.  **Pole 1**: $10$ rad/s ($-20$ dB/dec).
  4.  **Pole 2**: $20$ krad/s ($-20$ dB/dec).

:: right ::

<div class="flex justify-center items-center h-full">
  <img src="/example_16_8_asymptotes.svg" class="w-full bg-white p-2 rounded" />
</div>

---

- **Combined Plot**:
  - Starts rising at 20 dB/dec.
  - At $\omega=10$, slope becomes $20 - 20 = 0$ dB/dec (Flat).
  - Gain at $\omega=10$: calculated approx peak.
  - At $\omega=20,000$, slope becomes $0 - 20 = -20$ dB/dec.

<img src="/example_16_8_bode.svg" class="w-120 rounded bg-white p-1 mx-auto" />
<div class="text-xs text-center opacity-70">Fig 16.27: Bode Amplitude Plot</div>

---

## Practice 16.13

Construct a Bode magnitude plot for $H(s)$ equal to:
- (a) $50/(s + 100)$
- (b) $(s + 10) / (s + 100)$
- \(c) $(s + 10) / s$

**Answers**:
- (a) $-6 \text{ dB}$, $\omega < 100$; $-20 \text{ dB/decade}$, $\omega > 100$.
- (b) $-20 \text{ dB}$, $\omega < 10$; $+20 \text{ dB/decade}$, $10 < \omega < 100$; $0 \text{ dB}$, $\omega > 100$.
- \(c) $0 \text{ dB}$, $\omega > 10$; $-20 \text{ dB/decade}$, $\omega < 10$.

---

### Practice 16.13 (a) Solution
**$H(s) = 50/(s + 100)$**

<div class="flex justify-center">
  <img src="/practice_16_13_a.svg" class="h-100 bg-white p-2 rounded" />
</div>

---

### Practice 16.13 (b) Solution
**$H(s) = (s + 10) / (s + 100)$**

<div class="flex justify-center">
  <img src="/practice_16_13_b.svg" class="h-100 bg-white p-2 rounded" />
</div>

---

### Practice 16.13 (c) Solution
**$H(s) = (s + 10) / s$**

<div class="flex justify-center">
  <img src="/practice_16_13_c.svg" class="h-100 bg-white p-2 rounded" />
</div>

---

## Example 16.9

**Problem**: Draw the phase plot for the transfer function 

$$H(s) = \frac{-2s}{(1 + s/10)(1 + s/20,000)}$$

---
layout: two-cols
---

**Solution**:

$$ H(j\omega) = \frac{-j2\omega}{(1 + j\omega/10)(1 + j\omega/20000)} $$

- **Phase Components**:
  1.  **Numerator**: $-2s \implies -2(j\omega) = -j(2\omega) \implies -90^\circ$.
  2.  **Pole at 10**: Starts $0^\circ$, goes to $-90^\circ$. Center $-45^\circ$ at $\omega=10$.
  3.  **Pole at 20,000**: Starts $0^\circ$, goes to $-90^\circ$. Center $-45^\circ$ at $\omega=20k$.
- **Total Phase**:
  - $\omega \ll 10$: $-90^\circ$.
  - $\omega = 10$: $-90 - 45 = -135^\circ$.
  - $100 < \omega < 2000$: Constant at $-180^\circ$.

:: right ::

<div class="flex flex-col gap-2 h-full justify-center">
  <img src="/example_16_9_asymptotes.svg" class="w-full rounded bg-white p-5 mx-auto" />
  <div class="text-[10px] text-center opacity-70 mb-2">Phase Asymptotes</div>
</div>

---

## Practice 16.14

Draw the Bode phase plot for $H(s)$ equal to:
(a) $50/(s+100)$
(b) $(s+10) / (s+100)$
\(c) $(s+10) / s$

**Answers**:
- (a) $0^\circ$, $\omega < 10$; $-45^\circ$/decade, $10 < \omega < 1000$; $-90^\circ$, $\omega > 1000$.
- (b) $0^\circ$, $\omega < 1$; $+45^\circ$/decade, $1 < \omega < 10$; $45^\circ$, $10 < \omega < 100$; $-45^\circ$/decade, $100 < \omega < 1000$; $0^\circ$, $\omega > 1000$.
- \(c) $-90^\circ$, $\omega < 1$; $+45^\circ$/decade, $1 < \omega < 100$; $0^\circ$, $\omega > 100$.

---

### Practice 16.14 (a) Solution
**$H(s) = 50/(s+100)$**

<div class="flex justify-center">
  <img src="/practice_16_14_a.svg" class="h-100 bg-white p-2 rounded" />
</div>

---

### Practice 16.14 (b) Solution
**$H(s) = (s+10)/(s+100)$**

<div class="flex justify-center">
  <img src="/practice_16_14_b.svg" class="h-100 bg-white p-2 rounded" />
</div>

---

### Practice 16.14 \(c) Solution
**$H(s) = (s+10)/s$**

<div class="flex justify-center">
  <img src="/practice_16_14_c.svg" class="h-100 bg-white p-2 rounded" />
</div>
