import numpy as np
from .base import BaseSolver

class GradientSolver(BaseSolver):
    def solve(self):
        x = np.zeros_like(self.b)
        r = self.b - self.A @ x
        for k in range(self.max_iter):
            alpha = np.dot(r, r) / np.dot(r, self.A @ r)
            x = x + alpha * r
            r = self.b - self.A @ x
            if self._check_convergence(x):
                return x, k + 1
        raise ValueError("Gradient method did not converge")