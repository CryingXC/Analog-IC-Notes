# 00 · Roadmap

Analog IC design becomes much easier when learned in layers:

1. **Device physics** — MOS electrostatics, channel formation, inversion.
2. **Small-signal abstraction** — \(g_m\), \(r_o\), \(g_{mb}\), capacitances.
3. **Primitive blocks** — current mirrors, differential pair, single-stage amplifiers.
4. **Amplifier systems** — OTA / op-amp topology, gain, swing, slew rate.
5. **Dynamic behavior** — poles, zeros, feedback, stability, compensation.
6. **Non-idealities** — noise, mismatch, PVT, finite output resistance.
7. **Implementation** — layout matching, parasitics, verification.

A useful habit is to ask four questions for every circuit:

- What sets the **DC operating point**?
- Where does the **small-signal gain** come from?
- Which nodes create the **dominant poles / zeros**?
- Which **non-ideality** is likely to dominate silicon behavior?
