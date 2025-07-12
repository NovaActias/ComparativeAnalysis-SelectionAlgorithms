from GraphGenerationCode.Heap import maxHeapInt, maxHeapTuple, minHeapInt, minHeapTuple

def heapSelect(H1, k):
    if len(H1) > 0 and k > 0 and k <= len(H1):
        if k < len(H1) // 2:
            #print("\nMinHeap\n")

            minHeapInt.buildHeap(H1)
            H2 = minHeapTuple([])
        else:
            #print("\nMaxHeap\n")
            
            maxHeapInt.buildHeap(H1)
            H2 = maxHeapTuple([])
            k = len(H1) - k + 1
        # Node of H2 are tuple that have sa 1° element the a key of H1
        # and as 2° the position of that key in H1
        H2.push((H1[0], 0))
        
        #print("H1 : {} \nH2 : {} \n".format(H1, H2))

        for i in range(1, k):
            node = H2.pop()
            l = maxHeapInt.getLeft(H1, node[1])
            r = maxHeapInt.getRight(H1, node[1])
            if l[0] != None : H2.push(l)
            if r[0] != None : H2.push(r)
            
            #print("H1 : {} \nH2 : {} \n".format(H1, H2))

        return H2.pop()[0]
    else:
        return -1