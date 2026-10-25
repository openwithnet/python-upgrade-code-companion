# Chapter 6 P1 Word–Code Scoped Audit (2026-10-25)

**Finding: representative object-oriented P1 design, numerical trajectory and stated validation policy align. Release identity and rights NOT proven.**

- Word §6.5.1–6.5.2 names `finite_real`, `ParticleState`, `euler_step`, `Particle`, `TrajectoryRecord`, `Trajectory`, `simulate_particle`. GitHub `p1_particle_trajectory.py` provides these names and responsibilities.
- Word §6.5.2 includes a multi-paragraph canonical executable listing (Word paragraphs 898–907); this is substantially closer to a complete source than the Chapter 3 standalone excerpt. However exact byte-level/textual identity of full listing against the archived file has not yet been certified.
- Word §6.5.3 and source's `main()` both set x0=v0=0, acceleration=2 m/s², dt=.5 s, steps=4; position [0,0,.5,1.5,3], velocity [0,1,2,3,4], final exact x=4, Euler x=3, absolute error=1.
- `ParticleState` is frozen, and `euler_step` returns a new state. `Particle.predict` does not mutate; `Particle.advance` mutates only after successful construction.
- Tests cover bad/nonfinite/bool inputs, wrong step count, failed advance atomicity, duplicate/out-of-order trajectory time, and final trajectory.
- This model is pedagogical constant-acceleration explicit Euler; its observed error is not attributable to using classes.

**Known limits:** CI was executed for chapter entrypoints, but complete Word source listing byte match, third-party rights and all historical assertions remain open. Source `ARCHIVED_CHAPTER_REVIEW_COPY`. No Python source or Word edit. G3/G5/G6 HOLD.
