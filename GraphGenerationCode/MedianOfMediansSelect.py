'''
partition:
    Dato un array e un intervallo (p, q):
    1) Posiziona l'elemento in posizione q in posizione centrale dell'array.
    2) Mette a sinistra del pivot tutti gli elementi minori del pivot.
    3) Mette a destra del pivot tutti gli elementi maggiori del pivot.
'''
def partition(A, p, q):
    pivot = A[q]
    i = p-1
    for j in range(p, q+1):
        if A[j] < pivot:
            i = i+1
            swap(A, i, j)
    i+=1
    swap(A, i, q)
    return i

'''
swap:
    Dato un array e due indici posizionali:
    1) Scambia l'elemento in posizione i con quello in posizione j
'''
def swap(A, i, j):
    t = A[i]
    A[i] = A[j]
    A[j] = t

'''
insertionSort:
    Dato un array e un intervallo (start, end):
    1) Ordina la sezione di array delimitata dall'intervallo.
    2) Non ritorna l'array. Opera sull'array passato come parametro.
'''
def insertionSort(A, start, end):
    for i in range(start, end+1):
        j = i
        while j > start and A[j] < A[j-1]:
            swap(A, j, j-1)
            j-=1

'''
recMedianOfMediansSelect:
    Dato un array, un intervallo e un indice posizionale k:
    1) Divide l'array in blocchi da 5 elementi (fatta eccezione per l'ultimo che può averne meno) e li ordina con InsertionSort.
    2) Sposta il mediano di ogni blocco in testa all'array.
    3) Richiama ricorsivamente sé stessa nella porzione di testa dell'array, contenete i mediani. 
    5) Sposta il mediano dei mediani in fondo all'array quando arriva a considerare un sub-array di testa di $5$ elementi (caso base).
    6) Chiama Partition e richiama ricorsivamente RecMedianOfMedians sulla metà di array che contiene l'elemento cercato fino a quando il mediano dei mediani non è il $k-esimo$ elemento cercato.
'''
def recMedianOfMediansSelect(A, start, end, k):
    if k<0 or k>len(A):
        return -1
    if end-start+1<=5:
        insertionSort(A, start, end)
        return(A[k-1])
    else:
        posMediano=start
        for x in range(start+4, end, 5):
            insertionSort(A, x-4, x)
            swap(A, posMediano, x-2)
            posMediano+=1
            if end-x<=5:
                insertionSort(A, x+1, end)
                swap(A, posMediano, (end+x)//2)
        recMedianOfMediansSelect(A, start, posMediano, (posMediano+start+1)//2) 
        swap(A, end, (posMediano+start+1)//2) 

    pivotPos = partition(A, start, end)
    if pivotPos == k-1:
        return A[k-1]
    elif pivotPos < k-1:
        start = pivotPos + 1
    else:
        end = pivotPos - 1
    return recMedianOfMediansSelect(A, start, end, k)

'''
medianOfMediansSelect:
    funzione di appoggio utilizzata solo per l'inizializzazione dei paramentri per iniziare l'albero delle ricorsioni
'''
def medianOfMediansSelect(A, k):
    start = 0
    end = len(A)-1
    return recMedianOfMediansSelect(A, start, end, k)

'''
Il seguente codice permette di leggere i dati passati in input dal server
'''
A = [int(x) for x in input().split(" ") if x]
k = int(input())

print(medianOfMediansSelect(A, k))