# 10 · Compensation

## Miller compensation

A capacitor between two gain nodes creates pole splitting.

Very roughly, the dominant pole moves lower while the second pole moves higher, improving single-pole behavior around unity gain.

## Slew-rate relation

For a compensation capacitor charged by a limited current:

\[
SR \approx \frac{I}{C_C}
\]

So a larger \(C_C\) may improve stability but reduce slew rate.

## RHP zero

A plain Miller capacitor can create a right-half-plane zero approximately related to

\[
\omega_z \sim \frac{g_m}{C_C}
\]

A nulling resistor can move or remove this zero.

## Design mindset

Compensation is not "choose a capacitor until PM looks good." It is a controlled redistribution of poles, zeros, current and large-signal settling behavior.
