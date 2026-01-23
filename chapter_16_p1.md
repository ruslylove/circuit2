---
theme: seriph
background: https://cover.sli.dev
title: Chapter 16 Part I - Resonance
info: |
  ## Chapter 16 Part I: Resonance
  Frequency Response
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
layout: cover
---

# Chapter 16: Frequency Response

## Part I: Resonance

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

- Parallel Resonance
- Bandwidth and High-Q circuits
- Series Resonance
- Other Resonant Forms

---

## 16.1 Parallel Resonance

## Resonance

- In a two-terminal electrical network containing at least one inductor and one capacitor, we define **resonance** as the condition which exists when the input impedance of the network is **purely resistive**.
- A network is in **resonance** (or resonant) when the voltage and current at the network input terminals are in phase.



<div class="grid grid-cols-2 gap-4 items-center">
  <div class="flex justify-center">
    <img src="/parallel_resonant_circuit.svg" class="h-60" />
  </div>
  <div class="text-center">

  $Y = \frac{1}{R} + j\left( \omega C - \frac{1}{\omega L} \right) \qquad [1]$

  </div>
</div>

---

## Resonant Frequency

<div class="text-base">

- Resonance occurs when the input impedance is purely resistive (unity power factor). 
- This implies the imaginary part of the admittance $Y$ must be zero:

$$ \text{Im}(Y) = \omega C - \frac{1}{\omega L} = 0 $$
$$ \omega C = \frac{1}{\omega L} $$
$$ \omega^2 = \frac{1}{LC} $$
Hence, the resonant frequency is given by:
$$ \omega_0 = \frac{1}{\sqrt{LC}} \space\text{rad/s} \qquad [2]$$
or
$$ f_0 = \frac{1}{2\pi\sqrt{LC}} \space\text{Hz} \qquad [3]$$

</div>

---

## Pole-Zero Configuration

The pole-zero configuration of the admittance function can also be used to considerable advantage here. Given $Y(s)$,

$$ Y(s) = \frac{1}{R} + \frac{1}{sL} + sC $$

or

$$ Y(s) = C \frac{s^2 + s/RC + 1/LC}{s} \qquad [4] $$

We may display the zeros of $Y(s)$ by factoring the numerator:

$$ Y(s) = C \frac{(s + \alpha - j\omega_d)(s + \alpha + j\omega_d)}{s} $$

---

where $\alpha$ is the exponential damping coefficient and $\omega_d$ is the natural resonant frequency.

$$ \alpha = \frac{1}{2RC}, \qquad \omega_d = \sqrt{\omega_0^2 - \alpha^2} $$

<div class="flex justify-center my-4">
  <img src="/fig_16_2_pole_zero.svg" class="h-80" />
</div>

<div class="text-center text-sm">

  (a) Pole-zero constellation of admittance $Y(s)$. (b) Pole-zero constellation of impedance $Z(s)$.
</div>


---

<div class="flex justify-center my-4">
  <img src="/s_plane_surface.png" class="w-160" />
</div>

<div class="text-center text-sm">

  Magnitude of input impedance $|Z(s)|$ on s-plane. Inset: Frequency response $|Z(j\omega)|$ (cross-section along $j\omega$ axis).<br>
  Example: $Z(s) = \frac{s}{s^2 + 6s + 25}$ with $\alpha=3, \omega_d=4, \omega_0=5$.
</div>


---

## Resonance and the Voltage Response

<div class="">

- The response maximum occurs exactly at the resonant frequency $\omega_0$.
- The **admittance** possesses a constant conductance and a susceptance which has a minimum magnitude (zero) at resonance.
- The **minimum admittance magnitude** occurs at resonance, and is $1/R$.
- Hence, the **maximum impedance magnitude** is $R$, and it occurs at resonance.


<div class="grid grid-cols-2 gap-4 items-center">
  <div class="flex justify-center">

  $$ Y(j\omega) = \frac{1}{R} + j\left(\omega C - \frac{1}{\omega L}\right), Z(j\omega) = \frac{1}{Y(j\omega)} $$

    
  </div>
  <div class="flex justify-center">
    <img src="/z_y_plot.png" class="h-60" />
  </div>

</div>

</div>
---

## Resonance and the Voltage Response (cont.)

<div class="grid grid-cols-[3fr_2fr] gap-4">
<div>

- Let us examine the magnitude of the response, the voltage $V(s)$, as the frequency $\omega$ is varied.
- If we assume a **constant-amplitude sinusoidal current source**, the voltage response is proportional to the **input impedance**.
- At the resonant frequency, the voltage across the parallel resonant circuit is simply $IR$.

<div class="justify-center items-center">
  <img src="/parallel_resonant_circuit_1A.svg" class="h-55 mx-auto" />
</div>
</div>

<div>

Derivation at $\omega = \omega_0$:

$$ Y(j\omega_0) = \frac{1}{R} + j\left(\omega_0 C - \frac{1}{\omega_0 L}\right) = \frac{1}{R} $$

Since $\omega_0 C = 1/(\omega_0 L)$, the imaginary part is zero. Thus,

$$ V(j\omega_0) = \frac{I}{Y(j\omega_0)} = IR $$

</div>
</div>

---

<div class="flex justify-center my-4">
  <img src="/voltage_response.png" class="w-150" />
</div>

<div class="text-center text-sm">
  Magnitude of the voltage response as a function of frequency.
</div>



---

- The entire source current $I$ flows through the resistor.
- The current is also present in $L$ and $C$, but they sum to zero phase-wise (cancel each other).

<div class="justify-center items-center">
  <img src="/parallel_resonance_currents.svg" class="h-50 mx-auto p-2" />
</div>

The current in the inductor and capacitor at resonance can be found by:

$$ I_{L,0} = \frac{V}{j\omega_0 L} = \frac{IR}{j\omega_0 L} = -j \frac{R}{\omega_0 L} I = -j Q_0 I $$

$$ I_{C,0} = \frac{V}{1/j\omega_0 C} = j\omega_0 C V = j\omega_0 C R I = j Q_0 I $$

Thus, the currents in the inductor and capacitor are $Q_0$ times the source current magnitude and are $180^\circ$ out of phase.




---

## Quality Factor ($Q$)

- The height of the response curve depends only on $R$.
- The **width** of the curve or the steepness of the sides depends on the other two element values ($L$ and $C$).
- **Definition**: The response curve of any resonant circuit is determined by the maximum amount of energy that can be **stored** in the circuit, compared with the energy that is **lost** during one complete period of the response.

  $$ Q_0 = 2\pi \frac{\text{Maximum Energy Stored}}{\text{Total Energy Lost per Period}} $$

  For the parallel RLC circuit:
  $$ Q_0 = \omega_0 R C = \frac{R}{\omega_0 L} $$

  

