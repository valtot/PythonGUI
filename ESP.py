import serial, os
from errorsGui import PathError

class ESP32:
    # Class contructor
    def __init__(self, port, baudRate, output = 'terminal'):
        self.port = port
        self.baudRate = baudRate

        # Instantiate a serial port without opening it
        self.ser = serial.Serial()

        # Configure the serial port
        self.ser.port = port
        self.ser.baudrate = baudRate
        self.ser.timeout = .2
        self.output = output
        # self.ser.parity = serial.PARITY_EVEN


    # Method to support managing the port by using a "with" statement    
    def __enter__(self):
        if (self.ser.isOpen() == False):
            self.ser.open()
        else:
            print("Serial connection already opened.")

       
    # Method to support managing the port by using a "with" statement    
    def __exit__(self, exc_type, exc_value, tb):
        if (self.ser.isOpen() == True):
            self.ser.close()
        else:
            print("Serial Connection already closed.")

    def dataWaiting(self):
        return self.ser.in_waiting

    def read(self):
        msg = self.ser.readline()
        msg = msg.decode('utf-8').rstrip()
        return msg
#-----------------------------------------------------------------------------------------        
#added by vale
    def print(self):
        msg = self.read()
        if self.output == 'terminal':
            print(msg)
        else:
            if os.path.exists(os.path.dirname(self.output)):
                if os.path.isfile(os.path(self.output)): 
                    raise PathError("File already present")
                try:
                    with open(self.output, 'a') as fobj:
                        fobj.write(msg)
                except PermissionError:
                    raise PathError('File writing operation was requested on a directory')
            else:
                raise PathError('Invalid string indicated as path')
#-------------------------------------------------------------------------------------------

    def write(self, msg:str):
        self.ser.write(msg.encode('utf-8'))
        # print(msg)
        pass




if (__name__  == "__main__"):

    # Instantiates an object
    esp = ESP32("COM3", 115200)
    with esp:
        esp.write('K')
    # with esp:
    #     while True:
    #         if esp.dataWaiting():
    #             message = esp.write('K')
                # print(message)
