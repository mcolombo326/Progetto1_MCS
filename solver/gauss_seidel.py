import numpy as np
from .base import BaseSolver

class GaussSeidelSolver(BaseSolver):
    def solve(self):
        x = np.zeros_like(self.b)
        for k in range(self.max_iter):
            x_old = x.copy()
            for i in range(self.n):
                s1 = np.dot(self.A[i, :i], x[:i])
                s2 = np.dot(self.A[i, i + 1:], x_old[i + 1:])
                x[i] = (self.b[i] - s1 - s2) / self.A[i, i]
            if self._check_convergence(x):
                return x, k + 1
        raise ValueError("Gauss-Seidel method did not converge")
