import serial

class SerialPort:
    def _init_():
        print('Available serial ports:')
        print(list(serial.tools.list_ports.grep()))
        print('Input serial port which you would like to use:')
        serial_port = input('Serial port: ')
        connect = serial.Serial('/dev/'serial_port)

    def config():
        print('Set the boundrate:')
        set_baudrate = input('baudrate: ')
        print('Set the timeout:')
        set_timeout = input('timeout: ')
        serial_port = serial.Serial(
            port = connect
            baudrate = set_baudrate
            timeout = set_timeout
        
        
    
