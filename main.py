import time
from matrix_utils.config import MATRIX1_PATH, TOLERANCES
from matrix_utils.matrix_loader import prepare_system
from solver.jacobi import jacobi
import numpy as np

def main():
    # carica A e b dal file mtx
    A, b = prepare_system(MATRIX1_PATH)

    for tol in TOLERANCES:
        print("Jacobi with tolerance:", tol)
        start = time.time()
        # chiama Jacobi
        x_sol, err_rel, num_iter = jacobi(A, b, tol=tol)
        end = time.time()
        tempo = end - start

        print("Errore Relativo:", err_rel)
        print("Numero di iterazioni:", num_iter)
        print("Tempo di calcolo (s):", tempo)
        print("-" * 40)


if __name__ == "__main__":
    main()
