import os
import sys
import time

from utils.matrix_loader import prepare_system
from utils.result_exporter import export_results


def main():
    while(0<1):
        print("Scegli un'opzione:")
        print("1 - Analizza tutte le matrici nella cartella 'data/'")
        print("2 - Analizza una matrice da file .mtx")
        print("9 - Per terminare il programma")

        scelta = input("\nInserisci 1, 2, 9: ")

        if scelta == "1":
            print("\nAvvio analisi su tutte le matrici nella cartella 'data/'")
            export_results()

        elif scelta == "2":
            path = input("Inserisci il path completo del file .mtx (il path deve essere senza apici): ")
            if not os.path.exists(path):
                print("Il file specificato non esiste.")
                return

            print(f"\nAvvio analisi sulla matrice {path}")
            A, b = prepare_system(path)
            print_and_plot_results_custom(A, b, path)
            print(f"")

        elif scelta == "9":
            GREEN = "\033[92m"  # Verde chiaro
            RESET = "\033[0m"  # Reset colore
            length = 30

            print("\nChiusura in corso")
            for i in range(length + 1):
                percent = int(i / length * 100)
                bar = GREEN + "█" * i + RESET + " " * (length - i)
                sys.stdout.write(f"\r{percent:3}% [{bar}]")
                sys.stdout.flush()
                time.sleep(0.1)
            print("\nProgramma terminato.")
            break
        else:
            print("Scelta non valida. Riprova.\n")


# Funzione per stampare e plottare una singola matrice personalizzata
def print_and_plot_results_custom(A, b, path):
    from utils.result_plotter import collect_results, plot_error_rel_vs_tol, plot_iter_vs_tol, plot_time_vs_tol

    err_rel, iterazioni, tempi = collect_results(A, b)
    plot_error_rel_vs_tol(err_rel, path)
    plot_iter_vs_tol(iterazioni, path)
    plot_time_vs_tol(tempi, path)


if __name__ == "__main__":
    main()
