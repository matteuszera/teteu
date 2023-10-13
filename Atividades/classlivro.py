class Livro:
      def __init__ (self, titulo, autor, ano_publicacao):
          self. titulo = titulo 
          self. autor = autor
          self. ano_publicacao = ano_publicacao
      def descricao(self):
        return f"Autor: {self.autor} ano da publicaçao: {self.ano_publicacao} titulo é: {self.titulo}"

Livro1 = Livro("AutorMateus", "1500"," Nome do livro: Descoberta do Brasil")
