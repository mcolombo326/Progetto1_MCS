from solver.base import BaseSolver

class JacobiSolver(BaseSolver):
    def solve(self):
        x = np.zeros_like(self.b)  # x^(0) = vettore nullo
        D = np.diag(self.A)
        R = self.A - np.diagflat(D)  # R = A - D (cioè L + U)

        start_time = time.time()

        for k in range(self.max_iter):
            x_new = (self.b - np.dot(R, x)) / D  # formula iterativa di Jacobi

            # Verifica convergenza
            if self._check_convergence(x_new):
                elapsed = time.time() - start_time
                return x_new, k + 1, elapsed

            x = x_new

        elapsed = time.time() - start_time
        raise ValueError("Jacobi non converge entro il numero massimo di iterazioni.")
import numpy as np
import time
from solver.base import BaseSolver

class JacobiSolver(BaseSolver):
    def solve(self):
        x = np.zeros(self.n)
        x_new = np.zeros(self.n)

        start_time = time.perf_counter()

        for k in range(self.max_iter):
            for i in range(self.n):
                row = self.A.getrow(i).toarray().flatten()
                sigma = np.dot(row[:i], x[:i]) + np.dot(row[i+1:], x[i+1:])
                x_new[i] = (self.b[i] - sigma) / row[i]
                if np.isnan(x_new[i]) or np.isinf(x_new[i]):
                    raise ValueError(f"Jacobi diverge alla iterazione {k}, valore non valido trovato.")

            if self._check_convergence(x_new):
                elapsed_time = time.perf_counter() - start_time
                return x_new, k + 1, elapsed_time

            x[:] = x_new

        elapsed_time = time.perf_counter() - start_time
        raise ValueError(f"Jacobi: non converge dopo {self.max_iter} iterazioni.")