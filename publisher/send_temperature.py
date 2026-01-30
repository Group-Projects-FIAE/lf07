import time
import paho.mqtt.client as mqtt

SENSOR_FILE = "/sys/bus/w1/devices/28-3c01d607dc01/w1_slave"
MQTT_BROKER = "172.20.10.2"
MQTT_PORT = 1883
MQTT_TOPIC = "home/weather"

def read_temperature():
    try:
        with open(SENSOR_FILE, "r") as f:
            lines = f.readlines()

        # Check CRC
        if "YES" not in lines[0]:
            return None

        # Extract temperature
        temp_pos = lines[1].find("t=")
        if temp_pos != -1:
            temp_string = lines[1][temp_pos + 2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c
    except Exception as e:
        print("Error reading temperature:", e)

    return None

def main():
    client = mqtt.Client()
    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    while True:
        temperature = read_temperature()
        if temperature is not None:
            payload = temperature
            client.publish(MQTT_TOPIC, payload)
            print(f"Sent temperature: {payload} °C")
        else:
            print("Failed to read temperature")

        time.sleep(5)

if __name__ == "__main__":
    main()
