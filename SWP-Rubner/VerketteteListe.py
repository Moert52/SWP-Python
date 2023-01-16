import random

class ListenElement:

    def __init__(self, element):
        self.element = element
        self.nextElement = None

    def setNextElement(self, nextElement):
        self.nextElement = nextElement

    def getNextElement(self):
        return self.nextElement

    def getElement(self):
        return self.element

class VerketteListe:

    def __init__(self):
        self.startElement = ListenElement(None)

    def getLastElement(self):
        last = self.startElement
        while last.nextElement != None:
            last = last.getNextElement()
        return last

    def addLast(self, element):
        if isinstance(element, int):
            newElement = ListenElement(element)
            last = self.getLastElement()
            lastElement = last
            lastElement.setNextElement(newElement)

    def getLength(self, elem = None, n = 0):
        if elem == None:
            elem = self.startElement
        if elem.getNextElement() != None:
            elem = elem.getNextElement()
            n+=1
            return self.getLength(elem, n)
        return n

    def printAllElements(self):
        elem = self.startElement
        getAll = '| '
        while elem.getNextElement() != None:
            elem = elem.getNextElement()
            getAll += str(elem.getElement()) + ' | '
        return getAll

    #get the index of the first elem
    def getIndexOfElem(self, elem, start=None, n=0):
        if start == None:
             start = self.startElement
        if start.getNextElement() != None:
            if start.getNextElement().getElement() == elem:
                return n
            start = start.getNextElement()
            n+=1
            return self.getIndexOfElem(elem, start, n)
        return None


    def getElementbyIndex(self, index):
        start = self.startElement
        n = 0
        while start.getNextElement() != None:
            start = start.getNextElement()
            if n == index:
                return start.getElement()
            n+=1
        return None






if __name__ == '__main__':
    Liste = VerketteListe()
    randomlist = random.sample(range(0, 100), 10)
    elem = randomlist[9]
    for i in randomlist:
        Liste.addLast(i)

    print(Liste.printAllElements())
    print('Index: ' + str(Liste.getIndexOfElem(elem)))
    print('Elem: ' + str(Liste.getElementbyIndex((Liste.getIndexOfElem(elem)))))
    print('Länge: ' + str(Liste.getLength()))



