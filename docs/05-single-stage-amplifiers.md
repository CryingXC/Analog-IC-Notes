# 05 · Single-Stage Amplifiers

## Common source

High voltage gain, inverting:

\[
A_v \approx -g_m R_{out}
\]

## Source follower

Near-unity gain, low output impedance. A simple approximation:

\[
A_v \approx \frac{g_m R}{1+g_m R}
\]

Body effect reduces the achievable gain.

## Common gate

Low input impedance:

\[
R_{in}\approx \frac{1}{g_m}
\]

Useful for current-mode interfaces, wideband stages and cascode structures.

## Cascode

The cascode suppresses drain-voltage variation of the input transistor and raises output resistance:

\[
R_{out}\sim g_m r_o^2
\]

The cost is reduced output swing and additional bias complexity.
