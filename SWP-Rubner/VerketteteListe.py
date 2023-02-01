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

    def delete(self, elem):
        start = self.startElement
        s = start.getNextElement() != None
        s = elem != start.getElement()
        while start.getNextElement() != None and elem != start.getElement():
            if elem == start.getNextElement().getElement():
                if start.getNextElement().getNextElement() != None:
                    start.setNextElement(start.getNextElement().getNextElement())
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
        start = self.startElement.getNextElement()
        while start != None and start.getElement() != prevElem:
            start = start.getNextElement()
        newElem = ListenElement(elem)
        nextElem = start.getNextElement()
        start.setNextElement(newElem)
        newElem.setNextElement(nextElem)


if __name__ == '__main__':
    Liste = VerketteListe()
    randomlist = random.sample(range(0, 100), 10)
    elem = randomlist[5]
    for i in randomlist:
        Liste.addLast(i)

    print(Liste.printAllElements())
    print('Index: ' + str(Liste.getIndexOfElem(elem)))
    print('Element: ' + str(Liste.getElementbyIndex((Liste.getIndexOfElem(elem)))))
    print('Länge: ' + str(Liste.getLength()))
    print('Found Element %s: %s' % (elem, str(Liste.find(elem))))#
    print('Found Element %s: %s' % (99, str(Liste.find(99))))
    Liste.delete(elem)
    print(Liste.printAllElements())
    print('Länge: ' + str(Liste.getLength()))
    prev = randomlist[4]
    Liste.insertAfter(prev, elem)
    print(Liste.printAllElements())
    print('Länge: ' + str(Liste.getLength()))





