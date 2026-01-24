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
<img src="/example_18_1_harmonics.svg" class="h-120 mx-auto p-2" alt="Harmonics Convergence" />

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
