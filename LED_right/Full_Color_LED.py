'''
複数のGPIOから電流を流すことで
LEDを１つ点灯させる
'''

import RPi.GPIO as GPIO
import time

# 緑線でRaspberry Piから出ている箇所のGPIO番号
LED_PIN_GREEN = 22
# 青線でRaspberry Piから出ている箇所のGPIO番号
LED_PIN_BLUE = 23
# 赤線でRaspberry Piから出ている箇所のGPIO番号
LED_PIN_RED = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN_GREEN,GPIO.OUT)
GPIO.setup(LED_PIN_BLUE,GPIO.OUT)
GPIO.setup(LED_PIN_RED,GPIO.OUT)

GPIO.output(LED_PIN_GREEN,True)
GPIO.output(LED_PIN_BLUE,True)
GPIO.output(LED_PIN_RED,True)