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

## Evaluation of Fourier Coefficient: $a_0$

- To find $a_0$, integrate $f(t)$ over one period:
  $$\int_{0}^{T} f(t) \, dt = \int_{0}^{T} \left[ a_0 + \sum_{n=1}^{\infty} (a_n \cos n\omega_0 t + b_n \sin n\omega_0 t) \right] dt$$
- Integration is a linear operator:
  $$\int_{0}^{T} f(t) \, dt = \int_{0}^{T} a_0 \, dt + \sum_{n=1}^{\infty} a_n \int_{0}^{T} \cos n\omega_0 t \, dt + \sum_{n=1}^{\infty} b_n \int_{0}^{T} \sin n\omega_0 t \, dt$$
- Since $\int_{0}^{T} \cos n\omega_0 t \, dt = 0$ and $\int_{0}^{T} \sin n\omega_0 t \, dt = 0$ for $n \ge 1$:
  $$\int_{0}^{T} f(t) \, dt = a_0 T \implies \mathbf{a_0 = \frac{1}{T} \int_{0}^{T} f(t) \, dt}$$

---

## Evaluation of Fourier Coefficient: $a_n$

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

## Evaluation of Fourier Coefficient: $b_n$

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

## Recall: Orthogonality

Zero-Integral Terms:

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

## Orthogonality: Surviving Terms ($n=k$)

<div class="grid grid-cols-2 gap-4 mt-2 text-xs font-serif">
<div class="text-center border border-gray-100 dark:border-gray-800 p-2 rounded shadow-sm">

$$\int_{0}^{T} \cos^2(n\omega_0 t) \, dt = \frac{T}{2}$$
<img src="/ortho_cos_sq.svg" class="h-48 mx-auto" alt="Survival Term 1" />
</div>
<div class="text-center border border-gray-100 dark:border-gray-800 p-2 rounded shadow-sm">

$$\int_{0}^{T} \sin^2(n\omega_0 t) \, dt = \frac{T}{2}$$
<img src="/ortho_sin_sq.svg" class="h-48 mx-auto" alt="Survival Term 2" />
</div>
</div>

<div class="mt-6 text-sm bg-blue-50 dark:bg-blue-900/20 px-4 rounded border-l-4 border-blue-500 shadow-sm">
  <p class="font-bold mb-1 text-blue-700 dark:text-blue-300">Why is this useful?</p>
  
  <span class="text-gray-700 dark:text-gray-300">Orthogonality acts as a <strong>mathematical sieve</strong>. When we integrate the product of $f(t)$ and a specific harmonic, the "Zero-Integral" property kills off every term <em>except</em> the one matching that frequency. These surviving terms then allow us to solve for $a_n$ and $b_n$ directly.
  </span>
</div>

---

## Example 18.1

**Problem**: Determine the Fourier series for the "half-sine" wave (rectified sine wave is a common example). Let's assume it's the waveform from standard texts: a periodic train of pulses.

<img src="/example_18_1_half_wave.svg" class="h-60 mx-auto p-4" alt="Example 18.1 Half Wave" />

---

**Solution**:



1.  **Define Regions** for one period ($0 \le \omega_0 t \le 2\pi$):
    -   $0 \to \pi/2$: $v(t) = V_m \cos(\omega_0 t)$
    -   $\pi/2 \to 3\pi/2$: $v(t) = 0$
    -   $3\pi/2 \to 2\pi$: $v(t) = V_m \cos(\omega_0 t)$
2.  **Calculate $a_0$**:
    $$a_0 = \frac{1}{2\pi} \left[ \int_0^{\pi/2} V_m \cos x \, dx + \int_{3\pi/2}^{2\pi} V_m \cos x \, dx \right] = \frac{V_m}{2\pi}[1 - (-1)] = \frac{V_m}{\pi}$$
---

