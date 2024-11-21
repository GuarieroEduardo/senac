import mysql.connector 
from mysql.connector import Error


def conectar():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='escola'
        )
        if conexao.is_connected():
            print("Conexão bem-sucedida")
            return conexao

    except Error as e:
        print(f"Error ao conectar: {e}")
        return None
    
def inserir_dados(conexao, nome, idade, curso):
    try:
        cursor = conexao.cursor()
        query = "insert into alunos(nome, idade, curso) values(%s, %s, %s)"
        valores = (nome, idade, curso)
        cursor.execute(query, valores)
        conexao.commit()
        print("Dados inseridos com sucesso! ")

    except Error as e:
        print(f"Error ao conectar: {e}")
        

def atualizar_dados(conexao, nome_aluno, novo_curso):
    try:
        cursor = conexao.cursor()
        query = "update alunos set curso = %s where nome = %s"
        valores = (novo_curso, nome_aluno)
        cursor.execute(query, valores)
        conexao.commit()
        print("Dados atualizados com sucesso! ")

    except Error as e:
        print(f"Error ao conectar: {e}")
                

def deletar_dados(conexao, nome_aluno):
    try:
        cursor = conexao.cursor()
        query = "delete from alunos where nome = %s"
        valores = ( nome_aluno,)
        cursor.execute(query, valores)
        conexao.commit()
        print("Dados deletados com sucesso! ")

    except Error as e:
        print(f"Error ao conectar: {e}")

def consultar_dados(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("select * from alunos;")
        resultados = cursor.fetchall()
        print("Dados da tabela alunos: ")
        for linha in resultados:
            print(linha)
    except Error as e:
        print(f"Error ao conectar: {e}")




consultar_dados(conectar())