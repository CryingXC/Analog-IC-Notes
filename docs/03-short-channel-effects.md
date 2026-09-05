# 03 · Short-Channel Effects

## Vth roll-off

When channel length becomes short, source/drain depletion regions participate in channel electrostatics. The gate no longer controls the entire depletion charge alone, so the required gate voltage for inversion falls.

Result:

\[
L \downarrow \quad \Rightarrow \quad V_{TH} \downarrow
\]

## DIBL

Drain-Induced Barrier Lowering means a larger drain voltage lowers the source-channel energy barrier.

Qualitatively:

\[
V_{DS}\uparrow \Rightarrow \text{barrier}\downarrow \Rightarrow V_{TH,\text{effective}}\downarrow
\]

This increases off-state and subthreshold current.

DIBL resembles channel-length modulation only in the sense that the drain affects current beyond an ideal saturation picture. The mechanisms differ:

- **CLM:** effective channel length changes after pinch-off.
- **DIBL:** drain electric field alters the source-side potential barrier.

## Subthreshold leakage

A common form is

\[
I_D \propto \exp\left(\frac{V_{GS}-V_{TH}}{nV_T}\right)
\]

Therefore even a modest \(V_{TH}\) reduction can increase leakage exponentially.

## Gate leakage

As gate dielectric thickness decreases, direct tunneling becomes more important. High-\(k\) dielectrics reduce equivalent oxide thickness while allowing a physically thicker dielectric.

## Why advanced processes struggle with static power

Scaling reduces capacitance and supply voltage, but leakage mechanisms become more severe:
- subthreshold leakage;
- gate tunneling;
- junction leakage;
- DIBL-enhanced off current.
