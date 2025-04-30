from scipy.io import mmread
import numpy as np
import scipy.sparse as sp

def load_sparse_matrix(path):
    """Carica una matrice sparsa da file .mtx"""
    A = mmread(path)
    if not sp.isspmatrix_csr(A):
        A = A.tocsr()
    return A

def generate_rhs_and_solution(A):
    """Genera vettore b = A * x con x = [1, ..., 1]"""
    x_true = np.ones(A.shape[0])
    b = A @ x_true
    return b, x_true