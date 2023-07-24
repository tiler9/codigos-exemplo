# import numpy as np
# from scipy import fft
# from scipy.io import wavfile
# import json
# import sys
# import os
# import struct
# import serial
# from serial.serialutil import SerialException

# com_serial = serial.Serial()
# com_serial.port = "COM4"
# com_serial.baudrate = 115200
# com_serial.timeout = 2

# def frequency_spectrum(x, samplerate):
#     """
#     Derive frequency spectrum of a signal from time domain
#     :param x: signal in the time domain
#     :param sf: sampling frequency
#     :returns frequencies and their content distribution
#     """
#     x = x - np.average(x)  # zero-centering

#     n = len(x)
#     k = np.arange(n)
#     tarr = n / float(samplerate)
#     frqarr = k / float(tarr)  # two sides frequency range
#     frqarr = frqarr[range(n // 2)]  # one side frequency range
#     x = fft.fft(x) / n  # fft computing and normalization
#     x = x[range(n // 2)]

#     return frqarr, abs(x)

# class Musica:
#     def __init__(self, nome, frequencias, tempos):
#         self.nome = nome
#         self.frequencias = frequencias
#         self.tempos = tempos

# class Sistema:
#     def __init__(self):
#         self.localMusicasWav = os.path.dirname(os.path.realpath(__file__))+"/musics_wav/"
#         self.localMusicasTones = os.path.dirname(os.path.realpath(__file__))+"/musics_tones/"
#         self.listaMusicas = self.retornaListaMusicas(".wav")

#     def retornaListaMusicas(self, extensao):
#         lista = os.listdir(self.localMusicasWav) if (extensao == ".wav") else os.listdir(self.localMusicasTones)
#         for i,musica in enumerate(lista):
#             lista[i] = musica[0: len(musica)-len(extensao)]
#         return lista

#     def geraDadosMusicas(self, nomeMusica):

#         tempoFatia = 0.100

#         samplerate, signal = wavfile.read(self.localMusicasWav + nomeMusica + '.wav')

#         y = signal[:, 0]  

#         nMostrasPorFatia = int(samplerate*tempoFatia)

#         listaFrequencias = []
#         listaMagnitudes = []
#         listaFatiasFrequencias = []
#         listaMaxFrequenciasFatia = []

#         listaTempos = []

#         listaFrequencias, listaMagnitudes = frequency_spectrum(y, samplerate)

#         magRuidoGeral = max(listaMagnitudes)

#         for i in range(0, len(y), nMostrasPorFatia):    
#             # print(type(y[i-4410:i]))
#             listaFatiasFrequencias = y[i-nMostrasPorFatia:i]
#             if(len(listaFatiasFrequencias) > 0):
#                 listaFrequencias, listaMagnitudes = frequency_spectrum(listaFatiasFrequencias, samplerate)
#                 max_magnitudeFatia = max(listaMagnitudes)
#                 magRuidoRegional = max(listaMagnitudes)*0.99
#                 # print(max_magnitudeFatia, " > ", magRuidoRegional, " , ", magRuidoGeral)
#                 if( (max_magnitudeFatia > magRuidoRegional) and (max_magnitudeFatia > magRuidoGeral)):
#                     for i,mag in enumerate(listaMagnitudes):
#                         if(mag == max_magnitudeFatia):
#                             listaMaxFrequenciasFatia.append(int(listaFrequencias[i]))
#                 else:
#                     listaMaxFrequenciasFatia.append(1)

#                 max_magnitudeFatia = 0
        
#         for i in listaMaxFrequenciasFatia:
#             listaTempos.append(int(tempoFatia*1000))

#         print(listaMaxFrequenciasFatia)
#         print(listaTempos)

#         listaFrequenciasAgrupado = []
#         listaTemposAgrupado = []

#         i = 0
#         j= 0
#         achouDiferente = 0
#         tempoSomado = 0
#         while( i < len(listaMaxFrequenciasFatia) and i < len(listaMaxFrequenciasFatia) ):
#             achouDiferente = 0

