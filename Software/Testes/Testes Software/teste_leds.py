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
bot1 = Pin(botao1, Pin.IN,Pin.PULL_DOWN)
bot2 = Pin(botao2, Pin.IN,Pin.PULL_DOWN)
Leds = [Led1,Led2,Led3,Led4]
for led in Leds:
    led.value(0)