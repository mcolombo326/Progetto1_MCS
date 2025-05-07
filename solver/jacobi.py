import numpy as np

def jacobi(A, b, x0=None, tol=1e-10, max_iter=1000):
    n = len(b)
    x = np.zeros_like(b) if x0 is None else x0.copy()
    D = np.diag(A)
    R = A - np.diagflat(D)

    for k in range(max_iter):
        x_new = (b - np.dot(R, x)) / D

        #Calcolo del residuo
        residuo = (b - np.dot(A, x_new))
        err_rel = np.linalg.norm(residuo) / np.linalg.norm(b)

        # Controllo del criterio di arresto con la norma del residuo
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, err_rel, k+1
        x = x_new

    raise ValueError("Jacobi non converge entro il numero massimo di iterazioni")