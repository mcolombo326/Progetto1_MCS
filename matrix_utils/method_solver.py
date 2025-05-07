import time
import matrix_utils.config as cfg

def run_solver(solver_name, solver_func, A, b, tol):
    """
    Esegue un metodo iterativo, calcola tempo, errore relativo e numero iterazioni.

    Parametri:
        solver_name : nome del metodo (stringa)
        solver_func : funzione di risoluzione (Jacobi, Gauss-Seidel...)
        A, b : matrice dei coefficienti e termine noto
        tol : tolleranza

    Stampa i risultati.
    """
    print(f"{solver_name} con tolleranza: {tol}")
    start = time.time()

    x_sol, err_rel, num_iter = solver_func(A, b, tol=tol, max_iter=cfg.MAX_ITER)

    elapsed_time = time.time() - start

    print(f"  Errore relativo: {err_rel:.2e}")
    print(f"  Iterazioni: {num_iter}")
    print(f"  Tempo di calcolo: {elapsed_time:.3f} s")
    print("-" * 50)