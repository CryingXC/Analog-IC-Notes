# 02 · Small-Signal \(g_m\), \(r_o\), Body Effect

## Transconductance

\[
g_m=\frac{\partial I_D}{\partial V_{GS}}
\]

For the long-channel square-law model:

\[
g_m \approx \frac{2I_D}{V_{OV}}
\]

So, for a fixed current, lower \(V_{OV}\) gives larger \(g_m\) but usually costs voltage headroom and may move the device toward moderate / weak inversion.

## Output resistance

Channel-length modulation gives:

\[
r_o \approx \frac{1}{\lambda I_D}
\]

Intrinsic gain is therefore approximately

\[
A_{v0}=g_m r_o
\]

This single product is one of the most useful analog-design quantities.

## Body transconductance

\[
g_{mb}=\frac{\partial I_D}{\partial V_{BS}}
\]

Body effect turns substrate motion into channel-current modulation. In many topologies, \(g_{mb}\) acts like an unwanted extra transconductance path.

## A common-source stage

Ignoring loading:

\[
A_v \approx -g_m r_o
\]

With an active load, the effective output resistance becomes the parallel combination of the devices connected to the output node.
