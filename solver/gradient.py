import numpy as np
import time
from solver.base import BaseSolver

class GradientSolver(BaseSolver):
    def solve(self):
        x = np.zeros(self.n)
        r = self.b - self.A @ x

        start_time = time.perf_counter()

        for k in range(self.max_iter):
            Ar = self.A @ r
            num = np.dot(r, r)
            den = np.dot(r, Ar)

            # Evita divisione per zero o valori anomali
            if den == 0 or np.isnan(den) or np.isinf(den):
                raise ValueError(f"Gradient: divisione per zero o valore non valido alla iterazione {k}.")

            alpha = num / den
            x = x + alpha * r

            # controllo NaN/inf
            if np.any(np.isnan(x)) or np.any(np.isinf(x)):
                raise ValueError(f"Gradient diverge alla iterazione {k}, valore non valido trovato.")

            if self._check_convergence(x):
                elapsed_time = time.perf_counter() - start_time
                return x, k + 1, elapsed_time

            r = self.b - self.A @ x

        elapsed_time = time.perf_counter() - start_time
        raise ValueError(f"Gradient: non converge dopo {self.max_iter} iterazioni.")
