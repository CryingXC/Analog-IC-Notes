# 04 · Current Mirrors & Bias

A current mirror converts a reference current into one or more bias currents.

<div align="center">
<img src="../assets/figures/current-mirror.svg" alt="NMOS current mirror concept" width="92%" />
</div>

For matched long-channel MOS devices:

\[
\frac{I_{OUT}}{I_{REF}} \approx
\frac{(W/L)_{OUT}}{(W/L)_{REF}}
\]

## Non-idealities

Finite output resistance gives current dependence on output voltage:

\[
I_D \approx I_{D0}(1+\lambda V_{DS})
\]

Thus mirror accuracy improves when corresponding devices have similar \(V_{DS}\).

## Cascode mirror

A cascode raises output resistance roughly by another factor of \(g_m r_o\), but consumes voltage headroom.

## Bias-network questions

Always check:
- startup;
- minimum supply voltage;
- output compliance;
- PVT current spread;
- device saturation;
- mirror mismatch.
