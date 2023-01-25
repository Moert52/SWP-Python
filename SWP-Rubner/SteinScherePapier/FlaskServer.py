from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api
import requests
import json
from matplotlib import pyplot as plt
import datetime
import SteinScherePapier as ssp

app = Flask(__name__, template_folder='templates')
# creating an API object
api = Api(app)

class StatistikWeb(Resource):
    def post(self):
        data = request.get_json(force=True)
        saveToJson(data)
        getDia(readJson())
        print(data)

    def get(self):
        dic = readJson()
        return dic
api.add_resource(StatistikWeb, '/server')

def readJson():
    with open('../server.json', 'r') as file:
        return json.load(file)

def saveToJson(dic):
    jsFile = json.dumps(dic)
    with open("../server.json", "w") as file:
        file.write(jsFile)
        #file.close()

def plotti(axes, dic, user):
    if 'Wins' in dic[user]:
        del dic[user]['Wins']
    player = dic[user]
    names = list(player.keys())
    values = list(player.values())
    axes.bar(names, values, label=user)
    axes.set_title(user+ ':')

def getDia(dic):
    fig, axes = plt.subplots(nrows=1, ncols=2)
    plotti(axes[0], dic, 'Player')
    plotti(axes[1], dic, 'Computer')
    fig.tight_layout()
    fig.savefig('static/barplot.png')
    #plt.show()

@app.route('/')
def getSymWebsite():
    dic = readJson()
    getDia(dic)
    date = datetime.datetime.now()
    date = date.strftime("%c")
    return render_template('getSym.html', date=date)

def main():
    dic = readJson()
    getDia(dic)
    app.run(debug=True)  # debug=True lädt nach den Änderungen neu






if __name__ == '__main__':
    main()
