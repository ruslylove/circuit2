---
theme: seriph
background: https://cover.sli.dev
title: Chapter 18 Part II - Fourier Transforms
info: |
  ## Chapter 18 Part II
  Fourier Circuit Analysis: Complex Series and Transforms
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
layout: cover
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

## Trigonometric to Exponential

Starting with the trigonometric form:
$$f(t) = a_0 + \sum_{n=1}^{\infty} \left[ a_n \cos(n\omega_0 t) + b_n \sin(n\omega_0 t) \right]$$

Using **Euler's Formulas**:
$$\cos(n\omega_0 t) = \frac{e^{jn\omega_0 t} + e^{-jn\omega_0 t}}{2}, \quad \sin(n\omega_0 t) = \frac{e^{jn\omega_0 t} - e^{-jn\omega_0 t}}{2j}$$

Substitute these into the series:

$$f(t) = a_0 + \sum_{n=1}^{\infty} \left[ a_n \left( \frac{e^{jn\omega_0 t} + e^{-jn\omega_0 t}}{2} \right) + b_n \left( \frac{e^{jn\omega_0 t} - e^{-jn\omega_0 t}}{2j} \right) \right]$$


---

## Trigonometric to Exponential (Continued)

Grouping by exponential terms:
$$f(t) = a_0 + \sum_{n=1}^{\infty} \left[ \left( \frac{a_n - jb_n}{2} \right) e^{jn\omega_0 t} + \left( \frac{a_n + jb_n}{2} \right) e^{-jn\omega_0 t} \right]$$

Define the complex coefficients **$c_n$**:
- For $n > 0$: $c_n = \frac{1}{2}(a_n - jb_n)$
- For $n < 0$: $c_n = \frac{1}{2}(a_{-n} + jb_{-n})$
- For $n = 0$: $c_0 = a_0$

This allows us to write the **Complex Fourier Series**:
$$\mathbf{f(t) = \sum_{n=-\infty}^{\infty} c_n e^{jn\omega_0 t}}$$

---

## The Complex Coefficient $c_n$

We can derive a single integral formula for $c_n$:
$$c_n = \frac{1}{2}(a_n - jb_n) = \frac{1}{2} \left[ \frac{2}{T} \int_0^T f(t) \cos(n\omega_0 t) \, dt - j \frac{2}{T} \int_0^T f(t) \sin(n\omega_0 t) \, dt \right]$$

Combine the integrals:
$$c_n = \frac{1}{T} \int_0^T f(t) \left[ \cos(n\omega_0 t) - j \sin(n\omega_0 t) \right] \, dt$$

Using $e^{-jn\omega_0 t} = \cos(n\omega_0 t) - j \sin(n\omega_0 t)$:
$$\mathbf{c_n = \frac{1}{T} \int_{0}^{T} f(t) e^{-jn\omega_0 t} \, dt}$$

---

## Example 18.3

**Problem**: Determine $c_n$ for the square wave shown below. ($T=2, \omega_0 = \pi$).
- Even and Half-wave symmetry.

<img src="/square_wave_p2.svg" class="h-80 mx-auto p-4" alt="Square Wave (Period 2)" />

---

## Example 18.3: Step-by-Step Solution

**Step 1: Define the function**
For $T=2$ ($\omega_0 = \pi$), the waveform $f(t)$ with even symmetry is:
$f(t) = 1$ for $-0.5 < t < 0.5$
$f(t) = -1$ for $0.5 < t < 1.5$ (or $-1.5 < t < -0.5$)

**Step 2: Set up the Complex Coefficient integral**
$$c_n = \frac{1}{T} \int_{-T/2}^{T/2} f(t) e^{-jn\omega_0 t} \, dt = \frac{1}{2} \int_{-0.5}^{1.5} f(t) e^{-jn\pi t} \, dt$$

---

## Example 18.3: Step-by-Step Solution (Cont.)


**Step 3: Evaluate the Integral**
$$c_n = \frac{1}{2} \left[ \int_{-0.5}^{0.5} (1) e^{-jn\pi t} \, dt + \int_{0.5}^{1.5} (-1) e^{-jn\pi t} \, dt \right]$$

