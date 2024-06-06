from machine import UART, Pin
import time

class Reciever:
    def __init__(self, uart_num, buzzer, led, sled):
        self.uart = UART(uart_num)
        self.uart.init(baudrate = 115200, bits = 8, parity = None, stop = 1);
        self.uart.init(rx = 21, tx = 19);
        self.uart.init(txbuf=512, rxbuf=512)
        self.buzzer = buzzer
        self.led = led
        self.sled = sled
        self.message = ''

    def recieve(self, uart):
        if self.uart.any() != 0:
            message = str(uart.read(), 'UTF-8');
            print(self.message)
        
    def check_message(self):
        if self.message == "LED":
            self.led.set_color(255, 0, 0)
            time.sleep(1000)
            self.led.set_color(0, 0, 0)
        elif self.message == "BUZZER":
            self.buzzer.set_volume(50)
            time.sleep(1000)
            self.buzzer.set_volume(0)
        elif self.message == "SLED":
            self.sled.set_all_color(255, 0, 0)
            time.sleep(1000)
            self.sled_set_all_color(255, 0, 0)
        else:
            print("invalid command")
            
    def change_pin(self, pin):
        self.uart.init(pin = pin)
    
    def change_baudrate(self, baudrate):
        self.uart.init(baudrate = baudrate)
        
    def change_bits(self, bits):
        self.uart.init(bits = bits)
        
    def change_parity(self, parity):
        self.uart.init(parity = parity)
        
    def change_stop(self, stop):
        self.uart.init(stop = stop)
        
    def change_rx(self, rx):
        self.uart.init(rx = rx)
        
    def change_tx(self, tx):
        self.uart.init(tx = tx)
        
    def change_txbuf(self, txbuf):
        self.uart.init(txbuf = txbuf)
        
    def change_rxbuf(self, rxbuf):
        self.uart.init(rxbuf = rxbuf)            