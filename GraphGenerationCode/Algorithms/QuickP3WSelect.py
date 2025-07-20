import random

'''
swap:
    Given an array and two positional indices:
    1) Swaps the element at position i with the one at position j
'''
def swap(A,i,j):
    temp=A[i]
    A[i]=A[j]
    A[j]=temp

'''
partition:
    Given an array, start and end indices, and a pivot position:
    1) Moves the pivot to the end position
    2) Partitions the array around the pivot value
    3) Returns the final position of the pivot
'''
def partition(A,start,end, pPos):
    swap(A, pPos, end)
    pivotValue=A[end]
    i=start-1
    for j in range(start,end+1):
        if A[j]<=pivotValue:
            i+=1
            swap(A,i,j)
    return i

'''
partition3WayRandomized:
    Given an array and start/end indices:
    1) Performs a randomized 3-way partitioning
    2) Uses random pivot selection to improve performance
    3) Returns two partition positions (pos_a, pos_b)
'''
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

'''
quickSelectRandomized:
    Given an array and an index k:
    1) Returns the k-th smallest element present in the array
    2) Uses randomized 3-way partitioning for improved performance
    3) Returns None if k is not an acceptable value
'''
def quickSelectRandomized(A,k):
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
                
        # Return the result
        return A[k]