#             while( achouDiferente == 0):
#                 if(listaMaxFrequenciasFatia[i] == listaMaxFrequenciasFatia[j]):
#                     tempoSomado += listaTempos[0]
#                     if(j+1 < len(listaMaxFrequenciasFatia) ):
#                         j = j+1
#                     else:
#                         i = j
#                         achouDiferente = 1
#                         if(listaMaxFrequenciasFatia[i] != listaMaxFrequenciasFatia[i-1]):
#                             # print( listaMaxFrequenciasFatia[i])
#                             # print(tempoSomado)
#                             listaFrequenciasAgrupado.append(listaMaxFrequenciasFatia[i])
#                             listaTemposAgrupado.append(tempoSomado)
#                         i += 1
#                 elif(listaMaxFrequenciasFatia[i] != listaMaxFrequenciasFatia[j]):
#                     achouDiferente = 1
#                     listaFrequenciasAgrupado.append(listaMaxFrequenciasFatia[i])
#                     listaTemposAgrupado.append(tempoSomado)
#                     tempoSomado = 0
#                     i = j

#         print(listaFrequenciasAgrupado)
#         print(listaTemposAgrupado)

#         musica = {
#             "frequencias" : listaFrequenciasAgrupado,
#             "tempos" : listaTemposAgrupado,
#         }


#         file = open(self.localMusicasTones + nomeMusica + ".json", "w")
#         json.dump(musica, file)
#         file.close()

#     def abre_porta_serial(self):
#         print("Abrindo porta Serial " + com_serial.port)
#         try:
#             com_serial.open()
#             print("Serial " + com_serial.port + " conectado!")

#         except SerialException as erro:
#             print("Erro ao conectar a porta serial: ")
#             print(erro)
#             sys.exit()


#     def enviaMusica(self, musica: Musica):

#         musica_bytes = b'' 

#         for i in range(0, len(musica.frequencias)):
#             musica_bytes += struct.pack("H" , int(musica.frequencias[i])) 
            
#         for i in range(0, len(musica.tempos)):
#             musica_bytes += struct.pack("H" , int(musica.tempos[i])) 

#         pacoteEnvio = struct.pack("H", len(musica_bytes)) + musica_bytes

#         com_serial.write(pacoteEnvio)

#     def checaMusica(self, nomeMusica):

#         if(nomeMusica not in self.retornaListaMusicas(".json")):
#             print("Gerando dados para música", nomeMusica, "...")
#             self.geraDadosMusicas(nomeMusica)
#             print("Dados gerados ", nomeMusica, "...")
        
#         x = open( self.localMusicasTones + nomeMusica + ".json" )
#         data = json.load(x)
#         musica = Musica(nomeMusica, data['frequencias'], data['tempos'])

#         self.enviaMusica(musica)


# sistema = Sistema()

# sistema.abre_porta_serial()


# print("\n\n\n\t==== PyMuP ====")

# escolha_menu = 1
# while escolha_menu != 0:

#     print("\n\n\n")
#     for indexMusica,nomeMusica in enumerate(sistema.listaMusicas):
#         print(f'{indexMusica + 1} - {nomeMusica}')

#     escolha_menu = int(input("\nEscolha a música pelo número (0 para sair) : "))
#     if( (escolha_menu <= len(sistema.listaMusicas) ) and escolha_menu != 0  ):
#         sistema.checaMusica(sistema.listaMusicas[escolha_menu-1])
#     elif(escolha_menu > len(sistema.listaMusicas)):
#         print("\nOpção não está dentro da lista")

# import winsound
# # winsound.Beep(1000, 100)
# # winsound.Beep(440, 200)

# for i in range(200, 300, 1):
#     print(i)
#     winsound.Beep(i, 100)

from time import sleep
import sounddevice as sd
import numpy as np
# import matplotlib.pyplot as plt

framerate = 44100
time = 1000
f = 440
t = np.linspace(0, time/1000, int(framerate*time/1000))
print(len(t))
wave = np.sin(2*np.pi* f * t)

# print(t)
sd.play(wave, framerate)
sd.wait()

# print(t)
for i in range(0,1000,100):
    # t = np.linspace(0, time/10000, int(framerate*time/10000))
    print(len(t))
    wave = np.sin(2*np.pi* i * t)
    sd.play(wave, framerate)
    # sd.wait()
# sleep(10)