3.  **Calculate $a_n$**:
    -   Use the trigonometric identity: $\cos A \cos B = \frac{1}{2} [\cos(A+B) + \cos(A-B)]$.
    -   Apply to the integrand ($A=x, B=nx$):
        $$\cos x \cos nx = \frac{1}{2} [\cos((1+n)x) + \cos((1-n)x)]$$
    -   **Integral 1** ($0 \to \pi/2$):
        $$ \int_0^{\pi/2} \frac{V_m}{2} [\cos(1+n)x + \cos(1-n)x] \, dx $$
        $$ = \frac{V_m}{2} \left[ \frac{\sin(1+n)x}{1+n} + \frac{\sin(1-n)x}{1-n} \right]_0^{\pi/2} $$
        At $x=\pi/2$, $\sin((1\pm n)\pi/2) = \cos(n\pi/2)$.
        $$ = \frac{V_m}{2} \cos\left(\frac{n\pi}{2}\right) \left[ \frac{1}{1+n} + \frac{1}{1-n} \right] = \frac{V_m \cos(n\pi/2)}{1-n^2} $$
  
---

  -   **Integral 2** ($3\pi/2 \to 2\pi$):
        Similar logic yields the same result for even $n$ (and 0 for odd $n$).
  -   **Combine**:
        $$ a_n = \frac{1}{\pi} \left[ \frac{V_m \cos(n\pi/2)}{1-n^2} + \frac{V_m \cos(n\pi/2)}{1-n^2} \right] = \frac{2 V_m}{\pi(1-n^2)} \cos\left(\frac{n\pi}{2}\right) $$
4.  **Calculate $b_n$**:
    $$b_n = \frac{1}{\pi} \left[ \int_0^{\pi/2} V_m \cos x \sin nx \, dx + \int_{3\pi/2}^{2\pi} V_m \cos x \sin nx \, dx \right]$$
    -   Evaluating these integrals yields $b_n = 0$ for all $n$.

**Result**: Same as above. $v(t) = \frac{V_m}{\pi} + \frac{V_m}{2} \cos(\omega_0 t) + \frac{2V_m}{3\pi} \cos(2\omega_0 t) - \frac{2V_m}{15\pi} \cos(4\omega_0 t) + \dots$

---

### Fourier Series Convergence
<img src="/example_18_1_harmonics.svg" class="h-110 mx-auto p-2" alt="Harmonics Convergence" />

---

## Practice 18.2

**Problem**:
A periodic waveform $f(t)$ is described as follows:
- $f(t) = -4$, $0 < t < 0.3$
- $f(t) = 6$, $0.3 < t < 0.4$
- $f(t) = 0$, $0.4 < t < 0.5$
- $T = 0.5$

**Evaluate**:
\(a\) $a_0$
\(b\) $a_3$
\(c\) $b_1$

**Answers**:
- \(a\) **-1.2**
- \(b\) **1.383**
- \(c\) **-4.439**

---

**Solution 18.2**:

<img src="/practice_18_2_waveform.svg" class="h-40 mx-auto p-2" alt="Practice 18.2 Waveform" />


1.  **$a_0$**: $\frac{1}{0.5} [(-4)(0.3) + (6)(0.1)] = 2[-1.2 + 0.6] = \mathbf{-1.2}$

2.  **$a_n$**: $\omega_0 = \frac{2\pi}{0.5} = 4\pi$.
    $$ a_n = 4 \left[ \int_0^{0.3} -4 \cos(4n\pi t) dt + \int_{0.3}^{0.4} 6 \cos(4n\pi t) dt \right] $$
    $$ = \frac{1}{n\pi} [6\sin(1.6n\pi) - 10\sin(1.2n\pi)] $$
    For $n=3$: $a_3 = \frac{1}{3\pi} [6\sin(4.8\pi) - 10\sin(3.6\pi)] \approx \mathbf{1.383}$
---

3.  **$b_n$**:
    $$ b_n = 4 \left[ \int_0^{0.3} -4 \sin(4n\pi t) dt + \int_{0.3}^{0.4} 6 \sin(4n\pi t) dt \right] $$
    $$ = \frac{1}{n\pi} [10\cos(1.2n\pi) - 6\cos(1.6n\pi) - 4] $$
    For $n=1$: $b_1 = \frac{1}{\pi} [10\cos(1.2\pi) - 6\cos(1.6\pi) - 4] \approx \mathbf{-4.439}$

---
layout: two-cols
---

## Practice 18.3

**Problem**:
Write the Fourier series for the three voltage waveforms shown in Fig. 18.4.

:: right ::

<img src="/practice_18_3_waveforms.svg" class="h-120 mx-auto p-2" alt="Practice 18.3 Waveforms" />

---

