import os
import requests
from flask import Flask, request, jsonify, json
from bs4 import BeautifulSoup

app = Flask(__name__)

jogos = [
    "mega sena",
    "quina",
    "lotofacil"
]

url = "https://www.google.com/search?q={param}&oq={param}&aqs=chrome.0.69i59j35i19i39j69i60j69i65l3j69i60l2.568j0j7&sourceid=chrome&ie=UTF-8"

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
}


@app.route("/")
def ok():
    dezenas = []

    for j in jogos:
        dezenas.clear()

        site = requests.get(url.replace(
            "{param}", j.replace(" ", "+")), headers=headers)

        soup = BeautifulSoup(site.content, 'html.parser')

        print(soup.find_all(class_="UHlKbe"))

        for a in soup.find_all(class_="UHlKbe"):
            dezenas.append(a.get_text())

        with open(j.replace(" ", "") + '.json', 'w') as arquivo:
            arquivo.write('{\n\t"dezenas": ' + json.dumps(dezenas) + '\n}')

    return jsonify({"status": "success", "dezenas": dezenas})


@ app.route("/<name>")
def name(name):
    return jsonify(name=name, email="diego@b2c.srv.br")


@ app.route("/array")
def arrayT():

    contatos = [
        {'nome': 'Yan', 'number': '1234-5678'},
        {'nome': 'Diego', 'number': '1234-5678'},
        {'nome': 'Clara', 'number': '1234-5678'}
    ]
    return jsonify(contatos)


app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
