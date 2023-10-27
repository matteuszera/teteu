class Universidade:
    def __init__(self):
        self.cursos = {} 
        self.professores = {}  

    def adicionar_curso(self, nome_curso):
        self.cursos[nome_curso] = {'professor': None}

    def adicionar_professor(self, nome_professor):
        self.professores[nome_professor] = {'cursos': []}

    def designar_professor_para_curso(self, nome_professor, nome_curso):
        if nome_professor in self.professores and nome_curso in self.cursos:
            self.cursos[nome_curso]['professor'] = nome_professor
            self.professores[nome_professor]['cursos'].append(nome_curso)
            print(f'O professor {nome_professor} foi designado para o curso {nome_curso}.')
        else:
            print('Professor ou curso não encontrados.')

    def listar_cursos_do_professor(self, nome_professor):
        if nome_professor in self.professores:
            cursos_lecionados = self.professores[nome_professor]['cursos']
            if cursos_lecionados:
                print(f'O professor {nome_professor} leciona os seguintes cursos:')
                for curso in cursos_lecionados:
                    print(f'- {curso}')
            else:
                print(f'O professor {nome_professor} não leciona nenhum curso no momento.')
        else:
            print('Professor não encontrado.')


universidade = Universidade()

universidade.adicionar_curso('Matemática')
universidade.adicionar_curso('História')
universidade.adicionar_professor('Marcos')
universidade.adicionar_professor('Maria')

universidade.designar_professor_para_curso('Marcos', 'Matemática')
universidade.designar_professor_para_curso('Maria', 'História')

universidade.listar_cursos_do_professor('Marcos')
universidade.listar_cursos_do_professor('Maria')
universidade.listar_cursos_do_professor('Pedro')  
