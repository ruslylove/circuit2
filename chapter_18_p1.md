---
theme: seriph
background: https://cover.sli.dev
title: Chapter 18 Part 1
info: |
  ## Chapter 18 Part 1
  Fourier Circuit Analysis: Trigonometric Series and Symmetry
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Chapter 18: Fourier Circuit Analysis

## Part I

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

- Trigonometric Form of the Fourier Series
- The Use of Symmetry
- Complete Response to Periodic Forcing Function

---

## 18.1 Trigonometric Form of the Fourier Series

- In this section, we refocus our attention on forcing functions that are sinusoidal in nature.
- We discover how to write a general periodic function as a sum of such functions—leading us into a discussion of a new set of circuit analysis procedures.

---

## Harmonic

- Let us first assume a cosine function of radian frequency $\omega_0$.

### Practice 18.1

Let a third-harmonic voltage be added to the fundamental to yield $v = 2 \cos \omega_0 t + V_{in3} \sin 3 \omega_0 t$.

(a) Find the value of $V_{in3}$ so that $v(t)$ will have zero slope at $\omega_0 t = 2\pi/3$.
(b) Evaluate $v(t)$ at $\omega_0 t = 2\pi/3$.

**Answers**:
- (a) 0.577
- (b) -1.000

---

## Fourier Series

- Consider a periodic function $f(t)$.
- It can be expressed as an infinite sum of sine and cosine functions.

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
