cat led_sub.py 
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

BROKER_IP = "172.20.10.2"   # MQTT broker Pi
TOPIC = "home/weather"
LED_PIN = 18
THRESHOLD = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    print("Connected to broker with result code", rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    try:
        temperature = float(msg.payload.decode())
        print("Temperature received:", temperature)

        if temperature > THRESHOLD:
            GPIO.output(LED_PIN, GPIO.HIGH)
            print("LED ON")
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            print("LED OFF")

    except ValueError:
        print("Invalid payload:", msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_IP, 1883, 60)

print("Waiting for temperature data...")
client.loop_forever()
