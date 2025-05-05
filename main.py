from matrix_utils.matrix_loader import load_sparse_matrix, generate_rhs_and_solution
from matrix_utils.metrics import relative_error
from matrix_utils.timer import Timer
from solver.conjugate_gradient import ConjugateGradientSolver
from solver.gauss_seidel import GaussSeidelSolver
from solver.gradient import GradientSolver
from solver.jacobi import JacobiSolver

TOLERANCES = [1e-4, 1e-6, 1e-8, 1e-10]

if __name__ == "__main__":
    A = load_sparse_matrix("data/spa1.mtx")
    b, x_true = generate_rhs_and_solution(A)

    solvers = [
        ("Jacobi", JacobiSolver),
        #("Gauss-Seidel", GaussSeidelSolver),
        #("Gradient", GradientSolver),
        #("Conjugate Gradient", ConjugateGradientSolver),
    ]

    for tol in TOLERANCES:
        print(f"\n===== Risultati con tolleranza {tol:.0e} =====")
        for name, SolverClass in solvers:
            solver = SolverClass(A, b, tol)
            try:
                with Timer() as t:
                    x_approx, iters, elapsed = solver.solve()
                err = relative_error(x_approx, x_true)
                print(f"[{name:20}] iter={iters:5d} | err={err:.2e} | time={elapsed:.4f}s")
            except ValueError as e:
                print(f"[{name:20}] Non converge: {str(e)}")