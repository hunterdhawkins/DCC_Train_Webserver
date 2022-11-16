import pymodbus
from pymodbus.client.sync import ModbusTcpClient
'''
    PyModBus Sources:
    https://blog.jonasneubert.com/2019/11/02/using-pymodbus-to-communicate-with-a-plc/
    Functions( https://pymodbus.readthedocs.io/en/latest/source/library/pymodbus.client.html)
'''


def read_single_modbus_coil(address):
    result = client.read_coils(1, 1)
    print(result.bits[0])
    return result


def modbus_quick_check():
    try:
        client = ModbusTcpClient('129.101.98.229')

        # Param 1: address – Start address to read from
        # Param 2: value – Boolean to write
        # client.write_coil(400, True)

        # Param 1: address – Start address to read from
        # Param 2: count – (optional) Number of coils to read
        result = client.read_coils(400, 100)
        print(result.bits)
        print(result.bits[0])

        client.close()
    except:
        print("An exception occurred") 


def main():
    modbus_quick_check()


if __name__ == '__main__':
    main()
