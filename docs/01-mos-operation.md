# 01 · MOS Operation

## 1. Gate oxide is an insulator, not a "separator between all terminals"

The gate is electrically insulated from the channel by the gate dielectric. Ideally,

\[
I_G \approx 0
\]

in DC. Source and drain are not insulated from the channel; they are heavily doped terminals connected to the inversion layer when the device is on.

## 2. Threshold voltage

A simplified NMOS relation is

\[
V_{TH}=V_{TH0}+\gamma\left(\sqrt{2\phi_F+V_{SB}}-\sqrt{2\phi_F}\right)
\]

The body effect therefore increases \(V_{TH}\) when \(V_{SB}\) rises.

## 3. Strong inversion current

For long-channel intuition:

Linear region:

\[
I_D \approx \mu_n C_{ox}\frac{W}{L}
\left[(V_{GS}-V_{TH})V_{DS}-\frac{V_{DS}^2}{2}\right]
\]

Saturation:

\[
I_D \approx \frac{1}{2}\mu_n C_{ox}\frac{W}{L}(V_{GS}-V_{TH})^2
\]

Define overdrive:

\[
V_{OV}=V_{GS}-V_{TH}
\]

This is the key quantity connecting bias current, \(g_m\), headroom and inversion level.

## 4. Why lower Vth increases current

At fixed \(V_{GS}\),

\[
V_{OV}=V_{GS}-V_{TH}
\]

so a lower threshold directly increases overdrive. In the square-law model, \(I_D\propto V_{OV}^2\).

## 5. Practical view

Real advanced CMOS deviates from square-law behavior because of velocity saturation, mobility degradation, DIBL, series resistance and other short-channel effects. Use square-law for intuition, not as a signoff model.
