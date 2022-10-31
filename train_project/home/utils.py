import pymodbus
from pymodbus.client.sync import ModbusTcpClient

'''
    PyModBus Sources:
    https://blog.jonasneubert.com/2019/11/02/using-pymodbus-to-communicate-with-a-plc/
'''


def modbus_quick_check():
    try:
        client = ModbusTcpClient('127.0.0.1')
        client.write_coil(1, True)
        result = client.read_coils(1,1)
        print(result.bits[0])
        client.close()
    except:
        print("An exception occurred") 
