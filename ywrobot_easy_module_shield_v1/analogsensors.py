# Metro M0 + Yurobot easy module shield V1
# demo analoge sensors A0 .. A2
# 2017-0820 PePo added formula to calculate temperature LM35
# sources: 
# 1. http://arduinolearning.com/code/arduino-easy-module-shield-v1.php
# 2. https://playground.arduino.cc/Main/LM35HigherResolution
import board
import analogio
import time

# reading: 0 .. 65535 (16-bit)
# voltage: 0 .. 3.3
# LM35 Arduino: temp = (5.0 * analogRead(tempPin) * 100.0) / 1024
potmeter = analogio.AnalogIn(board.A0)
ldr = analogio.AnalogIn(board.A1)
lm35 = analogio.AnalogIn(board.A2)

def getSensorData(sensor):
    reading = sensor.value
    voltage = (reading / 65535.0) * sensor.reference_voltage
    return (reading, voltage)

def main(dt=1.0):
    #print('Sensor\tReading\tVoltage\tTemperature')
    #for i in range(8):
    while True:
        print('Sensor\tReading\tVoltage\tTemperature')
        # A0: potentiometer
        value, voltage = getSensorData(potmeter)
        print ('Pot\t{0}\t{1:0.2f}'.format(value, voltage))        

        # A1: LDR sensor
        value, voltage = getSensorData(ldr)
        print ('LDR\t{0}\t{1:0.2f}'.format(value, voltage))
        
        # A2: LM35 sensor
        value, voltage = getSensorData(lm35)
        temp = (voltage * 100.0)
        #temp = (reading * lm35.reference_voltage * 100.0) / 65535.0
        print('LM35\t{0}\t{1:0.2f}\t{2:0.2f}'.format(value, voltage, temp))
        print('-------------------------------------')
        time.sleep(dt)
# run
try:
    main(5.0)
except:
    print('main intercepted')
