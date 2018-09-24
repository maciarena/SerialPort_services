'''
This module task purpose is to provide easy interface to work with the serial port.

METHODS DESCRIPTION:
- _init_ - here you can setup your connection (port used, baudrate and timeout)

- input_connection - you can write data from serial port directly into file

- output_connection - you can read data from file and send it via serial port 

- close - closes a serial connection and a file
'''

import serial
import serial.tools.list_ports
import io

class SerialPort:
    def _init_():
        print('Available serial ports:')
        print('Input serial port which you would like to use:')
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            print(p)
        serial_port = input('Serial port: ')
        print ('Set the baudrate:')
        set_baudrate = input('Baudrate: ')
        baudrate = set_baudrate
        print ('Set the timeout:')
        set_timeout = input('Timeout: ')
        timeout = float(set_timeout)
        serial_connection = serial.Serial('/dev' + serial_port, baudrate, timeout)
        return serial_connection

    def input_connection():
        print('Input file name you would like to use:')
        file_to_work_on = input('Set the file path: ')
        file_to_work_on = open(file)
        print('Input decoding you would like to use')
        decoding = input('Set the decoding: ')
        while (file_to_work_on == isOpen()):
            serial_connection.readline(decoding)
            data = new_data.decode()
            file.write(data + '\n')
            file.flush()
            if KeyboardInterrupt:
                raise('KeyError: KeyboardInterrupt has been caught - connection has been closed')
            

    def output_connection():
        print('Input file from which you would like to read data:')
        file = input('File path: ')
        open(file)

    def close():
        file.close()
        serial_connection.close()
 
