from dccpi import *
import json


class TrainStateMachine():
    def __init__(self):
        self.user_input = ''
        self.states = {
            "move_to_ready_state": self.move_to_ready_state,
            "end_of_transport": self.end_of_song
            }

    def run_state(self):
        while self.state != "exit":
            self.states[self.state]()

    def move_to_ready_state(self):
        if self.user_input == "quit":
            self.state = "exit"

    def end_of_transport(self):
        print("Done transporting goods")
        self.state = "move_to_ready_state"


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
