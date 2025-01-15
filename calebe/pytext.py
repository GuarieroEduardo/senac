import mysql.connector
from mysql.connector import Error


def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="atividades",
            password="",
            database="sistemadevendas"

        )

        if conexao.is_connected():
            print("conexão bem-sucedida!")
            return conexao

    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None
    
def login(login, senha):
    conexao = conectar()
    
    if conexao:
        try:
            cursor = conexao.cursor()
            query = "SELECT * FROM usuarios WHERE login = %s AND senha = %s"
            cursor.execute(query, (login, senha))
            resultado = cursor.fetchone()

            if resultado:
                print("login bem-sucedido!")
                
            else:
                print("Usuário ou senha incorretos.")

        except Error as e:
            print(f"Erro ao consultar o banco de dados: {e}")
        finally:
            cursor.close()
            conexao.close()

    else:
        print("Erro com a conexão com o banco de dados")

        