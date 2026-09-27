import matplotlib.pyplot as plt


class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade


livros = []


def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    genero = input("Digite o gênero do livro: ")
    quantidade = int(input("Digite a quantidade disponível: "))

    novo_livro = Livro(titulo, autor, genero, quantidade)
    livros.append(novo_livro)

    print(f"Livro '{titulo}' cadastrado com sucesso!")


def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    print("\n--- Lista de Livros ---")

    for livro in livros:
        print(f"Título: {livro.titulo}, Autor: {livro.autor}, Gênero: {livro.genero}, Quantidade: {livro.quantidade}")

    print("-----------------------\n")


def buscar_livro_por_titulo():
    if not livros:
        print("Nenhum livro cadastrado para busca.")
        return

    titulo_busca = input("Digite o título do livro que deseja buscar: ")
    encontrado = False

    for livro in livros:
        if livro.titulo.lower() == titulo_busca.lower():
            print("\n--- Livro Encontrado ---")
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Gênero: {livro.genero}, Quantidade: {livro.quantidade}")
            print("------------------------\n")

            encontrado = True
            break

    if not encontrado:
        print(f"Livro com o título '{titulo_busca}' não encontrado.")


def gerar_grafico_por_genero():
    if not livros:
        print("Nenhum livro cadastrado para gerar o gráfico.")
        return

    generos = {}

    for livro in livros:
        generos[livro.genero] = generos.get(livro.genero, 0) + livro.quantidade

    nomes_generos = list(generos.keys())
    quantidades = list(generos.values())

    plt.bar(nomes_generos, quantidades, color='skyblue')
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade de Livros")
    plt.title("Quantidade de Livros por Gênero")
    plt.show()


def menu():
    while True:
        print("\n--- Sistema de Gerenciamento de Livros ---")
        print("1. Cadastrar novo livro")
        print("2. Listar todos os livros")
        print("3. Buscar livro por título")
        print("4. Gerar gráfico de livros por gênero")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_livro()
        elif escolha == '2':
            listar_livros()
        elif escolha == '3':
            buscar_livro_por_titulo()
        elif escolha == '4':
            gerar_grafico_por_genero()
        elif escolha == '5':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    menu()