---

  **Derivation**:
  1. Max Energy Stored ($W_{max}$):
     $$ W(t) = \int_0^t p(x) dx = \int_0^t v i dx = \int_0^v C v dv = \frac{1}{2} C v^2 $$
     $$ W_{max} = \frac{1}{2} C V_{max}^2 $$
     *(Alternatively, using Inductor: $W_{max} = \frac{1}{2} L I_{L,max}^2 = \frac{1}{2} L (\frac{V_{max}}{\omega_0 L})^2 = \frac{V_{max}^2}{2\omega_0^2 L}$)*
  2. Energy Lost per Period ($W_{lost}$):
     $$ W_{lost} = P_R \cdot T = \frac{V_{max}^2}{2R} \cdot \frac{2\pi}{\omega_0} = \frac{\pi V_{max}^2}{\omega_0 R} $$

---

  3. Calculate $Q_0$:
     $$ Q_0 = 2\pi \frac{\frac{1}{2} C V_{max}^2}{\frac{\pi V_{max}^2}{\omega_0 R}} = 2\pi \frac{C V_{max}^2}{2} \cdot \frac{\omega_0 R}{\pi V_{max}^2} = \omega_0 R C $$
     $$ \text{Or using } L: Q_0 = 2\pi \frac{W_{max,L}}{W_{lost}} = 2\pi \frac{V_{max}^2 / (2\omega_0^2 L)}{\pi V_{max}^2 / (\omega_0 R)} = \frac{R}{\omega_0 L} $$
     Substitute $\omega_0 = 1/\sqrt{LC}$:
     $$ Q_0 = R \sqrt{\frac{C}{L}} $$


---

## Interpretations of Q

- **Current Amplification**:
  - At resonance, the inductor and capacitor currents are each $Q_0$ times the source current magnitude.
  - They are $180^\circ$ out of phase with each other.
  - Example: If source is 2 mA and $Q_0 = 50$, then resistor current is 2 mA, but inductor/capacitor currents are 100 mA!
  - A parallel resonant circuit acts as a **current amplifier** (passive, so not a power amplifier).

---

## Important Parameters

- **Resonant Frequency ($\omega_0$)**
- **Quality Factor ($Q_0$)**

Both exponential damping coefficient ($\alpha$) and natural resonant frequency ($\omega_d$) can be expressed in terms of $\omega_0$ and $Q_0$.

$$ \alpha = \frac{\omega_0}{2Q_0} $$

$$ \omega_d = \omega_0 \sqrt{1 - \left(\frac{1}{2Q_0}\right)^2} $$

---

## Effect of Quality Factor $Q$ on Response Shape

<div class="grid grid-cols-2 gap-4 items-center">
  <div class="flex justify-center">
    <img src="/plot_q_normalized.png" class="h-80" />
  </div>
  <div class="text-sm">

  - **High Q**: Sharp peak, high selectivity. The circuit strongly prefers the resonant frequency.
  - **Low Q**: Broad peak, low selectivity. The circuit accepts a wider range of frequencies.
  - The bandwidth is inversely proportional to $Q$:
    $$ B = \frac{\omega_0}{Q_0} $$
  </div>
</div>

---

## Effect of Varying $R$

<div class="grid grid-cols-[1.2fr_1fr] gap-4 items-center">
  <div class="flex flex-col gap-2">
      <div class="flex justify-center">
        <img src="/plot_vary_r.png" class="h-55" />
      </div>
      <div class="flex justify-center">
        <img src="/s_plane_vary_r.png" class="h-55" />
      </div>
  </div>
  <div class="text-base">

  - **Parallel RLC Circuit**: $Q_0 = \omega_0 R C$.
  - Increasing $R$ increases $Q_0$ (decreasing damping $\alpha = \frac{1}{2RC}$).
  - **Peak Amplitude**: At resonance, $Z = R$, so $V_{max} = I \times R$.
  - Increasing $R$ increases **both** the $Q$ (selectivity) and the peak voltage response.
  - **S-Plane**: As $R$ increases, poles move closer to the $j\omega$ axis (smaller $\alpha$, higher $Q$), correlating with the sharper resonant peak.
  </div>
</div>

---

## Effect of Varying $L/C$ Ratio

<div class="grid grid-cols-[1.2fr_1fr] gap-4 items-center">
  <div class="flex flex-col gap-2">
      <div class="flex justify-center">
        <img src="/plot_vary_lc.png" class="h-55" />
      </div>
      <div class="flex justify-center">
        <img src="/s_plane_vary_lc.png" class="h-55" />
      </div>
  </div>
  <div class="text-base">

  - Fixed $\omega_0$ (constant $LC$ product) and Fixed $R$.
  - Varying the ratio $L/C$.
  - Since $Q_0 = R\sqrt{C/L}$, increasing $L$ (and decreasing $C$ to keep $\omega_0$ constant) results in a **smaller** $\sqrt{C/L}$ and thus lower $Q$.
  - **Peak Amplitude** remains constant ($V = IR$) because $R$ is fixed!
  - **S-Plane**: Poles move along the circle of radius $\omega_0$. Lower $Q$ (High $L/C$) moves poles further from $j\omega$ axis (higher damping).
  - This allows tuning bandwidth without changing gain.
  </div>
</div>

---

## Damping Factor ($\zeta$)
- In system/control theory, we use the damping factor $\zeta$ (zeta).
- The quadratic factor can be written utilizing $\zeta$ and $\omega_0$.

$$ \zeta = \frac{\alpha}{\omega_0} = \frac{1}{2Q_0} $$
$$ s^2 + 2\zeta\omega_0 s + \omega_0^2 $$

<div class="grid grid-cols-2 gap-4 items-center">
    <div class="flex justify-center">
      <img src="/plot_impulse_response.png" class="h-60" />
    </div>
  <div class="text-sm">

  - **Low $\zeta$ (High Q)**:
    - Time Domain: Oscillatory "ringing" response.
  - **High $\zeta$ (Low Q)**:
    - Time Domain: Fast decay, no ringing (overdamped).
  - **Critical Damping ($\zeta=1$)**:
    - Fastest decay without oscillation.
  </div>
</div>


---

## Example 16.1

Consider a parallel RLC circuit such that $L = 2 \text{ mH}$, $Q_0 = 5$, and $C = 10 \text{ nF}$.
Determine the value of $R$ and the magnitude of the steady-state admittance at $0.9\omega_0$, $\omega_0$, and $1.1\omega_0$.

**Solution**:
1.  Calculate $R$:
    $$ R = Q_0 \sqrt{\frac{L}{C}} = 5 \sqrt{\frac{2 \times 10^{-3}}{10 \times 10^{-9}}} = 2.236 \text{ k}\Omega $$
2.  Calculate $\omega_0$:
    $$ \omega_0 = \frac{1}{\sqrt{LC}} = 223.6 \text{ krad/s} $$

---

