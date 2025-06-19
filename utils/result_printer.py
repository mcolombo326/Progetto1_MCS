from utils.matrix_loader import prepare_system
from utils.result_plotter import *


# Funzione per stampare SOLO le tabelle
def print_table_result():
    for path in cfg.MATRIX_PATH:
        A, b = prepare_system(path)
        print(f"\nMatrice: {path[5:]}")
        collect_results(A, b)


# Funzione per stampare SOLO i grafici
def plot_results():
    for path in cfg.MATRIX_PATH:
        A, b = prepare_system(path)
        print(f"\nRisultati grafici per matrice: {path[5:]}")

        err_rel, iterazioni, tempi = collect_results(A, b)

        fig1 = plot_error_rel_vs_tol(err_rel, path)
        fig1.show()

        fig2 = plot_iter_vs_tol(iterazioni, path)
        fig2.show()

        fig3 = plot_time_vs_tol(tempi, path)
        fig3.show()


# Funzione per stampare TABELLE + GRAFICI insieme
def print_and_plot_results():
    for path in cfg.MATRIX_PATH:
        A, b = prepare_system(path)
        print(f"\nMatrice: {path[5:]}")

        err_rel, iterazioni, tempi = collect_results(A, b)

        fig1 = plot_error_rel_vs_tol(err_rel, path)
        fig1.show()

        fig2 = plot_iter_vs_tol(iterazioni, path)
        fig2.show()

        fig3 = plot_time_vs_tol(tempi, path)
        fig3.show()

