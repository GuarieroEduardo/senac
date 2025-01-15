from tkinter import *
import mysql.connector
from mysql.connector import Error

# Criar a janela de login
janela = Tk()
janela.title("Tela de Login")
janela.geometry("300x200")

# Rótulo e campo de entrada para "Usuário"
usuario = Label(janela, text="Usuário:")
usuario.grid(row=0, column=0, padx=10, pady=5)
entrada_usuario = Entry(janela)
entrada_usuario.grid(row=0, column=1, padx=10, pady=5)

# Rótulo e campo de entrada para "Senha"
senha = Label(janela, text="Senha:")
senha.grid(row=1, column=0, padx=10, pady=5)
entrada_senha = Entry(janela, show="*")
entrada_senha.grid(row=1, column=1, padx=10, pady=5)

# Rótulo para exibir mensagens de sucesso ou erro
mensagem_label = Label(janela, text="", fg="red")
mensagem_label.grid(row=3, column=0, columnspan=2, pady=10)

# Função para exibir a mensagem de login
def exibir_mensagem(mensagem, cor):
    mensagem_label.config(text=mensagem, fg=cor)
    print(mensagem)  # Para exibir também no terminal

# Função para conectar ao banco de dados
def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="atividades",  # Troque pelo seu usuário MySQL
            password="",  # Coloque sua senha aqui
            database="sistemadevendas"
        )
        if conexao.is_connected():
            return conexao
    except Error as e:
        exibir_mensagem(f"Erro ao conectar: {e}", "red")
        return None

# Função para realizar o login
def login():
    try:
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()

        # Verificar se os campos estão preenchidos
        if not usuario or not senha:
            exibir_mensagem("Usuário e senha são obrigatórios!", "red")
            return

        conexao = conectar()
        if conexao:
            try:
                cursor = conexao.cursor()
                query = "SELECT * FROM usuarios WHERE login = %s AND senha = %s"
                cursor.execute(query, (usuario, senha))
                resultado = cursor.fetchone()

                if resultado:
                    exibir_mensagem("Login bem-sucedido!", "green")
                else:
                    exibir_mensagem("Usuário ou senha incorretos.", "red")

            except Error as e:
                exibir_mensagem(f"Erro ao consultar o banco: {e}", "red")
            finally:
                cursor.close()
                conexao.close()
        else:
            exibir_mensagem("Erro na conexão com o banco", "red")
    except Exception as e:
        exibir_mensagem(f"Erro inesperado: {e}", "red")

# Botão de login
botao_login = Button(janela, text="Entrar", command=login)
botao_login.grid(row=2, column=0, columnspan=2)

# Exibir a janela
janela.mainloop()
