import pymodbus
from pymodbus.client.sync import ModbusTcpClient


'''
    PyModBus Sources:
        https://blog.jonasneubert.com/2019/11/02/using-pymodbus-to-communicate-with-a-plc/
        Functions( https://pymodbus.readthedocs.io/en/latest/source/library/pymodbus.client.html)
'''
client = ModbusTcpClient('129.101.98.229')


def read_modbus_holding_register(register):
    result = client.read_holding_registers(register)
    return result


def write_modbus_holding_register(register, value):
    pass


def read_single_modbus_coil(register):
    result = client.read_coils(register, 1)
    print(result.bits[0])
    return result


def write_modbus_coil(register, true_or_false):
    result = client.write_coil(register, true_or_false)
    print(result)
    return result
