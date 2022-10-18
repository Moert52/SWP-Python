import random

# min = 50
# max = 100
# anz = 7 Ziehungen
def zufall(min=0, max=45, anz=6):
    list = [*range(min, max+1, 1)]
    for i in range(anz):
        rand = random.randrange(0, max-min+1)
        lastposition = len(list)-1-i
        list[rand], list[lastposition], = list[lastposition], list[rand]
    return list[-anz:]

def statistik1(min, max, anz, anz_ziehungen=1000):
    stat_dic={}
    for i in range(min, max+1):
        stat_dic[i] = 0
    for i in range(anz_ziehungen):
        for zahl in zufall(min,max,anz):
            stat_dic[zahl] += 1
    return stat_dic

def statistik(min=0, max=45, anz=6, anzahl=1000):
    dic = {}
    for i in range(anzahl):
        for x in zufall(min, max, anz):
            if x in dic:
                dic[x] = dic[x] + 1
            else:
                dic.update({x:1})
    return dic

if __name__ == '__main__':
    print(zufall(0,15,22))
    #print(statistik1(50,100,7))

    #for x, y in sorted(statistik().items()):
    #   print(x, y)


