from numpy import zeros, diag, diagflat, dot, linalg

def jacobi(A, b, N=20000, tol=1e-8, x=None):
    """Solves the equation Ax=b via the Jacobi iterative method."""
    # Create an initial guess if needed
    if x is None:
        x = zeros(len(A[0]))

    # Create a vector of the diagonal elements of A
    D = diag(A)

    # And subtract them from A to get R = A - D
    R = A - diagflat(D)

    for i in range(N):
        # Iterative formula: x_new = (b - R @ x) / D
        x_new = (b - dot(R, x)) / D

        # Criterio di arresto: norma relativa del residuo
        rel_residual = linalg.norm(dot(A, x_new) - b) / linalg.norm(b)
        if rel_residual < tol:
            return x_new, N

        x = x_new

    # Se non converge entro N iterazioni restituisce comunque il valore calcolato
    return x, N
"""

def jacobi(A, b, x0=None, tol=1e-8, max_iter=20000):
    
    Metodo iterativo di Jacobi per risolvere Ax = b.

    Parametri:
        A : matrice dei coefficienti (numpy array o sparse)
        b : vettore dei termini noti (numpy array)
        x0 : vettore iniziale (se None, usa il vettore nullo)
        tol : tolleranza per il criterio di arresto
        max_iter : numero massimo di iterazioni

    Restituisce:
        x : soluzione approssimata
        num_iter : numero di iterazioni eseguite


    n = A.shape[0]  # numero di righe della matrice A (assumendo quadrata)

    # Se non viene fornito un vettore iniziale, usa il vettore nullo
    if x0 is None:
        x = np.zeros_like(b, dtype=float)  # crea un array di zeri con stesso tipo e dimensione di b
    else:
        x = x0.astype(float)  # converte il vettore iniziale in float per sicurezza

    # Estrai la diagonale di A (vettore dei coefficienti diagonali)
    D = A.diagonal()

    # Controllo: verifica che nessun elemento diagonale sia zero per evitare divisioni per zero
    if np.any(D == 0):
        raise ValueError("La matrice ha uno zero sulla diagonale, Jacobi non applicabile.")

    # Calcola il reciproco dei coefficienti diagonali
    D_inv = 1.0 / D  # vettore con gli inversi dei valori diagonali

    for k in range(max_iter):
        # Calcola il residuo r = b - A x
        r = b - A @ x

        # Aggiorna la soluzione: x_new = x + D_inv * r (formula vettorializzata)
        x_new = x + D_inv * r

        # Calcola il residuo normalizzato per il criterio di arresto
        residual_norm = np.linalg.norm(b - A @ x_new) / np.linalg.norm(b)

        # Se il residuo relativo è sotto la tolleranza, la soluzione è accettabile
        if residual_norm < tol:
            return x_new, k + 1  # convergenza raggiunta, restituisci risultato

        # Aggiorna la soluzione corrente
        x = x_new

    # Se si raggiunge il numero massimo di iterazioni senza convergenza
    print("Attenzione: massimo numero di iterazioni raggiunto")
    return x, max_iter
    """