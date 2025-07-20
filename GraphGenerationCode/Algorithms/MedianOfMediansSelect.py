'''
partition:
    Given an array and an interval (p, q):
    1) Places the element at position q in the central position of the array.
    2) Places all elements smaller than the pivot to the left of the pivot.
    3) Places all elements greater than the pivot to the right of the pivot.
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
    Given an array and two positional indices:
    1) Swaps the element at position i with the one at position j
'''
def swap(A, i, j):
    t = A[i]
    A[i] = A[j]
    A[j] = t

'''
insertionSort:
    Given an array and an interval (start, end):
    1) Sorts the array section delimited by the interval.
    2) Does not return the array. Operates on the array passed as parameter.
'''
def insertionSort(A, start, end):
    for i in range(start, end+1):
        j = i
        while j > start and A[j] < A[j-1]:
            swap(A, j, j-1)
            j-=1

'''
recMedianOfMediansSelect:
    Given an array, an interval and a positional index k:
    1) Divides the array into blocks of 5 elements (except for the last one which may have fewer) and sorts them with InsertionSort.
    2) Moves the median of each block to the head of the array.
    3) Recursively calls itself on the head portion of the array, containing the medians. 
    5) Moves the median of medians to the end of the array when it reaches considering a head sub-array of 5 elements (base case).
    6) Calls Partition and recursively calls RecMedianOfMedians on the half of the array that contains the sought element until the median of medians is the k-th element sought.
'''
def recMedianOfMediansSelect(A, start, end, k):
    if k<0 or k>len(A):
        return -1
    if end-start+1<=5:
        insertionSort(A, start, end)
        return(A[k-1])
    else:
        medianPos=start
        for x in range(start+4, end, 5):
            insertionSort(A, x-4, x)
            swap(A, medianPos, x-2)
            medianPos+=1
            if end-x<=5:
                insertionSort(A, x+1, end)
                swap(A, medianPos, (end+x)//2)
        recMedianOfMediansSelect(A, start, medianPos, (medianPos+start+1)//2) 
        swap(A, end, (medianPos+start+1)//2) 

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
    support function used only for parameter initialization to start the recursion tree
'''
def medianOfMediansSelect(A, k):
    start = 0
    end = len(A)-1
    return recMedianOfMediansSelect(A, start, end, k)

'''
The following code allows reading data passed as input from the server
'''
A = [int(x) for x in input().split(" ") if x]
k = int(input())

print(medianOfMediansSelect(A, k))