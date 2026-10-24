# CODE_COMPANION_ROLE: EXECUTABLE
# CODE_COMPANION_PROVENANCE: RECONSTRUCTED_NOT_ORIGINAL
# CODE_COMPANION_RELEASE: RETAIN_AS_CANDIDATE_NOT_FROZEN
import numpy as np
from . import OscillatorModel, EulerSolver, RK4Solver, SciPySolver, exact_state, energy

def main():
    model = OscillatorModel(m=1.0, k=4.0)
    initial = [1.0, 0.0]
    for label, solver in (("Euler", EulerSolver()), ("RK4", RK4Solver()), ("SciPy RK45", SciPySolver())):
        output = solver.solve(model, initial, dt=0.1, steps=10)
        print(label, np.round(output.states[-1], 6))
    print("Exact", np.round(exact_state(1.0, model, initial), 6))
    print("Initial energy", energy(model, initial))
if __name__ == "__main__":
    main()
