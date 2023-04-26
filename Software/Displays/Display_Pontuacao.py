"""!
@file display_oled_i2c_128x64_exemplo.py
@brief Programa para escrever em um display OLED I2C de 128x64 usando o Raspberry Pi Pico.
@details Este programa utiliza a biblioteca ssd1306 para escrever em um display OLED de 128x64 via barramento I2C.
         Referência: https://docs.micropython.org/en/latest/esp8266/tutorial/ssd1306.html
@author Rodrigo França
@date 2023-03-17
"""

# Importa as classes Pin e I2C da biblioteca machine para controlar o hardware do Raspberry Pi Pico
from machine import Pin, I2C
# Importa a classe SSD1306_I2C da biblioteca ssd1306.py
from ssd1306 import SSD1306_I2C
#importa a classe j1 e j2 da aleatoriedade_led
#from aleatoriedade_led import j1, j2
def display(j1,j2):
    # Define os pinos do Raspberry Pi Pico conectados ao barramento I2C 0
    i2c0_slc_pin = 9
    i2c0_sda_pin = 8
    #Parametros para a futura função
    pontuacao_jogador1= str(j1)
    pontuacao_jogador2= str(j2)



    # Inicializa o I2C0 com os pinos GPIO9 (SCL) e GPIO8 (SDA)
    i2c0 = I2C(0, scl=Pin(i2c0_slc_pin), sda=Pin(i2c0_sda_pin), freq=100000)

    # Inicializa o display OLED I2C de 128x64
    display = SSD1306_I2C(128, 64, i2c0)

    # Limpa o display
    display.fill(0)
    display.show()

    # Desenha o logo do MicroPython e imprime um texto
    display.fill(0)                        # preenche toda a tela com cor = 0

    display.hline(0, 10, 200, 1)            # desenha uma linha horizontal x = 0, y = 10, altura = 200, cor = 1
    display.vline(64,5,47,1)                #desenha uma linha vertical (x,y,h,cor)

    display.text('Jog. 1 | Jog. 2', 4, 0, 1)  # desenha algum texto em x = 40, y = 0 , cor = 1

    display.text(pontuacao_jogador1, 10, 16, 1)     # desenha algum texto em x = 40, y = 12, cor = 1
    display.text(pontuacao_jogador2, 74, 16, 1)     # desenha algum texto em x = 40, y = 12, cor = 1


    # Escreve na última linha do display
    display.text("Boa Sorte!", 27, 54)

    # Atualiza o display
    display.show()
def atualização():
    # Define os pinos do Raspberry Pi Pico conectados ao barramento I2C 0
    i2c0_slc_pin = 9
    i2c0_sda_pin = 8
    