import json
import time
import modbus_utils
# from dccpi import *

# False = order from website
# True = order from factory (TODO)
FACTORY_MODE = False

EXTRA_VGR_COMMS = False


class TrainStateMachine():
    # This is the state machine for the train.
    # Here are the current states (still being developed):
    # Initialize train state = create the virtual controller and register the train
    # Move to ready state = Poll for an order from the webserver (future = factory)
    # Drive to load area state = Used to drive to the front of the factory to be loaded

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
            "initialize_train_state": self.initialize_train_state,
            "move_to_ready_state": self.move_to_ready_state,
            "drive_to_load_area_state": self.drive_to_load_area_state,
            "load_train_state": self.load_train_state,
            "drive_to_unload_area_state": self.drive_to_unload_area_state,
            "unload_train_state": self.unload_train_state,
            "end_of_transport_state": self.end_of_transport_state,
            }

        self.state = "initialize_train_state"
        print("Moving to the initialize train state")
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

    def clear_order(self):
        file_path = self.train_order_file_path + '.json'
        fake_order_values = {
            'num_of_red': 0,
            'num_of_white': 0,
            'num_of_blue': 0,
            'num_of_faulty': 0,
        }
        with open(file_path, 'w') as fp:
            json.dump(fake_order_values, fp)

    # ##########################################
    # These are the states of the statemachine
    # ###############################################
    def run_state(self):
        while self.state != "exit":
            self.states[self.state]()

    def initialize_train_state(self):
        # NOTE: This should only be called once ***
        print("Initializing the train")
        '''
        # Create the DCC controller with the RPi encoder
        e = DCCRPiEncoder()
        controller = DCCController(e)

        # Create locos, args: Name, DCC Address (see DCCLocomotive class)
        l1 = DCCLocomotive("DCC6", 6)

        # Register locos on the controller
        controller.register(l1)
        '''
        print("Done initalizing the train")
        print("Moving to ready state")
        self.state = "move_to_ready_state"

    def move_to_ready_state(self):
        # This state assumes the train returns to the stating point every time
        # self.read_train_status()
        self.check_for_fake_order()
        time.sleep(5)
        # If we get an order from the factory advance the state
        if any(int(value) != 0 for value in self.order.values()):
            # Write order details to PLC
            print("Recieved order, moving to loading area")
            self.state = 'drive_to_load_area_state'

    def drive_to_load_area_state(self):
        # This state is used to drive in front of the factory
        print("Driving to loading area")
        # controller.start()             # Start the controller. Removes brake signal

        # l1.speed = 10                  # Change speed
        # print(l1)                      # Print loco information
        time.sleep(10)
        # controller.stop()              # IMPORTANT! Stop controller always. Emergency-stops
        print("Made it to the loading area")
        self.state = 'load_train_state'

    def load_train_state(self):
        # Write to the Factory PLC that we are in position
        # modbus_utils.write_modbus_coil(register, true_or_false)
        print("Loading the train")
        # Polling PLC until loading of the train is done
        if FACTORY_MODE is False:
            # Sleep 10 seconds to let user load materials
            time.sleep(10)
            print("Done loading the train")
            self.state = 'drive_to_unload_area_state'
        elif FACTORY_MODE is True:
            print("No factory yet")
            self.state = 'drive_to_unload_area_state'
            # modbus_utils.read_single_modbus_coil(register)

    def drive_to_unload_area_state(self):
        # This state is used to drive in front of the factory
        print("Driving to unloading area")
        # controller.start()             # Start the controller. Removes brake signal

        # l1.speed = 10                  # Change speed
        # print(l1)                      # Print loco information
        time.sleep(10)
        # controller.stop()              # IMPORTANT! Stop controller always. Emergency-stops
        print("Made it to the unloading area")
        self.state = 'unload_train_state'

    def unload_train_state(self):
        # Write to VGR PLC that the train is ready to be unloaded
        modbus_utils.write_modbus_coil(410, True)
        print("Unloading the train")
        time.sleep(20)
        print("Done unloading, resetting for next order")
        self.state = 'end_of_transport_state'

    def end_of_transport_state(self):
        # Clear the order
        self.clear_order()
        modbus_utils.client.close()
        # Move the train to its resting position
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
