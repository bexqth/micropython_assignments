from machine import UART, Pin

class Sender:
    def __init__(self, uart_num):
        self.uart = UART(uart_num)
        self.uart.init(baudrate = 115200, bits = 8, parity = None, stop = 1);
        self.uart.init(rx = 21, tx = 19);
        self.uart.init(txbuf=512, rxbuf=512)

    def send(self, message):
        self.uart.write(message)
    
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