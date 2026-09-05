# 13 · Comparators

## Static comparator

A high-gain amplifier operated open-loop. Advantages include simple analysis and potentially low kickback; drawbacks include static power and limited speed.

## Regenerative comparator

Positive feedback creates exponential regeneration.

Conceptually:

\[
v_d(t)\propto e^{t/\tau}
\]

where \(\tau\) depends on regenerative transconductance and node capacitance.

## Important non-idealities

- input-referred offset;
- kickback noise;
- metastability;
- common-mode dependence;
- clock feedthrough;
- decision time;
- input loading.
