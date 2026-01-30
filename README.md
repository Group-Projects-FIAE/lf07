# lf07
# Projekt: Implementierung eines Zweipunktreglers via MQTT
> Dieses Projekt simuliert eine Kühlanlage mittels drei Raspberry Pis. Ein Sensor misst die Temperatur und ein Aktuator (LED) reagiert basierend auf Schwellenwerten.


# Aufbau der Lernumgebung

Hardware: Drei Raspberry Pis, ein Temperatursensor und eine LED-Leuchte.
Verkabelung: Die LED und der Sensor sind über Breadboards an separate Pis angeschlossen.
Simulation: Die LED simuliert das Steuersignal zum Ein- und Ausschalten einer Kühlanlage.

# Kommunikation (MQTT Protokoll)
Die Kommunikation erfolgt über das MQTT-Protokoll:
- Broker (Pi ohne Zusätze): Agiert als Zentrale und leitet Nachrichten an Subscribed-Clients weiter. Er hostet zudem ein Dashboard zur Visualisierung.
- Sensor-Pi (Publisher): Sendet regelmäßig die gemessene Temperatur unter einem bestimmten Topic an den Broker.
- LED-Pi (Subscriber): Abonniert das Topic, empfängt die Temperaturwerte und steuert die LED basierend auf einem Schwellenwert.

# Code-Integration

Sensor-Skript (src/sensor_pi/send_temperature.py)
Dieses Skript liest den Sensor aus und sendet die Daten an den Broker.

# LED-Test ()
Basis-Skript zur Ansteuerung der LED über GPIO Pin 18.

# Benutzeroberfläche (Node-RED)
Zur Überwachung der Anlage wurde auf dem Broker-Pi ein Dashboard eingerichtet.

## Node-RED Dashboard (UI)
Der Broker-Pi (der Pi ohne zusätzliche Sensoren/Aktoren) übernimmt die Visualisierung der Daten. Hierfür wurde Node-RED eingesetzt, um ein browserbasiertes Dashboard zu erstellen.

## Funktionen des Dashboards
Das Dashboard dient der Überwachung der Temperaturwerte in Echtzeit:
- Gauge (Anzeigeinstrument): Visualisiert die aktuelle Temperatur als Zeigerinstrument im Bereich von 0 bis 50°C. Im Screenshot ist ein aktueller Wert von 23.312°C zu sehen.
- Chart (Diagramm): Zeigt den zeitlichen Verlauf der Temperatur an. In der Dokumentation ist ein Verlauf zwischen ca. 07:38:00 und 08:37:00 Uhr dargestellt.

## Visualisierung: 
Die Daten werden sowohl als Momentanwert (Gauge) als auch als historischer Verlauf (Chart) dargestellt.

## Zugriff: 
Das Dashboard ist im lokalen Netzwerk über die IP des Brokers (Port 1880/ui) erreichbar.

## Konfiguration des MQTT-Nodes
Um die Daten im UI anzuzeigen, muss der Node-RED Flow wie folgt konfiguriert sein:

- MQTT-In Node: Abonniert das Topic home/weather vom lokalen Broker.

- Dashboard-Nodes: Die empfangenen Daten werden direkt an einen Gauge-Node und einen Chart-Node weitergeleitet.