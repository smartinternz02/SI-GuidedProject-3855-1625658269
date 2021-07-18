from wiotp.sdk.device import DeviceClient
import random
import time
config = {
    "identity":{
        "orgId":"8vprpv",
        "typeId":"First",
        "deviceId":"1"
    },
    "auth":{
        "token":"12345678"
    }
}
def callBackFunc(cmd):
    data = {
        "water_level":cmd.data["water_level"],
        "light_intensity": cmd.data["light_intensity"]
    }
    print(f"Data acknowledged from cloud: \n\n{data}")
    print("\n==================================================================\n\n")

client = DeviceClient(config=config)
client.connect()
while True:
    data = {
        "water_level":random.randint(2,10),
        "light_intensity": random.random()
    }
    print("==================================================================\n")
    print(f"Data uploaded to cloud: \n\n{data}\n")
    client.publishEvent("upload",msgFormat="json",
    data=data)
    client.commandCallback = callBackFunc
    time.sleep(15)
client.disconnect()
