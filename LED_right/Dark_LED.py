'''
LEDを１つ点灯させる
点灯している時間を人間に検知できない間隔で短くすることで暗く見える
'''

import wiringpi as pi
import time

# 赤線でRaspberry Piから出ている箇所のGPIO番号
LED_PIN = 23

pi.wiringPiSetupGpio()
# GPIOを出力モードに設定
pi.pinMode(LED_PIN, pi.OUTPUT)

while True:
    pi.digitalWrite(LED_PIN, pi.LOW)
    time.sleep(0.005)

    pi.digitalWrite(LED_PIN, pi.HIGH)
    time.sleep(0.002)