$$c_n = \frac{1}{2} \left[ \frac{e^{-jn\pi t}}{-jn\pi} \right]_{-0.5}^{0.5} - \frac{1}{2} \left[ \frac{e^{-jn\pi t}}{-jn\pi} \right]_{0.5}^{1.5}$$

$$c_n = \frac{1}{-j2n\pi} \left[ (e^{-jn\pi/2} - e^{jn\pi/2}) - (e^{-j3n\pi/2} - e^{-jn\pi/2}) \right]$$

---

## Example 18.3: Step-by-Step Solution (Cont.)

Using $e^{-jx} - e^{jx} = -j2 \sin x$:
$$c_n = \frac{1}{-j2n\pi} \left[ -j2\sin(n\pi/2) - (-j2\sin(3n\pi/2)) \right]$$
$$c_n = \frac{1}{n\pi} \left[ \sin(n\pi/2) - \sin(3n\pi/2) \right]$$

Since $\sin(3n\pi/2) = -\sin(n\pi/2)$ for all $n$:
$$\mathbf{c_n = \frac{2}{n\pi} \sin\left(\frac{n\pi}{2}\right)}$$

---

## Example 18.3: Results

- **For $n=0$**: $c_0 = \frac{1}{T} \int f(t) dt = \frac{1}{2} [ (1)(1) + (-1)(1) ] = \mathbf{0}$.
- **For even $n$**: $\sin(n\pi/2) = 0 \implies \mathbf{c_n = 0}$.
- **For odd $n$**:
  - $n=1: c_1 = \frac{2}{\pi} \sin(\pi/2) = \frac{2}{\pi}$
  - $n=3: c_3 = \frac{2}{3\pi} \sin(3\pi/2) = -\frac{2}{3\pi}$
  - $n=5: c_5 = \frac{2}{5\pi} \sin(5\pi/2) = \frac{2}{\pi}$

**Complex Fourier Series**:
$$f(t) = \dots + \frac{-2}{3\pi}e^{-j3\pi t} + \frac{2}{\pi}e^{-j\pi t} + \frac{2}{\pi}e^{j\pi t} + \frac{-2}{3\pi}e^{j3\pi t} + \dots$$

---

## Example 18.4

A function $f(t)$ is a train of rectangular pulses of amplitude $V_0$ and duration $\tau$, recurring periodically every $T$ seconds. Find the exponential Fourier series for $f(t)$.

<img src="/pulse_train_ex18_4.svg" class="h-60 mx-auto p-4" alt="Rectangular Pulse Train" />

---

## Example 18.4: Solution

The fundamental frequency is $f_0 = 1/T$. The complex coefficient $c_n$ is:
$$c_n = \frac{1}{T} \int_{t_0}^{t_0+\tau} V_0 e^{-jn\omega_0 t} \, dt = \frac{V_0}{-jn\omega_0 T} \left[ e^{-jn\omega_0 t} \right]_{t_0}^{t_0+\tau}$$

Evaluating the limits and using $e^{-jx} - e^{jy} = e^{-j(x+y)/2} (-j2\sin((x-y)/2))$:
$$\mathbf{c_n = \frac{V_0 \tau}{T} \frac{\sin(n\omega_0 \tau / 2)}{n\omega_0 \tau / 2} e^{-jn\omega_0(t_0 + \tau/2)}}$$

---

## Example 18.4: Magnitude and Angle

From the complex coefficient formula, we can identify:

- **Magnitude**:
  $$|c_n| = \frac{V_0 \tau}{T} \left| \frac{\sin(n\omega_0 \tau / 2)}{n\omega_0 \tau / 2} \right| = \frac{V_0 \tau}{T} \left| \text{Sa}\left( \frac{n\omega_0 \tau}{2} \right) \right|$$

- **Angle**:
  $$\text{ang } c_n = -n\omega_0 (t_0 + \tau/2) + [0 \text{ or } \pi]$$
  *(The $\pi$ term is added whenever the sampling function is negative)*

---

## Example 18.4: Discrete Spectrums


<img src="/magnitude_spectrum_ex18_4.svg" class="py-2 h-45 mx-auto" />

<span class="text-xs mt-1 block text-center">Magnitude Spectrum: Envelope follows $|Sa(x)|$.</span>



<img src="/phase_spectrum_ex18_4.svg" class="py-2 h-45 mx-auto" />

