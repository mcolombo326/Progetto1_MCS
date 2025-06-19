import numpy as np

def conjugate_gradient(A, b, x0=None, tol=1e-10, max_iter=1000):

    x = np.zeros_like(b) if x0 is None else x0.copy()

    r = b - np.dot(A, x)
    d = r.copy()
    Ad = np.dot(A, d)
    r_dot = np.dot(r, r)

    for k in range(max_iter):
        alpha = r_dot / np.dot(d, Ad)
        x_new = x + alpha * d

        # Calcolo nuovo residuo
        r_new = b - np.dot(A, x_new)
        err_rel = np.linalg.norm(r_new) / np.linalg.norm(b)

        # Criterio di arresto
        if err_rel < tol:
            return x_new, err_rel, k+1

        Ar_new = np.dot(A, r_new)
        beta = np.dot(d, Ar_new) / np.dot(d, Ad)
        d = r_new - beta * d

        # Preparazione per la prossima iterazione
        x = x_new
        r = r_new
        Ad = np.dot(A, d)
        r_dot = np.dot(r, r)

    raise ValueError("Gradiente coniugato non converge entro il numero massimo di iterazioni")
