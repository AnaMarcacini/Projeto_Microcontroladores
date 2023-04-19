# Importa as classes Pin e I2C da biblioteca machine para controlar o hardware do Raspberry Pi Pico
from machine import Pin
import random


# Define o pino do Raspberry Pi Pico conectado ao módulo PIR HC-SR501

botao1 = 18
botao2 = 17

# Configura o pino da saída digital do sensorLed1 = Pin(Led_Amarelo, Pin.OUT)
bot1 = Pin(botao1, Pin.IN,Pin.PULL_UP)
bot2 = Pin(botao2, Pin.IN,Pin.PULL_UP)
botJ1 = [bot1]
botJ2 = [bot2]

Selecionado = botJ1[random.randint(0, botJ1.lenght)]
print(Selecionado)
Selecionado.value(1)

print(Selecionado)
print(Selecionado.value())
print(Selecionado.value()== 1)
while(1):
    print(Selecionado.value()== 1)



