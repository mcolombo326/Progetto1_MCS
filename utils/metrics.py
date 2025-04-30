import numpy as np

def relative_error(x_true: np.ndarray, x_approx: np.ndarray) -> float:
    """Errore relativo tra soluzione esatta e approssimata"""
    denominator = np.linalg.norm(x_true)
    if denominator == 0:
        return float('inf')
    return np.linalg.norm(x_true - x_approx) / denominator

def residual_norm(A, x, b):
    """Norma del residuo normalizzata"""
    r = A @ x - b
    return np.linalg.norm(r) / np.linalg.norm(b)