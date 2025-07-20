'''
quickSelect:
    Given an array and an index k:
    1) Returns the k-th smallest element present in the array.
    2) Returns None if k is not an acceptable value
'''
def quickSelect(A,k):
    # Validation of index k
    if k<1 or k>len(A):
        return None  # If k is not acceptable, return None
    else:

        # Variable initialization
        start = 0
        end = len(A) - 1
        k -= 1

        # Search for the k-th element
        while start < end:
            pivotPos = partition(A, start, end)
            if k >= start and k <= pivotPos-1: # if I need to search before the pivot 
                end = pivotPos - 1
            elif k >= pivotPos+1 and k <= end: # if I need to search after
                start = pivotPos + 1
            else: # if p = k-1
                break

        # Return the result
        return A[k]

'''
partition:
    Given an array and an interval (p, q):
    1) Moves all elements smaller than the pivot to the left of the pivot.
    2) Moves all elements greater than the pivot to the right of the pivot.
    3) Returns the position of the pivot.
'''
def partition(A,p,q):
    pivotValue=A[q]
    i=p-1
    for j in range(p,q+1):
        if A[j]<=pivotValue:
            i+=1
            swap(A,i,j)
    return i

'''
swap:
    Given an array and two positional indices:
    1) Swaps the element at position i with the one at position j
'''
def swap(A,i,j):
    temp=A[i]
    A[i]=A[j]
    A[j]=temp