3.  Calculate Admittance $|Y|$:
    $$ |Y| = \left| \frac{1}{R} + j\omega C + \frac{1}{j\omega L} \right| = \sqrt{\frac{1}{R^2} + \left(\omega C - \frac{1}{\omega L}\right)^2} $$
    
    <div class="grid grid-cols-2 gap-4 items-center">
    <div>

    - At $\omega_0$, $|Y| = 1/R = 4.472 \times 10^{-4} \text{ S}$
    - At $0.9\omega_0$: $|Y| = 6.504 \times 10^{-4} \text{ S}$
    - At $1.1\omega_0$: $|Y| = 6.182 \times 10^{-4} \text{ S}$
    </div>
    <div>
      <img src="/example_16_1_admittance.png" class="h-70 rounded" />
    </div>
    </div>



---

## Practice 16.1

A parallel resonant circuit is composed of:
- $R = 8 \text{ k}\Omega$
- $L = 50 \text{ mH}$
- $C = 80 \text{ nF}$

Find:
(a) $\omega_0$
(b) $Q_0$
\(c\) $\omega_d$
(d) $\alpha$
(e) $\zeta$

<div class="grid grid-cols-2 gap-4 items-center">
<div>

**Answers**:
- 15.811 krad/s
- 10.12
- 15.792 krad/s
- 781 Np/s
- 0.0494
</div>

<div v-click>

**Solution**:
1. $\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{50\text{mH} \cdot 80\text{nF}}} = 15.811 \text{ krad/s}$
2. $Q_0 = \omega_0 R C = 15811 \cdot 8000 \cdot 80\text{n} = 10.12$
3. $\alpha = \frac{\omega_0}{2Q_0} = \frac{15811}{20.24} = 781 \text{ Np/s}$
4. $\omega_d = \sqrt{\omega_0^2 - \alpha^2} = 15.792 \text{ krad/s}$
5. $\zeta = \frac{1}{2Q_0} = 0.0494$

</div>

</div>



---

## Practice 16.2

Find $R$, $L$, and $C$ in a parallel resonant circuit for which:
- $\omega_0 = 1000 \text{ rad/s}$
- $\omega_d = 998 \text{ rad/s}$
- $Y_{in} = 1 \text{ mS}$ at resonance.

<div class="grid grid-cols-2 gap-4 items-center">
<div>

**Answers**:
- $R = 1000 \Omega$
- $L = 126.4 \text{ mH}$
- $C = 7.91 \mu\text{F}$
</div>

<div v-click>

**Solution**:
1. At resonance, $Y = 1/R \Rightarrow R = 1/Y = 1 \text{ k}\Omega$.
2. $\alpha = \sqrt{\omega_0^2 - \omega_d^2} = \sqrt{1000^2 - 998^2} \approx 63.2 \text{ Np/s}$.
3. $C = \frac{1}{2R\alpha} = \frac{1}{2(1000)(63.2)} = 7.91 \mu\text{F}$.
4. $L = \frac{1}{\omega_0^2 C} = \frac{1}{10^6(7.91\mu)} = 126.4 \text{ mH}$.

</div>
</div>

---

## 16.2 Bandwidth and High-Q Circuits

<div class="grid grid-cols-2 gap-4 items-center">
  <div>

  - **Half-Power Frequencies ($\omega_1, \omega_2$)**:
    - The frequencies at which the magnitude of the input admittance is $\sqrt{2}$ times the magnitude at resonance ($1/R$).
    - Or, voltage response is $1/\sqrt{2}$ (0.707) of max value.
    - $\omega_1$: Lower half-power frequency.
    - $\omega_2$: Upper half-power frequency.

  ## Bandwidth ($B$)
  - The (half-power) bandwidth is defined as:
    $$ B = \omega_2 - \omega_1 $$
  </div>
  <div class="flex justify-center">
    <img src="/half_power_highlighted.png" class="w-full rounded" />
  </div>
</div>

---

## Exact Half-Power Frequencies

We can express the half-power frequencies $\omega_1$ and $\omega_2$ in terms of $\omega_0$ and $Q_0$:

$$ \omega_{1,2} = \omega_0 \left[ \sqrt{1 + \left(\frac{1}{2Q_0}\right)^2} \mp \frac{1}{2Q_0} \right] $$

- **Geometric Symmetry**:
  The resonant frequency is the geometric mean of the half-power frequencies:
  $$ \omega_0 = \sqrt{\omega_1 \omega_2} $$
- **Bandwidth**:
  $$ B = \omega_2 - \omega_1 = \frac{\omega_0}{Q_0} $$

---

## Proof of Geometric Symmetry

Multiply the expressions for $\omega_1$ and $\omega_2$:

$$ \omega_1 \omega_2 = \omega_0 \left[ \sqrt{1 + \left(\frac{1}{2Q_0}\right)^2} - \frac{1}{2Q_0} \right] \cdot \omega_0 \left[ \sqrt{1 + \left(\frac{1}{2Q_0}\right)^2} + \frac{1}{2Q_0} \right] $$

Using $(a-b)(a+b) = a^2 - b^2$:

$$ \omega_1 \omega_2 = \omega_0^2 \left[ \left( \sqrt{1 + \frac{1}{4Q_0^2}} \right)^2 - \left( \frac{1}{2Q_0} \right)^2 \right] $$

$$ \omega_1 \omega_2 = \omega_0^2 \left[ \left( 1 + \frac{1}{4Q_0^2} \right) - \frac{1}{4Q_0^2} \right] = \omega_0^2 (1) $$

$$ \therefore \omega_0 = \sqrt{\omega_1 \omega_2} $$

---

## Approximations for High-Q Circuits

- Many circuits are designed with high $Q_0$ for selectivity (narrow bandwidth).
- If $Q_0 \ge 5$, we can use useful approximations.
- In a high-Q circuit, each half-power frequency is located approximately **one-half bandwidth** from the resonant frequency.
  $$ \omega_1 \approx \omega_0 - \frac{B}{2} $$
  $$ \omega_2 \approx \omega_0 + \frac{B}{2} $$
  $$ \omega_0 \approx \frac{\omega_1 + \omega_2}{2} $$
- Error is less than 5% if $Q_0 \ge 5$.

---

<div class="flex justify-center">
  <img src="/high_q_approx.png" class="h-100 rounded" />
</div>

<div class="text-center text-sm mt-2">
  Comparison of Exact vs Approximate Half-Power Frequencies for Low-Q and High-Q circuits.
</div>

---

## High-Q Admittance Approximation

<div class="text-base">

Starting with the exact admittance:
$$ Y = \frac{1}{R} + j\left(\omega C - \frac{1}{\omega L}\right) = \frac{1}{R} \left[ 1 + jR\left(\omega C - \frac{1}{\omega L}\right) \right] $$

Using $Q_0 = \omega_0 RC = \frac{R}{\omega_0 L}$, we can rewrite the imaginary part:
$$ R\left(\omega C - \frac{1}{\omega L}\right) = Q_0 \left( \frac{\omega}{\omega_0} - \frac{\omega_0}{\omega} \right) $$

