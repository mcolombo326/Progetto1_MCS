import numpy as np

def gradient(A, b, x0=None, tol=1e-10, max_iter=1000):

    x = np.zeros_like(b) if x0 is None else x0.copy()

    # Calcolo del residuo iniziale
    r = b - np.dot(A, x)

    for k in range(max_iter):

        # Calcolo di A * r, usato per il denominatore di alpha
        Ar = np.dot(A, r)

        # Calcolo dello step ottimale alpha
        alpha = np.dot(r, r) / np.dot(r, Ar)

        # Aggiornamento della soluzione
        x_new = x + alpha * r

        # Aggiornamento del residuo
        r = b - np.dot(A, x_new)

        # Calcolo dell'errore relativo
        err_rel = np.linalg.norm(r) / np.linalg.norm(b)

        # Criterio di arresto
        if err_rel < tol:
            return x_new, err_rel, k+1

        x = x_new

    raise ValueError("Metodo del gradiente non converge entro il numero massimo di iterazioni")
