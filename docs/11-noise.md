# 11 · Noise

## Thermal noise

For a resistor:

\[
\overline{v_n^2}=4kTR\Delta f
\]

MOS channel thermal noise is often expressed in drain-current form:

\[
\overline{i_n^2}\approx 4kT\gamma g_m\Delta f
\]

## Flicker noise

A common qualitative model:

\[
S_{v,1/f}\propto \frac{1}{WLf}
\]

Increasing device area reduces 1/f noise and mismatch, but increases capacitance.

## Input-referred noise

Translate internal noise sources to the input using the signal gain from input to the observation node. Input-referred noise lets different architectures be compared on equal footing.

## Trade-offs

Noise competes with:
- power;
- bandwidth;
- area;
- input capacitance;
- bias current.
