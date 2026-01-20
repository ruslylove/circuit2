---
theme: seriph
background: https://cover.sli.dev
title: Chapter 16 Part 2
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

## Part II

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

- Scaling
- Bode Diagrams

---

# 16.5 Scaling

- The scaling procedures discussed in this section enable us to analyze networks composed of practical-sized elements by scaling the element values to permit more convenient numerical calculations.
- Let us select the parallel resonant circuit shown in Fig. 16.17a as our example.

---

# 16.5 Scaling (continued)

- Let us assume that our goal is to scale this network in such a way as to provide an impedance **maximum of 5000 $\Omega$** at a resonant frequency of **$5 \times 10^6$ rad/s**, or 796 kHz.
- We may use the same response curve shown in Fig. 16.17b if every number on the **ordinate** scale is increased by a factor of 2000 and every number on the **abscissa** scale is increased by a factor of $5 \times 10^6$.
- We will treat this as two problems:
  1.  Scaling in magnitude by a factor of **2000**
  2.  Scaling in frequency by a factor of **$5 \times 10^6$**

---

# Scaling Factors

- **Magnitude Response**:
  - $2.5 \Omega \to 5000 \Omega$
  - Magnitude scaling factor $K_m = 2000$

- **Resonant Frequency**:
  - $1 \text{ rad/s} \to 5 \times 10^6 \text{ rad/s}$
  - Frequency scaling factor $K_f = 5 \times 10^6$

---

# Magnitude Scaling

- Magnitude scaling is defined as the process by which the impedance of a two-terminal network is increased by a factor of $K_m$, the frequency remaining constant. The factor $K_m$ is real and positive.
- To increase the input impedance of a network by a factor of $K_m$, it is sufficient to increase the impedance of each element in the network by this same factor.
- A resistance $R$ must be replaced by a resistance $K_m R$.
- An impedance $sL$ must be replaced by $s(K_m L)$. Thus, $L \to K_m L$.
- An impedance $1/sC$ must be replaced by $1/s(C/K_m)$. Thus, $C \to C/K_m$.

---

# Frequency Scaling

- We define frequency scaling as the process by which the frequency at which any impedance occurs is increased by a factor of $K_f$.
- Frequency scaling is accomplished by scaling each passive element in frequency.
- **Resistors**: No change ($R \to R$).
- **Inductors**: Impedance $sL$ at frequency $\omega$ becomes $sL$ at frequency $K_f \omega$. To maintain impedance, $L \to L/K_f$.
- **Capacitors**: Impedance $1/sC$ at frequency $\omega$ becomes $1/sC$ at frequency $K_f \omega$. To maintain impedance, $C \to C/K_f$.

---

# Example 16.6

**Problem**: Scale the network shown in Fig. 16.20(a) by $K_m = 20$ and $K_f = 50$, and then find $Z_{in}(s)$ for the scaled network.

**Solution**:
1.  **Scaling Factors**: $K_m = 20$, $K_f = 50$.
2.  **Original Values**: Check Fig 16.20a (implied: $R=1\Omega, L=1H, C=1F$ or similar normalized values).
3.  **Scaled Values**:
    - $R_{new} = K_m R$.
    - $L_{new} = K_m L / K_f = (20/50) L = 0.4 L$.
    - $C_{new} = C / (K_m K_f) = C / (20 \cdot 50) = C / 1000$.
4.  **Result**:
    - If original $Z_{in}(s)$ was computed, replace $s$ with $s/K_f$ and multiply amplitude by $K_m$.
    - $Z_{in\_scaled}(s) = K_m Z_{in}(s/K_f)$.

---

# Practice 16.9

A parallel resonant circuit is defined by $C = 0.01 \text{ F}$, $B = 2.5 \text{ rad/s}$, and $\omega_0 = 20 \text{ rad/s}$. Find the values of $R$ and $L$ if the network is scaled in:

(a) magnitude by a factor of 800;
(b) frequency by a factor of $10^4$;
(c) magnitude by a factor of 800 and frequency by a factor of $10^4$.

**Answers**:
- (a) $32 \text{ k}\Omega, 200 \text{ H}$
- (b) $40 \Omega, 25 \mu\text{H}$
- (c) $32 \text{ k}\Omega, 20 \text{ mH}$

---

# 16.6 Bode Diagrams

