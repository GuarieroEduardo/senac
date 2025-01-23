import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.conexao = self.conectar()
        self.cursor = self.conexao.cursor() if self.conexao else None 
    def conectar(self):
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="sistemadevendas",
                use_pure=True
            )

            if conexao.is_connected():
                print("Conexão bem-sucedida!")
                return conexao
            else:
                print("Erro ao conectar com o banco de dados!")
        except Error as e:
            print(f"Erro ao conectar: {e}")
            return None
        
    def obter_produtos(self):
        if not self.cursor:
            print("Erro: Conexão não estabelecida.")
            return []
        try:
            # Consulta para obter todos os produtos
            query = "SELECT nome FROM produtos"
            self.cursor.execute(query)
            produtos = self.cursor.fetchall()
            # Retorna apenas os nomes dos produtos
            return [produto[0] for produto in produtos]
        except Error as e:
            print(f"Erro ao obter produtos: {e}")
            return []

    def cadastrar_produto(self, nome, descricao, quantidade, valor_unitario):
        if not self.cursor:
            print("Erro: Conexão não estabelecida.")
            return False
        try:
            query = "INSERT INTO produtos (nome, descricao, quantidade_estoque, valor_unitario) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (nome, descricao, quantidade, valor_unitario))
            self.conexao.commit()
            print("Produto cadastrado com sucesso!")
            return True
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao cadastrar produto: {e}")
            return False

    def cadastrar_usuario(self, nome, login, senha, tipo):
        if not self.cursor:
            print("Erro: Conexão não estabelecida.")
            return False
        if tipo not in ['admin', 'vendedor']:
            print("Tipo de usuário inválido. Use 'admin' ou 'vendedor'.")
            return False
        try:
            query = "INSERT INTO usuarios (nome, login, senha, tipo) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (nome, login, senha, tipo))
            self.conexao.commit()
            print("Usuário cadastrado com sucesso!")
            return True
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao cadastrar usuário: {e}")
            return False

    def verificar_estoque(self, produto_id, quantidade):
        if not self.cursor:
            print("Erro: Conexão não estabelecida.")
            return False
        try:
            query = "SELECT quantidade_estoque FROM produtos WHERE id = %s"
            self.cursor.execute(query, (produto_id,))
            resultado = self.cursor.fetchone()
            if resultado and resultado[0] >= quantidade:
                return True
            else:
                print("Estoque insuficiente.")
                return False
        except Error as e:
            print(f"Erro ao verificar estoque: {e}")
            return False

    def cadastrar_venda(self, cliente_id, vendedor_id, forma_pagamento, parcelas, produtos):
        if not self.cursor:
            print("Erro: Conexão não estabelecida.")
            return False
        try:
            query_venda = """
                INSERT INTO vendas (cliente_id, vendedor_id, forma_pagamento, parcelas)
                VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query_venda, (cliente_id, vendedor_id, forma_pagamento, parcelas))
            venda_id = self.cursor.lastrowid

            for produto_id, quantidade in produtos:
                if not self.verificar_estoque(produto_id, quantidade):
                    raise ValueError("Estoque insuficiente para o produto ID: {produto_id}")

                query_item = """
                    INSERT INTO itens_venda (venda_id, produto_id, quantidade)
                    VALUES (%s, %s, %s)
                """
                self.cursor.execute(query_item, (venda_id, produto_id, quantidade))

            self.conexao.commit()
            print("Venda cadastrada com sucesso!")
            return True
        except Exception as e:
            self.conexao.rollback()
            print(f"Erro ao cadastrar venda: {e}")
            return False

    def gerar_relatorio_vendas(self):
        if not self.cursor:
            print("Erro: Conexão não estabelecida.")
            return []
        try:
            query = """
                SELECT 
                    clientes.nome AS cliente,
                    usuarios.nome AS vendedor,
                    produtos.nome AS produto,
                    itens_venda.quantidade,
                    itens_venda.preco_total,
                    vendas.data_venda
                FROM vendas
                JOIN clientes ON vendas.cliente_id = clientes.id
                JOIN usuarios ON vendas.vendedor_id = usuarios.id
                JOIN itens_venda ON vendas.id = itens_venda.venda_id
                JOIN produtos ON itens_venda.produto_id = produtos.id
                ORDER BY vendas.data_venda;
            """
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            print(f"Erro ao gerar relatório de vendas: {e}")
            return []
        
    def gerar_relatorio_total_por_mes(self):
        if not self.cursor:
            print("Erro: Conexão não estabelecida.")
            return []
        try:
            query = """
                SELECT 
                    DATE_FORMAT(data_venda, '%Y-%m') AS mes,
                    SUM(itens_venda.preco_total) AS total_arrecadado
                FROM vendas
                JOIN itens_venda ON vendas.id = itens_venda.venda_id
                GROUP BY DATE_FORMAT(data_venda, '%Y-%m')
                ORDER BY mes;
            """
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            print(f"Erro ao gerar relatório mensal: {e}")
            return []


    def fechar_conexao(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()
            print("Conexão com o banco de dados encerrada.")

