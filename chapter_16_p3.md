---
theme: seriph
background: https://cover.sli.dev
title: Chapter 16 Part 3
info: |
    ## Chapter 16 Part 3
    Frequency Response: Bode Diagrams and Filters
class: text-center
drawings:
    persist: false
transition: slide-left
mdc: true
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

# Outline

- Bode Diagrams (Complex Conjugate Pairs)
- Filters

---

# Complex Conjugate Pairs

- Consider the standard quadratic form: $H(s) = 1 + 2\zeta(s/\omega_0) + (s/\omega_0)^2$
- The quantity $\zeta$ is the **damping factor**.
- $\omega_0$ is the **corner frequency** of the asymptotic response.
- If $\zeta = 1$, $H(s) = (1 + s/\omega_0)^2$ (Two identical real poles/zeros).
- If $\zeta > 1$, $H(s)$ can be factored into two distinct real poles/zeros.
- If $\zeta < 1$, the roots are complex conjugates.

---

# Magnitude Response (Complex Pairs)

- Asymptotes:
  - Low frequency ($\omega \ll \omega_0$): $0 \text{ dB}$
  - High frequency ($\omega \gg \omega_0$): Slope of **+40 dB/decade** (for zeros in numerator).
- Correction near $\omega_0$:
  - If $\zeta = 1$: +6 dB correction.
  - If $\zeta = 0.5$: No correction (0 dB error).
  - If $\zeta = 0.1$: -14 dB correction (peaking).

---

# Phase Response (Complex Pairs)

- For $H(j\omega) = 1 + j2\zeta(\omega/\omega_0) - (\omega/\omega_0)^2$
- Asymptotic approximation:
  - $0^\circ$ for $\omega < 0.1 \omega_0$
  - $180^\circ$ for $\omega > 10 \omega_0$
  - Straight line slope: **$90^\circ$/decade** between $0.1 \omega_0$ and $10 \omega_0$.
- At corner frequency $\omega_0$: Phase is **$90^\circ$**.

---

# Example 16.10

Construct the Bode plot for the transfer function:

$$
H(s) = \frac{100,000s}{(s + 1)(10,000 + 20s + s^2)} = \frac{10s}{(1 + s)(1 + 0.002s + 0.0001s^2)}
$$

**Solution**:
1.  **Quadratic Factor**: $1 + \frac{20s}{10000} + \frac{s^2}{10000} = 1 + 2\zeta(\frac{s}{\omega_0}) + (\frac{s}{\omega_0})^2$.
2.  **Parameters**:
    - $\omega_0^2 = 10000 \implies \omega_0 = 100$ rad/s.
    - $2\zeta/\omega_0 = 0.002 \implies \zeta = 0.1$.
3.  **Asymptotes**:
    - **Constant**: 10 (20 dB).
    - **Zero at Origin**: +20 dB/dec slope.
    - **Pole at $\omega=1$**: Slope changes by -20 dB/dec.
    - **Pole at $\omega=1$**: Slope changes by -20 dB/dec.
    - **Double Pole at $\omega=100$**: Slope changes by -40 dB/dec.
---

4.  **Resonant Peak**:
    - Since $\zeta = 0.1$, correction at $\omega_0$ is needed.
    - Peak correction $\approx -20 \log(2\zeta) = -20 \log(0.2) = +13.98 \text{ dB}$.
    - Actual magnitude at $\omega=100$ is $\sim 14 \text{ dB}$ above the asymptote.

![Example 16.10 Bode Plot](/example_16_10_bode.svg)
<div class="text-xs text-center opacity-70">Fig 16.10: Bode Magnitude Plot (Blue) and Asymptotes (Red)</div>

---

# Practice 16.15

If $H(s) = 1000s^2 / (s^2 + 5s + 100)$, sketch the Bode amplitude plot and calculate a value for:
(a) $\omega$ when $H_{dB} = 0$;
(b) $H_{dB}$ at $\omega = 1$;
(c) $H_{dB}$ as $\omega \to \infty$.

**Answers**:
- (a) 0.316 rad/s
- (b) 20 dB
- (c) 60 dB

---

# 16.7 Filters

- Filters are used in modern electronics to obtain DC voltages, eliminate noise, separate channels, etc.
- A filter selects the frequencies that may pass through a network.
- **Low-pass filter**: Passes frequencies below a cutoff, attenuates above.
- **High-pass filter**: Passes frequencies above a cutoff, attenuates below.
- **Bandpass filter**: Passes a specific range (passband), attenuates outside (stopband).
- **Bandstop/Notch filter**: Blocks a specific range of frequencies.

---

# Passive Low-Pass and High-Pass Filters

- Can be constructed using a single capacitor and resistor (RC circuit).
- **Low-Pass**: Output across Capacitor.
  - Transfer Function: $H(s) = \frac{1}{1 + sRC}$
  - Corner frequency $\omega_0 = 1/RC$.
  - Low freq gain $\approx 1$, High freq gain $\to 0$.

- **High-Pass**: Output across Resistor (swap R and C).
  - $H(s) = \frac{sRC}{1 + sRC}$
  - Passes high frequencies.

---

# Example 16.14

Design a high-pass filter with a corner frequency of 3 kHz.

*(Space for solution)*

---

# Practice 16.16

Design a high-pass filter with a cutoff frequency of 13.56 MHz, a common RF power supply frequency. Verify your design using PSpice.

*(Student exercise)*

---

# Bandpass Filters

- Combining low-pass and high-pass characteristics.
- Often realized with RLC circuits.
- The transfer function effectively has one zero (at origin) and two poles.
- Center frequency occurs where the magnitude is maximum.

---

# Example 16.12

Design a bandpass filter characterized by a bandwidth of 1 MHz and a high-frequency cutoff of 1.1 MHz.

*(Space for solution)*

---

# Practice 16.17

Design a bandpass filter with a low-frequency cutoff of 100 rad/s and a high-frequency cutoff of 10 krad/s.

**Answer**:
- One possible solution: $R = 990 \Omega$, $L = 100 \text{ mH}$, $C = 10 \mu\text{F}$.

---

# Active Filters

- Use active elements like Op Amps.
- Overcomes shortcomings of passive filters (loading effects, inductor size/loss).
- Can provide gain.

---

# Example 16.13

Design an active low-pass filter with a cutoff frequency of 10 kHz and a voltage gain of 40 dB.

*(Space for solution)*

---

# Practice 16.18

Design a low-pass filter circuit with a gain of 30 dB and a cutoff frequency of 1 kHz.

**Answer**:
- One possible solution: $R_1 = 100 \text{ k}\Omega$, $R_f = 3.062 \text{ M}\Omega$, $R_2 = 79.58 \Omega$, $C = 2 \mu\text{F}$.