For $\omega$ near $\omega_0$ (within $\pm 10\%$), let $\omega = \omega_0 + \Delta\omega$. Then $\frac{\omega}{\omega_0} = 1 + \frac{\Delta\omega}{\omega_0}$.
$$ \frac{\omega}{\omega_0} - \frac{\omega_0}{\omega} \approx \left(1 + \frac{\Delta\omega}{\omega_0}\right) - \left(1 - \frac{\Delta\omega}{\omega_0}\right) = \frac{2\Delta\omega}{\omega_0} = \frac{2(\omega - \omega_0)}{\omega_0} $$

Thus, substituting back:
$$ Y \approx \frac{1}{R} \left[ 1 + j Q_0 \left( \frac{2(\omega - \omega_0)}{\omega_0} \right) \right] = \frac{1}{R}(1 + jN) $$
where $N = 2Q_0\frac{\omega - \omega_0}{\omega_0}$.

</div>

---

<div class="flex justify-center mt-4">
  <img src="/admittance_approx.png" class="w-150 rounded" />
</div>

<div class="grid grid-cols-2 gap-4 mt-2 text-center text-sm">
  <div>
    <strong>Exact:</strong><br>
    
  $Y = \frac{1}{R} + j\left(\omega C - \frac{1}{\omega L}\right)$
  
  </div>
  <div>
    <strong>Approximate:</strong><br>
    
  $Y \approx \frac{1}{R}(1 + jN), N=2Q_0\frac{\omega - \omega_0}{\omega_0} \\$
  <span class="text-red-500 font-bold">$Q_0 \ge 5$ and $0.9\omega_0 \le \omega \le 1.1\omega_0$</span>
  </div>
</div>

---

## Conclusions: Parallel Resonance

For the parallel RLC circuit:
- $Q_0 = \omega_0 R C, \quad B = \frac{\omega_0}{Q_0}$

<div class="grid grid-cols-2 gap-4 mt-4">
<div>

### General Case (Low Q)
- Exact Frequencies:
  $$ \omega_{1,2} = \omega_0 \left[ \sqrt{1 + \left(\frac{1}{2Q_0}\right)^2} \mp \frac{1}{2Q_0} \right] $$
- Admittance:
  $$ Y = \frac{1}{R} + j\left(\omega C - \frac{1}{\omega L}\right) $$
</div>
<div>

### High-Q ($Q_0 \ge 5$)
- Approximate Frequencies:
  $$ \omega_{1,2} \approx \omega_0 \mp \frac{B}{2} $$
- Admittance:
  $$ Y \approx \frac{1}{R}(1 + jN) \approx \frac{\sqrt{1+N^2}}{R} \angle \tan^{-1}(N) $$
  $$ N \approx \frac{2Q_0(\omega - \omega_0)}{\omega_0} $$
  *(Valid for $0.9\omega_0 \le \omega \le 1.1\omega_0$)*
</div>
</div>



---

## Example 16.2

Determine the approximate value of the admittance of a parallel RLC network for which:
- $R = 40 \text{ k}\Omega$
- $L = 1 \text{ H}$
- $C = 1/64 \mu\text{F}$
- Operatiing frequency $\omega = 8.2 \text{ krad/s}$

---

**Solution**:
1.  **Calculate Parameters**:
    - $\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{1 \cdot (1/64) \times 10^{-6}}} = \frac{1}{\sqrt{1.5625 \times 10^{-8}}} = 8000 \text{ rad/s}$
    - $Q_0 = \omega_0 R C = 8000 \cdot 40000 \cdot (1.5625 \times 10^{-8}) = 5$
2.  **Analyze Q**:
    - Since $Q_0 = 5$, this is a high-Q circuit ($Q_0 \ge 5$).
3.  **Calculate Admittance**:
    - $\omega = 8.2 \text{ krad/s}$. $G = 1/R = 25 \mu S$.

<div class="grid grid-cols-2 gap-4 mt-2 text-base">
<div>

**Approximate Method**:
- $N = 2Q_0\frac{\omega - \omega_0}{\omega_0} = 10(0.025) = 0.25$
- $Y \approx G(1 + jN) = 25(1 + j0.25) \mu S$
- $Y \approx 25 + j6.25 \mu S$
- $Y \approx 25.77 \angle 14.04^\circ \mu S$
</div>
<div>

**Exact Method**:
- $Y = 1/R + j(\omega C - \frac{1}{\omega L})$
- $\omega C = 8200(15.625 \text{ nF}) = 128.125 \mu S$
- $\frac{1}{\omega L} = \frac{1}{8200 \text{ H}} \approx 121.95 \mu S$
- $\text{Im}(Y) = 128.125 - 121.95 = 6.175 \mu S$
- $Y = 25 + j6.175 \mu S = 25.75 \angle 13.87^\circ \mu S$
</div>
</div>



---

## Practice 16.3

A marginally high-Q parallel resonant circuit has $f_0 = 440 \text{ Hz}$ with $Q_0 = 6$. Obtain accurate values for:
(a) $f_1$
(b) $f_2$
And approximate values for:
\(c) $f_1$
(d) $f_2$

**Answers**:
- Accurate: $404.9 \text{ Hz}, 478.2 \text{ Hz}$
- Approximate: $403.3 \text{ Hz}, 476.7 \text{ Hz}$



---

**Solution**:

**Bandwidth**: $B = \frac{f_0}{Q_0} = \frac{440}{6} = 73.33 \text{ Hz}$.

**(a) & (b) Accurate Values**:
Using exact formulas: $f_{1,2} = f_0 \left[ \sqrt{1 + \left(\frac{1}{2Q_0}\right)^2} \mp \frac{1}{2Q_0} \right]$.
- Term $\frac{1}{2Q_0} = \frac{1}{12} \approx 0.0833$.
- Term $\sqrt{1 + (0.0833)^2} \approx 1.0035$.
- $f_1 = 440 [1.0035 - 0.0833] = 404.9 \text{ Hz}$.
- $f_2 = 440 [1.0035 + 0.0833] = 478.2 \text{ Hz}$.

**\(c) & (d) Approximate Values**:
- $f_1 \approx f_0 - \frac{B}{2} = 440 - 36.67 = 403.3 \text{ Hz}$.
- $f_2 \approx f_0 + \frac{B}{2} = 440 + 36.67 = 476.7 \text{ Hz}$.



---
layout: two-cols
---

## 16.3 Series Resonance
<img src="/series_rlc.svg" class="h-50 rounded bg-white p-2 mb-4" />
<div class="text-center">

$Z = R + j\left( \omega L - \frac{1}{\omega C} \right)$
</div>

:: right ::
- Resonance exists when the input impedance is purely resistive ($\text{Im}(Z) = 0$).
- This implies:
  $$ \omega L - \frac{1}{\omega C} = 0 \implies \omega^2 = \frac{1}{LC} $$
