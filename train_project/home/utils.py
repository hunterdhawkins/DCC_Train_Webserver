import pymodbus
import json
from pymodbus.client.sync import ModbusTcpClient


'''
    Template Sources:
https://stackoverflow.com/questions/12712592/how-to-make-a-small-image-move-from-one-side-of-the-screen-to-the-other-with-js
'''

train_file_path = '/home/hunterhawkins/Desktop/School/Train_Project/django_web_server/DCC_Train_Webserver/train_project/data/train_status'
fake_order_file_path = '/home/hunterhawkins/Desktop/School/Train_Project/django_web_server/DCC_Train_Webserver/train_project/data/train_order'
# interface document w/ garrett
# table purchase
# track purchase


def read_train_status():
    file_path = train_file_path + '.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    train_speed = data["speed"]
    train_headlight = data["headlight"]
    train_direction = data["direction"]
    return {
            'speed': train_speed,
            'headlight': train_headlight,
            'direction': train_direction,
    }


def write_data_to_train(speed, headlight, direction):
    file_path = train_file_path + '.json'
    new_train_values = {
                            'speed': speed,
                            'headlight': headlight,
                            'direction': direction,
    }
    with open(file_path, 'w') as fp:
        json.dump(new_train_values, fp)


def write_fake_order(num_of_red, num_of_white, num_of_blue, num_of_faulty):
    file_path = fake_order_file_path + '.json'
    fake_order_values = {
                            'num_of_red': num_of_red,
                            'num_of_white': num_of_white,
                            'num_of_blue': num_of_blue,
                            'num_of_faulty': num_of_faulty,
    }
    with open(file_path, 'w') as fp:
        json.dump(fake_order_values, fp)
