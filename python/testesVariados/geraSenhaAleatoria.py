from random import randint

Caracteres = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
listaCaracteres = list(Caracteres)
tamanhoSenha = 10
senha = ""
for i in range(0, tamanhoSenha):
    senha += listaCaracteres[randint(0, len(listaCaracteres) - 1)]

print(senha)
