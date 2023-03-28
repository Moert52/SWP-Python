import random

class ListenElement:

    def __init__(self, element):
        self.element = element
        self.previousElement = None
        self.nextElement = None
    def setPreviousElement(self, previousElement):
        self.previousElement = previousElement
    def setNextElement(self, nextElement):
        self.nextElement = nextElement

    def getPreviousElement(self):
        return self.previousElement
    def getNextElement(self):
        return self.nextElement

    def getElement(self):
        return self.element

class DoppeltVerketteListe:

    def __init__(self):
        self.startElement = ListenElement(None)
        self.lastElement = ListenElement(None)
        self.startElement.setNextElement(self.lastElement)
        self.lastElement.setPreviousElement(self.startElement)

    def getFirstElement(self):
        return self.startElement.getNextElement().getElement()

    def getLastElement(self):
        return self.lastElement.getPreviousElement()

    def addLast(self, element):
        if isinstance(element, int):
            newElement = ListenElement(element)
            lastElement = self.getLastElement()
            lastElement.setNextElement(newElement)
            newElement.setPreviousElement(lastElement)
            newElement.setNextElement(self.lastElement)
            self.lastElement.setPreviousElement(newElement)


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
        while elem.getNextElement().element != None:
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

    def delete(self, elem):
        start = self.startElement

        while start.getNextElement() != None and elem != start.getElement():
            if elem == start.getNextElement().getElement():
                if start.getNextElement().getNextElement() != None:
                    start.setNextElement(start.getNextElement().getNextElement())
                    start.getNextElement().setPreviousElement(start)
                else:
                    start.setNextElement(None)
                    break
            start = start.getNextElement()

    def find(self, elem):
        start = self.startElement
        while start.getNextElement() != None:
            if start.getNextElement().getElement() == elem:
                return True
            start = start.getNextElement()
        return False


    def insertAfter(self, prevElem, elem):
        pointer = self.startElement.getNextElement()
        while pointer != None and pointer.getElement() != prevElem:
            pointer = pointer.getNextElement()

        newElem = ListenElement(elem)
        if pointer != None:
            nextElem = pointer.getNextElement()
            pointer.setNextElement(newElem)
            newElem.setNextElement(nextElem)
            newElem.setPreviousElement(pointer)

    def insertBefore(self, nextItem, elem):
        pointer = self.startElement.getNextElement()
        newElem = ListenElement(elem)
        while pointer != None:
            if pointer.getElement() == nextItem:
                newElem.setPreviousElement(pointer.getPreviousElement())
                pointer.getPreviousElement().setNextElement(newElem)
                pointer.setPreviousElement(newElem)
                newElem.setNextElement(pointer)
            pointer = pointer.getNextElement()



if __name__ == '__main__':
    Liste = DoppeltVerketteListe()
    randomlist = random.sample(range(0, 100), 10)
    elem = randomlist[5]
    for i in randomlist:
        Liste.addLast(i)

    print(Liste.printAllElements())
    print('First Elem: ' + str(Liste.getFirstElement()))
    print('Index: ' + str(Liste.getIndexOfElem(elem)))
    print('Element: ' + str(Liste.getElementbyIndex((Liste.getIndexOfElem(elem)))))
    print('Länge: ' + str(Liste.getLength()))
    print('Found Element %s: %s' % (elem, str(Liste.find(elem))))#
    print('Found Element %s: %s' % (99, str(Liste.find(99))))
    Liste.delete(elem)
    print(Liste.printAllElements())
    print('Länge: ' + str(Liste.getLength()))
    prev = randomlist[4]
    before = randomlist[7]
    Liste.insertAfter(prev, elem)
    Liste.insertBefore(before, elem)
    print(Liste.printAllElements())
    print('Länge: ' + str(Liste.getLength()))





