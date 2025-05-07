from scipy.io import mmread
import numpy as np

def load_matrix_dense(file_path):
    """
    Legge una matrice da file .mtx e la restituisce come numpy array denso.

    Parametri:
        file_path : percorso del file .mtx

    Restituisce:
        A : matrice dei coefficienti (numpy array denso)
    """
    A_sparse = mmread(file_path)    # legge la matrice in formato sparse
    A = A_sparse.toarray()          # converte in matriceda densa
    return A

def prepare_system(file_path):
    """
    Carica una matrice da file .mtx e prepara il sistema Ax = b per Jacobi.

    Parametri:
        file_path : percorso del file .mtx

    Restituisce:
        A : matrice dei coefficienti (numpy array)
        b : vettore dei termini noti calcolato come b = A @ x_esatta
    """
    A = load_matrix_dense(file_path)
    n = A.shape[0]

    # soluzione esatta: vettore di tutti 1
    x_exact = np.ones(n)

    # calcolo b = A * x_esatta
    b = A @ x_exact

    return A, b
