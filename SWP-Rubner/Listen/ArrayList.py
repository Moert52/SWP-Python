import random


class ArrayList:

    def __init__(self):
        self.list = [None]*5
        self.numElements = 0

    def getLastElement(self):
        return self.list[self.numElements-1]

    def addLast(self, element):
        if self.numElements >= len(self.list):
            newList = [None] * (2*len(self.list))
            for i in range(0,len(self.list)):
                newList[i] = self.list[i]
            self.list = newList
        self.list[self.numElements] = element
        self.numElements += 1
        return self.list


    def getLength(self):
        return len(self.list)

    def printAllElements(self):
        getAll = '| '
        for i in self.list:
            getAll += str(i)+' | '
        return getAll


    #get the index of the first elem
    def getIndexOfElem(self, elem,  n=0):
        if self.list[n] != None:
            if self.list[n] == elem:
                return n
            n+=1
            return self.getIndexOfElem(elem,n)
        pass


    def getElementbyIndex(self, index):
        return self.list[index]

    def delete(self, index):
        self.list.pop(index)

    def find(self, elem):
        pass


    def insertAfter(self, prevElem, elem):
        pass


if __name__ == '__main__':
    Liste = ArrayList()
    randomlist = random.sample(range(0, 100), 10)
    elem = randomlist[5]
    for i in randomlist:
        Liste.addLast(i)

    print(Liste.printAllElements())
    print('Last Element: ' + str(Liste.getLastElement()))
    print('Index: ' + str(Liste.getIndexOfElem(elem)))
    print('Element: ' + str(Liste.getElementbyIndex((Liste.getIndexOfElem(elem)))))
    print('Länge: ' + str(Liste.getLength()))
    print('Found Element %s: %s' % (elem, str(Liste.find(elem))))#
    print('Found Element %s: %s' % (99, str(Liste.find(99))))
    Liste.delete(Liste.getIndexOfElem(elem))
    print(Liste.printAllElements())
    print('Länge: ' + str(Liste.getLength()))
    prev = randomlist[4]
    Liste.insertAfter(prev, elem)
    print(Liste.printAllElements())
    print('Länge: ' + str(Liste.getLength()))





