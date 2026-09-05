# 08 · Frequency Response

Every physical node has capacitance.

<div align="center">
<img src="../assets/figures/bode-pole-zero.svg" alt="Bode pole zero intuition" width="95%" />
</div>

A first-order pole is

\[
\omega_p = \frac{1}{RC}
\]

or

\[
f_p=\frac{1}{2\pi RC}
\]

High-impedance nodes therefore tend to create low-frequency poles.

## Miller effect

For a capacitor \(C\) between input and output with gain \(A_v\), the equivalent input capacitance is approximately

\[
C_{in}\approx C(1-A_v)
\]

For a large negative gain, this can be much larger than \(C\).

## Dominant-pole idea

If one pole is moved far below the others, loop gain crosses unity before higher-order phase lag becomes severe.

## Zeros

A zero can either improve or hurt phase margin depending on its sign and location. A right-half-plane zero contributes phase lag even though its magnitude rises.
