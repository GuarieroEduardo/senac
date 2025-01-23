from tkinter import *
import csv
from tkinter import ttk, messagebox, filedialog
from pytext import Database  # Importando a classe Database

# Instanciar a classe Database
db = Database()


def login(usuario, senha):
    try:
        query = "SELECT id, tipo FROM usuarios WHERE login = %s AND senha = %s"
        db.cursor.execute(query, (usuario, senha))
        resultado = db.cursor.fetchone()

        if resultado:
            id_usuario = resultado[0]
            tipo_usuario = resultado[1]
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")

            if tipo_usuario == "admin":
                abrir_home_admin()  # Redireciona para Home do Administrador
            elif tipo_usuario == "vendedor":
                abrir_home_vendedor(id_usuario)  # Redireciona para Home do Vendedor
            else:
                messagebox.showerror("Erro", "Tipo de usuário inválido!")
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao fazer login: {e}")


def abrir_login():
    limpar_tela()
    frame = Frame(janela, padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(frame, text="Usuário:", font=("Arial", 12)).grid(row=0, column=0, sticky=W)
    entrada_usuario = Entry(frame, width=25)
    entrada_usuario.grid(row=0, column=1, pady=5)

    Label(frame, text="Senha:", font=("Arial", 12)).grid(row=1, column=0, sticky=W)
    entrada_senha = Entry(frame, width=25, show="*")
    entrada_senha.grid(row=1, column=1, pady=5)

    Button(frame, text="Entrar", command=lambda: login(entrada_usuario.get(), entrada_senha.get()), width=20).grid(
        row=2, column=0, columnspan=2, pady=10
    )
def abrir_home_admin():
    limpar_tela()
    frame = Frame(janela, padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    Label(frame, text="Bem-vindo, Administrador!", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)
    Button(frame, text="Cadastrar Produto", command=abrir_cadastro_produto, width=20).grid(row=1, column=0,  pady=10, padx=20)
    Button(frame, text="Cadastrar Vendedor", command=abrir_cadastro_vendedor, width=20).grid(row=1, column=1,  pady=10, padx=20)
    Button(frame, text="Ver Relatórios", command=abrir_vendas_realizadas, width=20).grid(row=2, column=0,  pady=10, padx=20)
    Button(frame, text="Sair", command=abrir_login, width=20).grid(row=3, column=0, columnspan=2, pady=10)

def abrir_home_vendedor(id_usuario):
    limpar_tela()

    frame = Frame(janela, padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(frame, text="Bem-vindo, Vendedor!", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=20)

    Button(frame, text="Cadastrar Cliente e Venda", command=lambda: abrir_cadastro_venda(id_usuario), width=25).grid(row=1, column=0, pady=10, padx=20)
    Button(frame, text="Consultar Vendas", command=lambda: abrir_vendas_vendedor(id_usuario), width=25).grid(row=1, column=1, pady=10, padx=20)
    Button(frame, text="Sair", command=abrir_login, width=25).grid(row=2, column=0, columnspan=2, pady=20)



def abrir_cadastro_produto():
    limpar_tela()

    frame = Frame(janela, padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(frame, text="Cadastro de Produtos", font=("Arial", 16)).grid(row=0, column=0, columnspan=2 )

    # Criando os campos de entrada e centralizando na tela
    Label(frame, text="Nome do Produto:").grid(row=1, column=0,  pady=10, padx=20, sticky=W)
    nome_produto_entry = Entry(frame)
    nome_produto_entry.grid(row=1, column=1,  pady=10, padx=20)

    Label(frame, text="Descrição:").grid(row=2, column=0,  pady=10, padx=20, sticky=W)
    descricao_entry = Entry(frame)
    descricao_entry.grid(row=2, column=1, padx=10, pady=10)

    Label(frame, text="Quantidade em Estoque:").grid(row=3, column=0,  pady=10, padx=20, sticky=W)
    quantidade_entry = Entry(frame)
    quantidade_entry.grid(row=3, column=1,  pady=10, padx=20)

    Label(frame, text="Valor Unitário:").grid(row=4, column=0, padx=20, pady=10, sticky=W)
    valor_entry = Entry(frame)
    valor_entry.grid(row=4, column=1, padx=10, pady=10)

    def salvar_produto():
        nome = nome_produto_entry.get()
        descricao = descricao_entry.get()
        quantidade = quantidade_entry.get()
        valor = valor_entry.get()

        if not nome or not descricao or not quantidade or not valor:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        try:
            quantidade = int(quantidade)
            valor = float(valor)
        except ValueError:
            messagebox.showerror("Erro", "Quantidade e Valor devem ser numéricos!")
            return

        if db.cadastrar_produto(nome, descricao, quantidade, valor):
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
            abrir_home_admin()

    Button(frame, text="Salvar Produto", command=salvar_produto, width=20).grid(row=5, column=0,  pady=20, padx=30)
    Button(frame, text="Voltar", command=abrir_home_admin, width=20).grid(row=5, column=1,  pady=20, padx=30)

def abrir_cadastro_vendedor():
    limpar_tela()

    frame = Frame(janela, padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(frame, text="Cadastro de Vendedor", font=("Arial", 14)).grid(row=0, column=0, columnspan=2)

    # Campos de entrada
    Label(frame, text="Nome do Vendedor:").grid(row=1, column=0, padx=20, pady=10, sticky=W)
    nome_vendedor_entry = Entry(frame)
    nome_vendedor_entry.grid(row=1, column=1, padx=20, pady=10)

    Label(frame, text="Login:").grid(row=2, column=0, padx=20, pady=10, sticky=W)
    login_entry = Entry(frame)
    login_entry.grid(row=2, column=1, padx=10, pady=10)

    Label(frame, text="Senha:").grid(row=3, column=0, padx=20, pady=10, sticky=W)
    senha_entry = Entry(frame, show="*")
    senha_entry.grid(row=3, column=1, padx=20, pady=10)

    def salvar_vendedor():
        nome = nome_vendedor_entry.get()
        login = login_entry.get()
        senha = senha_entry.get()

        if nome and login and senha:
            try:
                query = "INSERT INTO usuarios (nome, login, senha, tipo) VALUES (%s, %s, %s, 'vendedor')"
                db.cursor.execute(query, (nome, login, senha))
                db.conexao.commit()
                messagebox.showinfo("Sucesso", "Vendedor cadastrado com sucesso!")
                abrir_home_admin()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao cadastrar vendedor: {e}")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

    Button(frame, text="Salvar Vendedor", command=salvar_vendedor, width=20).grid(row=4, column=0, pady=20, padx=20)
    Button(frame, text="Voltar", command=abrir_home_admin, width=20).grid(row=4, column=1, pady=20, padx=20)


def abrir_cadastro_venda(id_usuario):
    limpar_tela()

    # Criando o Frame para centralizar a interface
    frame = Frame(janela, padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Título
    Label(frame, text="Cadastro de Venda", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=20)

    # Dados do cliente
    Label(frame, text="Nome do Cliente:").grid(row=1, column=0, padx=10, pady=10, sticky=W)
    nome_cliente_entry = Entry(frame)
    nome_cliente_entry.grid(row=1, column=1, padx=10, pady=10)

    Label(frame, text="CPF:").grid(row=2, column=0, padx=10, pady=10, sticky=W)
    cpf_entry = Entry(frame)
    cpf_entry.grid(row=2, column=1, padx=10, pady=10)

    Label(frame, text="Endereço:").grid(row=3, column=0, padx=10, pady=10, sticky=W)
    endereco_entry = Entry(frame)
    endereco_entry.grid(row=3, column=1, padx=10, pady=10)

    # Dados da venda
    Label(frame, text="Forma de Pagamento:").grid(row=4, column=0, padx=10, pady=10, sticky=W)
    pagamento_options = ["avista", "parcelado"]
    pagamento_combobox = ttk.Combobox(frame, values=pagamento_options, state="readonly")
    pagamento_combobox.grid(row=4, column=1, padx=10, pady=10)

    Label(frame, text="Quantidade de Parcelas (se parcelado):").grid(row=5, column=0, padx=10, pady=10, sticky=W)
    parcelas_entry = Entry(frame)
    parcelas_entry.grid(row=5, column=1, padx=10, pady=10)

    # Produtos da venda
    Label(frame, text="Produto:").grid(row=6, column=0, padx=10, pady=10, sticky=W)
    produtos_combobox = ttk.Combobox(frame, values=db.obter_produtos(), state="readonly")
    produtos_combobox.grid(row=6, column=1, padx=10, pady=10)

    Label(frame, text="Quantidade:").grid(row=7, column=0, padx=10, pady=10, sticky=W)
    quantidade_produto_entry = Entry(frame)
    quantidade_produto_entry.grid(row=7, column=1, padx=10, pady=10)

    def salvar_venda(id_usuario):
        cliente_nome = nome_cliente_entry.get()
        cliente_cpf = cpf_entry.get()
        cliente_endereco = endereco_entry.get()
        forma_pagamento = pagamento_combobox.get()
        parcelas = parcelas_entry.get() if forma_pagamento == "parcelado" else 1
        produto_selecionado = produtos_combobox.get()
        quantidade_produto = quantidade_produto_entry.get()

        if cliente_nome and cliente_cpf and cliente_endereco and produto_selecionado and quantidade_produto:
            try:
                quantidade_produto = int(quantidade_produto)

                # Inserir cliente (ou atualizar se já existir)
                query_cliente = """
                    INSERT INTO clientes (nome, cpf, endereco)
                    VALUES (%s, %s, %s)
                    ON DUPLICATE KEY UPDATE nome = %s
                """
                db.cursor.execute(query_cliente, (cliente_nome, cliente_cpf, cliente_endereco, cliente_nome))
                db.conexao.commit()

                # Inserir a venda
                query_venda = """
                    INSERT INTO vendas (cliente_id, vendedor_id, forma_pagamento, parcelas)
                    VALUES (
                        (SELECT id FROM clientes WHERE cpf = %s),
                        %s,
                        %s,
                        %s
                    )
                """
                db.cursor.execute(query_venda, (cliente_cpf, id_usuario, forma_pagamento, parcelas))
                db.conexao.commit()

                # Obter o ID da venda recém-criada
                db.cursor.execute("SELECT LAST_INSERT_ID()")
                venda_id = db.cursor.fetchone()[0]

                query_preco_unitario = """
                    SELECT valor_unitario 
                    FROM produtos 
                    WHERE nome = %s
                """

                db.cursor.execute(query_preco_unitario, (produto_selecionado,))
                preco_unitario = db.cursor.fetchone()[0]

                query_prod_id = """
                    SELECT id FROM produtos WHERE nome = %s
                """
                db.cursor.execute(query_prod_id, (produto_selecionado,))
                produto_id = db.cursor.fetchone()[0]

                # Calcula o preço total
                preco_total = quantidade_produto * preco_unitario

                # Inserir o item de venda com o preço total
                query_item_venda = """
                    INSERT INTO itens_venda (venda_id, produto_id, quantidade, preco_total)
                    VALUES (%s, %s, %s, %s)
                """
                db.cursor.execute(query_item_venda, (venda_id, produto_id, quantidade_produto, preco_total))
                db.conexao.commit()

                messagebox.showinfo("Sucesso", "Venda registrada com sucesso!")
                abrir_home_vendedor(id_usuario)

            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao registrar venda: {e}")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")


    Button(frame, text="Salvar Venda", command=lambda: salvar_venda(id_usuario), width=20).grid(row=8, column=0, pady=20, padx=20)
    Button(frame, text="Voltar", command=lambda: abrir_home_vendedor(id_usuario), width=20).grid(row=8, column=1, pady=20, padx=20)

def abrir_vendas_realizadas():
    limpar_tela()

    # Criando o Frame para centralizar a interface
    frame = Frame(janela, padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Título
    Label(frame, text="Vendas Realizadas", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=20)

    # Relatório detalhado de vendas
    tree_detalhado = ttk.Treeview(frame, columns=("Cliente", "Vendedor", "Produto", "Quantidade", "Valor Total", "Data"), show="headings")
    tree_detalhado.heading("Cliente", text="Cliente")
    tree_detalhado.heading("Vendedor", text="Vendedor")
    tree_detalhado.heading("Produto", text="Produto")
    tree_detalhado.heading("Quantidade", text="Quantidade")
    tree_detalhado.heading("Valor Total", text="Valor Total")
    tree_detalhado.heading("Data", text="Data")
    tree_detalhado.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Carregar os dados do relatório detalhado
    try:
        vendas = db.gerar_relatorio_vendas()
        for venda in vendas:
            tree_detalhado.insert("", "end", values=venda)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar vendas detalhadas: {e}")

    # Relatório mensal de vendas
    Label(frame, text="Total Arrecadado por Mês", font=("Arial", 12, "bold")).grid(row=2, column=0, columnspan=2, pady=20)

    tree_mensal = ttk.Treeview(frame, columns=("Mês", "Total Arrecadado"), show="headings")
    tree_mensal.heading("Mês", text="Mês")
    tree_mensal.heading("Total Arrecadado", text="Total Arrecadado")
    tree_mensal.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Carregar os dados do relatório mensal
    try:
        relatorio_mensal = db.gerar_relatorio_total_por_mes()
        for mes, total in relatorio_mensal:
            tree_mensal.insert("", "end", values=(mes, f"R${total:.2f}"))
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar vendas mensais: {e}")

    Button(frame, text="Exporta - CSV", command=exportar_relatorio_vendas, width=20).grid(row=4, column=0,  pady=20)

    # Botão de voltar
    Button(frame, text="Voltar", command=abrir_home_admin, width=20).grid(row=4, column=1, pady=20)


def abrir_vendas_vendedor(id_usuario):
    limpar_tela()

    # Criando o Frame para centralizar a interface
    frame = Frame(janela, padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Título
    Label(frame, text="Minhas Vendas", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=20)

    # Relatório de vendas
    tree_vendas = ttk.Treeview(frame, columns=("Cliente", "Produto", "Quantidade", "Valor Total", "Data"), show="headings")
    tree_vendas.heading("Cliente", text="Cliente")
    tree_vendas.heading("Produto", text="Produto")
    tree_vendas.heading("Quantidade", text="Quantidade")
    tree_vendas.heading("Valor Total", text="Valor Total")
    tree_vendas.heading("Data", text="Data")
    tree_vendas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Carregar os dados das vendas do vendedor
    try:
        query = """
            SELECT 
                clientes.nome AS cliente_nome, 
                produtos.nome AS produto_nome, 
                itens_venda.quantidade, 
                itens_venda.preco_total, 
                vendas.data_venda
            FROM vendas
            JOIN clientes ON vendas.cliente_id = clientes.id
            JOIN itens_venda ON vendas.id = itens_venda.venda_id
            JOIN produtos ON itens_venda.produto_id = produtos.id
            WHERE vendas.vendedor_id = %s;
        """
        db.cursor.execute(query, (id_usuario,))
        vendas = db.cursor.fetchall()

        for venda in vendas:
            tree_vendas.insert("", "end", values=venda)

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar suas vendas: {e}")

    # Botão de voltar
    Button(frame, text="Voltar", command=lambda: abrir_home_vendedor(id_usuario), width=20).grid(row=2, column=0, columnspan=2, pady=20)

def exportar_relatorio_vendas():
    # Busca os dados de vendas no banco
    vendas = db.gerar_relatorio_vendas()  # Deve retornar uma lista de tuplas com os d

    # Configura o arquivo para salvar
    arquivo = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")],
        title="Salvar Relatório de Vendas"
    )

    if not arquivo:  # Se o usuário cancelar a operação
        return

    # Gera o relatório CSV
    try:
        with open(arquivo, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Cabeçalho do CSV
            writer.writerow(["Cliente", "Vendedor", "Produtos", "Quantidade", "Valor Total", "Data"])

            # Dados das vendas
            for venda in vendas:
                cliente_id, vendedor_id, produtos_nome, quantidade, valor_total, data = venda
                writer.writerow([cliente_id, vendedor_id, produtos_nome, quantidade,f"{valor_total:.2f}", data])

        # Mensagem de sucesso
        messagebox.showinfo("Sucesso", "Relatório exportado com sucesso!")
    except Exception as e:
        # Mensagem de erro em caso de falha
        messagebox.showerror("Erro", f"Não foi possível exportar o relatório: {e}")

def limpar_tela():
    for widget in janela.winfo_children():
        widget.destroy()

# Configuração inicial da janela
janela = Tk()
janela.title("Sistema de Vendas")
janela.geometry("400x300")
janela.configure(bg="#f0f0f0")
abrir_login()

janela.mainloop()
