import itertools
import serial

class MotorController:
    def __init__(self, port, baud_rate=9600):
        try:
            self.connection = serial.Serial(port, baud_rate)
        except Exception as e:
            raise Exception(f'Error opening port {port} Error: {e}')

    ## Arguments to build packet -> Number of bytes written (int)
    def write(self, header, num_id, length, cmd, params, checksum):
        args = list(header, num_id, length, cmd, params, checksum)
        flattened_args = list(itertools.chain.from_iterable(args))
        data = bytearray(flattened_args)
        return self.connection.write(data)
