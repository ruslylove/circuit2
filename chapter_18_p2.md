---
theme: seriph
background: https://cover.sli.dev
title: Chapter 18 Part 2
info: |
  ## Chapter 18 Part 2
  Fourier Circuit Analysis: Complex Series and Transforms
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Chapter 18: Fourier Circuit Analysis

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

## Outline

- Complex Form of the Fourier Series
- Definition of the Fourier Transform
- Some Properties of the Fourier Transform
- Fourier Transform Pairs for Some Simple Time Function
- The Fourier Transform of a General Periodic Time Function
- The System Function and Response in the Frequency Domain
- The Physical Significance of the System Function

---

## 18.4 Complex Form of the Fourier Series

- It is possible to obtain the amplitude directly by using a form of Fourier series in which each term is a cosine function with a phase angle.
- An even more convenient and concise form is obtained if the sines and cosines are expressed as **exponential functions** with complex multiplying constants.

---

## Example 18.3

**Problem**: Determine $c_n$ for the square wave of Fig 18.10. ($T=2, \omega_0 = \pi$).
- Even and Half-wave symmetry.

**Solution**:
- Formula using symmetry: $c_n = \frac{2}{T} \int_0^{T/2} f(t) \cos(n\omega_0 t) dt$? No, complex form.
- $c_n = \frac{1}{T} \int_{-T/2}^{T/2} f(t) e^{-jn\omega_0 t} dt$.
- Result derived in text: $c_n = \frac{2}{n\pi} \sin(n\pi/2)$.
- Values: $c_0=0$ (Average is 0? Check fig). $c_1 = 2/\pi$, $c_2 = 0$, $c_3 = -2/3\pi$.

---

## Practice 18.7

Determine the general coefficient $c_n$ in the complex Fourier series for the waveform shown:
(a) 18.4a
(b) 18.4c

**Ans**:
- (a) $-j2/(n\pi)$ for $n$ odd, $0$ for $n$ even.
- (c) $-j [4/(n^2 \pi^2)] \sin(n\pi/2)$ for all $n$.

---

## Sampling Function

- The trigonometric factor that occurs frequently in modern communication theory is called the **sampling function**.
- It is derived from the rectangular pulse train.
- The product of this sequence of pulses and any other function $f(t)$ represents samples of $f(t)$ every $T$ seconds.

---

## 18.5 Definition of the Fourier Transform

- We use the notation $\mathcal{F}\{ \}$ to symbolize "Fourier transform of".
- We obtain the Fourier transform of singularity functions like the unit impulse $\delta(t - t_0)$.

---

## 18.6/18.7 Properties & Pairs

**Unit Impulse Function**:
- We seek the Fourier transform of $\delta(t - t_0)$.

**The Signum Function**:
- A singularity function $sgn(t)$.

**The Unit Step Function**:
- $u(t)$.

---

## Physical Significance of Fourier Transform

- Suppose $f(t)$ is voltage across or current through a $1 \Omega$ resistor.
- $f^2(t)$ is the instantaneous power delivered.
- $|F(j\omega)|^2$ is the **energy density** or **energy per unit bandwidth** (J/Hz).
- This energy density is always a real, even, nonnegative function of $\omega$.

---

## Example 18.5

**Problem**: Use the Fourier transform to obtain the continuous spectrum of the single rectangular pulse (Fig 18.13a).
- Pulse $f(t) = V_0$ for $t_0 < t < t_0 + \tau$, and 0 otherwise.

**Solution**:
- $F(j\omega) = \int_{t_0}^{t_0+\tau} V_0 e^{-j\omega t} dt$.
- Result: $F(j\omega) = V_0 \tau \text{ sinc}(\frac{\omega \tau}{2}) e^{-j\omega(t_0+\tau/2)}$.
- Magnitude is $|V_0 \tau \text{ sinc}(\frac{\omega \tau}{2})|$.

#### Example 18.8

**Problem**: Find the voltage across the inductor of the circuit (Fig 18.22a) when input is $v_i(t) = 5e^{-3t}u(t)$. Network: $4\Omega$ resistor in series with $2H$ inductor.

**Solution**:
1.  **System Function**: $H(j\omega) = Z_L / (Z_R + Z_L) = j2\omega / (4 + j2\omega)$.
2.  **Input Transform**: $V_i(j\omega) = 5 / (3 + j\omega)$.
3.  **Output Transform**: $V_o(j\omega) = H(j\omega) V_i(j\omega) = \frac{j2\omega}{4+j2\omega} \frac{5}{3+j\omega}$.
4.  **Partial Fraction Expansion**:
    - $V_o(j\omega) = \dots$
    - Inverse Transform to get $v_o(t)$.
    - Text result: $v_o(t) = 5(3e^{-3t} - 2e^{-2t})u(t)$.

---

## 18.8 Fourier Transform of General Periodic Time Function

- Consider a periodic time function $f(t)$ with period $T$.
- We can determine its Fourier transform using the series expansion.

---

## 18.9 System Function and Response

- Assuming input and output are voltages, we apply the basic definition of the Fourier transform.
- The output can be expressed by the **convolution integral**.

---

## 18.10 Physical Significance of System Function

- Given a general linear two-port network N without initial energy storage.
- Assume sinusoidal forcing and response functions.
- Input voltage: $A \cos(\omega_x t + \theta)$.
- Output voltage: $B \cos(\omega_x t + \phi)$.
- In phasor form: $V_i = A e^{j\theta}$ and $V_o = B e^{j\phi}$.

---

## Example 18.8

Calculate the input impedance for the one-port resistor network shown in Fig 17.3.

*(Space for solution)*
