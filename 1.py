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

    def IO_connection():
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
            

    def close():
        file.close()
        serial_connection.close()
        
    
