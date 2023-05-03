from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
import math
import micropython

# Configuração do display OLED
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=100000)
oled = SSD1306_I2C(128, 32, i2c)

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
while True:
    micropython.schedule(lambda: print("Executando código em conjunto com o temporizador..."), 0)
    #time.sleep(2)
    print("oi")