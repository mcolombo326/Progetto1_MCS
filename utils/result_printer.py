import matplotlib.pyplot as plt
from tabulate import tabulate

import utils.config as cfg
from utils.matrix_loader import prepare_system
from utils.method_solver import run_all_methods

# Funzione per stampare i risultati in tabella
def print_table_result():
    for path in cfg.MATRIX_PATH:
        A, b = prepare_system(path)
        print(f"\n➡️  Matrice: {path[5:]}")

        for tol in cfg.TOLERANCES:
            metodi, risultati = run_all_methods(A, b, tol)

            headers = ["Metodo", "Tolleranza", "Errore Relativo", "Iterazioni", "Tempo (s)"]
            print(tabulate(risultati, headers=headers, tablefmt="pretty"))


# Funzione per stampare i risultati graficamente
def plot_results():
    for path in cfg.MATRIX_PATH:
        A, b = prepare_system(path)
        print(f"\n📊 Risultati grafici per matrice: {path[5:]}")

        for tol in cfg.TOLERANCES:
            metodi, risultati = run_all_methods(A, b, tol)

            iterazioni = [r[3] for r in risultati]
            tempi = [r[4] for r in risultati]

            # 📊 Grafico iterazioni
            plt.figure(figsize=(8, 5))
            plt.bar(metodi, iterazioni, color='steelblue')
            plt.title(f"Iterazioni per metodo (tol={tol}, {path[5:]})")
            plt.ylabel("Iterazioni")
            plt.grid(axis='y', linestyle='--', alpha=0.6)
            plt.tight_layout()
            plt.show()

            # 📉 Grafico tempi
            plt.figure(figsize=(8, 5))
            plt.bar(metodi, tempi, color='salmon')
            plt.title(f"Tempo di calcolo per metodo (tol={tol}, {path[5:]})")
            plt.ylabel("Tempo (s)")
            plt.grid(axis='y', linestyle='--', alpha=0.6)
            plt.tight_layout()
            plt.show()


# Funzione per stampare i risultati in tabella e graficamente
def print_and_plot_results():
    for path in cfg.MATRIX_PATH:
        A, b = prepare_system(path)
        print(f"\n➡️  Matrice: {path[5:]}")

        for tol in cfg.TOLERANCES:
            metodi, risultati = run_all_methods(A, b, tol)

            # Stampa tabella
            headers = ["Metodo", "Tolleranza", "Errore Relativo", "Iterazioni", "Tempo (s)"]
            print(tabulate(risultati, headers=headers, tablefmt="pretty"))

            # Estrai iterazioni e tempi
            iterazioni = [r[3] for r in risultati]
            tempi = [r[4] for r in risultati]

            # Grafico iterazioni
            plt.figure(figsize=(8, 5))
            plt.bar(metodi, iterazioni, color='steelblue')
            plt.title(f"Iterazioni (tol={tol}, {path[5:]})")
            plt.ylabel("Iterazioni")
            plt.grid(axis='y', linestyle='--', alpha=0.6)
            plt.tight_layout()
            plt.show()

            # Grafico tempi
            plt.figure(figsize=(8, 5))
            plt.bar(metodi, tempi, color='salmon')
            plt.title(f"Tempo (tol={tol}, {path[5:]})")
            plt.ylabel("Tempo (s)")
            plt.grid(axis='y', linestyle='--', alpha=0.6)
            plt.tight_layout()
            plt.show()
