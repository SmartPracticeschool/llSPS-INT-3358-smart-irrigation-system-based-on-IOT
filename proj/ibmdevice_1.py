import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import requests
#Provide your IBM Watson Device Credentials
organization = "lz78rk"
deviceType = "MAYANK"
deviceId = "123"
authMethod = "token"
authToken = "12345678"


def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)#Commands
        

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        
        hum=random.randint(40, 90)
        #print(hum)
        temp =random.randint(30, 45)
        #Send Temperature & Humidity to IBM Watson
        data = { 'Temperature' : temp, 'moisture': hum }
        #print (data)
        if hum<=50:
                r=requests.get('https://www.fast2sms.com/dev/bulk?authorization=kDXqEaH4UPjVgbstlYwnuWixdo9f5MC0cp1BLyzhG2IO7RNAvZ0QzPo9aWHSksJTZ4fVEA8gqLUBpXeI&sender_id=FSTSMS&message=turnmotoron&language=english&route=p&number=9818057020')
                print(r.status_code)
        
        def myOnPublishCallback():
            print ("Published Temperature = %s C" % temp, "moisture = %s %%" % hum, "to IBM Watson")

        success = deviceCli.publishEvent("Weather", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(2)
        
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
