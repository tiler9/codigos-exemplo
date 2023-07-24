import serial
import struct
import sys
import time
import codecs

from serial.serialutil import SerialException

serial_debug = serial.Serial()
serial_debug.port = "COM12"
# serial_debug.port = "/dev/ttyUSB0"
serial_debug.baudrate = 115200
serial_debug.timeout = 30


class PacoteRespostaControle:
    def __init__(self , respostaLista ):
        if(len(respostaLista) > 1):
            self.comVerifier = respostaLista[0]
            self.sizeBuffer = respostaLista[1]
            self.enterNecessity = respostaLista[2]
            self.nDigitsEntry = respostaLista[3]
            self.message = respostaLista[4:]

def abre_porta_serial():
    try:
        serial_debug.open()

    except SerialException as erro:
        print("Erro ao conectar a porta serial: ")
        print(erro)
        sys.exit()


def sinalEntrada(): # pra quando o usuário fazer a 1ª interação
    lista_bytes = b'' + struct.pack("B", 1) + struct.pack("Q", 200) 
    print("Enviando sinal de entrada.")
    return lista_bytes

# '2' nº de dados, '1' -> 0 - back; 1 - enter, 'dados' 
def montaListaBytes(dado):
    lista_bytes = b'' + struct.pack("B", 0) + struct.pack("Q", dado) 
    return lista_bytes

def enviaPacote(pacote):
    pacoteEnvio = struct.pack("BB", 55 ,len(pacote)) + pacote

    print("\n==Enviado")
    print(pacoteEnvio)
    print(list(pacoteEnvio))

    serial_debug.write(pacoteEnvio)
    readBytes()


def readBytes():
    resposta = b''
    resposta += serial_debug.read(2)
    if resposta != b'':
        size = resposta[1] - 2 # '-1' compensação de caracter nulo da string 
        #size = resposta[0]
        resposta += serial_debug.read(size)

        print("\n== Bytes Controle: ")
        print(resposta)
        respostaFormatada = ""

        try:
            respostaFormatada = PacoteRespostaControle(resposta)
            print("== Mensagem do Controle: " + str(respostaFormatada.message.decode('ascii')))
        except:
            print("\n Erro ao mostrar mensagem formatada: ")

        if(respostaFormatada != "" and respostaFormatada.nDigitsEntry == 0):
            readBytes()
    else:
        print("\nSem mensagens do controlador")

escolha_menu = 100
dado = 101
lista_dados_bytes = ''
lista_dados = []
abre_porta_serial()

#no primeiro uso, a tela estará desligada e o usuário aperta Enter
lista_dados_bytes = sinalEntrada()
enviaPacote(lista_dados_bytes)

        
while dado != 100:
    lista_dados = []
    lista_dados_bytes = b''
    dado = int(input("\n\nEntrada: \n (100 para sair) : "))
    if(dado != 100):
        print('\n\n== Enviado da IE: ' + str(dado))
        lista_dados_bytes = montaListaBytes(dado)

        if( len(lista_dados_bytes) > 0):
            enviaPacote(lista_dados_bytes)