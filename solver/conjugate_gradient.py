import numpy as np
import time
from solver.base import BaseSolver

class ConjugateGradientSolver(BaseSolver):
    def solve(self):
        x = np.zeros(self.n)
        r = self.b - self.A @ x
        p = r.copy()

        start_time = time.perf_counter()

        for k in range(self.max_iter):
            Ap = self.A @ p
            num = np.dot(r, r)
            den = np.dot(p, Ap)

            if den == 0 or np.isnan(den) or np.isinf(den):
                raise ValueError(f"Conjugate Gradient: divisione per zero o valore non valido alla iterazione {k}.")

            alpha = num / den
            x = x + alpha * p

            if self._check_convergence(x):
                elapsed_time = time.perf_counter() - start_time
                return x, k + 1, elapsed_time

            r_new = r - alpha * Ap

            if np.any(np.isnan(x)) or np.any(np.isinf(x)):
                raise ValueError(f"Conjugate Gradient diverge alla iterazione {k}, valore non valido trovato.")

            beta = np.dot(r_new, r_new) / num
            p = r_new + beta * p
            r = r_new

        elapsed_time = time.perf_counter() - start_time
        raise ValueError(f"Conjugate Gradient: non converge dopo {self.max_iter} iterazioni.")
