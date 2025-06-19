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

        # Formatta tol in notazione scientifica come stringa
        tol_str = "{:.0e}".format(tol)

        # Sovrascrivi la colonna Tolleranza dei risultati stampati a schermo
        risultati_formattati = []
        for r in risultati:
            r_formattato = list(r)  # copia
            r_formattato[1] = tol_str
            risultati_formattati.append(r_formattato)

        print(tabulate(risultati_formattati, headers=headers, tablefmt="pretty"))

        for m, r in zip(metodi, risultati):
            err_rel_per_method[m].append(r[2])
            iter_per_method[m].append(r[3])
            time_per_method[m].append(r[4])

    return err_rel_per_method, iter_per_method, time_per_method


def plot_error_rel_vs_tol(err_rel_per_method, path):
    tolleranze = np.arange(len(cfg.TOLERANCES))
    bar_width = 0.2

    fig, ax = plt.subplots(figsize=(10, 6))
    for idx, metodo in enumerate(err_rel_per_method):
        valori = err_rel_per_method[metodo]
        posizioni = tolleranze + idx * bar_width
        ax.bar(posizioni, valori, width=bar_width, label=metodo)

    ax.set_yscale('log')
    ax.set_xlabel("Tolleranza (indice)")
    ax.set_ylabel("Errore Relativo")
    ax.minorticks_off()
    ax.set_title(f"Errore Relativo per Tolleranza — {path[5:]}")
    ax.set_xticks(tolleranze + bar_width * 1.5)
    ax.set_xticklabels([f"{t:.0e}" for t in cfg.TOLERANCES])
    ax.grid(True, which="major", linestyle='--', alpha=0.4)
    ax.legend()
    fig.tight_layout()
    return fig


def plot_iter_vs_tol(iter_per_method, path):
    fig, ax = plt.subplots(figsize=(8, 6))
    for metodo in iter_per_method:
        ax.plot(cfg.TOLERANCES, iter_per_method[metodo], marker='o', label=metodo)
    ax.set_xscale('log')
    ax.set_xlabel("Tolleranza")
    ax.set_ylabel("Iterazioni")
    ax.minorticks_off()
    ax.set_title(f"Iterazioni vs Tolleranza — {path[5:]}")
    ax.grid(True, which="major", linestyle='--', alpha=0.4)
    ax.legend()
    fig.tight_layout()
    return fig

def plot_time_vs_tol(time_per_method, path):
    fig, ax = plt.subplots(figsize=(8, 6))
    for metodo in time_per_method:
        ax.plot(cfg.TOLERANCES, time_per_method[metodo], marker='o', label=metodo)
    ax.set_xscale('log')
    ax.set_xlabel("Tolleranza")
    ax.set_ylabel("Tempo (s)")
    ax.minorticks_off()
    ax.set_title(f"Tempo di Calcolo vs Tolleranza — {path[5:]}")
    ax.grid(True, which="major", linestyle='--', alpha=0.4)
    ax.legend()
    fig.tight_layout()
    return fig