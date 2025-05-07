import matrix_utils.config as cfg
from matrix_utils.matrix_loader import prepare_system
from method.conjugate_gradient import conjugate_gradient
from method.gauss_seidel import gauss_seidel
from method.gradient import gradient
from method.jacobi import jacobi
from matrix_utils.method_solver import run_solver


def main():
    for path in cfg.MATRIX_PATH:
        # carica A e b dal file mtx
        A, b = prepare_system(path)

        print(f"\n➡️  Matrice: {path[5:]}")

        for tol in cfg.TOLERANCES:
            # Jacobi
            run_solver("Jacobi", jacobi, A, b, tol)
            # Gauss-Seidel
            run_solver("Gauss-Seidel", gauss_seidel, A, b, tol)
            # Gradient
            run_solver("Gradient", gradient, A, b, tol)
            # Conjugate Gradient
            run_solver("Conjugate Gradient", conjugate_gradient, A, b, tol)


if __name__ == "__main__":
    main()
