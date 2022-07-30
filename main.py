import Adafruit_DHT
import time
 
sensor=Adafruit_DHT.DHT11
pin=17
 
while True:
     humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
     if temperature < 18 :
        print("suhu ruangan rendah ({0:0.1f}*C) dengan kelembapan ({1:0.1f}%)".format(temperature, humidity))

     elif temperature == 18 and temperature <= 22 :
        print("suhu ruangan ideal ({0:0.1f}*C) dengan kelembapan ({1:0.1f}%)".format(temperature, humidity))

     else :
        print("suhu ruangan tinggi ({0:0.1f}*C) dengan kelembapan ({1:0.1f}%)".format(temperature, humidity))
        time.sleep(0.5)

