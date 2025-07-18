"""
Set of function that modifyes the given array
- Organize the array satisfing MaxHeap invariant
- Perform Heap operation
"""
class maxHeapInt:
    def getLeft(H, i):
        lPos = 2 * i + 1
        if i >= 0 and lPos < len(H):
            return (H[lPos], lPos)
        else:
            return (None, -1)
    
    def getRight(H, i):
        rPos = 2 * i + 2
        if i >= 0 and rPos < len(H):
            return (H[rPos], rPos)
        else:
            return (None, -1)
  
    def getParent(H, i):
        pPos = (i - 1) // 2
        if i > 0 and i < len(H):
            return (H[pPos], pPos)
        else:
            return (None, -1)

    def buildHeap(H):
        for i in range((len(H) // 2) - 1, -1, -1):
            maxHeapInt.__heapify(H, i)

    def __heapify(H, i):
        l = maxHeapInt.getLeft(H, i)
        r = maxHeapInt.getRight(H, i)
        if l[0] != None and l[0] > H[i]:
            m = l[1]
        else:
            m = i
        if r[0] != None and r[0] > H[m]:
            m = r[1]
        if m != i:
            maxHeapInt.__swap(H, i, m)
            maxHeapInt.__heapify(H, m)

    def __swap(H, i, j):
        tmp = H[i]
        H[i] = H[j]
        H[j] = tmp


class minHeapInt:
    def getLeft(H, i):
        lPos = 2 * i + 1
        if i >= 0 and lPos < len(H):
            return (H[lPos], lPos)
        else:
            return (None, -1)
    
    def getRight(H, i):
        rPos = 2 * i + 2
        if i >= 0 and rPos < len(H):
            return (H[rPos], rPos)
        else:
            return (None, -1)
  
    def getParent(H, i):
        pPos = (i - 1) // 2
        if i > 0 and i < len(H):
            return (H[pPos], pPos)
        else:
            return (None, -1)

    def buildHeap(H):
        for i in range(len(H) // 2, -1, -1):
            minHeapInt.__heapify(H, i)

    def __heapify(H, i):
        l = minHeapInt.getLeft(H, i)
        r = minHeapInt.getRight(H, i)
        if l[0] != None and l[0] < H[i]:
            m = l[1]
        else:
            m = i
        if r[0] != None and r[0] < H[m]:
            m = r[1]
        if m != i:
            minHeapInt.__swap(H, i, m)
            minHeapInt.__heapify(H, m)

    def __swap(H, i, j):
        tmp = H[i]
        H[i] = H[j]
        H[j] = tmp
   

"""
Classes that realize Heap with node that can store indexed element
the 1° element is considered for the Heap organization (to preserve the invarint)
"""
class maxHeapTuple:
    def __init__(self, A):
        self.H = A
        self.__buildHeap()

    def getHeapSize(self):
        return len(self.H)

    def getLeftPosition(self, pos):
        l = 2 * pos + 1
        if pos >= 0 and l < self.getHeapSize():
            return l
        else:
            return -1 

    def getRightPosition(self, pos):
        r = 2 * pos + 2
        if pos >= 0 and r < self.getHeapSize():
            return r
        else:
            return -1

    def getParentPosition(self, pos):
        if pos > 0 and pos < self.getHeapSize():
            return (pos - 1) // 2
        else:
            return -1

    def getNode(self, pos):
        if pos >= 0 and pos < self.getHeapSize():
            return self.H[pos]
        else:
            return None

    def getLeft(self, pos):
        l = self.getLeftPosition(pos)
        if l != -1:
            return self.getNode(l)
        else:
            return None

    def getRight(self, pos):
        r = self.getRightPosition(pos)
        if r != -1:
            return self.getNode(r)
        else:
            return None

    def getParent(self, pos):
        p = self.getParentPosition(pos)
        if p != -1:
            return self.getNode(p)
        else:
            return None

    def __buildHeap(self):
        for pos in range(self.getHeapSize()//2, -1, -1):
            self.__heapify(pos)

    def __heapify(self, pos):
        l = self.getLeftPosition(pos)
        r = self.getRightPosition(pos)
        if l != -1 and self.getNode(l)[0] > self.getNode(pos)[0]:
            m = l
        else:
            m = pos
        if r != -1 and self.getNode(r)[0] > self.getNode(m)[0]:
            m = r
        if m != pos:
            self.__swap(m, pos)
            self.__heapify(m)

    def __swap(self, i, j):
        tmp = self.getNode(i)
        self.H[i] = self.getNode(j)
        self.H[j] = tmp

    def push(self, node):
        self.H.append(node)
        pos = self.getHeapSize() - 1
        while pos > 0 and self.getNode(pos)[0] > self.getParent(pos)[0]:
            self.__swap(pos, self.getParentPosition(pos))
            pos = self.getParentPosition(pos)
 
    def pop(self):
        if self.getHeapSize() > 0:
            node = self.getNode(0)
            self.__swap(0, self.getHeapSize() - 1)
            self.H.pop(self.getHeapSize() - 1)
            self.__heapify(0)
            return node
        else:
            return None

    def __str__(self):
        str = "[ "
        for x in self.H:
            str += "({}, {}) ".format(x[0], x[1])
        str += "]"
        return str


class minHeapTuple:
    def __init__(self, A):
        self.H = A
        self.__buildHeap()

    def getHeapSize(self):
        return len(self.H)

    def getLeftPosition(self, pos):
        l = 2 * pos + 1
        if pos >= 0 and l < self.getHeapSize():
            return l
        else:
            return -1 

    def getRightPosition(self, pos):
        r = 2 * pos + 2
        if pos >= 0 and r < self.getHeapSize():
            return r
        else:
            return -1

    def getParentPosition(self, pos):
        if pos > 0 and pos < self.getHeapSize():
            return (pos - 1) // 2
        else:
            return -1

    def getNode(self, pos):
        if pos >= 0 and pos < self.getHeapSize():
            return self.H[pos]
        else:
            return None

    def getLeft(self, pos):
        l = self.getLeftPosition(pos)
        if l != -1:
            return self.getNode(l)
        else:
            return None

    def getRight(self, pos):
        r = self.getRightPosition(pos)
        if r != -1:
            return self.getNode(r)
        else:
            return None

    def getParent(self, pos):
        p = self.getParentPosition(pos)
        if p != -1:
            return self.getNode(p)
        else:
            return None

    def __buildHeap(self):
        for pos in range(self.getHeapSize()//2, -1, -1):
            self.__heapify(pos)

    def __heapify(self, pos):
        l = self.getLeftPosition(pos)
        r = self.getRightPosition(pos)
        if l != -1 and self.getNode(l)[0] < self.getNode(pos)[0]:
            m = l
        else:
            m = pos
        if r != -1 and self.getNode(r)[0] < self.getNode(m)[0]:
            m = r
        if m != pos:
            self.__swap(m, pos)
            self.__heapify(m)

    def __swap(self, i, j):
        tmp = self.getNode(i)
        self.H[i] = self.getNode(j)
        self.H[j] = tmp

    def push(self, node):
        self.H.append(node)
        pos = self.getHeapSize() - 1
        while pos > 0 and self.getNode(pos)[0] < self.getParent(pos)[0]:
            self.__swap(pos, self.getParentPosition(pos))
            pos = self.getParentPosition(pos)
 
    def pop(self):
        if self.getHeapSize() > 0:
            node = self.getNode(0)
            self.__swap(0, self.getHeapSize() - 1)
            self.H.pop(self.getHeapSize() - 1)
            self.__heapify(0)
            return node
        else:
            return None

    def __str__(self):
        str = "[ "
        for x in self.H:
            str += "({}, {}) ".format(x[0], x[1])
        str += "]"
        return str