**Solution 18.3 (a)**:

(a) **Square Wave** ($T=2, \omega_0=\pi$):
- **$a_0$**: $\frac{1}{2} [\int_0^1 (1) dt + \int_1^2 (-1) dt] = \frac{1}{2} [1 - 1] = 0$.
- **$a_n$**: $\frac{2}{2} [\int_0^1 \cos(n\pi t) dt - \int_1^2 \cos(n\pi t) dt] = \frac{1}{n\pi}[\sin(n\pi)]_0^1 - \frac{1}{n\pi}[\sin(n\pi)]_1^2 = 0$.
- **$b_n$**: $\int_0^1 \sin(n\pi t) dt - \int_1^2 \sin(n\pi t) dt = \frac{1}{n\pi}[-\cos(n\pi t)]_0^1 - \frac{1}{n\pi}[-\cos(n\pi t)]_1^2 = \frac{2}{n\pi}(1 - \cos(n\pi))$.
  - For even $n$, $b_n=0$. For odd $n$, $b_n = \frac{4}{n\pi}$.

$$ v(t) = \sum_{n=1,3,5,\dots}^{\infty} \frac{4}{n\pi} \sin(n\pi t) $$

---

**Solution 18.3 (b)**:

(b) **Even Square Wave** ($T=2, \omega_0=\pi$):
- **$a_0$**: $\frac{1}{2} [\int_{-0.5}^{0.5} (1) dt + \int_{0.5}^{1.5} (-1) dt] = 0$.
- **$a_n$**: $\int_{-0.5}^{0.5} \cos(n\pi t) dt - \int_{0.5}^{1.5} \cos(n\pi t) dt = \frac{2}{n\pi} \sin(0.5n\pi) - \frac{1}{n\pi}[\sin(1.5n\pi) - \sin(0.5n\pi)] = \frac{4}{n\pi} \sin(n\pi/2)$.
- **$b_n$**: $\int_{-0.5}^{0.5} \sin(n\pi t) dt - \dots = 0$ (integrand is odd over symmetric limits).

$$ v(t) = \sum_{n=1,3,5,\dots}^{\infty} \frac{4}{n\pi} \sin\left(\frac{n\pi}{2}\right) \cos(n\pi t) $$

---

**Solution 18.3 \(c\)**:

\(c\) **Triangle Wave** ($T=2, \omega_0=\pi$):
Define $v(t)$: $2t$ ($0<t<0.5$), $2-2t$ ($0.5<t<1.5$), $2t-4$ ($1.5<t<2$).
- **$a_0$**: Average value is clearly 0 by inspection of area.
- **$a_n$**: $\int_0^2 v(t) \cos(n\pi t) dt$. Integration by parts ($u=t, dv=\cos$) leads to cancellation for specific limits or zero.
- **$b_n$**: $\int_0^{0.5} 2t \sin(n\pi t) dt + \int_{0.5}^{1.5} (2-2t) \sin(n\pi t) dt + \int_{1.5}^2 (2t-4) \sin(n\pi t) dt$.
  - Using $\int t \sin(kt) dt = \frac{\sin(kt)}{k^2} - \frac{t \cos(kt)}{k}$, sum contributions.
  - Result: $b_n = \frac{8}{n^2\pi^2} \sin(n\pi/2)$.

$$ v(t) = \sum_{n=1,3,5,\dots}^{\infty} \frac{8}{n^2\pi^2} \sin\left(\frac{n\pi}{2}\right) \sin(n\pi t) $$



---
layout: two-cols-header
---

## Line and Phase Spectra

:: left ::

- We depicted the function $v(t)$ of Example 18.1 graphically and analytically.
- Both representations are in the time domain.
- The **line spectrum** (or amplitude spectrum) and **phase spectrum** show the amplitudes and phases of the harmonic components vs. frequency.

  - $a_0 = \frac{V_m}{\pi} \approx 0.318 V_m$
  - $a_1 = \frac{V_m}{2} = 0.5 V_m$
  - $a_2 = \frac{2V_m}{3\pi} \approx 0.212 V_m$
  - $a_4 = -\frac{2V_m}{15\pi} \approx -0.042 V_m$
  - $a_6 = \frac{2V_m}{35\pi} \approx 0.018 V_m$
  - $a_8 = -\frac{2V_m}{63\pi} \approx -0.010 V_m$
  - $a_{10} = \frac{2V_m}{99\pi} \approx 0.006 V_m$

