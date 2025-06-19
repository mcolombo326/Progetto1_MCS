import os
import shutil

import matplotlib.pyplot as plt
import pandas as pd

import utils.config as cfg
from utils.matrix_loader import prepare_system
from utils.result_printer import (
    collect_results,
    plot_error_rel_vs_tol,
    plot_iter_vs_tol,
    plot_time_vs_tol
)


# Funzione per svuotare la cartella di output
def clear_output_folder(folder):
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)

# Funzione per esportare risultati e grafici

def export_results(output_folder="risultati_report"):
    clear_output_folder(output_folder)

    for path in cfg.MATRIX_PATH:
        A, b = prepare_system(path)
        matrice_nome = path[5:]
        print(f"\nMatrice: {path[5:]}")

        err_rel, iterazioni, tempi = collect_results(A, b)

        # Salva tabelle CSV per ogni tolleranza
        for i, tol in enumerate(cfg.TOLERANCES):
            dati = []
            for metodo in err_rel:
                dati.append([
                    metodo, tol, err_rel[metodo][i], iterazioni[metodo][i], tempi[metodo][i]
                ])

            df = pd.DataFrame(dati, columns=["Metodo", "Tolleranza", "Errore Relativo", "Iterazioni", "Tempo (s)"])
            csv_name = f"{output_folder}/{matrice_nome}_tol{tol}_risultati.csv"
            df.to_csv(csv_name, index=False)

        # Esporta grafici già pronti con funzioni di result_printer
        # Salvando invece di mostrare


        plot_error_rel_vs_tol(err_rel, path)
        plt.savefig(f"{output_folder}/{matrice_nome}_errori.png")
        plt.close()


        plot_iter_vs_tol(iterazioni, path)
        plt.savefig(f"{output_folder}/{matrice_nome}_iterazioni.png")
        plt.close()


        plot_time_vs_tol(tempi, path)
        plt.savefig(f"{output_folder}/{matrice_nome}_tempi.png")
        plt.close()

    print(f"\nTutti i risultati e grafici esportati in: {output_folder}")
