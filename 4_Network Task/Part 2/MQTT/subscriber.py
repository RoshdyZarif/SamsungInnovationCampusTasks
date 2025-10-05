import paho.mqtt.client as mqtt

broker = "127.0.0.1"
topic = "temperature"

client = mqtt.Client()
client.connect(broker, 1883, 60)

def on_message(client, userdata, msg):
    print(f"Received Temperature: {msg.payload.decode()}")

client.subscribe(topic)
client.on_message = on_message

print("Waiting for messages...")
client.loop_forever()
