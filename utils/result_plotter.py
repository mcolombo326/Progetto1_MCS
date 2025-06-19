import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

import utils.config as cfg
from utils.method_solver import run_all_methods


def collect_results(A, b):
    err_rel_per_method = {m: [] for m in ["Jacobi", "Gauss-Seidel", "Gradient", "Conj. Gradient"]}
    iter_per_method = {m: [] for m in err_rel_per_method}
    time_per_method = {m: [] for m in err_rel_per_method}

    for tol in cfg.TOLERANCES:
        metodi, risultati = run_all_methods(A, b, tol)

        # Stampa tabella per questa tolleranza
        headers = ["Metodo", "Tolleranza", "Errore Relativo", "Iterazioni", "Tempo (s)"]
        print(tabulate(risultati, headers=headers, tablefmt="pretty"))

        for m, r in zip(metodi, risultati):
            err_rel_per_method[m].append(r[2])
            iter_per_method[m].append(r[3])
            time_per_method[m].append(r[4])

    return err_rel_per_method, iter_per_method, time_per_method


def plot_error_rel_vs_tol(err_rel_per_method, path):
    tolleranze = np.arange(len(cfg.TOLERANCES))
    bar_width = 0.2

    plt.figure(figsize=(10, 6))
    for idx, metodo in enumerate(err_rel_per_method):
        valori = err_rel_per_method[metodo]
        posizioni = tolleranze + idx * bar_width
        plt.bar(posizioni, valori, width=bar_width, label=metodo)

    plt.yscale('log')
    plt.xlabel("Tolleranza (indice)")
    plt.ylabel("Errore Relativo")
    plt.minorticks_off()
    plt.title(f"Errore Relativo per Tolleranza — {path[5:]}")
    plt.xticks(tolleranze + bar_width * 1.5, [f"{t:.0e}" for t in cfg.TOLERANCES])
    plt.grid(True, which="major", linestyle='--', alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_iter_vs_tol(iter_per_method, path):
    plt.figure(figsize=(8, 6))
    for metodo in iter_per_method:
        plt.plot(cfg.TOLERANCES, iter_per_method[metodo], marker='o', label=metodo)
    plt.xscale('log')
    plt.xlabel("Tolleranza")
    plt.ylabel("Iterazioni")
    plt.minorticks_off()
    plt.title(f"Iterazioni vs Tolleranza — {path[5:]}")
    plt.grid(True, which="major", linestyle='--', alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_time_vs_tol(time_per_method, path):
    plt.figure(figsize=(8, 6))
    for metodo in time_per_method:
        plt.plot(cfg.TOLERANCES, time_per_method[metodo], marker='o', label=metodo)
    plt.xscale('log')
    plt.xlabel("Tolleranza")
    plt.ylabel("Tempo (s)")
    plt.minorticks_off()
    plt.title(f"Tempo di Calcolo vs Tolleranza — {path[5:]}")
    plt.grid(True, which="major", linestyle='--', alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.show()