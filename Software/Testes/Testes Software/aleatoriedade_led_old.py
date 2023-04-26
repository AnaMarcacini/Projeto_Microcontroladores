# Importa as classes Pin e I2C da biblioteca machine para controlar o hardware do Raspberry Pi Pico
from machine import Pin
import random


# Define o pino do Raspberry Pi Pico conectado ao módulo PIR HC-SR501
Led_Amarelo = 22
Led_Vermelho = 21
Led_Verde = 20
Led_Amarelo2 = 19
botao11 = 18
botao21 = 17

# Configura o pino da saída digital do sensorLed1 = Pin(Led_Amarelo, Pin.OUT)
Led1 = Pin(Led_Amarelo, Pin.OUT)
Led2 = Pin(Led_Vermelho, Pin.OUT)
Led3 = Pin(Led_Verde, Pin.OUT)
Led4 = Pin(Led_Amarelo2, Pin.OUT)
bot11 = Pin(botao11, Pin.IN,Pin.PULL_DOWN) #botao do led 1 (amarelo)--> jog1
bot21 = Pin(botao21, Pin.IN,Pin.PULL_DOWN) #botao do led 1 (amarelo)--> jog2
bot12 = Pin(16, Pin.IN,Pin.PULL_DOWN) #botao do led 2 (vermelho)--> jog1
bot22 = Pin(16, Pin.IN,Pin.PULL_DOWN) #botao do led 2 (vermelho)--> jog2
bot13 = Pin(16, Pin.IN,Pin.PULL_DOWN) #botao do led 3 (verde)--> jog1
bot23 = Pin(16, Pin.IN,Pin.PULL_DOWN) #botao do led 3 (verde)--> jog2
bot14 = Pin(16, Pin.IN,Pin.PULL_DOWN) #botao do led 4 (amarelo2)--> jog1
bot24 = Pin(16, Pin.IN,Pin.PULL_DOWN) #botao do led 4 (amarelo2)--> jog2
Leds = [Led1,Led2,Led3,Led4]
#button1 = {Led1: bot11,Led2: bot12,Led3: bot13,Led4: bot14}
#button2 = {Led1: bot21,Led2: bot22,Led3: bot23,Led4: bot24}
button1 = [bot11,bot12,bot13,bot14]
button2 = [bot21,bot22,bot23,bot24]

#print(random.randint(a, b))
#print(Leds[random.randint(a, b)])
Led4.value(0)
numero_sorteio = random.randint(0, 3)
Selecionado = Leds[numero_sorteio]
Selecionado.value(1)
print(Selecionado)
print("BT")
print(button2[numero_sorteio])
print(button1[numero_sorteio])
'''
j1=0
j2=0
print(bot1.value())
print(bot2.value())

print("Jogador 1:")
print(j1)
print("Jogador 2: ")
print(j2)


while(1):
    Selecionado = Leds[random.randint(0, 3)] #ta selecionando mais de 1 por vez e adiciona muito no jogador2 
    Selecionado.value(1)
    print(Selecionado)
    while(1):
        if bot1.value() == 1:
            print("bot 1")
            print(bot1.value())
            Selecionado.value(0)#Apaga led selecionado ao clicar
            bot1.value(0)
            j1+=1
            print("Jogador 1:")
            print(j1)
            print("Jogador 2: ")
            print(j2)
            print("Interno")
            print(Selecionado)
            break
    


        if bot2.value() == 1:
            print("bot 2")
            print(bot2.value())
            Selecionado.value(0)#Apaga led selecionado ao clicar
            j2+=1
            print("Jogador 1:")
            print(j1)
            print("Jogador 2: ")
            print(j2)
            
            bot2.value(0)
            break
   '''   