- To discover a quick method of obtaining an approximate picture of the amplitude and phase variation of a given transfer function as functions of $\omega$.

## The Decibel (dB) Scale

- The approximate response curve we construct is called **an asymptotic plot**, or **a Bode plot**, or **a Bode diagram**, after its developer, Hendrik W. Bode.
- Both the magnitude and phase curves are shown using a logarithmic frequency scale for the abscissa.
- The magnitude itself is also shown in logarithmic units called **decibels (dB)**.
- Definition: $H_{dB} = 20 \log_{10} |H(j\omega)|$

---

# Practice 16.10

Calculate $H_{dB}$ at $\omega = 146 \text{ rad/s}$ if $H(s)$ equals:
(a) $20/(s+100)$
(b) $20(s+100)$
(c) $20s$

Calculate $|H(j\omega)|$ if $H_{dB}$ equals:
(d) $29.2 \text{ dB}$
(e) $-15.6 \text{ dB}$
(f) $-0.318 \text{ dB}$

**Answers**:
- (a) $-18.94 \text{ dB}$
- (b) $71.0 \text{ dB}$
- (c) $69.3 \text{ dB}$
- (d) $28.8$
- (e) $0.1660$
- (f) $0.964$

---

# Determination of Asymptotes

- Our next step is to factor $H(s)$ to display its poles and zeros.
- We first consider a zero at $s = -a$.
- The Bode diagram for this function consists of the two asymptotic curves approached by $H_{dB}$ for very large and very small values of $\omega$.

- When $\omega \ll a$: $H_{dB} \approx 20 \log a$ (Constant)
- When $\omega \gg a$: $H_{dB} \approx 20 \log \omega$ (Sloped line)

---

# Determination of Asymptotes (cont.)

- At $\omega = a$, $H_{dB}$ error is max.
- At $\omega = 10a$, $H_{dB}$ increases by 20 dB.
- Thus, the value of $H_{dB}$ increases **20 dB** for every 10-fold increase in frequency.
- The asymptote therefore has a slope of **20 dB/decade**.
- Since $H_{dB}$ increases by **6 dB** when $\omega$ doubles, an alternate value for the slope is **6 dB/octave**.

- The frequency $\omega = a$ is described as the **corner**, **break**, **3 dB**, or **half-power frequency**.

---

# Example 16.7

**Problem**: Obtain the Bode plot of the input impedance of the network shown in Fig. 16.22 (Series RL with $R=20\Omega$, $L=0.2H$ based on solution).

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
![Example 16.7 Bode Plot](/example_16_7_bode.svg)
<div class="text-xs text-center opacity-70">Fig 16.22: Bode Plot of Input Impedance</div>
---

# Practice 16.11

Construct a Bode magnitude plot for $H(s) = 50 + s$.

**Answers**:
- 34 dB, $\omega < 50 \text{ rad/s}$
- slope = +20 dB/decade, $\omega > 50 \text{ rad/s}$

---

# Phase Response

- Since the angle is $45^\circ$ at $\omega = a$, we now construct the straight-line asymptote extending from:
  - $0^\circ$ at $\omega = 0.1a$
  - through $45^\circ$ at $\omega = a$
  - to $90^\circ$ at $\omega = 10a$.
- This straight line has a slope of **$45^\circ$/decade**.

**Errors**:
- Max diff $\pm 5.71^\circ$ at $\omega = 0.1a$ and $10a$.
- Errors of $\pm 5.29^\circ$ occur at $\omega = 0.394a$ and $2.54a$.
- Error is zero at $\omega = 0.159a$, $a$, and $6.31a$.

---

# Practice 16.12

Draw the Bode phase plot for the transfer function of Example 16.7.

**Answers**:
- $0^\circ$, $\omega \le 10$
- $90^\circ$, $\omega \ge 1000$
- $45^\circ$, $\omega = 100$
- $45^\circ$/dec slope, $10 < \omega < 1000$. ($\omega$ in rad/s).

---

# Additional Considerations

- **Single Pole**:
  - Since this is the reciprocal of a zero, the logarithmic operation leads to a Bode plot which is the negative of that obtained previously.
  - Amplitude: 0 dB up to $\omega = a$, then slope is **-20 dB/decade**.
  - Phase: $0^\circ$ for $\omega < 0.1a$, $-90^\circ$ for $\omega > 10a$, slope **$-45^\circ$/decade** in between.

