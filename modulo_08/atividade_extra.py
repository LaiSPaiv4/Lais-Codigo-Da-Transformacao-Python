print("\n===== Atividade Extra =====\n")

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"{self.titulo} - {self.autor} [{status}]"

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.acervo = [] 

    def adicionar_livro(self, livro):
        self.acervo.append(livro)
        print(f"Livro '{livro.titulo}' adicionado ao acervo de {self.nome}.")

    def listar_livros(self):
        print(f"\n----- Livros na {self.nome} ------\n")
        for livro in self.acervo:
            print(livro) 

    def emprestar_livro(self, titulo_procurado):
        for livro in self.acervo:
            if livro.titulo == titulo_procurado:
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"\n>> Empréstimo realizado: {livro.titulo}")
                    return
                else:
                    print(f"O livro '{livro.titulo}' já está emprestado.")
                    return
        print(f"O livro '{titulo_procurado}' não foi encontrado no acervo.")

# Simulando o Sistema
minha_biblioteca = Biblioteca("Biblioteca Municipal")

# Criamos alguns livros
livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("O Hobbit", "J.R.R. Tolkien")

# Adicionamos os livros à biblioteca
minha_biblioteca.adicionar_livro(livro1)
minha_biblioteca.adicionar_livro(livro2)

# Operações
minha_biblioteca.listar_livros()
minha_biblioteca.emprestar_livro("O Hobbit")
minha_biblioteca.listar_livros()