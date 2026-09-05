# 15 · Voltage References & Bandgap

A bandgap reference combines:

- a **CTAT** term, typically related to \(V_{BE}\);
- a **PTAT** term, typically related to \(\Delta V_{BE}\).

Conceptually:

\[
V_{REF}=V_{CTAT}+K V_{PTAT}
\]

Choose \(K\) so first-order temperature coefficients approximately cancel.

## Practical blocks

- startup circuit;
- bias core;
- amplifier;
- resistor ratio network;
- trimming;
- supply filtering.

## Real limitations

Curvature, resistor tempco, amplifier offset, mismatch and finite loop gain all perturb the ideal cancellation.
