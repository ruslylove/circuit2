---
theme: seriph
background: https://cover.sli.dev
title: Chapter 18 Part I - Fourier Series
info: |
  ## Chapter 18 Part I - Fourier Series
  Fourier Circuit Analysis: Trigonometric Series and Symmetry
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
layout: cover
---

# Chapter 18: Fourier Circuit Analysis

## Part I - Fourier Series

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

- Trigonometric Form of the Fourier Series
- The Use of Symmetry
- Complete Response to Periodic Forcing Function

---

## 18.1 Trigonometric Form of the Fourier Series

- In this section, we refocus our attention on forcing functions that are sinusoidal in nature.
- We discover how to write a general periodic function as a sum of such functions—leading us into a discussion of a new set of circuit analysis procedures.

---

## Harmonics

- Consider a periodic function $v(t)$ with period **$T$**.
- The **fundamental frequency** (or first harmonic) is:
  $$\omega_0 = \frac{2\pi}{T}$$
- The **fundamental component** is the first term ($n=1$) of the Fourier series:
  $$v_1(t) = a_1 \cos(\omega_0 t) + b_1 \sin(\omega_0 t)$$
- **Harmonics** are sinusoidal components with frequencies that are integer multiples of the fundamental frequency:
  $$\omega_n = n\omega_0$$
  where $n = 1, 2, 3, \dots$
- The **first harmonic** ($n=1$) is the fundamental frequency.
- The **second harmonic** ($n=2$) has frequency $2\omega_0$, and so on.

---

## Harmonics Plots


**Plot 1: In-Phase Harmonic**
- Fundamental: $v_1(t) = 2\cos(\omega_0 t)$
- Harmonic: $v_{3a}(t) = \cos(3\omega_0 t)$
- Sum: $v(t) = 2\cos(\omega_0 t) + \cos(3\omega_0 t)$
- The peak is "sharpened" because the third harmonic adds to the fundamental at $t=0$.

<img src="/harmonic_sum_3a.svg" class="h-60 mx-auto p-4" alt="Harmonic sum 3a" />



---

## Harmonics Plots (Continued)

**Plot 2: Larger In-Phase Harmonic**
- Fundamental: $v_1(t) = 2\cos(\omega_0 t)$
- Harmonic: $v_{3b}(t) = 1.5\cos(3\omega_0 t)$
- Sum: $v(t) = 2\cos(\omega_0 t) + 1.5\cos(3\omega_0 t)$
- Significant distortion leads to multiple local peaks (ringing) near the fundamental peak.


<img src="/harmonic_sum_3b.svg" class="h-60 p-4 mx-auto" alt="Harmonic sum 3b" />


---

## Harmonics Plots (Continued)

**Plot 3: Quadrature Harmonic**
- Fundamental: $v_1(t) = 2\cos(\omega_0 t)$
- Harmonic: $v_{3c}(t) = \sin(3\omega_0 t)$
- Sum: $v(t) = 2\cos(\omega_0 t) + \sin(3\omega_0 t)$
- A $90^\circ$ phase shift in the harmonic introduces asymmetry in the waveform's rising and falling edges.

<img src="/harmonic_sum_3c.svg" class="h-60 p-4 mx-auto" alt="Harmonic sum 3c" />


---

### Practice 18.1

Let a third-harmonic voltage be added to the fundamental to yield $v = 2 \cos \omega_0 t + V_{in3} \sin 3 \omega_0 t$.

(a) Find the value of $V_{in3}$ so that $v(t)$ will have zero slope at $\omega_0 t = 2\pi/3$.
(b) Evaluate $v(t)$ at $\omega_0 t = 2\pi/3$.

**Answers**:
- (a) 0.577
- (b) -1.000

---

**Solution**:

(a) Let $x = \omega_0 t$. The voltage is $v(x) = 2 \cos x + V_{in3} \sin 3x$.
- The slope is $v'(x) = -2 \sin x + 3 V_{in3} \cos 3x$.
- At $x = 2\pi/3$:
  $-2 \sin(2\pi/3) + 3 V_{in3} \cos(3 \cdot 2\pi/3) = 0$
  $-2 (\sqrt{3}/2) + 3 V_{in3} \cos(2\pi) = 0$
  $-\sqrt{3} + 3 V_{in3} = 0 \implies V_{in3} = \sqrt{3}/3 \approx \mathbf{0.577}$.

(b) Evaluate $v(x)$ at $x = 2\pi/3$:
- $v(2\pi/3) = 2 \cos(2\pi/3) + (\sqrt{3}/3) \sin(2\pi)$
- $v(2\pi/3) = 2(-1/2) + 0 = \mathbf{-1.000}$.

<img src="/practice_18_1_plot.svg" class="h-50 mx-auto p-4" alt="Practice 18.1 Plot" />

