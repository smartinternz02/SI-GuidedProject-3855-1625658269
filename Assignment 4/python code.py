from pytz import timezone
from wiotp.sdk.device import DeviceClient
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

    print("==================================================================\n")
    print(f"Text Entered on MIT App: {cmd.data['from_mit_app']}\n")
    print("==================================================================\n\n")

client = DeviceClient(config=config)
client.connect()
while True:
    client.commandCallback = callBackFunc
client.disconnect()
