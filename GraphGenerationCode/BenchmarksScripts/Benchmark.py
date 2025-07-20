from Algorithms.HeapSelect import heapSelect
from Algorithms.QuickSelect import quickSelect
from Algorithms.QuickP3WSelect import quickSelectRandomized
from Algorithms.MedianOfMediansSelect import medianOfMediansSelect

import random
import time
import os
#################################### ! DISCLAIMER ! ###################################################################

# IL SEGUENTE BENCHMARK NON È STATO PENSATO PER ESSERE ESEGUITO SU WINDOWS. 
# È STATO TESTATO SU MACOSX E UBUNTU, PERTANTO SCONSIGLIAMO L'ESECUZIONE SU SISTEMI OPERATIVI DIFFERENTI.
# IN PARTICOLARE I TEMPI DI ESECUZIONE DEL BENCHMARK, SU WINDOWS, POSSONO RISULTARE ESTREMEAMENTE PIÙ ELEVATI. 
# INOLTRE IL GRAFICO NON VERRÀ GENERATO.



'''
tempoMinimoMisurabile:
    Restituisce il tempo minimo misurabile dal contatore time.monotonic().
'''
def tempoMinimoMisurabile():
    inizioMisurazione = time.monotonic()
    while time.monotonic() == inizioMisurazione:
        pass
    fineMisurazione = time.monotonic()
    return fineMisurazione - inizioMisurazione


'''
misuraTempi:
    1) Misura in modo accurato il tempo di esecuzione di ciascun algoritmo nella lista algoritmiDiSelezione.
    2) Garantisce un errore relativo inferiore all' 1%.
    3) Aggiunge il tempo medio misurato al contatore del tempo medio di ogni algoritmo eseguito.
'''
tMinMisurabile = tempoMinimoMisurabile() * (1 + (1 / 0.01))  # max_rel_error = 1% = 0.01

def misuraTempi(array, k, algoritmiDiSelezione, tempiMedi):
    for i, func in enumerate(algoritmiDiSelezione):
        count = 0
        tempoIniziale = time.monotonic()
        while time.monotonic() - tempoIniziale < tMinMisurabile:
            func(array.copy(), k)
            count += 1
        durata = time.monotonic() - tempoIniziale
        tempiMedi[i] += (durata / count)


'''
benchmark:
    1) Misura il tempo medio di esecuzione di ciascun algoritmo nella lista algoritmiDiSelezione.
    2) Genera passiSuccessione(100) array di dimensione crescente seguendo una serie geometrica. 
        La dimensione degli array va da 100 a 100000.
    3) Ad ogni passo vengono eseguiti testPerOgniN(500) test con k random per garantire che i tempi di esecuzione degli algoritmi siano medi.
    4) In ogni test viene riempito l'array di dimensione prefissata, con valori casuali in un range [-1000,1000].
    5) In ogni test viene misurato il tempo di esecuzione.
    6) Alla fine dei test viene salvata la media dei tempi per quel passo della successione in una lista di liste tempiMedi.
    7) Ad ogni passo, dopo aver eseguito i testPerOgniN(500), viene salvata la dimensione dell'array su cui è stato eseguito quel passo.
    8) Alla fine dei 100 passi, vengono salvati i dati dei tempi medi in dei file separati. Uno per ogni algoritmo. 
    9) Infine, viene richiamata la funzione che disegna il grafico prendendo i dati dai file generati.
'''
# Lista degli algoritmi di selezione
algoritmiDiSelezione = [quickSelect, quickSelectRandomized, heapSelect, medianOfMediansSelect]
nomi_algoritmiDiSelezione = ["QuickSelect", "QuickSelectRandomizedPTW", "HeapSelect", "MedianOfMediansSelect"]


# Inizializza le liste per i tempi medi
tempiMedi = [[] for _ in algoritmiDiSelezione]     #lista di tante liste quanti sono gli algoritmi di selezione 
dimensioneArrayGenerati = []

def benchmark():
    A = 100  # Inizio della serie geometrica
    B = (100000 / 100) ** (1 / 99)  # Calcolo di B per ottenere n finale di 100000 (radice 99-esima)
    passiSuccessione = 100
    testPerOgniN = 500


    for i in range(passiSuccessione):
        dimArray = int(A * (B ** i))
        print("Eseguo il passo {} / {} della successione \t len(A) : {}".format(i+1, passiSuccessione, dimArray))
        
        # Inizializza i tempi medi per questa dimensione dell'array
        tempiMediPasso = [0] * len(algoritmiDiSelezione)
    
        for _ in range(testPerOgniN):
            array = [random.randint(-1000, 1000) for _ in range(dimArray)]
            k = random.randint(1, dimArray)
            misuraTempi(array, k, algoritmiDiSelezione, tempiMediPasso)
            
        for j in range(len(algoritmiDiSelezione)):
            tempiMedi[j].append(tempiMediPasso[j] / testPerOgniN)

        dimensioneArrayGenerati.append(dimArray)


    # Imposta la directory di lavoro relativa alla posizione di questo file
    directoryPath = os.path.join(os.path.dirname(__file__), 'RisultatiBenchmark')

    # Verifica se la cartella esiste, altrimenti creala
    if not os.path.exists(directoryPath):
        os.makedirs(directoryPath)

    # Costruisci i percorsi dei file relativi a questa directory
    dimensioniArray_path = os.path.join(directoryPath, 'dimensioniArray.txt')

    # Scrive la dimensione di ogni array generato in un file. 
    with open(dimensioniArray_path, 'w') as f:
        for n in dimensioneArrayGenerati:
            f.write(f"{n}\n")

    # Scrive i risultati dei tempi di esecuzione in file di testo separati. Uno per ogni algoritmo. 
    for i, nome in enumerate(nomi_algoritmiDiSelezione):
        file_path = os.path.join(directoryPath, f'tempi{nome}.txt')
        with open(file_path, 'w') as f:
            for tempo in tempiMedi[i]:
                f.write(f"{tempo}\n")

print("Benchmark partito")
benchmark()
print("Benchmark terminato")