:: right ::

<img src="/example_18_1_spectrum.svg" class="h-100 mx-auto p-2" alt="Example 18.1 Spectrum" />


---

## 18.2 The Use of Symmetry

### Even and Odd Symmetry

- $f(t)$ possesses the property of **even symmetry** if $f(t) = f(-t)$.
- $f(t)$ possesses the property of **odd symmetry** if $f(t) = -f(-t)$.

<div class="grid grid-cols-2 gap-4 mt-10">
  <div class="text-center">

<p class="text-sm font-bold mb-2">

(a) Cosine-like with small dip at $t=0$</p>

<img src="/even_sym_cosine_dip.svg" class="h-60 mx-auto" alt="Even symmetry cosine dip" />
  </div>
  <div class="text-center">

<p class="text-sm font-bold mb-2">

(b) Odd sym. clipped sawtooth wave</p>

<img src="/odd_sym_clipped_sawtooth.svg" class="h-60 mx-auto" alt="Odd symmetry clipped sawtooth" />
  </div>

</div>

---

## Products of Symmetric Functions

The product of two symmetric functions follows rules similar to those for multiplying even and odd numbers:
- **Even $\times$ Even = Even**
- **Odd $\times$ Odd = Even**
- **Even $\times$ Odd = Odd**

### Integral Properties over Symmetric Intervals $[-a, a]$:

- If $f(t)$ is **even**: $\int_{-a}^{a} f(t) \, dt = 2 \int_{0}^{a} f(t) \, dt$
- If $f(t)$ is **odd**: $\int_{-a}^{a} f(t) \, dt = 0$

<div class="text-center mt-6">
  <img src="/integration_properties.svg" class="h-50 mx-auto" alt="Integration properties of symmetric functions" />
</div>


---

## Symmetry and Fourier Series Terms

### Even Symmetry
- If $f(t)$ is **even**, $f(t) \cdot \cos(n\omega_0 t)$ is **even** and $f(t) \cdot \sin(n\omega_0 t)$ is **odd**.
- **Proof for $b_n = 0$**:
  $$b_n = \frac{2}{T} \int_{-T/2}^{T/2} \text{even} \cdot \text{odd} \, dt = \frac{2}{T} \int_{-T/2}^{T/2} \text{odd} \, dt = 0$$
- **Simplified Formulas**:
  $$\mathbf{a_0 = \frac{2}{T} \int_{0}^{T/2} f(t) \, dt}, \quad \mathbf{a_n = \frac{4}{T} \int_{0}^{T/2} f(t) \cos(n\omega_0 t) \, dt}$$

---

### Odd Symmetry
- If $f(t)$ is **odd**, $f(t) \cdot \cos(n\omega_0 t)$ is **odd** and $f(t) \cdot \sin(n\omega_0 t)$ is **even**.
- **Proof for $a_n = 0$**:
  $$a_n = \frac{2}{T} \int_{-T/2}^{T/2} \text{odd} \cdot \text{even} \, dt = \frac{2}{T} \int_{-T/2}^{T/2} \text{odd} \, dt = 0$$
- **DC Term**: $a_0 = 0$ (Average of an odd function over a period is zero).
- **Simplified Formula**:
  $$\mathbf{b_n = \frac{4}{T} \int_{0}^{T/2} f(t) \sin(n\omega_0 t) \, dt}$$

---

## Half-Wave Symmetry

- $f(t)$ possesses half-wave symmetry if $f(t) = -f(t - T/2)$.
- The Fourier series of a function with half-wave symmetry contains only odd harmonics.
- Coefficients $a_n$ and $b_n$ are zero for even $n$.

<div class="grid grid-cols-2 gap-4 mt-6">
  <div class="text-center">
    <p class="text-sm font-bold mb-2">(a) HWS Even symmetry</p>
    <img src="/hws_even_cosine.svg" class="h-60 mx-auto" alt="HWS Even symmetry" />
  </div>
  <div class="text-center">
    <p class="text-sm font-bold mb-2">(b) HWS Odd symmetry</p>
    <img src="/hws_odd_clipped.svg" class="h-60 mx-auto" alt="HWS Odd symmetry" />
  </div>