- **Resonant Frequency**:
  $$ \omega_0 = \frac{1}{\sqrt{LC}} \space\text{rad/s} $$
- **Quality Factor**: 
  $$ Q_0 = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 CR} $$
- **At Resonance**: $|Z|_{min} = R$. 
- **Half-Power Points**: $|Z| = \sqrt{2}R$.

---

## Series Resonance Parameters

Similarly to the parallel case, the input impedance $Z(s)$ describes the circuit response.

<div class="grid grid-cols-2 gap-4">
<div>

- **Input Impedance**:
  $$ Z(s) = R + sL + \frac{1}{sC} = L \frac{s^2 + \frac{R}{L}s + \frac{1}{LC}}{s} $$
- **Pole-Zero Configuration**:
  $$ Z(s) = L \frac{(s + \alpha - j\omega_d)(s + \alpha + j\omega_d)}{s} $$
- **Key Definitions**:
  - $\omega_0 = \frac{1}{\sqrt{LC}}$ (Resonant frequency)
  - $\alpha = \frac{R}{2L}$ (Damping coefficient)
  - $\omega_d = \sqrt{\omega_0^2 - \alpha^2}$ (Natural frequency)

</div>
<div>

- **Quality Factor**:
  $$ Q_0 = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 CR} $$
- **Bandwidth**:
  $$ B = \frac{\omega_0}{Q_0} = \frac{R}{L} = 2\alpha $$
- **High-Q Relations**: 
  - $\omega_0 \approx \frac{\omega_1 + \omega_2}{2}$
  - $B \approx \omega_2 - \omega_1$
  - Symmetry holds for $Q_0 \ge 5$.

</div>
</div>

---


## Series Resonance Conclusions

For the series RLC circuit:
- $Q_0 = \frac{\omega_0 L}{R}, \quad B = \frac{\omega_0}{Q_0} = \frac{R}{L}$

<div class="grid grid-cols-2 gap-4 mt-4">
<div>

### General Case (Low Q)
- Exact Frequencies:
  $$ \omega_{1,2} = \omega_0 \left[ \sqrt{1 + \left(\frac{1}{2Q_0}\right)^2} \mp \frac{1}{2Q_0} \right] $$
- Impedance:
  $$ Z = R + j\left(\omega L - \frac{1}{\omega C}\right) $$
</div>
<div>

### High-Q ($Q_0 \ge 5$)
- Approximate Frequencies:
  $$ \omega_{1,2} \approx \omega_0 \mp \frac{B}{2} $$
- Impedance:
  $$ Z \approx R(1 + jN) \approx \sqrt{1+N^2}R \angle \tan^{-1}(N) $$
  $$ N = \frac{2Q_0(\omega - \omega_0)}{\omega_0} $$
  *(Valid for $0.9\omega_0 \le \omega \le 1.1\omega_0$)*
</div>
</div>


---

## Example 16.3

The voltage $v_s = 100 \cos \omega t$ mV is applied to a series resonant circuit composed of a $10 \Omega$ resistance, a $200$ nF capacitance, and a $2$ mH inductance. 

Calculate the current amplitude if $\omega = 48$ krad/s using both **exact** and **approximate** methods.

---

## Example 16.3 Solution

$\omega_0 = 1/\sqrt{LC} = 50$ krad/s, $Q_0 = \omega_0 L / R = 10$ (**High-Q**), $B = \omega_0 / Q_0 = 5$ krad/s.

<div class="grid grid-cols-2 gap-4 text-base">
<div>

### Approximate Method
- Dev. from resonance:
  $$ N = \frac{\omega - \omega_0}{B/2} = \frac{48 - 50}{2.5} = -0.8 $$
- Impedance:
  $$ Z \approx R(1 + jN) = 10(1 - j0.8) \Omega $$
  $$ Z \approx \mathbf{12.81 \angle -38.66^\circ \Omega} $$
- Current Amplitude:
  $$ |I| \approx \frac{100 \text{ mV}}{12.81 \Omega} = \mathbf{7.806 \text{ mA}} $$

</div>
<div>

### Exact Method
- Component Reactances:
  $$ X_L = \omega L = 96 \Omega $$
  $$ X_C = 1/(\omega C) = 104.17 \Omega $$
- Impedance:
  $$ Z = 10 + j(96 - 104.17) \Omega $$
  $$ Z = 10 - j8.17 \Omega = \mathbf{12.91 \angle -39.24^\circ \Omega} $$
- Current Amplitude:
  $$ |I| = \frac{100 \text{ mV}}{12.91 \Omega} = \mathbf{7.746 \text{ mA}} $$

</div>
</div>

<div class="mt-4 text-center text-sm font-bold text-green-600">
  Error is less than 1% for this high-Q circuit at 4% frequency deviation.
</div>

---

## Practice 16.4


A series resonant circuit has a bandwidth of 100 Hz, $L = 20 \text{ mH}$, $C = 2 \mu\text{F}$. Determine:
(a) $f_0$
(b) $Q_0$
\(c) $Z_{in}$ at resonance
(d) $f_2$

<v-click>

**Answers**: (a) 796 Hz; (b) 7.96; \(c) $12.57 \Omega$; (d) 846 Hz.

</v-click>

---

## Practice 16.4 Solution

$B = 100 \text{ Hz}, \quad L = 20 \text{ mH}, \quad C = 2 \mu\text{F}$

<div class="text-base">

- **(a) Resonant Frequency**:
  <v-click>

  $$ f_0 = \frac{1}{2\pi \sqrt{LC}} = \frac{1}{2\pi \sqrt{(20 \times 10^{-3})(2 \times 10^{-6})}} \approx \mathbf{795.78 \text{ Hz}} $$
  </v-click>

- **(b) Quality Factor**:
  <v-click>
  
  $$ Q_0 = \frac{f_0}{B} = \frac{795.78}{100} \approx \mathbf{7.96} $$
  </v-click>

- **\(c) Input Impedance at Resonance ($Z_{in} = R$)**:
  <v-click>
  
  $$ B = \frac{R}{2\pi L} \implies R = 2\pi B L = 2\pi(100)(20 \times 10^{-3}) = 4\pi \approx \mathbf{12.57 \Omega} $$
  </v-click>

- **(d) Upper Half-Power Frequency (Approx since $Q_0 \ge 5$)**:
  <v-click>
  
  $$ f_2 \approx f_0 + \frac{B}{2} = 795.78 + 50 = \mathbf{845.78 \text{ Hz}} $$
  </v-click>

</div>

---
layout: two-cols-header
---

## 16.4 Other Resonant Forms

:: left ::

- The idealized model depends on operating frequency range, Q, element materials, etc.
- Practical inductors (modeled by series $R$).
- Practical capacitors (modeled by parallel $R$).

<img src="/practical_parallel_rlc.svg" class="h-40 my-4 rounded bg-white mx-auto" />

