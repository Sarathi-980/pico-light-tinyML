from machine import ADC, Pin
from model import predict_light
import time 

ADC_PIN = 26

sensor = ADC(Pin(ADC_PIN))

while True:
    raw = sensor.read_u16()
    prediction = predict_light(raw)
    print("raw_adc_value:", raw, "prediction:", prediction)
    time.sleep(1)
