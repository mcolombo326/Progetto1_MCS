import numpy as np
import time
from abc import ABC, abstractmethod

class BaseSolver(ABC):
    def __init__(self, A: np.ndarray, b: np.ndarray, tol: float, max_iter: int = 20000):
        self.A = A
        self.b = b
        self.tol = tol
        self.max_iter = max_iter
        self.n = b.shape[0]

    @abstractmethod
    def solve(self):
        pass

    def _check_convergence(self, xk):
        denominator = np.linalg.norm(self.b)
        if denominator == 0:
            return float('inf')
        res = np.linalg.norm(self.A @ xk - self.b) / denominator
        return res < self.tol
