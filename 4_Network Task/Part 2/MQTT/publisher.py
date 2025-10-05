import paho.mqtt.client as mqtt
from time import sleep
import random

broker = "127.0.0.1"
topic = "temperature"

client = mqtt.Client()

client.connect(broker, 1883, 60)

while True:
    tempC = round(random.uniform(20, 40), 2) 
    client.publish(topic, tempC)
    print(f"Published Temperature: {tempC}")
    sleep(2)
