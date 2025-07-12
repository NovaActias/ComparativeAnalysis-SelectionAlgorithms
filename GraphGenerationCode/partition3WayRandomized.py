import random

def swap(A,i,j):
    temp=A[i]
    A[i]=A[j]
    A[j]=temp
    
def partition(A,start,end, pPos):
    swap(A, pPos, end)
    valorePivot=A[end]
    i=start-1
    for j in range(start,end+1):
        if A[j]<=valorePivot:
            i+=1
            swap(A,i,j)
    return i


def partition3WayRandomized(A, start, end):   
    pos_a = partition(A, start, end, random.randint(start, end))
    if pos_a < (start + end)//2:
        if pos_a != end:
            pos_b = partition(A, pos_a+1, end, random.randint(pos_a+1, end))
        else:
            pos_b = end
    else:
        if pos_a != start:
            pos_b = partition(A, start, pos_a-1, random.randint(start, pos_a-1))
        else:
            pos_b = start

    if pos_a < pos_b:
        return (pos_a, pos_b)
    else:
        return (pos_b, pos_a)
    
def quickSelectRandomized(A,k):
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
            pos_a, pos_b = partition3WayRandomized(A, start, end)
            if k == pos_a or k == pos_b:
                break
            elif k < pos_a:
                end = pos_a
            elif k < pos_b:
                start = pos_a
                end = pos_b
            else:
                start = pos_b
                
        #Restituzione del risultato
        return A[k]
