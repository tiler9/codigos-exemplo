from abc import abstractmethod
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import operator

from MainWindow import Ui_MainWindow
from serialInterface import *

import struct

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.serial = SerialInterface("COM12")
        self.setupUi(self)

        self.eventEnter = 0
        self.numbersToPress = 0
        self.pressed = "0"
        # Setup numbers.
        for n in range(0, 10):
            getattr(self, 'pushButton_n%s' % n).pressed.connect(lambda v=n: self.input_number(v))
        self.pushButton_back.pressed.connect(self.back)
        self.pushButton_enter.pressed.connect(self.enter)

        #self.reset()
        #self.send_receive(200, self.pressed)
        #self.send_receive(self.pressed, 200)
        self.sendCommand(self.pressed, 200)
        #self.display()
        #self.show()

    def back(self):
        if self.pressed == "":
            #self.send_receive(self.pressed, 0)
            self.sendCommand(2, self.pressed)
        else:
            self.pressed = ""
        self.display()

    def enter(self):
       #if self.eventEnter == 1 and len(self.pressed) <= self.numbersToPress:
        if len(self.pressed) <= self.numbersToPress:
            #self.send_receive(self.pressed, 1)
            self.sendCommand(1, self.pressed)
            self.pressed = ""
            self.display()

    def display(self):
        self.lcdLabel.setText(self.stack+self.pressed)        

    def input_number(self, v):
        if len(self.pressed) < self.numbersToPress:
            v=str(v)
            self.pressed += v
            self.display()
            #if len(self.pressed) == self.numbersToPress and self.eventEnter == 0:
            if len(self.pressed) == self.numbersToPress:
                #self.send_receive(self.pressed, 1)
                #self.sendCommand(self.pressed, 0)
                self.sendCommand(0, self.pressed)
                self.pressed = ""
                self.display()

    def reset(self):
        self.pageNumber = 0
        self.pressed = "0"
        self.stack = ""
        self.last_operation = None
        self.current_op = None
        self.display()

    def sendCommand(self, event, numbers):
        packet = b''
        event = int(event)
        if(numbers != ""):
            numbers = int(numbers)
            packet = struct.pack("BBB", 55, 9, event) + struct.pack("Q", numbers)
        else:
            packet = struct.pack("BBB", 55, 9, event) + struct.pack("Q", 0)
        self.serial.send(packet)
        self.receiveControlResponse()

    def receiveControlResponse(self):
        resposta = self.serial.receive()
        try:
            self.eventEnter = resposta[2]
            self.numbersToPress = resposta[3]
            self.stack = resposta[4:].decode()
            #print("eventEnter: " + str(self.eventEnter))
            #print("numbersToPress: " + str(self.numbersToPress))
            print("\nMensagem do Controlador: " + str(self.stack))
            #print(resposta)
            self.display()
            self.show()
            # print("== Mensagem do Controle: " + str(self.stack.decode('ascii')))
            # print("== Mensagem do Controle: " + str(self.stack.decode()) )

            if(self.numbersToPress == 0):
                self.receiveControlResponse()
        except:
            print("Erro ao formatar mensagem")

    def send_receive(self, event, numbers):
        #print(numbers, numbers[::-1])
        #numbers = int(numbers[::-1])
        event = int(event)
        packet = struct.pack("BBB", 55, 9, event) + struct.pack("Q", numbers)
        #print(event, numbers, packet)
        
        '''
        if event == 0:
            if self.pageNumber != 0:
                self.pageNumber -= 1
        else:
            self.pageNumber +=1

        if self.pageNumber == 0:
            received = b"\x00\x01Tranca:\n"
        elif self.pageNumber == 1:
            received = b"\x01\x06Senha:\n"
        elif self.pageNumber == 2:
            received = b"\x01\x06Senha2:\n"
        else:
            self.pageNumber -= 1
            return
        '''
        b"\x00\x01Tranca:\n"
        
        #received = self.serial.sendReceive(packet)
        self.serial.send(packet)
        
        

        # self.eventEnter = received[2]
        # self.numbersToPress = received[3]
        # self.stack = received[4:].decode()
        # print("eventEnter: " + str(self.eventEnter))
        # print("numbersToPress: " + str(self.numbersToPress))
        # print("stack: " + str(self.stack))
        # print(received)
        self.display()
        #self.show()
        if self.numbersToPress == 0:
            #self.send_receive(event, 0)
            received = self.serial.receive()


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Tranca")

    window = MainWindow()
    app.exec_()