---

## Fourier Series

- A function $f(t)$ is **periodic** if there exists a positive constant $T$ such that:
  $$f(t) = f(t + T)$$
  for all $t$. The smallest such value of $T$ is the **period**.

- For a periodic function to have a valid Fourier series expansion, it must satisfy the **Dirichlet conditions**:
  1. $f(t)$ must be **single-valued** everywhere.
  2. $f(t)$ must have a **finite number of finite discontinuities** in any one period.
  3. $f(t)$ must have a **finite number of maxima and minima** in any one period.
  4. $f(t)$ must be **absolutely integrable** over a period: $\int_0^T |f(t)| dt < \infty$.

---

- If these are satisfied, $f(t)$ can be expressed as:
  $$f(t) = a_0 + \sum_{n=1}^{\infty} \left(a_n \cos(n\omega_0 t) + b_n \sin(n\omega_0 t)\right)$$

where $a_0$ is the **average value** (DC component) of $f(t)$ and **$\omega_0 = 2\pi/T$**. The coefficients are calculated as:

$$a_0 = \frac{1}{T} \int_{0}^{T} f(t) \, dt$$
$$a_n = \frac{2}{T} \int_{0}^{T} f(t) \cos(n\omega_0 t) \, dt$$
$$b_n = \frac{2}{T} \int_{0}^{T} f(t) \sin(n\omega_0 t) \, dt$$

---

## Derivation of $a_0$

- To find $a_0$, integrate $f(t)$ over one period:
  $$\int_{0}^{T} f(t) \, dt = \int_{0}^{T} \left[ a_0 + \sum_{n=1}^{\infty} (a_n \cos n\omega_0 t + b_n \sin n\omega_0 t) \right] dt$$
- Integration is a linear operator:
  $$\int_{0}^{T} f(t) \, dt = \int_{0}^{T} a_0 \, dt + \sum_{n=1}^{\infty} a_n \int_{0}^{T} \cos n\omega_0 t \, dt + \sum_{n=1}^{\infty} b_n \int_{0}^{T} \sin n\omega_0 t \, dt$$
- Since $\int_{0}^{T} \cos n\omega_0 t \, dt = 0$ and $\int_{0}^{T} \sin n\omega_0 t \, dt = 0$ for $n \ge 1$:
  $$\int_{0}^{T} f(t) \, dt = a_0 T \implies \mathbf{a_0 = \frac{1}{T} \int_{0}^{T} f(t) \, dt}$$

---

## Derivation of $a_n$

- Multiply $f(t)$ by $\cos k\omega_0 t$ and integrate over one period:
<div class="text-sm">

  $$\int_{0}^{T} f(t) \cos k\omega_0 t \, dt = \int_{0}^{T} a_0 \cos k\omega_0 t \, dt + \sum_{n=1}^{\infty} a_n \int_{0}^{T} \cos n\omega_0 t \cos k\omega_0 t \, dt + \sum_{n=1}^{\infty} b_n \int_{0}^{T} \sin n\omega_0 t \cos k\omega_0 t \, dt$$
</div>

- **Using Orthogonality**:
  1. $\int_{0}^{T} a_0 \cos k\omega_0 t \, dt = 0$
  2. $\int_{0}^{T} \cos n\omega_0 t \cos k\omega_0 t \, dt = 0 \text{ (if } n \neq k)$
  3. $\int_{0}^{T} \sin n\omega_0 t \cos k\omega_0 t \, dt = 0$

- Only the $n=k$ term survives:
  $$\int_{0}^{T} f(t) \cos n\omega_0 t \, dt = a_n \left(\frac{T}{2}\right) \implies \mathbf{a_n = \frac{2}{T} \int_{0}^{T} f(t) \cos n\omega_0 t \, dt}$$

---

## Recall: Orthogonality

<div class="grid grid-cols-3 gap-2 mt-4 text-xs font-serif">
<div class="text-center border border-gray-100 dark:border-gray-800 p-2 rounded">

$$\int_{0}^{T} \cos(k\omega_0 t) \, dt = 0$$
<img src="/ortho_cos.svg" class="h-40 mx-auto" alt="Orthogonality 1" />
</div>
<div class="text-center border border-gray-100 dark:border-gray-800 p-2 rounded">

$$\int_{0}^{T} \cos(n\omega_0 t) \cos(k\omega_0 t) \, dt = 0$$
<img src="/ortho_cos_cos.svg" class="h-40 mx-auto" alt="Orthogonality 2" />

<span>(if $n \neq k$)</span>
</div>
<div class="text-center border border-gray-100 dark:border-gray-800 p-2 rounded">

$$\int_{0}^{T} \sin(n\omega_0 t) \cos(k\omega_0 t) \, dt = 0$$
<img src="/ortho_sin_cos.svg" class="h-40 mx-auto" alt="Orthogonality 3" />
</div>
</div>

