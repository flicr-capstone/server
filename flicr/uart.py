#!/usr/bin/env python3
import serial


class Uart:
    def __init__(self):
        self.ser = serial.Serial(
            port="/dev/serial0",
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=None,
        )

    def write_str_ln(self, string):
        return self.ser.write(f"{string}\n".encode("ascii"))

    def write_bytes(self, data):
        return self.ser.write(data)

    def close(self):
        return self.ser.close()
