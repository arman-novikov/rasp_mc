import paho.mqtt.client as mqtt
from topics import TOPICS
from time import sleep


MQTT_HOST = "192.168.10.1"
MQTT_PORT = 1883


def mqtt_on_connect(client, user_data, flags, rc):
    ignore = user_data
    ignore = flags
    print("MQTT: Connected, rc: " + str(rc))
    for topic, handler in TOPICS.items():
        client.subscribe(topic)

    client.subscribe("/er/cmd")


def mqtt_on_message(client, user_data, msg):
    ignore = client
    ignore = user_data

    topic = msg.topic
    payload = msg.payload.decode()
    try:
        TOPICS[topic](payload)
    except KeyError:
        print("no handler for topic \"{}\"".format(topic))


MQTT_client = mqtt.Client()
MQTT_client.on_connect = mqtt_on_connect
MQTT_client.on_message = mqtt_on_message


def mqtt_routine():
    MQTT_client.connect(MQTT_HOST, MQTT_PORT, 60)
    print('MQTT: Connecting {0}:{1} ...'.format(MQTT_HOST, MQTT_PORT))

    while True:
        MQTT_client.loop()
        sleep(0.05)


if __name__ == "__main__":
    mqtt_routine()
