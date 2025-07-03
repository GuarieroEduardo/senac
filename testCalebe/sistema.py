class Vendedor:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = [] 


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = float(preco)  # Erro 1: garantir que o preço seja armazenado como número (float)


class Venda:
    def __init__(self, vendedor, produto, comissao):
        self.vendedor = vendedor
        self.produto = produto
        self.comissao = produto.preco * (comissao / 100.0)  # Erro 2: calcular porcentagem corretamente


class SistemaComissao:
    def __init__(self):
        self.vendedores = []
        self.produtos = []
        self.vendas = []
        self.comissao_geral = None

    def cadastrar_vendedor(self):
        nome = input("Nome do vendedor: ")
        for v in self.vendedores:
            if v.nome == nome:
                print("Esse vendedor já existe.")
                return  # Erro 3: usar return para interromper o cadastro em caso de duplicidade

        vendedor = Vendedor(nome)
        self.vendedores.append(vendedor)  # Erro 4: precisa salvar o objeto Vendedor, não apenas o nome
        print("Vendedor cadastrado com sucesso!")

    def cadastrar_produto(self):
        nome = input("Nome do produto: ")
        preco = input("Preço do produto: ")
        produto = Produto(nome, preco)
        self.produtos.append(produto)  # Erro 5: precisa salvar o objeto Produto
        print("Produto registrado.")

    def definir_comissao(self):
        valor = input("Digite a porcentagem da comissão (ex: 5 para 5%): ")
        self.comissao_geral = float(valor)
        print("Comissão definida.")

    def cadastrar_venda(self):
        nome_vendedor = input("Nome do vendedor: ")
        vendedor_encontrado = None
        for v in self.vendedores:
            if v.nome == nome_vendedor:
                vendedor_encontrado = v  # Erro 6: corrigido para armazenar o objeto vendedor encontrado
                break

        if vendedor_encontrado is None:
            print("Vendedor não encontrado.")
            return

        if not self.produtos:
            print("Nenhum produto cadastrado.")  # Erro 7: é necessário verificar se há produtos cadastrados
            return

        print("Lista de produtos:")
        for i in range(len(self.produtos)):
            print(f"{i} - {self.produtos[i].nome} - R$ {self.produtos[i].preco}")

        escolha = input("Escolha o número do produto: ")
        produto = self.produtos[int(escolha)]

        if self.comissao_geral is None:
            print("Comissão ainda não cadastrada.")
            return  # Erro 8: necessário impedir venda caso a comissão não tenha sido definida

        venda = Venda(vendedor_encontrado, produto, self.comissao_geral)
        self.vendas.append(venda)
        vendedor_encontrado.vendas.append(venda)
        print("Venda realizada com sucesso!")

    def relatorio_vendas(self):
        if len(self.vendas) == 0:
            print("Nenhuma venda registrada.")
        else:
            for venda in self.vendas:
                print(f"{venda.vendedor.nome} vendeu {venda.produto.nome} por {venda.produto.preco}")  
                # Erro 9: é necessário usar venda.produto.nome, e não o objeto direto

    def relatorio_comissao(self):
        nome = input("Digite o nome do vendedor para consultar a comissão: ")
        total = 0
        for v in self.vendedores:
            if v.nome == nome:
                for venda in v.vendas:
                    total += venda.comissao  # Erro 10: corrigido para somar a comissão, não o objeto Produto
        print(f"Total de comissão: R$ {total:.2f}")

    def menu(self):
        sair = False
        while not sair:
            print("\n===== MENU =====")
            print("1 - Cadastrar Vendedor")
            print("2 - Cadastrar Produto")
            print("3 - Definir Comissão")
            print("4 - Registrar Venda")
            print("5 - Relatório de Vendas")
            print("6 - Relatório de Comissão por Vendedor")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")
            
            # Erro 11: input retorna string, precisa comparar como string
            if opcao == "1": 
                self.cadastrar_vendedor()
            elif opcao == "2":
                self.cadastrar_produto()
            elif opcao == "3":
                self.definir_comissao()
            elif opcao == "4":
                self.cadastrar_venda()
            elif opcao == "5":
                self.relatorio_vendas()
            elif opcao == "6":
                self.relatorio_comissao()
            elif opcao == "0":
                sair = True
            else:
                print("Opção inválida")


# Execução
sistema = SistemaComissao()
sistema.menu()
