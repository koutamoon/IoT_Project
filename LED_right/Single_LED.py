'''
LEDを１つ点灯させる
'''

import wiringpi as pi
import time

# 赤線でRaspberry Piから出ている箇所のGPIO番号
LED_PIN = 18

pi.wiringPiSetupGpio()
# GPIOを出力モードに設定
pi.pinMode(LED_PIN, pi.OUTPUT)

while True:
    pi.digitalWrite(LED_PIN, pi.LOW)
    print('LOW')
    time.sleep(1)

    pi.digitalWrite(LED_PIN, pi.HIGH)
    print('HIGH')
    time.sleep(1)
