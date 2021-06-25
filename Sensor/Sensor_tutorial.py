import wiringpi as pi
import time

INPUT_PIN = 18
OUTPUT_PIN = 23

pi.wiringPiSetupGpio()

pi.pinMode(INPUT_PIN, pi.INPUT)
pi.pinMode(OUTPUT_PIN, pi.OUTPUT)

while True:
    print(pi.digitalRead(INPUT_PIN))
    if (pi.digitalRead(INPUT_PIN) == pi.HIGH):
        pi.digitalWrite(OUTPUT_PIN, pi.HIGH)
    else:
       pi.digitalWrite(OUTPUT_PIN, pi.LOW)
    time.sleep(2)
