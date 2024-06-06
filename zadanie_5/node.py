from machine import UART, Pin
import time

class Node:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver

    def relay_message(self):
        if self.receiver.uart.any() != 0:
            message = self.receiver.uart.read()
            self.sender.uart.write(message)