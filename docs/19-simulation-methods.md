# 19 · Simulation Methods

Each simulation answers a different question.

| Analysis | Main purpose |
|---|---|
| DC operating point | Are devices biased in the intended region? |
| DC sweep | How does transfer behavior change with input / supply / load? |
| AC | Small-signal gain, poles, bandwidth |
| STB / loop analysis | Loop gain, phase margin, gain margin |
| Transient | Large-signal timing, settling, slew, startup |
| Noise | Input/output-referred noise |
| PVT corners | Deterministic process / voltage / temperature robustness |
| Monte Carlo | Statistical variation / mismatch |

## Order of operations

A practical sequence:

1. verify DC bias;
2. verify nominal small-signal behavior;
3. verify nominal transient behavior;
4. sweep load / input / supply;
5. run PVT;
6. run Monte Carlo;
7. repeat critical checks post-layout.

Never use a single passing waveform as evidence for a whole design.