<span class="text-xs mt-1 block text-center">Phase Spectrum: Linear drift with $\pi$ jumps.</span>


---

## The Sampling Function

The trigonometric factor in the magnitude of $c_n$ is called the **sampling function**:
$$\text{Sa}(x) = \frac{\sin x}{x}$$

- **Magnitude of $c_n$**: $|c_n| = \frac{V_0 \tau}{T} |\text{Sa}(\frac{n\omega_0 \tau}{2})|$
- **Properties**:
  - $\text{Sa}(0) = 1$
  - $\text{Sa}(n\pi) = 0$ for $n = \pm 1, \pm 2, \dots$
  - The envelope of the spectrum is determined by the pulse width $\tau$.

---

## Practice 18.7

Determine the general coefficient $c_n$ in the complex Fourier series for the waveform shown:

<div class="grid grid-cols-2 gap-4">

<div>
<img src="/practice_18_7_a.svg" class="w-full h-40" />
<span class="text-xs mt-1 block text-center">(a) Square wave, $T=2$, $A=1$.</span>
</div>

<div>
<img src="/practice_18_7_b.svg" class="w-full h-40" />
<span class="text-xs mt-1 block text-center">(b) Triangle wave, $T=2$, $A=1$.</span>
</div>

</div>

**Ans**:
- (a) $-j2/(n\pi)$ for $n$ odd, $0$ for $n$ even.
- (b) $-j [4/(n^2 \pi^2)] \sin(n\pi/2)$ for all $n$.

---

## Practice 18.7: Solution (a) Square Wave

**Step 1: Symmetry and Limits**
For the odd square wave ($T=2, \omega_0 = \pi, A=1$):
$f(t) = 1$ for $0 < t < 1$ and $f(t) = -1$ for $-1 < t < 0$.

**Step 2: Integral Setup**
$$c_n = \frac{1}{2} \left[ \int_{-1}^{0} (-1)e^{-jn\pi t} dt + \int_{0}^{1} (1)e^{-jn\pi t} dt \right]$$

**Step 3: Evaluate**
$$c_n = \frac{1}{2} \left[ \frac{e^{-jn\pi t}}{jn\pi} \right]_{-1}^{0} + \frac{1}{2} \left[ \frac{e^{-jn\pi t}}{-jn\pi} \right]_{0}^{1}$$
$$c_n = \frac{1}{j2n\pi} [1 - (-1)^n] - \frac{1}{j2n\pi} [(-1)^n - 1] = \frac{1 - (-1)^n}{jn\pi}$$

- If $n$ is even: $c_n = 0$.
- If $n$ is odd: $c_n = \frac{2}{jn\pi} = \mathbf{-j\frac{2}{n\pi}}$.


---

## Practice 18.7: Solution (b) Triangle Wave (Direct)

**Step 1: Symmetry and Limits**
For the odd triangle wave ($T=2, \omega_0 = \pi, A=1$):
Since $f(t)$ is **odd**, $c_n$ is purely imaginary:
$$c_n = -j \frac{2}{T} \int_{0}^{T/2} f(t) \sin(n\omega_0 t) \, dt = -j \int_0^1 f(t) \sin(n\pi t) \, dt$$

**Step 2: Define $f(t)$ on $[0,1]$**
$f(t) = 2t$ for $0 < t < 0.5$
$f(t) = 2 - 2t$ for $0.5 < t < 1$

---

## Practice 18.7: Solution (b) (Cont.)

**Step 3: Evaluate Integrals** (using integration by parts)
<div class="text-xs">

$$c_n = -j \left[ \int_0^{0.5} 2t \sin(n\pi t) \, dt + \int_{0.5}^1 (2-2t) \sin(n\pi t) \, dt \right]$$
$$c_n = -j \left( \left[ \frac{2\sin(n\pi t)}{n^2\pi^2} - \frac{2t\cos(n\pi t)}{n\pi} \right]_0^{0.5} + \left[ \frac{-2\cos(n\pi t)}{n\pi} - \left( \frac{2\sin(n\pi t)}{n^2\pi^2} - \frac{2t\cos(n\pi t)}{n\pi} \right) \right]_{0.5}^1 \right)$$
</div>

**Step 4: Result**
Summing terms and simplifying:
$$\mathbf{c_n = -j\frac{4}{n^2\pi^2} \sin\left(\frac{n\pi}{2}\right)}$$

