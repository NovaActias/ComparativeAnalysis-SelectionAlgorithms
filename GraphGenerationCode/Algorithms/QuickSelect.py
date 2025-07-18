'''
quickSelect:
    Dato un array e un indice k:
    1) Restituisce il k-esimo elemento più piccolo presente nell'array.
    2) Restituisce None se k non è un valore accettabile
'''
def quickSelect(A,k):
    #Validazione dell'indice k
    if k<1 or k>len(A):
        return None  #Se k non e' accettabile stampa None
    else:

        #Inizializzazione delle variabili
        start = 0
        end = len(A) - 1
        k -= 1

        #Ricerca del k-esimo elemento
        while start < end:
            pivotPos = partition(A, start, end)
            if k >= start and k <= pivotPos-1: #se devo cercare prima del pivot 
                end = pivotPos - 1
            elif k >= pivotPos+1 and k <= end: #se devo cercare dopo
                start = pivotPos + 1
            else: # se p = k-1
                break

        #Restituzione del risultato
        return A[k]

'''
partition:
    Dato un array e un intervallo (p, q):
    1) Sposta a sinistra del pivot tutti gli elementi minori del pivot.
    2) Sposta a destra del pivot tutti gli elementi maggiori del pivot.
    3) Restituisce la posizione del pivot.
'''
def partition(A,p,q):
    valorePivot=A[q]
    i=p-1
    for j in range(p,q+1):
        if A[j]<=valorePivot:
            i+=1
            swap(A,i,j)
    return i

'''
swap:
    Dato un array e due indici posizionali:
    1) Scambia l'elemento in posizione i con quello in posizione j
'''
def swap(A,i,j):
    temp=A[i]
    A[i]=A[j]
    A[j]=temp