import paho.mqtt.client as mqtt
import os

MQTT_BROKER = "IP_BROKERA_MQTT"
MQTT_PORT = 1883
MQTT_TOPIC_START = "minecraft/start"
MQTT_TOPIC_STOP = "minecraft/stop"
MQTT_USERNAME = "TWÓJ_UŻYTKOWNIK"
MQTT_PASSWORD = "TWOJE_HASŁO"

def on_message(client, userdata, message):
    if message.topic == MQTT_TOPIC_START and message.payload.decode() == "start":
        os.system("sudo -u minecraftuser /ścieżka/do/start_minecraft.sh")
    elif message.topic == MQTT_TOPIC_STOP and message.payload.decode() == "stop":
        os.system("sudo -u minecraftuser /ścieżka/do/stop_minecraft.sh")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe(MQTT_TOPIC_START)
        client.subscribe(MQTT_TOPIC_STOP)

client = mqtt.Client()
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()
