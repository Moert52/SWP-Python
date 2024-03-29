import random
import json
import sys
from os.path import exists
import webbrowser
import FlaskServer
import copy
import requests

# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
# creating an API object
api = Api(app)

CountList = {}

class Symbol:

    def __init__(self, sym, defeat1, lose1, defeat2, lose2):
        self.sym = sym
        self.defeat1 = defeat1
        self.defeat2 = defeat2
        self.lose1 = lose1
        self.lose2 = lose2

    def lose(self, lose):
        if lose == self.lose1 or lose ==self.lose2:
            return True

    def play(self):
        return self.sym, 1

    def getSymComp(self):
        return print(f'\tDer Computer hat das Symbol {self.sym} ausgewählt')

    def __str__(self):
        return f"{self.sym}: \ndefeats ({self.defeat1} and {self.defeat2}) \nloses agains ({self.lose1} and {self.lose2})"


syms = ['Rock', 'Lizard', 'Spock', 'Scrissor', 'Paper']

def onCreate(sym):
    symbols = syms
    if (sym in symbols):
        id=symbols.index(sym)
        #print(symbols)
        newArr =  symbols[id:] + symbols[:id]
        #print(newArr)
        return Symbol(newArr[0],newArr[1],newArr[2],newArr[3],newArr[4])
    return print('Bitte ein gülitges Symbol angeben')

def statistik(user, elem, CountList):
    if user in CountList:
        if elem in CountList[user]:
            CountList[user][elem] = CountList[user][elem] + 1
        else:
            CountList[user].update({elem:1})

    else:
        CountList.update({user: {elem: 1}})

def checkWin(pwin,cwin, CountList):
    if pwin == 3:
        statistik('Player', 'Wins',CountList)
        print('Player hat gewonnen')
        return restart()

        #restart()
    elif cwin == 3:
        statistik('Computer', 'Wins',CountList)
        print('Computer hat gewonnen')
        return restart()
    return None

def restart():
    while True:
        restart = input('Wollen Sie erneut spielen? (Ja/Nein): ').capitalize()
        if restart == 'Nein':
            return False
        elif restart != 'Ja':
            print('Bitte geben sie eine eindeutige Antwort (Ja / Nein) an!')
        else:
            return True

def savePlayedSymbols(player, comp, CountList):
    statistik('Player',player.sym, CountList)
    statistik('Computer', comp.sym, CountList)

def game(CountList, pwin=0, cwin=0):
    if exists('../data.json'):
        CountList = readJson()
    round = 1
    print('Willkommen zur erweiteten Version von Schere Stein Papier:\n')

    print('\tBitte geben sie ein gültiges Symbol ein:')
    print('\tDiese Symbole stehen zur Auswahl: [Rock, Spock, Lizard, Spock, Scrissor, Paper\n')
    while True:
        while True:
            playerInput = input('Ihre Auswahl: ').capitalize()
            if playerInput in syms:
                break
            print('Bitte ein gültiges Symbol eingeben ' + str(syms))

        player = onCreate(playerInput)
        comp = onCreate(calculatedStepForComp())
        comp.getSymComp()
        if player.sym == comp.sym:
            print('\tUnentschieden')
        elif player.lose(comp.sym):
            print('\tDie Runde hat der Computer gewonnen')
            cwin +=1
        else:
            print('\tDie Runde haben sie gewonnen')
            pwin+=1
        savePlayedSymbols(player, comp, CountList)
        #print(CountList)
        print(f'Aktueller Stand des Spieles | Runde: {round}\n'
              f'Player: {pwin} | {cwin} :Computer')
        saveToJson(CountList)
        #print(CountList)
        win= checkWin(pwin,cwin, CountList)

        if win==False:
            saveToJson(CountList)
            break
        elif win==True:
            round = 0
            pwin = 0
            cwin = 0
            saveToJson(CountList)
            continue
        round+=1
    return CountList

def count_dic(dic, counter=0):
    for key in dic:
        if key != 'Wins':
            if isinstance(dic[key], int):
                counter+=dic[key]

    return counter

def getPercOfSym(dic, size):
    percDic = {}
    for key in dic:
        if key != 'Wins':
            if isinstance(dic[key], int):
                percDic[key] = round((dic[key] / size) * 100)

    return percDic

def makeSymStep(percDic, start=0):
    rand = random.randrange(0, count_dic(percDic), 1)
    for key, value in percDic.items():
        start+=value
        if rand <= start:
            return key


def calculatedStepForComp():
    if exists('../data.json'):
        CountList = readJson()
        CountList = CountList['Player']
        lenList = count_dic(CountList)
        percDic = getPercOfSym(CountList, lenList)
        return makeSymStep(percDic)
    return random.choice(syms)




def Test():
    game()
    pass

def saveToJson(dic):
    jsFile = json.dumps(dic)
    with open("../data.json", "w") as file:
        file.write(jsFile)
        #file.close()

def readJson():
    with open('../data.json', 'r') as file:
        return json.load(file)

def stats(CountList):
    for i in CountList:
        print(i+':')
        for j in CountList[i]:
            print(f'\t{j} : {CountList[i][j]}')


def main():
    CountList = readJson()
    print('Folgende Befehle gibt es: \n'
          '\tEnd - Zum Beenden des Programmes\n'
          '\tStart - Zum Starten des Spiels\n'
          '\tStats - Um die Statistik anzuzeigen\n'
          '\tData - Um die Daten and den Server upzuloaden\n'
          '\tWebsite - um die Statistik auf dem Webserver anschauen')
    while True:

        eingabe = input('Ihre Eingabe (End/Start/Stats/Data/Website): ').capitalize()
        if eingabe == 'End':
            saveToJson(CountList)
            break
        elif eingabe == 'Start':
            CountList = game(CountList)
        elif eingabe == 'Stats':
            CountList = readJson()
            stats(CountList)
        elif eingabe == 'Data':
            print(CountList)
            saveToJson(CountList)

            with app.app_context():
                res = requests.post("http://127.0.0.1:5000/server", data=json.dumps(CountList))

            if res.status_code == 200:
                print("\nDaten wurden upgeloadet\n")
            else:
                print('Daten wurden nicht upgeloadet')
        elif eingabe == 'Website':
            saveToJson(CountList)
            webbrowser.open('http://127.0.0.1:5000')
        else:
            print('Bitte gib einen gültigen Befehl ein')





if __name__ == '__main__':

    main()
    #Test()








