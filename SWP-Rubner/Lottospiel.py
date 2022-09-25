import random

list = [*range(1,46,1)]

def zufall(list):
    arr = []
    while len(arr) < 6:
        rand = random.choice(list)
        list.remove(rand)
        arr.append(rand)
    return arr

if __name__ == '__main__':
    print(zufall(list))