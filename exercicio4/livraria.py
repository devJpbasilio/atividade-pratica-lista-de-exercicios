
#Mensagens de boas-vindas
print('     Bem-vindo a Livraria do João Silva.    ')
#Lista para armazenar os livros = []
lista_livro = []

id_global = 0

def cadastrar_livro(id):
    print("-" * 44)
    print('------------MENU CADASTRAR LIVRO------------')
    nome = input('Por favor entre com o nome do livro: ')
    autor = input('Por favor entre com o autor do livro: ')
    editora = input('Por favor entre com a editora do livros: ')
    
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(livro)
    print('Livro cadastrado com sucesso!\n')
    
    
def consultar_livro():
    print("-" * 44)
    print('------------MENU CONSULTAR LIVRO------------')
    while True:
        opcao = input("""
        Escolha a opção de consulta:
        1 - Consultar Todos os Livros
        2 - Consultar Livro por ID
        3 - Consultar Livro(s) por Autor
        4 - Retornar
        >>: """
        )
        
        if opcao == "1":
            print("\nLista de todos os Livros:")
            for livro in lista_livro:
                print(f"ID: {livro['id']}")
                print(f"Nome: {livro['nome']}")
                print(f"Autor: {livro['autor']}")
                print(f"Editora: {livro['editora']}")
                print("-" * 44)
        elif opcao == "2":
            id_consulta = int(input("Digite o ID do livro: "))
            livro_encontrado = next((livro for livro in lista_livro if livro["id"] == id_consulta), None)
            if livro_encontrado:
                print(f"ID: {livro_encontrado['id']}")
                print(f"Nome: {livro_encontrado['nome']}")
                print(f"Autor: {livro_encontrado['autor']}")
                print(f"Editora: {livro_encontrado['editora']}")
                print("-" * 44)
            else:
                print("ID não encontrado!")
        elif opcao == "3":
            autor_consulta = input("Digite o autor do(s) livro(s): ")
            livros_autor = [livro for livro in lista_livro if livro["autor"] == autor_consulta]
            if livros_autor:
                for livro in livros_autor:
                    print(f"ID: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Editora: {livro['editora']}")
                    print("-" * 44)
            else:
                print("Nenhum livro encontrado para este autor.")
        elif opcao == "4":
            break
        else:
            print("Opção inválida! Tente novamente.")
            

def remover_livro():
    while True:
        print("-" * 44)
        print('------------MENU REMOVER LIVRO------------')
        id_remover = int(input('Digite o ID do Livro a ser removido: '))
        for livro in lista_livro:
            if livro['id'] == id_remover:
                lista_livro.remove(livro)
                print('Livro removido com sucesso.\n')
                return
        print('ID inválido! Tente novamente.')
        
        
# Estrutura do menu principal
while True:
    print("-" * 44)
    print('---------------MENU PRINCIPAL---------------')
    opcao = input("""
    Escolha uma opção:
    1 - Cadastrar Livro
    2 - Consultar Livro(s)
    3 - Remover Livro
    4 - Sair
    >> """
    )
    
    if opcao == "1":
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == "2":
        consultar_livro()
    elif opcao == "3":
        remover_livro()
    elif opcao == "4":
        print("Programa encerrado. Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")