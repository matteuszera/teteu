def minha_funcao(**kwargs):
    for chave, valor in kwargs.items():
        print(f"A chave é {chave} é o valor é {valor}")
    print(type(kwargs))

minha_funcao(nome="Joao", idade=26, pais="Brasil")