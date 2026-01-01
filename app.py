
from flask import Flask, render_template, request, redirect
import _sqlite3
import database

app = Flask(__name__)

def conectar():
          return _sqlite3.connect("loja.db") 

@app.route("/ ")
def index():
        return render_template("index.html")

@app.route("/contato", methods=["POST"])
def contato():
        nome = request.form["nome"]
        telefone = request.form["telafone"]
        aparelho = request.form["aparelho"]
        defeito = request.form["defeito"]
        data = request.form["data"]

        servico = {}
        servico.nome = nome
        servico.telefone = telefone
        servico.aparelho = aparelho
        servico.defeito = defeito
        servico.data = data

        database.salvar_servico(servico)

        # conn = conectar()
        # cur = conn.cursor()
        # cur.execute("""
        #    INSERT INTO servicos VALUES (NULL, ?, ?, ? ' Em andamento')
        #     """,(nome, telefone, aparelho, defeito))
        # conn.commit()
        # conn.close()

        return redirect ("/")

if __name__== "__main__":
        app.run(debug=True)

"""import sqlite3

conn = sqlite3.connect("loja.db")
cur = conn.cursor()

cur.execute("""
"""CREATE TABLE IF NOT EXISTS servicos (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          nome TEXT,
          telefone TEXT
          aparelho TEXT
          defeito TEXT
          estatus TEXT
)
)"""

"""conn.commit()
conn.close()

import sqlite3

conn = sqlite3.connect("loja.db")
cur = conn.cursor()

nome_servico = "Troca de Tela do iphone 12"


cur.execute("INSERT INTO servicos (nome) VALUES (?)", (nome_servico,))

conn.commit()

conn.close()

print(f"serviço '{nome_servico}' adicionado com sucesso! ")"""