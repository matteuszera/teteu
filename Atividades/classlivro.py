class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
    
    def descricao(self):
        return f"Autor: {self.autor}, ano da publicação: {self.ano_publicacao}, título: {self.titulo}"

Livro1 = Livro("Descoberta do Brasil", "AutorMateus", 1500)
