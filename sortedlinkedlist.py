class Node:
    def __init__(self):
        self.__key = None
        self.__next = None
        self.__prev = None

    def setKey(self, key):
        self.__key = key

    def getKey(self):
        return self.__key

    def setNext(self, next):
        self.__next = next

    def getNext(self):
        return self.__next

    def hasNext(self):
        return self.__next != None
    
    def setPrev(self, prev):
        self.__prev = prev
    
    def getPrev(self):
        return self.__prev

    def hasPrev(self):
        return self.__prev != None
    
    def __str__(self):
        return str(self.getKey())
    
    def __lt__(self, other):
        return self.getKey() < other.getKey()
    

class LinkedList:
    def __init__(self):
        self._head = None
        self._length = 0
    
    def traverse(self):
        current = self._head
        while current != None:
                print(current.getKey(), end = ' ')
                current = current.getNext()
        print()
    
    def setHead(self, head):
        self._head = head

    def getHead(self):
        return self._head

    def isEmpty(self):
        return self._length == 0

    def getLength(self):
        current = self._head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        self._length = count
        return count
    
    def search(self, key):
        elem = self._head
        while elem != None and elem.getKey() != key:
            elem = elem.getNext()
        return elem

    def prepend(self, elem):
        elem.setNext(self._head)
        if self._head != None:
            self._head.setPrev(elem)
        self._head = elem
        self._length += 1

    def insert(self, elem, target):
        elem.setNext(target.getNext())
        elem.setPrev(target)
        if target.hasNext():
            target.getNext().setPrev(elem)
        target.setNext(elem)
        self._length += 1
              
    def deleteWithNode(self, elem):
        if elem.hasPrev():
            elem.getPrev().setNext(elem.getNext())
        else:
            self._head = elem.getNext()
        if elem.hasNext():
            elem.getNext().setPrev(elem.getPrev())
            
    def clear(self):
        self._head = None



class SortNode(Node):
    def __init__(self):
        super().__init__()
        self.__greater = None
        self.__lesser = None

    def setGreater(self, greater):
        self.__greater = greater

    def getGreater(self):
        return self.__greater
    
    def hasGreater(self):
        return self.__greater != None

    def setLesser(self, lesser):
        self.__lesser = lesser

    def getLesser(self):
        return self.__lesser
    
    def hasLesser(self):
        return self.__lesser != None
    


class SortedLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
        self.__max = None
        self.__min = None
        self.__sorted = False
    
    def getMax(self):
        return self.__max

    def getMin(self):
        return self.__min
    
    def prepend(self, elem):        
        super().prepend(elem)
        self.position(elem)
    
    def insert(self, elem, target):
        super().insert(elem, target)
        self.position(elem)
        
    def deleteWithNode(self, elem):
        if elem.hasLesser():
            elem.getLesser().setGreater(elem.getGreater())
        if elem.hasGreater():
            elem.getGreater().setLesser(elem.getLesser)
        return super().deleteWithNode(elem)
    
    def sort(self):
        if self.__sorted:
            return
        else:
            elem = self._head
            while elem != None:
                self.position(elem)
                elem = elem.getNext()
            self.__sorted = True
            return
    
    def traverseInSortedOrder(self, reversed = False):
        if not reversed:
            current = self.__min
            while current != None:
                print(current, end = ' ')
                current = current.getGreater()
        else:
            current = self.__max
            while current != None:
                print(current, end = ' ')
                current = current.getLesser()
        print()

    def position(self, elem):
        greaterLs = []
        lesserLs = []
        current = self._head
        key = elem.getKey()

        while current != None:
            if current == elem:
                current = current.getNext()
            else:
                if current.getKey() > key:
                    greaterLs.append(current)

                else:
                    lesserLs.append(current)
                current = current.getNext()

        if greaterLs:
            greater = min(greaterLs)
            elem.setGreater(greater)
            greater.setLesser(elem)
        else:
            self.__max = elem

        if lesserLs:
            lesser = max(lesserLs)
            elem.setLesser(lesser)
            lesser.setGreater(elem)
        else:
            self.__min = elem
   

if __name__ == '__main__':
    n1 = SortNode()
    n1.setKey(42)
    n2 = SortNode()
    n2.setKey(28)
    n3 = SortNode()
    n3.setKey(63)
    n4 = SortNode()
    n4.setKey(34)
    n5 = SortNode()
    n5.setKey(40)
    n6 = SortNode()
    n6.setKey(61)

    n1.setNext(n2)
    n2.setNext(n3)
    n3.setNext(n4)
    n4.setNext(n5)
    n5.setNext(n6)

    sl = SortedLinkedList()
    sl.setHead(n1)

    print('List at first')
    sl.traverse()
    print('length =', end = ' ')
    print(sl.getLength())
    print('Sorted traversal:')
    sl.sort()
    sl.traverseInSortedOrder()

    n7 = SortNode()
    n7.setKey(156)

    print('Inserting n7 node with key 156 after n5')
    sl.insert(n7, n5)
    sl.traverse()
    sl.traverseInSortedOrder()
    print()

    print('Deleting n6 with key 61')
    sl.deleteWithNode(n6)
    sl.traverse()
    sl.traverseInSortedOrder()
    print()

    print('Prepending np node with key 100')
    np = SortNode()
    np.setKey(100)
    sl.prepend(np)
    sl.traverse()
    sl.traverseInSortedOrder()

    print('getting max')
    print(sl.getMax())
    print()

    print('getting min')
    print(sl.getMin())
    sl.clear()
