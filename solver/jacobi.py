import numpy as np
from .base import BaseSolver

class JacobiSolver(BaseSolver):
    def solve(self):
        x = np.zeros_like(self.b)
        D = np.diag(self.A)
        R = self.A - np.diagflat(D)

        for k in range(self.max_iter):
            x_new = (self.b - R @ x) / D
            if self._check_convergence(x_new):
                return x_new, k + 1
            x = x_new

        raise ValueError("Jacobi method did not converge")