# Importa as classes Pin e I2C da biblioteca machine para controlar o hardware do Raspberry Pi Pico

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
import math
import micropython

import random
import Display_Pontuacao as dp
# Configuração do display OLED
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=100000)
oled = SSD1306_I2C(128, 64, i2c)

# Função para converter um valor de hora, minuto ou segundo em um formato "hh:mm:ss"
def segundos_para_hms(segundos):
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = segundos % 60
    return "{:02d}:{:02d}:{:02d}".format(h, m, s)

# Função para atualizar o display OLED com o tempo restante
def atualizar_display(tempo_restante):
    oled.fill(0)
    oled.text("Tempo restante:", 0, 0)
    oled.text(segundos_para_hms(tempo_restante), 0, 10)
    oled.show()

# Configuração do temporizador
tempo_restante = 60
temporizador = machine.Timer(-1)

# Função a ser executada a cada segundo pelo temporizador
def callback_temporizador(timer):
    global tempo_restante
    tempo_restante -= 1
    atualizar_display(tempo_restante)
    if tempo_restante <= 0:
        temporizador.deinit()
        oled.fill(0)
        oled.text("Tempo esgotado!", 0, 0)
        oled.show()
        # aqui você pode colocar o código que deve ser executado quando o temporizador acabar

# Inicia o temporizador e atualiza o display OLED com o tempo restante
temporizador.init(period=1000, mode=machine.Timer.PERIODIC, callback=callback_temporizador)
atualizar_display(tempo_restante)

# Código a ser executado em conjunto com o temporizador

def setup():
    # Define o pino do Raspberry Pi Pico conectado ao módulo PIR HC-SR501
    Led_Amarelo = 22
    Led_Vermelho = 21
    Led_Verde = 20
    Led_Amarelo2 = 19

    # Configura o pino da saída digital do sensorLed1 = Pin(Led_Amarelo, Pin.OUT)
    Led1 = Pin(Led_Amarelo, Pin.OUT)
    Led2 = Pin(Led_Vermelho, Pin.OUT)
    Led3 = Pin(Led_Verde, Pin.OUT)
    Led4 = Pin(Led_Amarelo2, Pin.OUT)
    bot11 = Pin(18, Pin.IN,Pin.PULL_DOWN) #botao do led 1 (amarelo)--> jog1
    bot21 = Pin(17, Pin.IN,Pin.PULL_DOWN) #botao do led 1 (amarelo)--> jog2
    bot12 = Pin(16, Pin.IN,Pin.PULL_DOWN) #botao do led 2 (vermelho)--> jog1
    bot22 = Pin(15, Pin.IN,Pin.PULL_DOWN) #botao do led 2 (vermelho)--> jog2
    bot13 = Pin(14, Pin.IN,Pin.PULL_DOWN) #botao do led 3 (verde)--> jog1
    bot23 = Pin(13, Pin.IN,Pin.PULL_DOWN) #botao do led 3 (verde)--> jog2
    bot14 = Pin(12, Pin.IN,Pin.PULL_DOWN) #botao do led 4 (amarelo2)--> jog1
    bot24 = Pin(11, Pin.IN,Pin.PULL_DOWN) #botao do led 4 (amarelo2)--> jog2
    Leds = [Led1,Led2,Led3,Led4]
    button1 = [bot11,bot12,bot13,bot14]
    button2 = [bot21,bot22,bot23,bot24]
    for led in Leds:
        led.value(0)
    return Leds,button1,button2
def sorteio(Leds):
    numero_sorteio = random.randint(0, 3)
    Selecionado = Leds[numero_sorteio]
    Selecionado.value(1)
    
    print(Selecionado)
    return numero_sorteio
    #print(button2[numero_sorteio])Programa principal
    #print(button1[numero_sorteio])
def visualizar():
    print("Jogador 1:")
    print(j1)
    print("Jogador 2: ")
    print(j2)
    
Leds, button1, button2 = setup()
#numero_sorteio = sorteio(Leds)
'''
print("BT")
print(button2[numero_sorteio])
print(button1[numero_sorteio])

'''
j1=0
j2=0
visualizar()
ativos1 = [0,0,0,0]
ativos2 = [0,0,0,0]

while(1):
    #print("Novo Sorteio")
    for led in Leds:
        led.value(0)
    numero_sorteio = sorteio(Leds)
    p = dp.display(j1,j2)
    #print(numero_sorteio)
    print("___________________________________________________")
    while(1):

        if button1[numero_sorteio].value() == 1 and ativos1[numero_sorteio] == 0  :
            Leds[numero_sorteio].value(0)#Apaga led selecionado ao clicar
            j1+=1
            visualizar()
            ativos1[numero_sorteio] = 1
            print("vencedor j1")
        elif button1[numero_sorteio].value() == 0 and ativos1[numero_sorteio] == 1:
            ativos1[numero_sorteio] = 0
            break

        if button2[numero_sorteio].value() == 1 and ativos2[numero_sorteio] == 0 :
            Leds[numero_sorteio].value(0)#Apaga led selecionado ao clicar
            j2+=1
            visualizar()
            ativos2[numero_sorteio] = 1
            print("vencedor j2")
        elif button2[numero_sorteio].value() == 0 and ativos2[numero_sorteio] == 1:
            ativos2[numero_sorteio] = 0
            break



