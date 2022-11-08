from dccpi import *


def send_feedback_to_webserver():
	pload = 
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
	if loco.fl == True:
		loco.fl = False
	else:
		loco.fl = True


def main():
	# Create the DCC controller with the RPi encoder
	e = DCCRPiEncoder()
	controller = DCCController(e)
	
	# Create locos, args: Name, DCC Address (see DCCLocomotive class)
	l1 = DCCLocomotive("DCC6", 6)

	# Register locos on the controller
	controller.register(l1)

	controller.start()             # Start the controller. Removes brake signal
	l1.reverse()                   # Change direction bit
	l1.fl = True                   # Change fl function bit

	l1.speed = 10                  # Change speed

	l3.slower()                    # Reduce 1 speed step
	l3.faster()                    # Increase 1 speed step
	l1                             # Print loco information

	 
	controller.stop()              # IMPORTANT! Stop controller always. Emergency-stops


if __name__ == "__main__":
    main()
