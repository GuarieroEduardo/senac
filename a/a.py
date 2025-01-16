import mysql.connector

def conectar():
    try:
        print("Tentando conectar...")

        conexao = mysql.connector.connect(
            host="localhost",  
            user="root",
            password="",  
            database="sistemadevendas",
            port=3307,  
            use_pure=True
        )

        print("Conexão estabelecida!")
        return conexao

    except mysql.connector.Error as e:
        print(f"Erro ao conectar: {e}")
        return None


def testar_select():
    conexao = conectar()
    if conexao:
        try:
            # Crie o cursor para executar consultas
            cursor = conexao.cursor()
            
            # Execute um SELECT simples (altere a tabela e colunas conforme seu banco)
            query = "SELECT * FROM usuarios;"  # Substitua "sua_tabela" pelo nome da tabela no banco
            cursor.execute(query)
            
            # Obtenha os resultados
            resultados = cursor.fetchall()
            
            # Verifique se há resultados e exiba-os
            if resultados:
                print("Resultados obtidos:")
                for linha in resultados:
                    print(linha)
            else:
                print("Nenhum dado encontrado na tabela.")

        except mysql.connector.Error as e:
            print(f"Erro ao executar SELECT: {e}")
        finally:
            # Feche a conexão
            conexao.close()

# Execute a função
testar_select()