- **Pole/Zero at Origin**:
  - If $H(s) = s$: Infinite straight line passing through 0 dB at $\omega = 1$ with slope **20 dB/decade**.
  - If $H(s) = 1/s$: Straight line passing through 0 dB at $\omega = 1$ with slope **-20 dB/decade**.

---

# Example 16.8

**Problem**: Obtain the Bode plot for the gain of the circuit shown in Fig. 16.26 ($V_{in}$ to $V_{out}$).

**Solution**:
- **Transfer Function** (derived): $H(s) = \frac{-2s}{(1 + s/10)(1 + s/20,000)}$.
- **Factors**:
  1.  **Constant**: $-2 \implies 20 \log |-2| = 6 \text{ dB}$.
  2.  **Zero at Origin**: $s \implies +20$ dB/dec slope always, passing through 0dB at $\omega=1$.
  3.  **Pole 1**: $\omega_1 = 10$ rad/s (Slope -20 dB/dec).
  4.  **Pole 2**: $\omega_2 = 20,000$ rad/s (Slope -20 dB/dec).
- **Combined Plot**:
  - Starts rising at 20 dB/dec.
  - At $\omega=10$, slope becomes $20 - 20 = 0$ dB/dec (Flat).
  - Gain at $\omega=10$: calculated approx peak.
  - At $\omega=20,000$, slope becomes $0 - 20 = -20$ dB/dec.

![Example 16.8 Bode Plot](/example_16_8_bode.svg)
<div class="text-xs text-center opacity-70">Fig 16.27: Bode Amplitude Plot</div>

---

# Practice 16.13

Construct a Bode magnitude plot for $H(s)$ equal to:
(a) $50/(s + 100)$
(b) $(s + 10) / (s + 100)$
(c) $(s + 10) / s$

**Answers**:
(a) $-6 \text{ dB}$, $\omega < 100$; $-20 \text{ dB/decade}$, $\omega > 100$.
(b) $-20 \text{ dB}$, $\omega < 10$; $+20 \text{ dB/decade}$, $10 < \omega < 100$; $0 \text{ dB}$, $\omega > 100$.
(c) $0 \text{ dB}$, $\omega > 10$; $-20 \text{ dB/decade}$, $\omega < 10$.

---

# Example 16.9

**Problem**: Draw the phase plot for the transfer function $H(s) = \frac{-2s}{(1 + s/10)(1 + s/20,000)}$.

**Solution**:
- $H(j\omega) = \frac{-j2\omega}{(1 + j\omega/10)(1 + j\omega/20000)}$.
- **Phase Components**:
  1.  **Numerator**: $-j \implies -90^\circ$. (Wait, $-2(j\omega)$? Numerator is $-2s$. $s=j\omega$, so $-2j\omega$. Angle $-90^\circ$. Correct.)
  2.  **Pole at 10**: Starts $0^\circ$, goes to $-90^\circ$. Center $-45^\circ$ at $\omega=10$.
  3.  **Pole at 20,000**: Starts $0^\circ$, goes to $-90^\circ$. Center $-45^\circ$ at $\omega=20k$.
- **Total Phase**:
  - $\omega \ll 10$: $-90^\circ$.
  - $\omega = 10$: $-90 - 45 = -135^\circ$.
  - $10 < \omega < 20k$: Flat region? No, pole effects accumulate.
![Example 16.9 Bode Plot](/example_16_9_bode.svg)
<div class="text-xs text-center opacity-70">Fig 16.28: Bode Phase Response</div>

---

# Practice 16.14

Draw the Bode phase plot for $H(s)$ equal to:
(a) $50/(s+100)$
(b) $(s+10) / (s+100)$
(c) $(s+10) / s$

**Answers**:
(a) $0^\circ$, $\omega < 10$; $-45^\circ$/decade, $10 < \omega < 1000$; $-90^\circ$, $\omega > 1000$.
(b) $0^\circ$, $\omega < 1$; $+45^\circ$/decade, $1 < \omega < 10$; $45^\circ$, $10 < \omega < 100$; $-45^\circ$/decade, $100 < \omega < 1000$; $0^\circ$, $\omega > 1000$.
(c) $-90^\circ$, $\omega < 1$; $+45^\circ$/decade, $1 < \omega < 100$; $0^\circ$, $\omega > 100$.
