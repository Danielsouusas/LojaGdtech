import sqlite3

# conn = sqlite3.connect("loja.db")
# cur = conn.cursor()

# cur.execute("""
# CREATE TABLE IF NOT EXISTS servicos (
#           id INTEGER PRIMARY KEY AUTOINCREMENT,
#           nome TEXT,
#           telefone TEXT
#           aparelho TEXT
#           defeito TEXT
#           estatus TEXT
# )
# """)

# conn.commit()
# conn.close()

# import sqlite3

# conn = sqlite3.connect("loja.db")
# cur = conn.cursor()

# nome_servico = "Troca de Tela do iphone 12"


# cur.execute("INSERT INTO servicos (nome) VALUES (?)", (nome_servico,))

# conn.commit()

# conn.close()

# print(f"serviço '{nome_servico}' adicionado com sucesso! ")

def criar_tabela_no_bd():
        
          conn = sqlite3.connect("loja.db")
          cur = conn.cursor()

          cur.execute("""
          CREATE TABLE IF NOT EXISTS servicos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    telefone TEXT
                    aparelho TEXT
                    defeito TEXT
                    estatus TEXT
          )
          """)

          conn.commit()
          conn.close()


def salvar_servico(servico: dict):
          conn = sqlite3.connect("loja.db")
          cur = conn.cursor()

          nome_servico = "Troca de Tela do iphone 12"


          cur.execute("""INSERT INTO servicos VALUES (NULL, ?, ?, ? 'Em andamento') """, 
                      (servico.nome, servico.telefone, servico.aparelho, servico.defeito))

          conn.commit()

          conn.close()
          print(f"serviço '{nome_servico}' adicionado com sucesso! ")