</div>

---

## Proof: Half-Wave Symmetry

For HWS functions, we can show that $a_n, b_n = 0$ for even $n$ by splitting the integral:
$$a_n = \frac{2}{T} \left[ \int_{0}^{T/2} f(t) \cos(n\omega_0 t) \, dt + \int_{T/2}^{T} f(t) \cos(n\omega_0 t) \, dt \right]$$

In the second integral, let $t = x + T/2$. Since $f(x + T/2) = -f(x)$ & $\omega_0 T/2 = \pi$:
$$\int_{T/2}^{T} f(t) \cos(n\omega_0 t) \, dt = \int_{0}^{T/2} -f(x) \underbrace{\cos(n\omega_0 x + n\pi)}_{(-1)^n \cos(n\omega_0 x)} \, dx = -(-1)^n \int_{0}^{T/2} f(t) \cos(n\omega_0 t) \, dt$$

---

### Resulting Formulas for HWS:
$$a_n = \frac{2}{T} [1 - (-1)^n] \int_{0}^{T/2} f(t) \cos(n\omega_0 t) \, dt, \quad b_n = \frac{2}{T} [1 - (-1)^n] \int_{0}^{T/2} f(t) \sin(n\omega_0 t) \, dt$$

- If $n$ is **even**: $1 - (-1)^n = 0 \implies \mathbf{a_n = 0, \ b_n = 0, \ a_0 = 0}$
- If $n$ is **odd**: $1 - (-1)^n = 2 \implies$
  $$\mathbf{a_n = \frac{4}{T} \int_{0}^{T/2} f(t) \cos(n\omega_0 t) \, dt}, \quad \mathbf{b_n = \frac{4}{T} \int_{0}^{T/2} f(t) \sin(n\omega_0 t) \, dt}$$

> [!NOTE]
> Half-wave symmetry always implies the absence of all even harmonics (including the DC term).


---

## Combined Symmetry

If a function possesses both **Even/Odd** symmetry **and** **Half-Wave Symmetry**, the integration range is further reduced to $T/4$:

### Even + Half-Wave Symmetry
- $f(t)$ is even ($b_n=0$) and HWS ($a_n, b_n=0$ for even $n$).
- Result: Only odd-harmonic cosine terms $a_{1,3,5,...}$ exist.
- Formula: 

$$\mathbf{a_n = \frac{8}{T} \int_{0}^{T/4} f(t) \cos(n\omega_0 t) \, dt}$$

---

### Odd + Half-Wave Symmetry
- $f(t)$ is odd ($a_n, a_0=0$) and HWS ($a_n, b_n=0$ for even $n$).
- Result: Only odd-harmonic sine terms $b_{1,3,5,...}$ exist.
- Formula: 

$$\mathbf{b_n = \frac{8}{T} \int_{0}^{T/4} f(t) \sin(n\omega_0 t) \, dt}$$


---

## Summary of Symmetry-based Simplified Formulas

| Symmetry Type | Characteristic | Simplified Formulas |
| :--- | :--- | :--- |
| **Even** | $f(t) = f(-t)$ | $b_n = 0$<br>$a_0, a_n = \frac{4}{T}\int_{0}^{T/2}...$ |
| **Odd** | $f(t) = -f(-t)$ | $a_0, a_n = 0$<br>$b_n = \frac{4}{T}\int_{0}^{T/2}...$ |
| **Half-Wave** | $f(t) = -f(t - T/2)$ | $a_{ev}, b_{ev} = 0$<br>$a_{odd}, b_{odd} = \frac{4}{T}\int_{0}^{T/2}...$ |
| **Even + HWS** | Even & HWS | $b_n=0, a_{ev}=0, a_0=0$<br>$a_{odd} = \frac{8}{T}\int_{0}^{T/4}...$ |
| **Odd + HWS** | Odd & HWS | $a_n=0, b_{ev}=0, a_0=0$<br>$b_{odd} = \frac{8}{T}\int_{0}^{T/4}...$ |


---

## Practice 18.4

Sketch each of the functions described; state whether or not even symmetry, odd symmetry, and half-wave symmetry are present; and give the period:

