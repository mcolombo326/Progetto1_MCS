import numpy as np

def conjugate_gradient(A, b, x0=None, tol=1e-10, max_iter=1000):
    x = np.zeros_like(b) if x0 is None else x0.copy()
    r = b - A @ x # Calcolo del residuo iniziale
    d = r.copy() # Direzione di ricerca iniziale = residuo iniziale
    delta_new = np.dot(r, r)

    for k in range(max_iter):
        Ad = A @ d

        # Calcolo dello step ottimale alpha lungo la direzione d
        alpha = delta_new / np.dot(d, Ad)

        # Aggiornamento della soluzione
        x = x + alpha * d

        # Aggiornamento del residuo
        r = r - alpha * Ad

        # Controllo del residuo relativo
        err_rel = np.linalg.norm(r) / np.linalg.norm(b)
        if err_rel < tol:
            return x, err_rel, k + 1

        delta_old = delta_new
        delta_new = np.dot(r, r)
        beta = delta_new / delta_old
        d = r + beta * d # Nuova direzione: r + beta * direzione precedente

    raise ValueError("Gradiente coniugato non converge entro il numero massimo di iterazioni")
