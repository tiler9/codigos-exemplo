import json
import serial


class SerialInterface:
    def __init__(self, serialPort):
        self.ser = serial.Serial(serialPort, 115200, timeout=300)

    def sendReceive(self, msgToSend):
        value = b''
        self.ser.write(msgToSend)
        value = self.ser.read(2)
        value += self.ser.read(value[1])

        return value

    def send(self, msgToSend):
        self.ser.write(msgToSend)
        #print("\n==Enviado")
        #print(msgToSend)
        #print(list(msgToSend))
    
    def receive(self):
        resposta = b''
        resposta += self.ser.read(2)
        if resposta != b'':
            size = resposta[1] - 2 # '-2' compensação de caracter nulo da string 
            resposta += self.ser.read(size)

            #print("\n== Bytes Controle: ")
            #print(resposta)

        else:
            print("\nSem mensagens do controlador")
        #value += self.ser.read(value[1])
        return resposta
