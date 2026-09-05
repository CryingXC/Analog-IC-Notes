# 12 · Mismatch & Monte Carlo

Identically drawn devices are not physically identical.

A common Pelgrom-style model is

\[
\sigma(\Delta V_{TH})\propto \frac{1}{\sqrt{WL}}
\]

Larger device area generally improves matching.

## Local mismatch vs process variation

- **Process variation:** many devices move together.
- **Mismatch:** nominally matched neighbors differ from each other.

## Monte Carlo

Monte Carlo simulation samples statistical model variation. Use it to estimate distributions, not just a single "worst" waveform.

Useful outputs:
- mean;
- standard deviation;
- percentile / yield;
- correlation with device parameters.

## Layout connection

Common-centroid, interdigitation, dummy devices, symmetry and equal surroundings reduce systematic mismatch but cannot eliminate random mismatch.