(a) $v = 0, -2 < t < 0$ and $2 < t < 4$; $v = 5, 0 < t < 2$; $v = -5, 4 < t < 6$; repeats.
(b) $v = 10, 1 < t < 3$; $v = 0, 3 < t < 7$; $v = -10, 7 < t < 9$; repeats.
\(c\) $v = 8t, -1 < t < 1$; $v = 0, 1 < t < 3$; repeats.

---

## Solution 18.4

<div class="grid grid-cols-3 gap-2 mb-4">
  <img src="/practice_18_4_a.svg" class="h-30 mx-auto" />
  <img src="/practice_18_4_b.svg" class="h-30 mx-auto" />
  <img src="/practice_18_4_c.svg" class="h-30 mx-auto" />
</div>

| Case | Even | Odd | HWS | Period ($T$) |
| :---: | :---: | :---: | :---: | :---: |
| **(a)** | No | No | Yes | 8 |
| **(b)** | No | No | No | 8 |
| **\(c\)** | No | Yes | No | 4 |

**Key Observations:**
- (a) $f(t) = -f(t-4)$, so HWS is present.
- \(c\) $f(t) = -f(-t)$ for all $t$, so Odd symmetry is present.

---

## Practice 18.5

Determine the Fourier series for the waveforms of Practice Problem 18.4a and b.

---

## Solution 18.5(a) Detail

**Waveform (a):** $v=5$ (~$0 < t < 2$), $T=8$, $\omega_0 = \pi/4$, HWS confirmed.

**1. Calculate $a_n$:**
$$a_n = \frac{4}{T}\int_0^{T/2} f(t)\cos(n\omega_0 t)dt = \frac{4}{8}\int_0^2 5\cos\Big(\frac{n\pi t}{4}\Big)dt$$
$$a_n = \frac{5}{2} \cdot \frac{4}{n\pi} \Big[ \sin\Big(\frac{n\pi t}{4}\Big) \Big]_0^2 = \frac{10}{n\pi} \sin\Big(\frac{n\pi}{2}\Big)$$

**2. Calculate $b_n$:**
$$b_n = \frac{4}{T}\int_0^{T/2} f(t)\sin(n\omega_0 t)dt = \frac{4}{8}\int_0^2 5\sin\Big(\frac{n\pi t}{4}\Big)dt$$
$$b_n = \frac{5}{2} \cdot \frac{4}{n\pi} \Big[ -\cos\Big(\frac{n\pi t}{4}\Big) \Big]_0^2 = \frac{10}{n\pi} \Big[ 1 - \cos\Big(\frac{n\pi}{2}\Big) \Big]$$

---

**Resulting Fourier Series ($n$ odd):**
Since $\cos(n\pi/2) = 0$ for all odd $n$:
$$v(t) = \sum_{n=1,3,...}^{\infty} \frac{10}{n\pi} \left[ \sin\Big(\frac{n\pi}{2}\Big)\cos\Big(\frac{n\pi t}{4}\Big) + \sin\Big(\frac{n\pi t}{4}\Big) \right]$$

---

## Solution 18.5(b) Detail

**Waveform (b):** $v=10$ ($1 < t < 3$), $v=-10$ ($7 < t < 9$), $T=8$, $\omega_0 = \pi/4$.

**1. Calculate $a_n$:**
$$a_n = \frac{2}{8} \int_1^9 f(t) \cos(n\omega_0 t)dt = \frac{1}{4} \Big[ \int_1^3 10 \cos\frac{n\pi t}{4} dt + \int_7^9 -10 \cos\frac{n\pi t}{4} dt \Big]$$
$$a_n = \frac{10}{n\pi} \Big[ \sin\frac{3n\pi}{4} - \sin\frac{n\pi}{4} - \underbrace{\sin\frac{9n\pi}{4}}_{\sin(n\pi/4)} + \underbrace{\sin\frac{7n\pi}{4}}_{-\sin(n\pi/4)} \Big] = \frac{10}{n\pi} \Big[ \sin\frac{3n\pi}{4} - 3\sin\frac{n\pi}{4} \Big]$$

