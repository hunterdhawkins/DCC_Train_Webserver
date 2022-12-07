import json
import time
# from dccpi import *

# False = order from website
# True = order from factory (TODO)
FACTORY_MODE = False


class TrainStateMachine():
    # This is the state machine for the train
    # I am still designing the states but we currently have
    # The run state = used to run the train until we want to exit
    # The move to ready state = which currently just lets the user quit
    # The end of transportation state which returns us to the ready state

    def __init__(self):
        self.user_input = ''
        self.train_status_file_path = '/home/hunterhawkins/Desktop/School/Train_Project/django_web_server/DCC_Train_Webserver/train_project/data/train_status'
        self.train_order_file_path = '/home/hunterhawkins/Desktop/School/Train_Project/django_web_server/DCC_Train_Webserver/train_project/data/train_order'
        self.train_speed = 0
        self.train_headlight = False
        self.train_direction = None
        self.order = {
            'num_of_red': 0,
            'num_of_white': 0,
            'num_of_blue': 0,
            'num_of_faulty': 0,
        }

        self.states = {
            "move_to_ready_state": self.move_to_ready_state,
            "drive_to_load_area": self.drive_to_load_area,
            "end_of_transport": self.end_of_transport,
            }

        self.state = "move_to_ready_state"
        print("Moving to the ready state")
        self.run_state()

    # ##############################################
    # These are helper functions of the state machine
    # ##################################################
    def read_train_status(self):
        file_path = self.train_status_file_path + '.json'
        with open(file_path, 'r') as f:
            data = json.load(f)
        self.train_speed = data["speed"]
        self.train_headlight = data["headlight"]
        self.train_direction = data["direction"]
        # print("Speed " + self.train_speed, " Headlight " + str(self.train_headlight), " Direction " + str(self.train_direction))

    def check_for_fake_order(self):
        file_path = self.train_order_file_path + '.json'
        with open(file_path, 'r') as f:
            data = json.load(f)
        self.order['num_of_red'] = data["num_of_red"]
        self.order['num_of_white'] = data["num_of_white"]
        self.order['num_of_blue'] = data["num_of_blue"]
        self.order['num_of_faulty'] = data["num_of_faulty"]
        print(self.order)

    # ##########################################
    # These are the states of the statemachine
    # ###############################################
    def run_state(self):
        while self.state != "exit":
            self.states[self.state]()

    def move_to_ready_state(self):
        # This state assumes the train returns to the stating point every time
        self.read_train_status()
        self.check_for_fake_order()
        time.sleep(5)
        if any(int(value) != 0 for value in self.order.values()):
            self.state = 'drive_to_load_area'

    def drive_to_load_area(self):
        print("Here")
        time.sleep(5)

    def end_of_transport(self):
        print("Done transporting goods")
        self.state = "move_to_ready_state"


# ###################################
# Train functions (TODO)
########################################
def write_data_to_file(feedback_dict):
    with open('result.json', 'w') as fp:
        json.dump(feedback_dict, fp)


def send_feedback_to_webserver():
    pload = {'test': 123}
    r = requests.post('http://localhost:8000/ajax/home', data=pload)
    return r.status_code


def change_loco_speed(loco, speed):
    loco.speed = speed


def increment_loco_speed(loco):
    loco.faster()


def decrement_loco_speed(loco):
    loco.slower()


def change_loco_direction(loco):
    loco.reverse()


def start_controller(controller):
    controller.start()


def stop_controller(controller):
    controller.stop()


def create_loco(name, address):
    # Create a loco, args: Name, DCC Address (see DCCLocomotive class)
    loco = DCCLocomotive(name, address)
    return loco


def toggle_loco_headlight(loco):
    if loco.fl is True:
        loco.fl = False
    else:
        loco.fl = True


def main():
    # # Create the DCC controller with the RPi encoder
    # e = DCCRPiEncoder()
    # controller = DCCController(e)

    # # Create locos, args: Name, DCC Address (see DCCLocomotive class)
    # l1 = DCCLocomotive("DCC6", 6)

    # # Register locos on the controller
    # controller.register(l1)

    # controller.start()             # Start the controller. Removes brake signal
    # l1.reverse()                   # Change direction bit
    # l1.fl = True                   # Change fl function bit

    # l1.speed = 10                  # Change speed

    # print(l1)                      # Print loco information
    # controller.stop()              # IMPORTANT! Stop controller always. Emergency-stops

    train = TrainStateMachine()
    train.run_state()


if __name__ == "__main__":
    main()
