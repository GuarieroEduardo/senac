from tkinter import *
from pytext import *


janela = Tk()
janela.title("Tela de Login")
janela.geometry("300x150")


usuario = Label(janela, text="Usuário:")
usuario.grid(row=0, column=0, padx=10, pady=5)
entrada_usuario = Entry(janela)
entrada_usuario.grid(row=0, column=1, padx=10, pady=5)


senha = Label(janela, text="Senha:")
senha.grid(row=1, column=0, padx=10, pady=5)
entrada_senha = Entry(janela, show="*")
entrada_senha.grid(row=1, column=1, padx=10, pady=5)

botao_login = Button(janela, text="Entrar", command=lambda: login(entrada_usuario.get(), entrada_senha.get()))
botao_login.grid(row=2, column=0, padx=10, columnspan=2)

janela.mainloop()