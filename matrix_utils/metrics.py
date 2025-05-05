import numpy as np

def relative_error(x_true: np.ndarray, x_approx: np.ndarray) -> float:
    denominator = np.linalg.norm(x_true)
    if denominator == 0:
        return float('inf')
    return np.linalg.norm(x_true - x_approx) / denominator

def residual_norm(A, x, b):
    r = A @ x - b
    return np.linalg.norm(r) / np.linalg.norm(b)
