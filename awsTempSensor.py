import Adafruit_DHT as DHT
import time as t
import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

# Define ENDPOINT, CLIENT_ID, PATH_TO_CERT, PATH_TO_KEY, PATH_TO_ROOT, MESSAGE, TOPIC, and RANGE
ENDPOINT = "a264l7bykep3jn-ats.iot.us-west-2.amazonaws.com"
CLIENT_ID = "testDevice"
PATH_TO_CERT = "/home/pi/Documents/AWS/Certificates/device.pem.crt"
PATH_TO_KEY = "/home/pi/Documents/AWS/Certificates/private.pem.key"
PATH_TO_ROOT = "/home/pi/Documents/AWS/Certificates/Amazon-root-CA-1.pem"
TOPIC = "test/testing"
RANGE = 5

# Define sensor and pin
SENSOR = DHT.DHT11
PIN = 12

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)

myAWSIoTMQTTClient.connect()
print('Begin Publish')

for i in range (RANGE):
	humidity, temperature = DHT.read(SENSOR, PIN)
	message = "Temperature: {}".format(temperature)
	myAWSIoTMQTTClient.publish(TOPIC, json.dumps(message), 1) 
	print("Published: '" + json.dumps(message) + "' to the topic: " + "'test/testing'")
	t.sleep(5)

print('Publish End')
myAWSIoTMQTTClient.disconnect()