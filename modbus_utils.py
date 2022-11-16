def read_single_modbus_coil(address):
    result = client.read_coils(1, 1)
    print(result.bits[0])
    return result


def modbus_quick_check():
    try:
        client = ModbusTcpClient('127.0.0.1')

        # Param 1: address – Start address to read from
        # Param 2: value – Boolean to write
        # client.write_coil(1, True)

        # Param 1: address – Start address to read from
        # Param 2: count – (optional) Number of coils to read
        result = client.read_coils(1, 1)

        print(result.bits[0])
        client.close()
    except:
        print("An exception occurred") 