**2. Calculate $b_n$:**
$$b_n = \frac{10}{n\pi} \Big[ \Big(-\cos\frac{3n\pi}{4} + \cos\frac{n\pi}{4}\Big) - \Big(-\cos\frac{9n\pi}{4} + \cos\frac{7n\pi}{4}\Big) \Big]$$
$$b_n = \frac{10}{n\pi} \Big[ \cos\frac{n\pi}{4} - \cos\frac{3n\pi}{4} + \underbrace{\cos\frac{n\pi}{4}}_{\cos(9n\pi/4)} - \underbrace{\cos\frac{n\pi}{4}}_{\cos(7n\pi/4)} \Big] = \frac{10}{n\pi} \Big[ \cos\frac{n\pi}{4} - \cos\frac{3n\pi}{4} \Big]$$

---

**Resulting Fourier Series:**
$$v(t) = \sum_{n=1}^{\infty} \frac{10}{n\pi} \left[ \left(\sin\frac{3n\pi}{4} - 3\sin\frac{n\pi}{4}\right) \cos\frac{n\pi t}{4} + \left(\cos\frac{n\pi}{4} - \cos\frac{3n\pi}{4}\right) \sin\frac{n\pi t}{4} \right]$$

---

## 18.3 Complete Response to Periodic Forcing Function


- Through the use of the Fourier series, we may now express an arbitrary periodic forcing function as the sum of an infinite number of sinusoidal forcing functions.
- The forced response to each of these functions may be determined by conventional steady-state analysis.
- The complete response is then obtained as the sum of the forced and natural responses.



---

## Example 18.2

For the circuit shown, determine the periodic response $i(t)$ corresponding to the forcing function $v_s(t)$ if $i(0) = 0$.

<div class="grid grid-cols-2 gap-4">


<div>
<img src="/rl_circuit_switch.svg" class="w-full h-40" />

<span class="text-xs mt-2">Series circuit with $L=2$H, $R=4\Omega$, and a switch closing at $t=0$.</span>
</div>

<div>
<img src="/pulse_train_vs.svg" class="w-full h-40" />

<span class="text-xs mt-2">Positive pulse train with magnitude 10 and period $T = \pi$.</span>
</div>

</div>

---

## Transformation: $j\omega$ to Time Domain (Revisited Chapter 10.4)

The transition from the frequency ($j\omega$) domain back to the time ($t$) domain is a critical step in finalizing circuit analysis.

### Case 1: Individual Harmonics (Phasors)
A frequency-domain response phasor $\mathbf{I}_n = I_m \angle \theta_n$ at frequency $\omega_n = n\omega_0$ is transformed using:
$$i_n(t) = \text{Re}\{ \mathbf{I}_n e^{j n \omega_0 t} \} = I_m \cos(n\omega_0 t + \theta_n)$$

### Case 2: Complete Fourier Series
The total time-domain response is the sum of the DC component and all individual harmonics:
$$i(t) = I_{dc} + \sum_{n=1}^{\infty} i_n(t)$$

---

### Step-by-Step Procedure:
1.  **Solve** the circuit in the phasor domain for each harmonic frequency $n\omega_0$.
2.  **Multiply** each phasor by $e^{j n \omega_0 t}$.
3.  **Extract** the real part to obtain the time-domain expression for that harmonic.
4.  **Sum** all terms (including $a_0$) to construct the complete response.

---

## Example 18.2: Step 1 - Forcing Function

The forcing function $v_s(t)$ is a positive pulse train with magnitude $V_m=10$ and period $T=\pi$ ($\omega_0 = 2\pi/T = 2\,$rad/s).

**1. Fourier Series of $v_s(t)$:**
By inspection (square wave shifted by $+5$), the series is:
$$v_s(t) = 5 + \sum_{n=1,3,...}^{\infty} \frac{20}{n\pi} \sin(2nt)$$

**2. Harmonic Forcing Function ($n^{th}$ harmonic):**
$$v_{s,n}(t) = \frac{20}{n\pi} \sin(2nt) = \frac{20}{n\pi} \cos(2nt - 90^\circ)$$
**Phasor Domain:**
$$\mathbf{V}_{s,n} = \frac{20}{n\pi} \angle -90^\circ = -j\frac{20}{n\pi}$$

---

## Example 18.2: Step 2 - Forced Response

**1. System Impedance at $\omega = 2n$:**
$$\mathbf{Z}_n = R + j\omega L = 4 + j(2n)(2) = 4 + j4n$$

