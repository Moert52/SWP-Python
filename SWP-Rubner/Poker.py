import random
import operator

def model_poker(anz=5):
    pokerlist = [*range(0, 52, 1)]
    for i in range(anz):
        rand = random.randrange(0, 52)
        lastposition = len(pokerlist) - 1-i
        pokerlist[rand], pokerlist[lastposition], = pokerlist[lastposition], pokerlist[rand]
    for i in pokerlist[-anz:]:
        pokerlist[pokerlist.index(i)] = symbol(i)
    return pokerlist[-anz:]

def symbol(zahl):
    num = zahl % 13
    n = num+1
    if num == 10:
        num = 'Bub'
    elif num == 11:
        num = 'Dame'
    elif num == 12:
        num = 'König'
    elif num + 1 == 1:
        num = 'Ass'
    else:
        num = num +1

    sym = zahl // 13
    if sym == 0:
        sym = 'Pik'
    elif sym == 1:
        sym = 'Herz'
    elif sym == 2:
        sym = 'Karo'
    else:
        sym = 'Kreuz'

    return  n, (str(num), sym)


def statistik(anzahl=100000, anz=5):
    dic = {}
    for i in range(anzahl):
            x = kombination(model_poker(anz))
            if x in dic:
                dic[x] = dic[x] + 1
            else:
                dic.update({x:1})
    return dict( sorted(dic.items(), key=operator.itemgetter(1),reverse=True)), anzahl


def kombination(karten):
    zahlen = []
    for i in karten:
        zahlen.append(i[0])
    for i in karten:
        k = i[0]
        if check_royal_flush(karten):
            return 'Royal flush'
        elif check_straigt_flush(karten):
            return 'Straight flush'
        elif zahlen.count(k) == 4:
            return 'Four of a kind'
        elif check_full_house(zahlen):
            return 'Full House'
        elif check_flush(karten):
            return 'Flush'
        elif check_straight(zahlen):
            return 'Straight'
        elif zahlen.count(k) ==3:
            return 'Three of a kind'
        elif check_two_pair(zahlen):
            return 'Two pair'
        elif zahlen.count(k) == 2:
            return 'Pair'
    return "High Card"



def check_straight(karten):
    dic = {}
    for i in karten:
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic.update({i: 1})
    isStraight = max(karten) - min(karten)
    k = len(set(dic.values()))
    if(k ==1 and isStraight==4):
        return True
    elif set(karten) == set([1,13,12,11,10]):
        return True
    return False

def check_straigt_flush(karten):
    zahlen = []
    if check_flush(karten):
        for i in karten:
            zahlen.append(i[0])
        if check_straight(zahlen):
            return True
    return False


def check_royal_flush(karten):
    zahlen = []
    if check_flush(karten):
        for i in karten:
            zahlen.append(i[0])
        if set(zahlen) == set([1,13,12,11,10]):
            return True
    return False

def check_flush(karten):
    dic = {}
    for i in karten:
        k = i[1][1]
        if k in dic:
            dic[k] = dic[k] + 1
        else:
            dic.update({k: 1})
    if len(set(dic)) == 1:
        return True

    return False


def check_two_pair(karten):
    dic = {}
    for i in karten:
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic.update({i: 1})
    if sorted(dic.values()) == [1,2,2]:
        return True
    return False

def check_full_house(karten):
    dic = {}
    for i in karten:
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic.update({i: 1})
    if sorted(dic.values()) == [2, 3]:
        return True
    return False

def gesamt_kombis(statistik):
    stat = statistik[0]
    pstat = statistik[1]
    for i in stat:
        print(i +' : ' + str(stat[i]))
    print('#######################################')
    print('Errechnete prozentueller Anteil: ')
    for i in stat:
        print(i +' : ' + str(round((stat[i] / pstat) * 100, 5)) + ' %')
    print('#######################################')
    print('Richtige prozentueller Anteil: ')
    for i in richtigeAnteile:
        print(i)

#https://www.888poker.de/magazine/strategy/wahrscheinlichkeit-nutzen-poker
richtigeAnteile = [
'High Card		50.1177%',
'One Pair		42.2569%',
'Two Pair		4.7539%',
'3-of-a-Kind	2.1128%',
'Straight		0.3925%',
'Flush			0.1965%',
'Full House		0.1441%',
'4-of-a-Kind	0.0240%',
'Straight Flush	0.00139%',
'Royal Flush	0.000154%'
]
if __name__ == '__main__':

    gesamt_kombis(statistik(600000))
    #check_straigt_flush([(1, ('1', 'Herz')), (13, ('13', 'Herz')), (12, ('12', 'Herz')), (11, ('11', 'Herz')), (10, ('10', 'Herz'))])
    #check_straight([1,13,11,12,10])
    #check_full_house([1,1,1,3,3])
    #print(model_poker())
    #test()