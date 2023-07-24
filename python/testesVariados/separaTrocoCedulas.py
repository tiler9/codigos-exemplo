def validaString(valor):

    mensagem = ""

    contadorSeparadores = 0
    caracteresInvalidos = []

    for a in list(valor):
        # checando por mais de 1 separador decimal
        if a in ",.":
            contadorSeparadores += 1
        # checando se todos os caracteres indicam se um número
        if (a.isdigit() == False) and (a not in ",."):
            caracteresInvalidos.append(a)

    if contadorSeparadores > 1:
        mensagem += "Apenas 1 separador de casa decimal (',', '.') permitido . "

    if len(caracteresInvalidos) > 0:
        mensagem += f"Caracteres inválidos foram mandados : {caracteresInvalidos} .  "

    return mensagem


def separaCedulas(valor):
    valorSeparado = ""
    separador = ',' if ',' in valor else '.'
    listaNotas = [100, 50, 20, 10, 5, 2, 1]
    listaMoedas = [50, 25, 10, 5, 1]

    NotasMoedas = valor.split(separador)

    # notas
    notas = float(NotasMoedas[0])
    stringNotas = "Notas: \n"

    for i in range(0, 7):
        if notas // listaNotas[i] > 0:
            stringNotas += f"{notas // listaNotas[i]} nota(s) de {listaNotas[i]} reais\n"
            notas -= (notas // listaNotas[i])*listaNotas[i]

    # moedas
    moedas = float(NotasMoedas[1])
    stringMoedas = "Moedas: \n"

    for i in range(0, 5):
        if moedas // listaMoedas[i] > 0:
            stringMoedas += f"{moedas // listaMoedas[i]} moeda(s) de {listaMoedas[i]} centavos\n"
            moedas -= (moedas // listaMoedas[i])*listaMoedas[i]

    valorSeparado = stringNotas + stringMoedas

    return valorSeparado


if __name__ == "__main__":
    valor = input("Coloque o valor do troco: ")

    mensagemErro = validaString(valor)

    if(mensagemErro) == "":
        print(separaCedulas(valor))
    else:
        print(mensagemErro)