**2. Forced Response Current (Harmonic Phasor):**
$$\mathbf{I}_{f,n} = \frac{\mathbf{V}_{s,n}}{\mathbf{Z}_n} = \frac{-j20/n\pi}{4 + j4n} = \frac{-j5}{n\pi(1+jn)}$$

**3. Time-Domain Transformation:**
$$\mathbf{I}_{f,n} = \frac{-j5(1-jn)}{n\pi(1+n^2)} = \frac{-5n - j5}{n\pi(1+n^2)}$$
$$i_{f,n}(t) = \text{Re}\{ \mathbf{I}_{f,n} e^{j2nt} \} = \frac{1}{n\pi(1+n^2)} \text{Re}\{ (-5n - j5)(\cos 2nt + j\sin 2nt) \}$$
$$i_{f,n}(t) = \frac{-5n\cos 2nt + 5\sin 2nt}{n\pi(1+n^2)} = \frac{5}{\pi(1+n^2)} \left[ \frac{\sin 2nt}{n} - \cos 2nt \right]$$

---

**4. DC Component ($n=0$):**
$$V_{dc} = 5\,\text{V} \implies I_{dc} = \frac{5}{R} = \frac{5}{4} = 1.25\,\text{A}$$

**5. Total Forced Response:**
$$i_f(t) = 1.25 + \sum_{n=1,3,...}^{\infty} i_{f,n}(t)$$

---

## Example 18.2: Step 3 - Natural Response

**1. Natural Response Form:**
From the circuit's single pole at $s = -R/L = -4/2 = -2$:
$$i_n(t) = Ae^{-2t}$$

**2. Complete Response:**
$$i(t) = i_f(t) + i_n(t) = 1.25 + i_{f,harm}(t) + Ae^{-2t}$$

**3. Initial Condition at $t=0$:**
Since $i(0) = 0$:
$$0 = 1.25 + i_{f,harm}(0) + A$$
Evaluating $i_{f,harm}(0)$ using $n$ terms (exact sum $\approx -1.146$):
$$A \approx -0.104$$

---

## Example 18.2: Final Result

The complete current response for $i(0) = 0$:

$$i(t) = -0.104e^{-2t} + 1.25 + \frac{5}{\pi} \sum_{n=1,3,...}^{\infty} \left[ \frac{\sin(2nt)}{n(1+n^2)} - \frac{\cos(2nt)}{1+n^2} \right] \text{ A}$$

**Key Components:**
- **Transient term:** $-0.104e^{-2t}$ (dies out over time).
- **DC term:** $1.25\,$A.
- **Harmonic summation:** Steady-state periodic response.


---

## Practice 18.6

Use the methods of Chap. 8 to determine the value of the current sketched in Fig. 18.9 at $t$ equal to:

<img src="/example_18_2_current.svg" class="mx-auto h-50" />

(a) $\pi/2$
(b) $\pi$
(c\) $3\pi/2$

**Answers**:
- (a) 2.392 A
- (b) 0.1034 A
- \(c\) 2.396 A

---

## Solution 18.6: Transient Analysis (Ch. 8)

Circuit: $L=2$H, $R=4\Omega \implies \tau = L/R = 0.5$s. $v_s(t)$ switches every $\pi/2 \approx 1.57$s.

**\(a\) Interval $0 \le t \le \pi/2$:** ($V_s = 10$V, $i(0) = 0$)
$$i(t) = \frac{V_s}{R}(1 - e^{-t/\tau}) = 2.5(1 - e^{-2t}) \implies i(\pi/2) = 2.5(1 - e^{-\pi}) \approx \mathbf{2.392\,A}$$

**\(b\) Interval $\pi/2 \le t \le \pi$:** ($V_s = 0$V, $i(\pi/2) = 2.392$A)
$$i(t) = i(\pi/2)e^{-2(t-\pi/2)} \implies i(\pi) = 2.392e^{-\pi} \approx \mathbf{0.1034\,A}$$

**\(c\) Interval $\pi \le t \le 3\pi/2$:** ($V_s = 10$V, $i(\pi) = 0.1034$A)
$$i(t) = 2.5 + (0.1034 - 2.5)e^{-2(t-\pi)} \implies i(3\pi/2) = 2.5 - 2.3966e^{-\pi} \approx \mathbf{2.396\,A}$$