<div class="mt-6 px-2 bg-purple-50 border-l-4 border-purple-500 text-xs">

  <span class="font-bold text-purple-700">Theoretical Insight:</span> Note that <b>$R_2$</b> does <u>not</u> appear in the $\omega_0$ formula. Because $R_2$ is purely real, it contributes only to the real part of $Y$. It scales the response magnitude but has <b>zero effect</b> on the resonant frequency.
</div>


:: right ::

<div class="text-base">

**Admittance Equation:**
$$ Y = \frac{1}{R_2} + j\omega C + \frac{1}{R_1 + j\omega L} $$
$$ Y = \frac{1}{R_2} + j\omega C + \frac{R_1 - j\omega L}{R_1^2 + \omega^2 L^2} $$

**Resonance Condition ($\text{Im}(Y) = 0$):**
$$ \omega_0 C - \frac{\omega_0 L}{R_1^2 + \omega_0^2 L^2} = 0 \implies C = \frac{L}{R_1^2 + \omega_0^2 L^2} $$
$$ R_1^2 + \omega_0^2 L^2 = \frac{L}{C} \implies \omega_0^2 L^2 = \frac{L}{C} - R_1^2 $$

**Resonant Frequency:**
$$ \omega_0 = \sqrt{\frac{1}{LC} - \left(\frac{R_1}{L}\right)^2} $$



</div>

---

## Example 16.4: Practical Resonant Circuit

Using the values $R_1 = 2 \Omega$, $L = 1 \text{H}$, $C = 0.125 \text{F}$, and $R_2 = 3 \Omega$ for the circuit shown previously, determine the **resonant frequency** and the **impedance at resonance**.



---

## Example 16.4 Solution

<div class="grid grid-cols-2 gap-4 items-center mt-2">
  <div class="text-base">

Using the derived formula for $\omega_0$:
$$ \omega_0 = \sqrt{\frac{1}{(1)(0.125)} - \left(\frac{2}{1}\right)^2} = \sqrt{8 - 4} = \mathbf{2 \text{ rad/s}} $$

- **At resonance ($\omega = 2$):**
  $$ Y(j2) = \frac{1}{3} + j(2)(0.125) + \frac{1}{2 + j2} \\= \frac{1}{3} + j0.25 + \frac{2-j2}{8} = \mathbf{0.583 \text{ S}} $$

- **Impedance at resonance:**
  $$ Z(j2) = \frac{1}{0.583} \approx \mathbf{1.714 \Omega} $$

*(Note: Maximum impedance magnitude occurs at $\omega_m = 3.26$ rad/s, not at $\omega_0$.)*

  </div>
  <div class="flex flex-col items-center">
    <img src="/example_16_4_plot.png" class="h-60 rounded" />
    <div class="mt-4 p-2 bg-blue-50 border-l-4 border-blue-500 text-xs w-full">

  <span class="font-bold text-blue-700">Key Takeaway:</span> In non-ideal or Low-Q circuits, <b>Resonance</b> ($\text{Im}(Y)=0$) and <b>Maximum Response</b> ($|Z|_{max}$) occur at <u>different</u> frequencies. They only converge as $Q$ increases.
  </div>
  </div>
</div>

---

## Practice 16.5

Referring to the circuit of Fig. 16.9a (Practical inductor in RLC Parallel circuit  ):
- $R_{1} = 1 \text{ k}\Omega$ 
- $C = 2.533 \text{ pF}$
- Target Resonant Frequency: 1 MHz

Determine inductance necessary.

<v-click>

**Answer**: 10 mH.

</v-click>

---

## Practice 16.5 Solution

$f_0 = 1 \text{ MHz} \implies \omega_0 = 2\pi \times 10^6 \text{ rad/s}, \quad R_1 = 1 \text{ k}\Omega, \quad C = 2.533 \text{ pF}$

<div class="text-base">

Using the exact resonant frequency formula for a practical parallel circuit:
<v-click>

$$ \omega_0^2 = \frac{1}{LC} - \frac{R_1^2}{L^2} \implies L^2 \omega_0^2 C - L + R_1^2 C = 0 $$
</v-click>

Substitute values ($4\pi^2 C \approx 100 \times 10^{-12}$):
<v-click>

$$ L^2 (100) - L + (10^6)(2.533 \times 10^{-12}) = 0 $$
$$ 100 L^2 - L + 2.533 \times 10^{-6} = 0 $$
</v-click>

Solve using quadratic formula $L = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$:
<v-click>

$$ L = \frac{1 \pm \sqrt{1 - 1.0132 \times 10^{-3}}}{200} \approx \frac{1 \pm 0.9995}{200} $$
</v-click>

<v-click>

- $L_1 = \frac{1.9995}{200} \approx \mathbf{10 \text{ mH}}$ (Matching textbook solution)
- $L_2 = \frac{0.0005}{200} \approx 2.5 \mu\text{H}$
</v-click>

</div>


---

## Practice 16.5 Solution (Cont.)

<div class="grid grid-cols-2 gap-4 items-center mt-2">
  <div class="text-base">

Using $L = 10 \text{ mH}$, we can calculate the **actual** peak shift:
- **Resonant frequency** ($f_0$):
  $f_0 = \frac{1}{2\pi}\sqrt{\frac{1}{LC} - \left(\frac{R_1}{L}\right)^2} \approx \mathbf{0.9999 \text{ MHz}}$
- **Max Response frequency** ($f_m$):
  $f_m \approx 1.0000 \text{ MHz}$
- **Quality Factor** ($Q_0$):
  $Q_0 = \omega_0 L / R_1 \approx \mathbf{62.8}$

<div class="mt-4 p-2 bg-green-50 border-l-4 border-green-500 text-[10px]">

<span class="font-bold text-green-700">Visual Verification:</span> Because $Q_0$ is high ($\ge 10$), the discrepancy between resonance and peak magnitude is negligible ($< 0.1\%$). This justifies the assumption $f_0 \approx 1/\sqrt{LC}$ in many high-Q designs.
</div>

  </div>
  <div class="flex flex-col items-center">
    <img src="/practice_16_5_plot.png" class="h-60 rounded" />
  </div>
</div>



---

## Equivalent Series and Parallel Combinations

<div class="text-sm">

To transform a practical circuit (series $R_s, L_s$) into an ideal parallel form ($R_p \parallel L_p$), we equate their admittances at a specific frequency $\omega$.

</div>

<div class="grid grid-cols-2 gap-8 text-sm">
<div>

**Series Network ($R_s, X_s$)**
$$ Y_s = \frac{1}{R_s + jX_s} = \frac{R_s - jX_s}{R_s^2 + X_s^2} $$

**Quality Factor ($Q$):**
$$ Q_s = \frac{|X_s|}{R_s} $$

</div>
<div>

**Parallel Network ($R_p, X_p$)**
$$ Y_p = \frac{1}{R_p} + \frac{1}{jX_p} = \frac{1}{R_p} - j\frac{1}{X_p} $$

