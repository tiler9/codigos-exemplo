import serial
import struct
import sys

from serial.serialutil import SerialException

serial_debug = serial.Serial()
serial_debug.port = "COM4"
# serial_debug.port = "/dev/ttyUSB0"
serial_debug.baudrate = 115200
serial_debug.timeout = 2


class Pacote:
    def __init__(self, metodo, n1, n2, n3):
        self.metodo = metodo
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3


def abre_porta_serial():
    print("Abrindo porta Serial " + serial_debug.port)
    try:
        serial_debug.open()
        print("Serial " + serial_debug.port + " conectado!")

    except SerialException as erro:
        print("Erro ao conectar a porta serial: ")
        print(erro)
        sys.exit()


def enviaPacote(pacote):
    pacoteEnvio = struct.pack("B", len(pacote)) + pacote

    print("==Enviado")
    print(pacoteEnvio)
    print(list(pacoteEnvio))

    serial_debug.write(pacoteEnvio)
    resposta = b''
    resposta += serial_debug.read(1)
    # print(resposta)
    # print(resposta[0])

    if resposta != b'':
        size = resposta[0]
        resposta += serial_debug.read(size)
        return resposta
    return resposta

def montaPacote1(pacote: Pacote):
    pacote_bytes = b'' + struct.pack("B", pacote.metodo) + struct.pack("B" , pacote.n1) + struct.pack("B", pacote.n2) + struct.pack("B", pacote.n3)

    resposta = enviaPacote(pacote_bytes)
    print("==Resposta")
    print(resposta)
    print(list(resposta))

def montaPacote2(pacote: Pacote):
    pacote_bytes = b'' + struct.pack("B", pacote.metodo) + struct.pack("H" , pacote.n1) + struct.pack("H", pacote.n2) + struct.pack("H", pacote.n3)

    resposta = enviaPacote(pacote_bytes)
    print("==Resposta")
    print(resposta)
    print(list(resposta))
    print(type(resposta))

    # x = struct.unpack("H", resposta[3:])
    # print(x)

    x = struct.unpack("BBHHH", resposta)
    print(x)

escolha_menu = 1
abre_porta_serial()
while escolha_menu != 0:
    escolha_menu = int(input("\n\nDigite o teste \n (0 para sair) : "))
    if(escolha_menu == 1):
        # envia BBB
        pacote = Pacote(1, 10, 120, 100)
        montaPacote1(pacote)
    elif(escolha_menu == 2):
        # envia HHH
        pacote = Pacote(2, 3001, 2800, 10)
        montaPacote2(pacote)
    elif(escolha_menu == 3):
        # envia HHH, recuperando o que foi mandado em 2
        pacote = Pacote(3, 0, 0, 0)
        montaPacote2(pacote)