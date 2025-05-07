import time

import utils.config as cfg
from method.conjugate_gradient import conjugate_gradient
from method.gauss_seidel import gauss_seidel
from method.gradient import gradient
from method.jacobi import jacobi

# Funzione per runnare un metodo iterativo e calcolare tempo, errore relativo e numero iterazioni
def run_solver(solver_func, A, b, tol):
    """
    Esegue un metodo iterativo, calcola tempo, errore relativo e numero iterazioni.

    Parametri:
        solver_name : nome del metodo (stringa)
        solver_func : funzione di risoluzione (Jacobi, Gauss-Seidel...)
        A, b : matrice dei coefficienti e termine noto
        tol : tolleranza

    Stampa i risultati.
    """
    start = time.time()
    x_sol, err_rel, num_iter = solver_func(A, b, tol=tol, max_iter=cfg.MAX_ITER)
    elapsed_time = time.time() - start

    return err_rel, num_iter, elapsed_time

# Funzione per runnare tutti i metodi iterativi e restituire i risultati
def run_all_methods(A, b, tol):
    metodi = ["Jacobi", "Gauss-Seidel", "Gradient", "Conj. Gradient"]
    funzioni = [jacobi, gauss_seidel, gradient, conjugate_gradient]

    risultati = []

    for nome, funzione in zip(metodi, funzioni):
        err_rel, iterazioni, tempo = run_solver(funzione, A, b, tol)
        risultati.append([nome, tol, err_rel, iterazioni, tempo])

    return metodi, risultati
