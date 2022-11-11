import pymodbus
import json
from pymodbus.client.sync import ModbusTcpClient

'''
    PyModBus Sources:
    https://blog.jonasneubert.com/2019/11/02/using-pymodbus-to-communicate-with-a-plc/
'''

'''
    Template Sources:
https://stackoverflow.com/questions/12712592/how-to-make-a-small-image-move-from-one-side-of-the-screen-to-the-other-with-js
'''

train_file_path = '/home/hunterhawkins/Desktop/School/Train_Project/django_web_server/DCC_Train_Webserver/train_project/data/train_status'

# interface document w/ garrett
# table purchase
# track purchase


def modbus_quick_check():
    try:
        client = ModbusTcpClient('127.0.0.1')
        client.write_coil(1, True)
        result = client.read_coils(1,1)
        print(result.bits[0])
        client.close()
    except:
        print("An exception occurred") 


def read_train_status():
    file_path = train_file_path + '.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    train_speed = data["speed"]
    train_headlight = data["headlight"]
    return {
            'speed': train_speed,
            'headlight': train_headlight,
    }


def write_data_to_train(speed, headlight):
    file_path = train_file_path + '.json'
    new_train_values = {
                            'speed': speed,
                            'headlight': headlight,
    }
    with open(file_path, 'w') as fp:
        json.dump(new_train_values, fp)
