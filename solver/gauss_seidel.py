import numpy as np
import time
from solver.base import BaseSolver

class GaussSeidelSolver(BaseSolver):
    def solve(self):
        x = np.zeros(self.n)

        start_time = time.perf_counter()

        for k in range(self.max_iter):
            for i in range(self.n):
                row = self.A.getrow(i).toarray().flatten()
                sigma = np.dot(row[:i], x[:i]) + np.dot(row[i+1:], x[i+1:])
                x[i] = (self.b[i] - sigma) / row[i]

                # controllo NaN/inf
                if np.isnan(x[i]) or np.isinf(x[i]):
                    raise ValueError(f"Gauss-Seidel diverge alla iterazione {k}, valore non valido trovato.")

            if self._check_convergence(x):
                elapsed_time = time.perf_counter() - start_time
                return x, k + 1, elapsed_time

        elapsed_time = time.perf_counter() - start_time
        raise ValueError(f"Gauss-Seidel: non converge dopo {self.max_iter} iterazioni.")
