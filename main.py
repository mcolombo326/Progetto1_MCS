import time

import matrix_utils.config as cfg
from matrix_utils.matrix_loader import prepare_system
from solver.jacobi import jacobi
from solver.gauss_seidel import gauss_seidel
from solver.gradient import gradient
from solver.conjugate_gradient import conjugate_gradient


def main():

    for path in cfg.MATRIX_PATH:
        # carica A e b dal file mtx
        A, b = prepare_system(path)

        print("\nMatrice:", path[4:])

        for tol in cfg.TOLERANCES:
            print("Conjugate Gradient with tolerance:", tol)
            start = time.time()
            # chiama Jacobi
            x_sol, err_rel, num_iter = conjugate_gradient(A, b, tol=tol, max_iter=cfg.MAX_ITER)
            end = time.time()
            tempo = end - start

            print("Errore Relativo:", err_rel)
            print("Numero di iterazioni:", num_iter)
            print("Tempo di calcolo (s):", tempo)
            print("-" * 40)


if __name__ == "__main__":
    main()
