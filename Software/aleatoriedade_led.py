# Importa as classes Pin e I2C da biblioteca machine para controlar o hardware do Raspberry Pi Pico
from machine import Pin
import random


# Define o pino do Raspberry Pi Pico conectado ao módulo PIR HC-SR501
Led_Amarelo = 22
Led_Vermelho = 21
Led_Verde = 20
Led_Azul = 19
botao1 = 18
botao2 = 17

# Configura o pino da saída digital do sensorLed1 = Pin(Led_Amarelo, Pin.OUT)
Led1 = Pin(Led_Amarelo, Pin.OUT)
Led2 = Pin(Led_Vermelho, Pin.OUT)
Led3 = Pin(Led_Verde, Pin.OUT)
Led4 = Pin(Led_Azul, Pin.OUT)
bot1 = Pin(botao1, Pin.IN,Pin.PULL_UP)
bot2 = Pin(botao2, Pin.IN,Pin.PULL_UP)
Leds = [Led1,Led2,Led3,Led4]

#print(random.randint(a, b))
#print(Leds[random.randint(a, b)])
#Led4.value(0)
Selecionado = Leds[random.randint(0, 3)]
print(Selecionado)
Selecionado.value(1)
j1=0
j2=0
print(bot1)
print(bot1.value())
print(bot1.value()== 1)
'''
while(1):
    if(bot1.value() == 0):
        Selecionado.value(0)
        j1+=1
        break
    
    if(bot2.value() == 0):
        Selecionado.value(0)
        j2+=1
        break
    print("ahha")
'''

print("Jogador 1: " + j1)
print("Jogador 2: " + j2)