**Quality Factor ($Q$):**
$$ Q_p = \frac{R_p}{|X_p|} $$

</div>
</div>

At equivalence: **$Q_s = Q_p = Q$**

<div class="flex justify-center my-4">
  <img src="/series_parallel_equivalence.svg" class="h-35 bg-white rounded" />
</div>


---

## Transformation Formulas

Equating the real and imaginary parts of $Y_s = Y_p$:

<div class="grid grid-cols-2 gap-4">
<div class="bg-blue-50 p-4 rounded border border-blue-200">

**Exact Formulas**
$$ R_p = R_s(1 + Q^2) $$
$$ X_p = X_s\left(1 + \frac{1}{Q^2}\right) $$

</div>
<div class="bg-green-50 p-4 rounded border border-green-200">

**High-Q Approximation ($Q \ge 5$)**
$$ R_p \approx Q^2 R_s $$
$$ X_p \approx X_s $$
($L_p \approx L_s$ or $C_p \approx C_s$)

</div>
</div>

<v-click>

**Note**: The transformation is frequency-dependent! The networks are equivalent **only** at the specific frequency $\omega$ used to calculate $Q$.

</v-click>

---

## The "Q" Notation

<div class="text-sm">

The symbol $Q$ is used in different contexts. Understanding the nuance is key to analysis.

| Symbol | Name | Formula | Application Context |
| :--- | :--- | :---: | :--- |
| **$Q$** | General Quality Factor | $2\pi \frac{\text{Energy Stored}}{\text{Energy Dissipated}}$ | The fundamental definition for **any** resonant system. |
| **$Q_0$** | Resonant $Q$ | $Q(\omega)\vert_{\omega = \omega_0}$ | The $Q$ value **at resonance**. Determines $B$ and selectivity. |
| **$Q_s$** | Series Branch $Q$ | $\frac{\omega L_s}{R_s}$ or $\frac{1}{\omega C_s R_s}$ | Used for a **single branch** of series components. |
| **$Q_p$** | Parallel Branch $Q$ | $\frac{R_p}{\omega L_p}$ or $\omega C_p R_p$ | Used for a **single branch** of parallel components. |


</div>

<div class="mt-6 flex justify-center">
<div class="bg-blue-50 px-2 rounded border-l-4 border-blue-500 text-sm">

**The Connection**: When we perform a series-parallel transformation at frequency $\omega$, the network is equivalent **only if** they have the same Quality Factor:
<div class="text-center font-bold mt-2">

$Q_s = Q_p = Q$

</div>
</div>
</div>

---

## Practical to Ideal RLC Transformation

Why do we transform series branches into parallel? **To simplify the circuit analysis.**

<div class="grid grid-cols-2 gap-4 mt-4 text-sm">
<div class="bg-red-50 p-4 rounded border border-red-200">

### 1. The Practical Model
A real inductor has series resistance ($R_s$).

<img src="/practical_parallel_rlc.svg" class="h-30 mx-auto my-2 rounded" />

**The Math Headache:**
- Resonant frequency is complex:
  $\omega_0 = \sqrt{\frac{1}{LC} - \left(\frac{R_s}{L}\right)^2}$
- Simple $1/\sqrt{LC}$ formula **fails**.
- Finding bandwidth ($B$) is difficult.

</div>
<div class="bg-green-50 p-4 rounded border border-green-200">

### 2. The Ideal (Simple) Model
We transform $R_s, L_s$ into parallel $R_p, L_p$.

<img src="/ideal_parallel_rlc.svg" class="h-30 mx-auto my-2 rounded" />

**The Math Shortcut:**
- Resonant frequency is simple:
  $\omega_0 = \mathbf{1/\sqrt{L_p C}}$
- Bandwidth is simple:
  $B = \mathbf{1/R_p C}$
- **Total Resistance** ($R_p$):
  $R_p = R_2 \parallel R_{transformed}$

</div>
</div>


---

## Example 16.5: Parallel Equivalence

Find the parallel equivalent of the series combination of a **100 mH** inductor and a **5 $\Omega$** resistor at **$\omega = 1000$ rad/s**.

<div class="grid grid-cols-2 gap-4 items-center">
<div>

**1. Calculate $X_s$ and $Q$:**
- $X_s = \omega L_s = (1000)(0.1) = \mathbf{100 \Omega}$
- $Q = X_s / R_s = 100 / 5 = \mathbf{20}$

**2. Check Approximation ($Q=20 \ge 5$):**
- $L_p \approx L_s = \mathbf{100 \text{ mH}}$
- $R_p \approx Q^2 R_s = (20^2)(5) = \mathbf{2000 \Omega}$

</div>
<v-click>

**3. Accuracy Check:**
$Z_s = 5 + j100 = \mathbf{100.1 \angle 87.1^\circ \Omega}$

$Z_p = 2000 \parallel j100 = \frac{2000(j100)}{2000 + j100}$
$Z_p = \mathbf{99.9 \angle 87.1^\circ \Omega}$

<span class="text-green-600 font-bold">The accuracy is impressive $(< 0.2\% \text{ error})$.</span>

</v-click>
</div>

---

## Frequency Sensitivity

The series-to-parallel transformation is **narrowband**. The equivalence is exact **only** at the target frequency $\omega$.

<div class="grid grid-cols-2 gap-4 items-center mt-4">
  <div>

**Key Limitations:**
- **Calculated values** ($R_p, L_p$) change as $\omega$ changes.
- **Physical implementation** usually uses constant components.
- **Error grows** as you move away from the "design" frequency.

</div>
</div>


---

## Shortcut Calculations

How do we get the **Ideal Model** values for the comparison?

<div class="grid grid-cols-2 gap-4 mt-2">
<div class="bg-blue-50 p-4 rounded border border-blue-200 text-xs">

### 1. Low-Q Case (Ex 16.4)
$\omega_0 = 2, R_1 = 2, L = 1, R_2 = 3$

- $X_s = \omega_0 L = (2)(1) = \mathbf{2 \Omega}$
- $Q = X_s/R_1 = 2/2 = \mathbf{1}$
- $R_{transformed} = R_1(1+Q^2) = 2(2) = \mathbf{4 \Omega}$
- $L_p = L(1+1/Q^2) = 1(2) = \mathbf{2 \text{ H}}$
- **Total $R_p$**: $R_2 \parallel R_{transformed} = 3 \parallel 4 = \mathbf{1.714 \Omega}$

**Ideal Shortcut Model**:
$1.714 \Omega \parallel 2 \text{ H} \parallel 0.125 \text{ F}$

</div>
<div class="bg-green-50 p-4 rounded border border-green-200 text-xs">

### 2. High-Q Case (Prac 16.5)
$f_0 = 1\text{MHz}, R_1 = 1\text{k}, L = 10\text{m}, C = 2.533\text{p}$

