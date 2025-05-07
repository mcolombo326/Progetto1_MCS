import os

import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate

import utils.config as cfg
from utils.matrix_loader import prepare_system
from utils.method_solver import run_all_methods

# Funzione per esportare tabelle e grafici nella cartella "risultati_report"
def export_results(output_folder="risultati_report"):
    os.makedirs(output_folder, exist_ok=True)

    for path in cfg.MATRIX_PATH:
        A, b = prepare_system(path)
        matrice_nome = path[5:]

        for tol in cfg.TOLERANCES:
            metodi, risultati = run_all_methods(A, b, tol)

            # Salva CSV
            df = pd.DataFrame(risultati, columns=["Metodo", "Tolleranza", "Errore Relativo", "Iterazioni", "Tempo (s)"])
            csv_name = f"{output_folder}/{matrice_nome}_tol{tol}_risultati.csv"
            df.to_csv(csv_name, index=False)

            # Estrai iterazioni e tempi per i grafici
            iterazioni = [r[3] for r in risultati]
            tempi = [r[4] for r in risultati]

            #Grafico iterazioni
            plt.figure(figsize=(8, 5))
            plt.bar(metodi, iterazioni, color='steelblue')
            plt.title(f"Iterazioni (tol={tol}, {matrice_nome})")
            plt.ylabel("Iterazioni")
            plt.grid(axis='y', linestyle='--', alpha=0.6)
            plt.tight_layout()
            iter_plot_name = f"{output_folder}/{matrice_nome}_tol{tol}_iterazioni.png"
            plt.savefig(iter_plot_name)
            plt.close()

            #Grafico tempi
            plt.figure(figsize=(8, 5))
            plt.bar(metodi, tempi, color='salmon')
            plt.title(f"Tempo di calcolo (tol={tol}, {matrice_nome})")
            plt.ylabel("Tempo (s)")
            plt.grid(axis='y', linestyle='--', alpha=0.6)
            plt.tight_layout()
            time_plot_name = f"{output_folder}/{matrice_nome}_tol{tol}_tempi.png"
            plt.savefig(time_plot_name)
            plt.close()

    print(f"\nTutti i risultati e grafici salvati in: {output_folder}")

# Funzione per esportare tabelle e grafici nella cartella "risultati_report" e stampare a console
def export_and_print_results(output_folder="risultati_report"):
    os.makedirs(output_folder, exist_ok=True)

    for path in cfg.MATRIX_PATH:
        A, b = prepare_system(path)
        matrice_nome = path[5:]

        for tol in cfg.TOLERANCES:
            metodi, risultati = run_all_methods(A, b, tol)

            #Stampa tabella a console
            print(f"\nMatrice: {matrice_nome}, Tolleranza: {tol}")
            headers = ["Metodo", "Tolleranza", "Errore Relativo", "Iterazioni", "Tempo (s)"]
            print(tabulate(risultati, headers=headers, tablefmt="pretty"))

            #Salva CSV
            df = pd.DataFrame(risultati, columns=headers)
            csv_name = f"{output_folder}/{matrice_nome}_tol{tol}_risultati.csv"
            df.to_csv(csv_name, index=False)

            #Estrai iterazioni e tempi
            iterazioni = [r[3] for r in risultati]
            tempi = [r[4] for r in risultati]

            #Grafico iterazioni
            plt.figure(figsize=(8, 5))
            plt.bar(metodi, iterazioni, color='steelblue')
            plt.title(f"Iterazioni (tol={tol}, {matrice_nome})")
            plt.ylabel("Iterazioni")
            plt.grid(axis='y', linestyle='--', alpha=0.6)
            plt.tight_layout()
            iter_plot_name = f"{output_folder}/{matrice_nome}_tol{tol}_iterazioni.png"
            plt.savefig(iter_plot_name)
            plt.close()

            #Grafico tempi
            plt.figure(figsize=(8, 5))
            plt.bar(metodi, tempi, color='salmon')
            plt.title(f"Tempo di calcolo (tol={tol}, {matrice_nome})")
            plt.ylabel("Tempo (s)")
            plt.grid(axis='y', linestyle='--', alpha=0.6)
            plt.tight_layout()
            time_plot_name = f"{output_folder}/{matrice_nome}_tol{tol}_tempi.png"
            plt.savefig(time_plot_name)
            plt.close()

    print(f"\nTutti i risultati, grafici e tabelle stampate salvati in: {output_folder}")