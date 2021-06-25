'''
複数のGPIOから電流を流すことで
LEDを１つ点灯させる
'''

import wiringpi as pi
import time

# 緑線でRaspberry Piから出ている箇所のGPIO番号
LED_PIN_GREEN = 22
# 青線でRaspberry Piから出ている箇所のGPIO番号
LED_PIN_BLUE = 23
# 赤線でRaspberry Piから出ている箇所のGPIO番号
LED_PIN_RED = 12


pi.wiringPiSetupGpio()
# GPIOを出力モードに設定
pi.pinMode(LED_PIN_GREEN, pi.OUTPUT)
pi.pinMode(LED_PIN_BLUE, pi.OUTPUT)
pi.pinMode(LED_PIN_RED, pi.OUTPUT)

# GPIOを出力強度を設定
pi.softPwmCreate(LED_PIN_GREEN, 0, 100)
pi.softPwmCreate(LED_PIN_BLUE, 0, 100)
pi.softPwmCreate(LED_PIN_RED, 0, 100)

count = 0

while count < 3:
    pi.softPwmWrite(LED_PIN_GREEN,100)
    pi.softPwmWrite(LED_PIN_BLUE, 100)
    pi.digitalWrite(LED_PIN_RED, 0)
    time.sleep(1)

    pi.softPwmWrite(LED_PIN_GREEN, 0)
    pi.softPwmWrite(LED_PIN_BLUE, 100)
    pi.digitalWrite(LED_PIN_RED, 100)
    time.sleep(1)

    pi.softPwmWrite(LED_PIN_GREEN, 100)
    pi.softPwmWrite(LED_PIN_BLUE, 0)
    pi.digitalWrite(LED_PIN_RED, 100)
    time.sleep(1)

    pi.softPwmWrite(LED_PIN_GREEN, 100)
    pi.softPwmWrite(LED_PIN_BLUE, 100)
    pi.digitalWrite(LED_PIN_RED, 100)
    time.sleep(1)
    count+=1

pi.cleanup()
