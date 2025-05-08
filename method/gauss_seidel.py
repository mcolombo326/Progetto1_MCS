import numpy as np

def gauss_seidel(A, b, x0=None, tol=1e-10, max_iter=1000):
    n = len(b)
    x = np.zeros_like(b) if x0 is None else x0.copy()

    for k in range(max_iter):
        x_old = x.copy()

        for i in range(n):
            somma1 = np.dot(A[i, :i], x[:i])     # usa x aggiornato (k+1)
            somma2 = np.dot(A[i, i+1:], x_old[i+1:])  # usa x_old (k)
            x[i] = (b[i] - somma1 - somma2) / A[i, i]

        # Calcolo del residuo
        r = b - np.dot(A, x)
        err_rel = np.linalg.norm(r) / np.linalg.norm(b)

        # Criterio di arresto
        #if np.linalg.norm(x - x_old, ord=np.inf) < tol:
        if err_rel < tol:
            return x, err_rel, k+1

    raise ValueError("Gauss-Seidel non converge entro il numero massimo di iterazioni")
