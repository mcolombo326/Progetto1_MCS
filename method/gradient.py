import numpy as np

def gradient(A, b, x0=None, tol=1e-10, max_iter=1000):
    n = len(b)
    x = np.zeros_like(b) if x0 is None else x0.copy()

    r = b - np.dot(A, x)
    err_rel = np.linalg.norm(r) / np.linalg.norm(b)

    for k in range(max_iter):
        Ar = np.dot(A, r)
        alpha = np.dot(r, r) / np.dot(r, Ar)
        x_new = x + alpha * r

        # Calcolo del residuo aggiornato
        r = b - np.dot(A, x_new)
        err_rel = np.linalg.norm(r) / np.linalg.norm(b)

        # Criterio di arresto
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, err_rel, k+1

        x = x_new

    raise ValueError("Metodo del gradiente non converge entro il numero massimo di iterazioni")
