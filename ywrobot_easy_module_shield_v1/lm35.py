# Metro M0 + Yurobot easy module shield V1
# demo temperature LM35
# 2017-0820 PePo added formula to calculate temperature LM35
# 2017-0819 PePo new, not tested
# sources: 
# 1. http://arduinolearning.com/code/arduino-easy-module-shield-v1.php
# 2. https://playground.arduino.cc/Main/LM35HigherResolution
import board
import analogio
import time

# reading: 0 .. 65535 (16-bit)
# voltage: 0 .. 3.3
# Arduino: temp = (5.0 * analogRead(tempPin) * 100.0) / 1024
lm35 = analogio.AnalogIn(board.A2) #get 16-bit number

def main(dt=1.0):
    print('Reading\tVoltage\tTemperature')
    while True:
        reading = lm35.value
        voltage = (reading / 65535.0) * lm35.reference_voltage
        #temp = v * 100.0
        temp = (voltage * 100.0)
        #temp = (reading * lm35.reference_voltage * 100.0) / 65535.0
        #temp = ((lm35.reference_voltage * t) * 100.0)
        print('{0}\t{1:0.2f}\t{2:0.2f}'.format(reading, voltage, temp))
        time.sleep(dt)
# run
try:
    main()
except:
    print('main intercepted')
