from sortedlinkedlist import SortNode, SortedLinkedList

def serialize(sortedlist, filepath):
    with open(filepath, 'w') as file:
        current = sortedlist.getHead()
        while current != None:
            node = f'{current.getPrev()} {current.getLesser()} {current.getKey()} {current.getGreater()} {current.getNext()}\n'
            file.write(node)
            current = current.getNext()


def deserialize(filepath):
    sl = SortedLinkedList()
    current = 0
    nodeList = []
    nodeDict = {}
    min = None
    max = None
    with open(filepath, 'r') as file:
        for line in file:
            line = line.split()
            for i in range(len(line)):
                try:
                    line[i] = int(line[i])
                except:
                    line[i] = None
            
            node = SortNode()
            node.setPrev(line[0])
            node.setLesser(line[1])
            node.setKey(line[2])
            node.setGreater(line[3])
            node.setNext(line[4])

            if not min:
                min = node
            else:
                if min.getKey() > node.getKey():
                    min = node
            
            if not max:
                max = node
            else:
                if max.getKey() < node.getKey():
                    max = node

            nodeList.append(node)
            nodeDict.update({line[2] : node})

            current = node
    
    for node in nodeList:
        if isinstance(node.getPrev(), int):
            node.setPrev(nodeDict[node.getPrev()])
        if isinstance(node.getLesser(), int):
             node.setLesser(nodeDict[node.getLesser()])
        if isinstance(node.getGreater(), int):
            node.setGreater(nodeDict[node.getGreater()])
        if isinstance(node.getNext(), int):
            node.setNext(nodeDict[node.getNext()])

    sl.setHead(nodeList[0])
    sl.setMin(min)
    sl.setMax(max)
    return sl
        

        

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
    sl.sort()

    print('List before serialization- unsorted and sorted:')
    sl.traverse()
    sl.traverseInSortedOrder()
    print()

    serialize(sl, 'sortedlist.txt')
    sl = deserialize('sortedlist.txt')

    print('List after deserialization - unsorted and sorted: ')
    sl.traverse()
    sl.traverseInSortedOrder()
