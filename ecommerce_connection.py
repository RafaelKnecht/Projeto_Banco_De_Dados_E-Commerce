import mysql.connector

def conectar(usuario, senha):
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",   # igual ao que aparece no Workbench
            user=usuario,
            password=senha,
            database="ECOMMERCE"
        )
        if conexao.is_connected():
            print("✅ Conectado com sucesso ao banco ECOMMERCE!")
            return conexao
    except mysql.connector.Error as erro:
        print(" Erro ao conectar ao MySQL:", erro)
        return None
import mysql.connector

def conectar(usuario, senha):
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user=usuario,
            password=senha,
            database="ECOMMERCE"
        )
        if conexao.is_connected():
            print(f"✅ Conectado como {usuario}")
            return conexao
    except mysql.connector.Error as erro:
        print("❌ Erro ao conectar ao MySQL:", erro)
        return None
