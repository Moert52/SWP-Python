import random




def zufall():
    list = [*range(1, 46, 1)]
    arr = []
    while len(arr) < 6:
        rand = random.choice(list)
        list.remove(rand)
        arr.append(rand)
    return arr

def statistik():
    dic = {}
    for i in range(1,1001):
        arr = zufall()
        for x in arr:
            if x in dic:
                dic[x] = dic[x] + 1
            else:
                dic.update({x:1})
    return dic

if __name__ == '__main__':
    #print(zufall())

    for x, y in sorted(statistik().items()):
        print(x, y)


