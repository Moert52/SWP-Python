import random
import copy
from ArrayList_Decorator import Decorator


class ArrayList:

    def __init__(self):
        self.list = [None]*5
        self.numElements = 0

    @Decorator.getLastElement
    def getLastElement(self):
        return 'Last Element: '

    def addLast(self, element):
        if self.numElements >= len(self.list):
            newList = [None] * (2*len(self.list))
            for i in range(0,len(self.list)):
                newList[i] = self.list[i]
            self.list = newList
        self.list[self.numElements] = element
        self.numElements += 1
        return self.list

    @Decorator.getLength
    def getLength(self):
        return 'Länge: '

    @Decorator.printAllElements
    def __str__(self):
        return self.list


    @Decorator.getIndexOfElem
    #get the index of the first elem
    def getIndexOfElem(self, elem,  n=0):
        return 'Index: '

    @Decorator.getElementbyIndex
    def getElementbyIndex(self, index):
        return 'Element: '

    @Decorator.delete
    def delete(self, index):
        return
    @Decorator.find
    def find(self, elem):
        return 'Found Element '

    @Decorator.add
    def insertAfter(self, prevElem, elem):
        pass


if __name__ == '__main__':
    Liste = ArrayList()
    randomlist = random.sample(range(0, 100), 10)
    elem = randomlist[5]
    for i in randomlist:
        Liste.addLast(i)

    print(Liste)
    Liste.getLastElement()
    Liste.getIndexOfElem(elem)
    Liste.getElementbyIndex((Liste.getIndexOfElem(elem)))
    Liste.getLength()
    Liste.find(elem)
    Liste.find(99)
    Liste.delete(Liste.getIndexOfElem(elem))
    print(Liste)
    Liste.getLength()
    prev = randomlist[4]
    Liste.insertAfter(prev, elem)
    print(Liste)
    Liste.getLength()




