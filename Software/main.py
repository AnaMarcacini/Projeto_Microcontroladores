# Importa as classes Pin e I2C da biblioteca machine para controlar o hardware do Raspberry Pi Pico

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
import math
import micropython

import random
import Display_Pontuacao as dp
# Configuração do display OLED
disp1 = I2C(1, scl=Pin(3), sda=Pin(2), freq=100000)
oled = SSD1306_I2C(128, 32, disp1)
clock = 1 # tempo para iniciar
Tempo_de_Partida = 40 #tempo em segundos da partida
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
tempo_restante = Tempo_de_Partida
temporizador = machine.Timer(-1)

# Função a ser executada a cada segundo pelo temporizador
def callback_temporizador(timer):
    global tempo_restante, clock
    tempo_restante -= 1
    atualizar_display(tempo_restante)
    if tempo_restante <= 0:#Fim do temporizador
        temporizador.deinit()
        clock = 0 #fim do tempo

temporizador.init(period=1000, mode=machine.Timer.PERIODIC, callback=callback_temporizador)#começar o temporizador
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
    
def vitorioso(j1,j2):
    if j1>j2:
        oled.fill(0)
        oled.text("Vencedor:", 30, 10)
        oled.text("Jogador 1", 30, 20)
        oled.show()
        return "J1"
    if j2>j1:
        oled.fill(0)
        oled.text("Vencedor:", 30, 10)
        oled.text("Jogador 2", 30, 20)
        oled.show()
        return "J2"
    else:
        oled.fill(0)
        oled.text("Empate :(", 30, 20)
        oled.show()
        return "Empate"


#--------Codigo_Principal---------------------
Leds, button1, button2 = setup()
reset = Pin(4, Pin.IN,Pin.PULL_DOWN) #botao reset
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
    while(clock):

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
    while(not clock):
        for led in Leds:
            led.value(0)
        #chamar display vitorioso
        vitorioso(j1,j2)
        #print(vitorioso(j1,j2))
        
        for led in Leds:
            led.value(1)
            time.sleep(0.25)
        if reset.value() ==1:#botão recomeçar
            clock = 1
            j1=0
            j2=0
            tempo_restante = Tempo_de_Partida
            temporizador = machine.Timer(-1)
            temporizador.init(period=1000, mode=machine.Timer.PERIODIC, callback=callback_temporizador)
            atualizar_display(tempo_restante)
    #Colocar buzer
    print("sai")