- $X_s = \omega_0 L = (2\pi \cdot 10^6)(10\text{m}) \approx \mathbf{62.8 \text{ k}\Omega}$
- $Q = X_s/R_1 \approx \mathbf{62.8}$
- $R_p = R_1(1+Q^2) \approx (1k)(1+62.8^2) \approx \mathbf{3.94 \text{ M}\Omega}$
- $L_p = L(1+1/Q^2) \approx 10\text{m}(1.0002) \approx \mathbf{10 \text{ mH}}$

**Ideal Shortcut Model**:
$3.94 \text{ M}\Omega \parallel 10 \text{ mH} \parallel 2.533 \text{ pF}$

</div>
</div>

<div class="mt-4 p-2 bg-purple-50 text-center rounded text-xs">
  Both models stay resonant at the <b>same</b> design frequency, but the <b>Low-Q</b> model is a poor approximation elsewhere.
</div>

---

## Transformation Check: Ex 16.4 vs. Prac 16.5

How accurate is the **Simple RLC** shortcut compared to the **Actual** practical circuit response?

<div class="grid grid-cols-2 gap-4 items-center mt-4">
  <div class="text-base">

**1. Low-Q Case (Ex 16.4, $Q \approx 1$)**
- **Peak Sensitivity**: High.
- **Result**: The shortcut predicts peak at $\omega_0=2$, but actual peak shifts to $\omega_m = 3.26$.
- **Verdict**: <span class="text-red-600 font-bold">Unreliable.</span> Use exact derivation.

**2. High-Q Case (Prac 16.5, $Q \approx 63$)**
- **Peak Sensitivity**: Negligible.
- **Result**: Response curves are virtually identical.
- **Verdict**: <span class="text-green-600 font-bold">Excellent.</span> The ideal shortcut is safe and efficient!
</div>

<div class="flex flex-col items-center">
  <img src="/transformation_comparison_plots.png" class="rounded bg-white w-full" />
    <p class="text-[10px] mt-2 text-gray-500 text-center">Blue: Actual Model | Red (Dashed): Ideal Shortcut Model</p>
</div>

</div>

---

## Practice 16.6 & 16.7

**Practice 16.6**: Find the parallel equivalent of a series combination of $L = 8$ H and $R = 8$ k$\Omega$ at $f = 20$ kHz.

<v-click>

- $\omega = 2\pi(20k) \approx 125.7 \text{ krad/s}$
- $X_s = \omega L \approx 1005 \text{ k}\Omega$
- $Q = X_s/R_s \approx 125.6$
- **Answer**: $L_p = \mathbf{8 \text{ H}}, R_p = Q^2 R_s \approx \mathbf{126 \text{ M}\Omega}$.

</v-click>

<br>

**Practice 16.7**: Find the series equivalent for a parallel network of $R_p = 250$ k$\Omega$ and $L_p = 5$ H at $\omega = 10^5$ rad/s.
<v-click>

- $X_p = \omega L_p = 500 \text{ k}\Omega$
- $Q = R_p/X_p = 250k / 500k = \mathbf{0.5}$ (Low Q!)
- $R_s = R_p / (1+Q^2) = 250k / 1.25 = \mathbf{200 \text{ k}\Omega}$
- $X_s = X_p / (1+1/Q^2) = 500k / 5 = \mathbf{100 \text{ k}\Omega} \implies L_s = \mathbf{1 \text{ H}}$

</v-click>





---

## Summary: Key Equations

<div class="grid grid-cols-2 gap-4 text-base mt-2">
<div class="bg-blue-50 px-3 rounded border border-blue-200">

**Fundamental Parameters**
- **Resonant Frequency**: $\omega_0 = \frac{1}{\sqrt{LC}}$
- **Bandwidth**: $B = \omega_2 - \omega_1 = \frac{\omega_0}{Q_0}$
- **Damping Coefficient**: $\alpha = \frac{\omega_0}{2Q_0}$
- **Damping Factor**: $\zeta = \frac{1}{2Q_0}$

</div>
<div class="bg-green-50 px-3 rounded border border-green-200 text-xs">

**Exact Half-Power Frequencies**
$$ \omega_{1,2} = \omega_0 \left[ \sqrt{1 + \left(\frac{1}{2Q_0}\right)^2} \mp \frac{1}{2Q_0} \right] $$

**High-Q Approximation ($Q_0 \ge 5$)**
$$ \omega_{1,2} \approx \omega_0 \mp \frac{B}{2} $$
$$ \omega_0 \approx \frac{\omega_1 + \omega_2}{2} $$

</div>


<div class="bg-purple-50 px-3 rounded border border-purple-200 text-xs">

**Quality Factor ($Q_0$)**
- **Parallel**: $Q_0 = \omega_0 RC = R \sqrt{\frac{C}{L}}$
- **Series**: $Q_0 = \frac{\omega_0 L}{R} = \frac{1}{R} \sqrt{\frac{L}{C}}$
- **Peak Current (Parallel)**: $I_L = I_C \approx Q_0 I_s$
- **Peak Voltage (Series)**: $V_L = V_C \approx Q_0 V_s$

</div>
<div class="bg-orange-50 px-3 rounded border border-orange-200">

**Transformations ($Y_s = Y_p$)**
- **Exact**: 
  $R_p = R_s(1 + Q^2)$
  $X_p = X_s(1 + 1/Q^2)$
- **High-Q ($Q \ge 5$)**:
  $R_p \approx Q^2 R_s$, $X_p \approx X_s$

</div>
</div>

---

## Summary: Key Concepts

<div class="grid grid-cols-2 gap-6 text-sm mt-8">
<div>

### 1. Resonance Condition
- Occurs when input impedance $Z(j\omega)$ or admittance $Y(j\omega)$ is **purely resistive**.
- The imaginary part of the immittance is zero.
- Unity power factor ($PF = 1$).

### 2. Frequency Response Shape
- **High Q**: Sharp peak, narrow bandwidth, high selectivity.
- **Low Q**: Broad peak, wide bandwidth, low selectivity.
- Peak height depends only on $R$ (impedance at $\omega_0$).

</div>
<div>

### 3. Symmetry
- **Geometric Symmetry**: Always exact. $\omega_0 = \sqrt{\omega_1 \omega_2}$.
- **Arithmetic Symmetry**: Accurate only for high Q.  $\\ \omega_0 \approx (\omega_1 + \omega_2)/2$.

### 4. Practical Components
- Inductors have series resistance $R_L$.
- Impacts resonance: $\omega_0 = \sqrt{\frac{1}{LC} - \frac{R_L^2}{L^2}}$.
- Causes the response to shift and broaden compared to ideal model.

</div>
</div>

<div class="mt-8 flex justify-center">
  <div class="bg-yellow-50 px-4 py-2 rounded-full border border-yellow-200 font-bold text-yellow-800">

  $\omega_0 = \frac{1}{\sqrt{LC}} \quad \text{vs} \quad Q_0 = \frac{\text{Energy Stored}}{\text{Energy Lost}}$
  </div>
</div>
