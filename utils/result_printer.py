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

        # Dizionari per raccogliere metriche per ogni metodo alle varie tolleranze
        err_rel_per_method = {m: [] for m in ["Jacobi", "Gauss-Seidel", "Gradient", "Conj. Gradient"]}
        iter_per_method = {m: [] for m in err_rel_per_method}
        time_per_method = {m: [] for m in err_rel_per_method}

        for tol in cfg.TOLERANCES:
            metodi, risultati = run_all_methods(A, b, tol)

            for m, r in zip(metodi, risultati):
                err_rel_per_method[m].append(r[2])
                iter_per_method[m].append(r[3])
                time_per_method[m].append(r[4])

        # 📈 Grafico errore relativo vs tolleranza (scala log-log)
        plt.figure(figsize=(8, 6))
        for metodo in err_rel_per_method:
            plt.plot(cfg.TOLERANCES, err_rel_per_method[metodo], marker='o', label=metodo)
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel("Tolleranza richiesta")
        plt.ylabel("Errore relativo ottenuto")
        plt.minorticks_off()
        plt.title(f"Errore Relativo vs Tolleranza per {path[5:]}")
        plt.grid(True, which="major", linestyle='--', alpha=0.4)
        plt.legend()
        plt.tight_layout()
        plt.show()

        # 📈 Grafico iterazioni vs tolleranza
        plt.figure(figsize=(8, 6))
        for metodo in iter_per_method:
            plt.plot(cfg.TOLERANCES, iter_per_method[metodo], marker='o', label=metodo)
        plt.xscale('log')
        plt.xlabel("Tolleranza richiesta")
        plt.ylabel("Numero Iterazioni")
        plt.minorticks_off()
        plt.title(f"Iterazioni vs Tolleranza per {path[5:]}")
        plt.grid(True, which="major", linestyle='--', alpha=0.4)
        plt.legend()
        plt.tight_layout()
        plt.show()

        # 📈 Grafico tempo di calcolo vs tolleranza
        plt.figure(figsize=(8, 6))
        for metodo in time_per_method:
            plt.plot(cfg.TOLERANCES, time_per_method[metodo], marker='o', label=metodo)
        plt.xscale('log')
        plt.xlabel("Tolleranza richiesta")
        plt.ylabel("Tempo di calcolo (s)")
        plt.minorticks_off()
        plt.title(f"Tempo di Calcolo vs Tolleranza per {path[5:]}")
        plt.grid(True, which="major", linestyle='--', alpha=0.4)
        plt.legend()
        plt.tight_layout()
        plt.show()



# Funzione per stampare i risultati in tabella e graficamente
def print_and_plot_results():
    for path in cfg.MATRIX_PATH:
        A, b = prepare_system(path)
        print(f"\n➡️  Matrice: {path[5:]}")

        # Dizionari per raccogliere metriche per ogni metodo alle varie tolleranze
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

        # 📈 Grafico errore relativo vs tolleranza
        plt.figure(figsize=(8, 6))
        for metodo in err_rel_per_method:
            plt.plot(cfg.TOLERANCES, err_rel_per_method[metodo], marker='o', label=metodo)
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel("Tolleranza richiesta")
        plt.ylabel("Errore relativo ottenuto")
        plt.minorticks_off()
        plt.title(f"Errore Relativo vs Tolleranza per {path[5:]}")
        plt.grid(True, which="major", linestyle='--', alpha=0.4)
        plt.legend()
        plt.tight_layout()
        plt.show()

        # 📈 Grafico iterazioni vs tolleranza
        plt.figure(figsize=(8, 6))
        for metodo in iter_per_method:
            plt.plot(cfg.TOLERANCES, iter_per_method[metodo], marker='o', label=metodo)
        plt.xscale('log')
        plt.xlabel("Tolleranza richiesta")
        plt.ylabel("Numero Iterazioni")
        plt.minorticks_off()
        plt.title(f"Iterazioni vs Tolleranza per {path[5:]}")
        plt.grid(True, which="major", linestyle='--', alpha=0.4)
        plt.legend()
        plt.tight_layout()
        plt.show()

        # 📈 Grafico tempo di calcolo vs tolleranza
        plt.figure(figsize=(8, 6))
        for metodo in time_per_method:
            plt.plot(cfg.TOLERANCES, time_per_method[metodo], marker='o', label=metodo)
        plt.xscale('log')
        plt.xlabel("Tolleranza richiesta")
        plt.ylabel("Tempo di calcolo (s)")
        plt.minorticks_off()
        plt.title(f"Tempo di Calcolo vs Tolleranza per {path[5:]}")
        plt.grid(True, which="major", linestyle='--', alpha=0.4)
        plt.legend()
        plt.tight_layout()
        plt.show()