---

## Derivation of $b_n$

- Multiply $f(t)$ by $\sin k\omega_0 t$ and integrate over one period:
<div class="text-sm">

  $$\int_{0}^{T} f(t) \sin k\omega_0 t \, dt = \int_{0}^{T} a_0 \sin k\omega_0 t \, dt + \sum_{n=1}^{\infty} a_n \int_{0}^{T} \cos n\omega_0 t \sin k\omega_0 t \, dt + \sum_{n=1}^{\infty} b_n \int_{0}^{T} \sin n\omega_0 t \sin k\omega_0 t \, dt$$

</div>

- **Using Orthogonality**:
  1. $\int_{0}^{T} a_0 \sin k\omega_0 t \, dt = 0$
  2. $\int_{0}^{T} \sin n\omega_0 t \sin k\omega_0 t \, dt = 0 \text{ (if } n \neq k)$
  3. $\int_{0}^{T} \cos n\omega_0 t \sin k\omega_0 t \, dt = 0$

- Only the $n=k$ term survives:
  $$\int_{0}^{T} f(t) \sin n\omega_0 t \, dt = b_n \left(\frac{T}{2}\right) \implies \mathbf{b_n = \frac{2}{T} \int_{0}^{T} f(t) \sin n\omega_0 t \, dt}$$

---

## Some Useful Trigonometric Integrals

- Let both $n$ and $k$ represent any element of the set of integers 1, 2, 3, ...
- Integration limits are typically from $0$ to $T$.

---

## Evaluation of Fourier Coefficients

- Every term in the summation is of the form of trigonometric integrals.
- Coefficients $a_n$ and $b_n$ are determined by integrating $f(t)$ multiplied by $\cos(n\omega_0 t)$ and $\sin(n\omega_0 t)$ respectively.

---

## Example 18.1 / 17.1

Calculate the Fourier series for the waveform shown in the referenced figure.

## Example 18.1

**Problem**: Determine the Fourier series for the "half-sine" wave (rectified sine wave is a common example). Let's assume it's the waveform from standard texts: a periodic train of pulses.

**Derivation**:
1.  **Identify Period**: $T$. Angular freq $\omega_0 = 2\pi/T$.
2.  **Symmetry**: Is it even? Odd?
    - If even ($f(t)=f(-t)$): $b_n = 0$.
    - If odd ($f(t)=-f(-t)$): $a_n = 0$.
3.  **Calculate $a_0$**: $\frac{1}{T} \int_0^T f(t) dt$ (Average value).
4.  **Calculate $a_n$**: $\frac{2}{T} \int_0^T f(t) \cos(n\omega_0 t) dt$.
5.  **Calculate $b_n$**: $\frac{2}{T} \int_0^T f(t) \sin(n\omega_0 t) dt$.

*(Refer to specific waveform graph for precise limits)*

---

## Line and Phase Spectra

- We depicted the function $v(t)$ of Example 18.1 graphically and analytically.
- Both representations are in the time domain.
- The **line spectrum** (or amplitude spectrum) and **phase spectrum** show the amplitudes and phases of the harmonic components vs. frequency.

---

## 18.2 The Use of Symmetry

### Even and Odd Symmetry

- $f(t)$ possesses the property of **even symmetry** if $f(t) = f(-t)$.
- $f(t)$ possesses the property of **odd symmetry** if $f(t) = -f(-t)$.

---

## Symmetry and Fourier Series Terms

### Even Symmetry
- The Fourier series of any even function is composed of only a constant and cosine functions.
- All sine coefficients ($b_n$) are zero.

### Odd Symmetry
- A function having odd symmetry can contain no constant term or cosine terms in its Fourier expansion.
- All cosine coefficients ($a_n$) and the DC term ($a_0$) are zero.

---

## Half-Wave Symmetry

- $f(t)$ possesses half-wave symmetry if $f(t) = -f(t - T/2)$.
- The Fourier series of a function with half-wave symmetry contains only odd harmonics.
- Coefficients $a_n$ and $b_n$ are zero for even $n$.

---

## 18.3 Complete Response to Periodic Forcing Function

- Through the use of the Fourier series, we may now express an arbitrary periodic forcing function as the sum of an infinite number of sinusoidal forcing functions.
- The forced response to each of these functions may be determined by conventional steady-state analysis.
- The complete response is then obtained as the sum of the forced and natural responses.

---

## Practice 18.6

Use the methods of Chap. 8 to determine the value of the current sketched in Fig. 18.9 at $t$ equal to:

(a) $\pi/2$
(b) $\pi$
(c) $3\pi/2$

**Answers**:
- (a) 2.392 A
- (b) 0.1034 A
- (c) 2.396 A
