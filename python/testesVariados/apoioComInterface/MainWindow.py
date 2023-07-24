# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(484, 433)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        #self.lcdNumber = QtWidgets.QLCDNumber(self.centralWidget)
        #self.lcdNumber.setDigitCount(10)
        #self.lcdNumber.setObjectName("lcdNumber")
        #self.verticalLayout.addWidget(self.lcdNumber)
        self.lcdLabel = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.lcdLabel.setFont(font)
        self.lcdLabel.setText("0123456789abcdef\n0123456789abcdef")
        self.verticalLayout.addWidget(self.lcdLabel)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")

        
        self.pushButton_n0 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n0.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n0.setFont(font)
        self.pushButton_n0.setStyleSheet("QPushButton {\n"
"color: #1976D2;\n"
"}")
        self.pushButton_n0.setObjectName("pushButton_n0")
        self.gridLayout.addWidget(self.pushButton_n0, 5, 1, 1, 1)

        
        self.pushButton_n1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n1.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n1.setFont(font)
        self.pushButton_n1.setStyleSheet("QPushButton {\n"
"color: #1976D2;\n"
"}")
        self.pushButton_n1.setObjectName("pushButton_n1")
        self.gridLayout.addWidget(self.pushButton_n1, 2, 0, 1, 1)


        self.pushButton_n2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n2.setFont(font)
        self.pushButton_n2.setStyleSheet("QPushButton {\n"
"color: #1976D2;\n"
"}")
        self.pushButton_n2.setObjectName("pushButton_n2")
        self.gridLayout.addWidget(self.pushButton_n2, 2, 1, 1, 1)
        

        self.pushButton_n3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n3.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n3.setFont(font)
        self.pushButton_n3.setStyleSheet("QPushButton {\n"
"color: #1976D2;\n"
"}")
        self.pushButton_n3.setObjectName("pushButton_n3")
        self.gridLayout.addWidget(self.pushButton_n3, 2, 2, 1, 1)
        
        
        self.pushButton_n4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n4.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n4.setFont(font)
        self.pushButton_n4.setStyleSheet("QPushButton {\n"
"color: #1976D2;\n"
"}")
        self.pushButton_n4.setObjectName("pushButton_n4")
        self.gridLayout.addWidget(self.pushButton_n4, 3, 0, 1, 1)


        self.pushButton_n5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n5.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n5.setFont(font)
        self.pushButton_n5.setStyleSheet("QPushButton {\n"
"color: #1976D2;\n"
"}")
        self.pushButton_n5.setObjectName("pushButton_n5")
        self.gridLayout.addWidget(self.pushButton_n5, 3, 1, 1, 1)


        self.pushButton_n6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n6.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n6.setFont(font)
        self.pushButton_n6.setStyleSheet("QPushButton {\n"
"color: #1976D2;\n"
"}")
        self.pushButton_n6.setObjectName("pushButton_n6")
        self.gridLayout.addWidget(self.pushButton_n6, 3, 2, 1, 1)

        
        self.pushButton_n7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n7.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n7.setFont(font)
        self.pushButton_n7.setStyleSheet("QPushButton {\n"
"color: #1976D2;\n"
"}")
        self.pushButton_n7.setObjectName("pushButton_n7")
        self.gridLayout.addWidget(self.pushButton_n7, 4, 0, 1, 1)
        
        
        self.pushButton_n8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n8.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n8.setFont(font)
        self.pushButton_n8.setStyleSheet("QPushButton {\n"
"color: #1976D2;\n"
"}")
        self.pushButton_n8.setObjectName("pushButton_n8")
        self.gridLayout.addWidget(self.pushButton_n8, 4, 1, 1, 1)        
        
        
        self.pushButton_n9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n9.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n9.setFont(font)
        self.pushButton_n9.setStyleSheet("QPushButton {\n"
"color: #1976D2;\n"
"}")
        self.pushButton_n9.setObjectName("pushButton_n9")
        self.gridLayout.addWidget(self.pushButton_n9, 4, 2, 1, 1)


        self.pushButton_back = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_back.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setStyleSheet("QPushButton {\n"
"color: #1976D2;\n"
"}")
        self.pushButton_back.setObjectName("back")
        self.gridLayout.addWidget(self.pushButton_back, 5, 0, 1, 1)


        self.pushButton_enter = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_enter.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_enter.setFont(font)
        self.pushButton_enter.setStyleSheet("QPushButton {\n"
"color: #1976D2;\n"
"}")
        self.pushButton_enter.setObjectName("ENTER")
        self.gridLayout.addWidget(self.pushButton_enter, 5, 2, 1, 1)
        
        
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tranca"))
        self.pushButton_n4.setText(_translate("MainWindow", "4"))
        self.pushButton_n4.setShortcut(_translate("MainWindow", "4"))
        self.pushButton_n1.setText(_translate("MainWindow", "1"))
        self.pushButton_n1.setShortcut(_translate("MainWindow", "1"))
        self.pushButton_n8.setText(_translate("MainWindow", "8"))
        self.pushButton_n8.setShortcut(_translate("MainWindow", "8"))
        self.pushButton_n7.setText(_translate("MainWindow", "7"))
        self.pushButton_n7.setShortcut(_translate("MainWindow", "7"))
        self.pushButton_n6.setText(_translate("MainWindow", "6"))
        self.pushButton_n6.setShortcut(_translate("MainWindow", "6"))
        self.pushButton_n5.setText(_translate("MainWindow", "5"))
        self.pushButton_n5.setShortcut(_translate("MainWindow", "5"))
        self.pushButton_n0.setText(_translate("MainWindow", "0"))
        self.pushButton_n0.setShortcut(_translate("MainWindow", "0"))
        self.pushButton_n2.setText(_translate("MainWindow", "2"))
        self.pushButton_n2.setShortcut(_translate("MainWindow", "2"))
        self.pushButton_n9.setText(_translate("MainWindow", "9"))
        self.pushButton_n9.setShortcut(_translate("MainWindow", "9"))
        self.pushButton_n3.setText(_translate("MainWindow", "3"))
        self.pushButton_n3.setShortcut(_translate("MainWindow", "3"))
        self.pushButton_back.setText(_translate("MainWindow", "BACK"))
        self.pushButton_back.setShortcut(_translate("MainWindow", "ESC"))
        self.pushButton_enter.setText(_translate("MainWindow", "ENTER"))
        self.pushButton_enter.setShortcut(_translate("MainWindow", "ENTER"))

