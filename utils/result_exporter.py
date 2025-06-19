import os
import shutil

import matplotlib.pyplot as plt
import pandas as pd

import utils.config as cfg
from utils.matrix_loader import prepare_system
from utils.result_plotter import format_scientific
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
        print(f"\nMatrice: {matrice_nome}")

        err_rel, iterazioni, tempi = collect_results(A, b)

        dati_totali = []  # raccolta di tutte le righe

        for i, tol in enumerate(cfg.TOLERANCES):
            for metodo in err_rel:
                tol_str = format_scientific(cfg.TOLERANCES[i], 0)
                dati_totali.append([
                    metodo, tol_str, format_scientific(err_rel[metodo][i]),
                    iterazioni[metodo][i],
                    format_scientific(tempi[metodo][i])
                ])

        df = pd.DataFrame(dati_totali, columns=["Metodo", "Tolleranza", "Errore Relativo", "Iterazioni", "Tempo (s)"])
        csv_name = f"{output_folder}/{matrice_nome}_risultati_completi.csv"
        df.to_csv(csv_name, index=False)

        # Grafici come prima (assumendo che plot_... ritornino figure)
        fig = plot_error_rel_vs_tol(err_rel, path)
        fig.savefig(f"{output_folder}/{matrice_nome}_errori.png")
        fig.show()
        plt.close(fig)

        fig_iter = plot_iter_vs_tol(iterazioni, path)
        fig_iter.savefig(f"{output_folder}/{matrice_nome}_iterazioni.png")
        fig_iter.show()
        plt.close(fig_iter)

        fig_time = plot_time_vs_tol(tempi, path)
        fig_time.savefig(f"{output_folder}/{matrice_nome}_tempi.png")
        fig_time.show()
        plt.close(fig_time)

    print(f"\nTutti i risultati e grafici esportati in: {output_folder}")
