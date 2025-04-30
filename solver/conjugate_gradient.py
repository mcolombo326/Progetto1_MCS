import numpy as np
from .base import BaseSolver

class ConjugateGradientSolver(BaseSolver):
    def solve(self):
        x = np.zeros_like(self.b)
        r = self.b - self.A @ x
        p = r.copy()
        rsold = np.dot(r, r)

        for k in range(self.max_iter):
            Ap = self.A @ p
            alpha = rsold / np.dot(p, Ap)
            x = x + alpha * p
            r = r - alpha * Ap
            rsnew = np.dot(r, r)
            if np.sqrt(rsnew) / np.linalg.norm(self.b) < self.tol:
                return x, k + 1
            p = r + (rsnew / rsold) * p
            rsold = rsnew

        raise ValueError("Conjugate Gradient did not converge")