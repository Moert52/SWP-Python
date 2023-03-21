def getLastElement(func):
    def wrapper(*args, **kwargs):
        t = args[0]
        print(func(*args, **kwargs) + str(t.list[t.numElements-1]))
        return t.list[t.numElements-1]
    return wrapper


def addLast(func):
    def wrapper(*args, **kwargs):
        getList, element = func(*args, **kwargs)
        numelement = 0
        for i in range(0, len(getList),1):
            if getList[i] == None:
                getList[i] = element
                return getList
            numelement = i+1

        newList = [None] * (2 * len(getList))
        for i in range(0, len(getList)):
            newList[i] = getList[i]
        getList = newList
        getList[numelement] = element
        return getList
    return wrapper

def getLength(func):
    def wrapper(*args, **kwargs):
        getList = args[0].list
        print(func(*args, **kwargs) + str(len(getList)))
        return len(getList)
    return wrapper


def printAllElements(func):
    def wrapper(*args, **kwargs):
        getAll = '| '
        for i in func(*args, **kwargs):
            getAll += str(i) + ' | '
        return getAll
    return wrapper


# get the index of the first elem
def getIndexOfElem(func):
    def wrapper(*args, **kwargs):
        getList, elem = args[0].list, args[1]
        n = 0
        for i in range(0, len(getList)):
            if getList[n] == elem:
                print(func(*args, **kwargs) + str(n))
                return n
            n += 1
        return print('No Element found')
    return wrapper


def getElementbyIndex(func):
    def wrapper(*args, **kwargs):
        getList, index = args[0].list, args[1]
        print(func(*args, **kwargs) + str(getList[index]))
        return getList[index]
    return wrapper


def delete(func):
    def wrapper(*args, **kwargs):
        getList, index = args[0].list, args[1]
        return getList.pop(index)

    return wrapper

def find(func):
    def wrapper(*args, **kwargs):
        getList, elem = args[0].list, args[1]
        for i in getList:
            if i == elem:
                print(func(*args, **kwargs)+ '%s: %s' % (elem, True))  #
                return True
        print(func(*args, **kwargs)+'%s: %s' % (elem, False))
        return False
    return wrapper

def add(func):
    def wrapper(*args, **kwargs):
        getList, index, elem = args[0].list, args[1], args[2]
        getList.insert(index, elem)
        return getList
    return wrapper