---

## Practice 18.7: Alternative Solution (b)

**Step 1: Use Differentiation Property**
The derivative $f'(t)$ of this triangle wave is an **even square wave** of amplitude $A'=2$ and period $T=2$.

**Step 2: Derivative Coefficients**
From Example 18.3, the complex coefficients $c_n'$ for $f'(t)$ are:
$$c_n' = \frac{4}{n\pi} \sin\left(\frac{n\pi}{2}\right)$$

**Step 3: Solve for $c_n$** (using $c_n' = jn\omega_0 c_n$)
$$c_n = \frac{c_n'}{jn\pi} = \mathbf{-j\frac{4}{n^2\pi^2} \sin\left(\frac{n\pi}{2}\right)}$$


---

## 18.5 Definition of the Fourier Transform
### Limiting Process: From Series to Transform
To analyzer nonperiodic functions, we begin with a periodic function and let the period **$T \to \infty$**.

As $T$ increases:
- The fundamental frequency $\omega_0$ becomes vanishingly small.
- The frequency components (harmonics) become more and more closely spaced.
- In the limit, the **discrete line spectrum** becomes a **continuous spectrum**.

### The Limiting Conditions
Let us define the operations as the period $T$ becomes infinite:
1.  **Fundamental Frequency**: $\omega_0 \to d\omega$
2.  **Harmonic Index**: $n\omega_0 \to \omega$ (a continuous variable)
3.  **Period Relationship**: $\frac{1}{T} = \frac{\omega_0}{2\pi} \to \frac{d\omega}{2\pi}$
4.  **Coefficient Scaling**: $c_n T \to F(j\omega)$




---

## Defining the Fourier Transform

Starting with the complex coefficient $c_n$:
$$c_n = \frac{1}{T} \int_{-T/2}^{T/2} f(t) e^{-jn\omega_0 t} \, dt \implies c_n T = \int_{-T/2}^{T/2} f(t) e^{-jn\omega_0 t} \, dt$$

Applying the limit $T \to \infty$:
$$\mathbf{F(j\omega) = \int_{-\infty}^{\infty} f(t) e^{-j\omega t} \, dt}$$
This $F(j\omega)$ represents the **continuous frequency spectrum**.

---

### Why $c_n T \to F(j\omega)$?
The scaling $c_n T$ is necessary because of the transition from discrete to continuous analysis.

<img src="/spectral_density_evolution.svg" class="h-100 mx-auto p-2" alt="Spectral Density Evolution Visualization" />

---

- **Discrete Case ($c_n$):** Each coefficient represents the **actual strength** (amplitude) of a single frequency component. As $T \to \infty$, each $c_n$ vanishes toward zero.

- **Continuous Case ($F(j\omega)$):** Instead of individual strengths, we use **Spectral Density** (strength per unit frequency).
  $$c_n = F(j n \omega_0) \Delta f = F(j n \omega_0) \frac{1}{T}$$
  
Therefore, the product **$c_n T$** remains finite and represents the "density" of the signal at frequency $\omega$:
$$\mathbf{F(j\omega) = \lim_{T \to \infty} c_n T}$$

---

## The Inverse Fourier Transform

Now apply the limit to the summation for $f(t)$:
$$f(t) = \sum_{n=-\infty}^{\infty} c_n e^{jn\omega_0 t} = \sum_{n=-\infty}^{\infty} (c_n T) e^{jn\omega_0 t} \frac{1}{T}$$

Substituting the limiting values:
$$f(t) = \sum_{n=-\infty}^{\infty} F(j\omega) e^{j\omega t} \frac{d\omega}{2\pi}$$

In the limit, the summation becomes an integral:
$$\mathbf{f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(j\omega) e^{j\omega t} \, d\omega}$$

---

## The Fourier Transform Pair

These two equations collectively define the **Fourier Transform Pair**:

<div class="grid grid-cols-1 gap-4 mt-10">
<div class="border-2 border-blue-500 p-4 rounded-lg bg-blue-50 dark:bg-blue-900/20 text-center">

$$F(j\omega) = \mathcal{F}\{f(t)\} = \int_{-\infty}^{\infty} f(t) e^{-j\omega t} \, dt$$
</div>

<div class="border-2 border-green-500 p-4 rounded-lg bg-green-50 dark:bg-green-900/20 text-center">

$$f(t) = \mathcal{F}^{-1}\{F(j\omega)\} = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(j\omega) e^{j\omega t} \, d\omega$$
</div>
</div>



---

## Example 18.5: Rectangular Pulse Transform

**Problem**: Obtain the continuous spectrum of a single rectangular pulse:
$f(t) = V_0$ for $t_0 < t < t_0 + \tau$, and $0$ otherwise.

<img src="/rect_pulse_spectrum.svg" class="h-60 mx-auto p-2" alt="Rectangular Pulse and Spectrum" />

---

**Solution**:
1.  **Fourier Transform Definition**:
    $$F(j\omega) = \int_{t_0}^{t_0+\tau} V_0 e^{-j\omega t} dt = V_0 \left[ \frac{e^{-j\omega t}}{-j\omega} \right]_{t_0}^{t_0+\tau}$$
2.  **Simplification**:
    $$F(j\omega) = V_0 \tau \text{ Sa}\left(\frac{\omega \tau}{2}\right) e^{-j\omega(t_0+\tau/2)}$$
    where $\text{Sa}(x) = \frac{\sin x}{x}$.

---

## Practice 18.8

**Problem**: If $f(t) = -10$ V for $-0.2 < t < -0.1$ s, $f(t) = 10$ V for $0.1 < t < 0.2$ s, and $f(t) = 0$ otherwise, evaluate $F(j\omega)$ at:
(a) $0$; (b) $10\pi$; \(c\) $-10\pi$; (d) $15\pi$; (e) $-20\pi$ rad/s.

**Ans**:
- (a) $0$
- (b) $j1.273$ V/(rad/s)
- \(c\) $-j1.273$ V/(rad/s)
- (d) $-j0.424$ V/(rad/s)
- (e) $0$

---

## Practice 18.8: Solution

**Integral Setup**:
$$F(j\omega) = \int_{-0.2}^{-0.1} -10 e^{-j\omega t} dt + \int_{0.1}^{0.2} 10 e^{-j\omega t} dt$$

**Evaluation**:
$$F(j\omega) = \frac{10}{j\omega} [e^{-j\omega t}]_{-0.2}^{-0.1} - \frac{10}{j\omega} [e^{-j\omega t}]_{0.1}^{0.2}$$
$$F(j\omega) = \frac{10}{j\omega} (e^{j0.1\omega} - e^{j0.2\omega} - e^{-j0.2\omega} + e^{-j0.1\omega})$$

**Final Form**:
$$F(j\omega) = \frac{20}{j\omega} [\cos(0.1\omega) - \cos(0.2\omega)] \text{ V/(rad/s)}$$
Evaluating this for $\omega = 0, 10\pi, \dots$ yields the answers.

---

## Practice 18.9

**Problem**: If $F(j\omega) = -10$ V/(rad/s) for $-4 < \omega < -2$ rad/s, $+10$ V/(rad/s) for $2 < \omega < 4$ rad/s, and $0$ otherwise, find $f(t)$ at:
(a) $10^{-4}$ s; (b) $10^{-2}$ s; \(c\) $\pi/4$ s; (d) $\pi/2$ s; (e) $\pi$ s.

**Ans**:
- (a) $j1.91 \times 10^{-3}$ V
- (b) $j0.191$ V
- (c) $j4.05$ V
- (d) $-j4.05$ V
- (e) $0$

---

## Practice 18.9: Solution

**Inverse Transform Setup**:
$$f(t) = \frac{1}{2\pi} \left[ \int_{-4}^{-2} -10 e^{j\omega t} d\omega + \int_{2}^{4} 10 e^{j\omega t} d\omega \right]$$

**Evaluation**:
$$f(t) = \frac{-10}{j2\pi t} [e^{j\omega t}]_{-4}^{-2} + \frac{10}{j2\pi t} [e^{j\omega t}]_{2}^{4}$$
$$f(t) = \frac{10}{j2\pi t} (e^{j4t} + e^{-j4t} - e^{j2t} - e^{-j2t})$$

**Final Form**:
$$f(t) = \frac{10}{j\pi t} [\cos(4t) - \cos(2t)] \text{ V}$$
Evaluating this for $t = 10^{-4}, 10^{-2}, \dots$ yields the answers.

---

## Parseval's Theorem

Parseval's theorem relates the total power or energy of a signal in the **time domain** to its representation in the **frequency domain**.

### 1. For Periodic Signals (Power)
The average power $P_{avg}$ delivered to a $1 \Omega$ resistor is:
$$P_{avg} = \frac{1}{T} \int_{0}^{T} |f(t)|^2 \, dt = \sum_{n=-\infty}^{\infty} |c_n|^2$$
Total power is the sum of powers in all harmonic components.

---

## Parseval's Theorem: Derivation (Energy)

For aperiodic signals, we calculate total energy $W_{1\Omega}$:
$$W_{1\Omega} = \int_{-\infty}^{\infty} f^2(t) \, dt$$

**Step 1: Substitute one $f(t)$ with its Inverse Transform**
$$W_{1\Omega} = \int_{-\infty}^{\infty} f(t) \left[ \frac{1}{2\pi} \int_{-\infty}^{\infty} F(j\omega) e^{j\omega t} \, d\omega \right] dt$$

**Step 2: Interchange the order of integration**
$$W_{1\Omega} = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(j\omega) \left[ \int_{-\infty}^{\infty} f(t) e^{j\omega t} \, dt \right] d\omega$$

---

## Parseval's Theorem: Derivation (Cont.)

**Step 3: Recognize the inner integral**
The inner integral $\int_{-\infty}^{\infty} f(t) e^{j\omega t} \, dt$ is exactly **$F(-j\omega)$** (or $F^*(j\omega)$ for real $f(t)$).

**Step 4: Final Formula**
$$W_{1\Omega} = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(j\omega) F^*(j\omega) \, d\omega = \mathbf{\frac{1}{2\pi} \int_{-\infty}^{\infty} |F(j\omega)|^2 \, d\omega}$$

---

## Physical Significance: Energy Density

Parseval's theorem tells us how energy is distributed:

<img src="/energy_spectral_density.svg" class="h-70 mx-auto p-2" alt="Energy Spectral Density Diagram" />

- $|F(j\omega)|^2$ is the **Energy Spectral Density** (J / rad/s).
- The total energy is the area under the $|F(j\omega)|^2$ curve (scaled by $1/2\pi$).
- $|F(j\omega)|^2$ is always a real, even, and nonnegative function of $\omega$.
- Energy density is independent of the **phase** of $F(j\omega)$.

---

## Example 18.6: Bandpass Filter Energy

**Problem**: A pulse $v(t) = 4e^{-3t}u(t)$ V is applied to an ideal bandpass filter with passband $1 < |f| < 2$ Hz. Calculate the output energy.

<img src="/example_18_6_visualization.svg" class="h-60 mx-auto p-2" alt="Signal and Spectrum with Passband" />

---

**Solution**:
1.  **Fourier Transform Calculation**:
    $$V(j\omega) = \int_{-\infty}^{\infty} 4e^{-3t}u(t) e^{-j\omega t} dt = \int_{0}^{\infty} 4e^{-(3+j\omega)t} dt$$
    $$V(j\omega) = 4 \left[ \frac{e^{-(3+j\omega)t}}{-(3+j\omega)} \right]_{0}^{\infty} = \frac{4}{-(3+j\omega)} (0 - 1) = \mathbf{\frac{4}{3+j\omega}}$$
2.  **Energy in Passband**:
    The passband corresponds to $2\pi < |\omega| < 4\pi$.
    $$W_{out} = \frac{1}{2\pi} \left[ \int_{-4\pi}^{-2\pi} \frac{16}{9+\omega^2} d\omega + \int_{2\pi}^{4\pi} \frac{16}{9+\omega^2} d\omega \right]$$

---

3.  **Calculation Steps**:
    Using the standard integral $\int \frac{dx}{a^2 + x^2} = \frac{1}{a} \tan^{-1}\left(\frac{x}{a}\right)$:
    - Here $a^2 = 9$, so $a = 3$.
    $$W_{out} = \frac{16}{\pi} \int_{2\pi}^{4\pi} \frac{1}{9+\omega^2} d\omega$$
    $$W_{out} = \frac{16}{\pi} \left[ \frac{1}{3} \tan^{-1}\left(\frac{\omega}{3}\right) \right]_{2\pi}^{4\pi} = \frac{16}{3\pi} \left[ \tan^{-1}\left(\frac{4\pi}{3}\right) - \tan^{-1}\left(\frac{2\pi}{3}\right) \right]$$
    $$W_{out} \approx \frac{16}{3\pi} [\tan^{-1}(4.189) - \tan^{-1}(2.094)] = \frac{16}{3\pi} [1.337 - 1.125] \approx \mathbf{358 \text{ mJ}}$$

---

## Practice 18.10

**Problem**: If $i(t) = 10e^{20t} [u(t + 0.1) - u(t - 0.1)]$ A, evaluate $F_i(j\omega)$ for $\omega$ equal to:
(a) $0$; (b) $10\pi$; \(c\) $-10\pi$; (d) $15\pi$; (e) $-20\pi$ rad/s.

**Ans**: 
- (a) $3.63$ A/(rad/s)
- (b) $3.33 \angle -31.7^\circ$ A/(rad/s)
- \(c\) $A_i(10) = 2.83$ A/(rad/s)
- (d) $B_i(10) = -1.749$ A/(rad/s)
- (e) $\phi_i(10) = -31.7^\circ$

---

## Practice 18.10: Solution

**Step 1: Integrate**
$$F_i(j\omega) = \int_{-0.1}^{0.1} 10e^{(20-j\omega)t} dt = \left[ \frac{10}{20-j\omega} e^{(20-j\omega)t} \right]_{-0.1}^{0.1}$$
$$F_i(j\omega) = \frac{10}{20-j\omega} (e^{2-j0.1\omega} - e^{-2+j0.1\omega})$$

**Step 2: Evaluate at $\omega=10$**
Using $e^{2-j1} - e^{-2+j1} = (e^2-e^{-2})\cos(1) - j(e^2+e^{-2})\sin(1)$:
$$F_i(j10) = \frac{3.919 - j6.331}{2-j1} = 2.833 - j1.748$$
- **$A_i(10) \approx 2.83$**
- **$B_i(10) \approx -1.75$**
- **$\phi_i(10) = \tan^{-1}(-1.75/2.83) = -31.7^\circ$**

---

## Practice 18.11

**Problem**: Find the $1 \Omega$ energy associated with $i(t) = 20e^{-10t}u(t)$ A in the interval:
(a) $-0.1 < t < 0.1$ s; (b) $-10 < \omega < 10$ rad/s; \(c\) $10 < \omega < \infty$ rad/s.

**Ans**: (a) $17.29$ J; (b) $10$ J; \(c\) $5$ J.

---

## Practice 18.11: Solution

**Part (a) Time Interval**:
$$W = \int_{0}^{0.1} (20e^{-10t})^2 dt = \int_{0}^{0.1} 400e^{-20t} dt = \left[ -20e^{-20t} \right]_0^{0.1} = \mathbf{17.29 \text{ J}}$$

**Part (b) Frequency Interval**:
Using $F(j\omega) = \frac{20}{10+j\omega}$ and $|F|^2 = \frac{400}{100+\omega^2}$:
$$W = \frac{1}{2\pi} \int_{ -10}^{10} \frac{400}{100+\omega^2} d\omega = \frac{40}{\pi} [ \tan^{-1}(1) - \tan^{-1}(-1) ] = \frac{40}{\pi} \left(\frac{\pi}{2}\right) = \mathbf{10 \text{ J}}$$
*(Error in previous manual check: $\frac{40}{\pi} \cdot \frac{\pi}{2} = 20$, but $\frac{1}{2\pi}$ factor makes it $10$.)*

**Part \(c\) High Frequencies**:
Total energy $W_{total} = 20$ J. Energy in $|\omega|<10$ is $10$ J.
Remaining $10$ J is split between $(10, \infty)$ and $(-\infty, -10)$.
$W(10 < \omega < \infty) = \mathbf{5 \text{ J}}$.

---

## 18.6/18.7 Properties & Pairs

**Unit Impulse Function**:
- We seek the Fourier transform of $\delta(t - t_0)$.

**The Signum Function**:
- A singularity function $sgn(t)$.

**The Unit Step Function**:
- $u(t)$.

---

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
