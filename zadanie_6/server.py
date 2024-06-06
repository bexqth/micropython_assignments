import network
import socket
import time
from machine import Pin
from zadanie_2.buzzer_class import Buzzer
from zadanie_3.serialrgbled_class import SerialRGBLed
from zadanie_2.rgb_led_class import RGBLED

class Server:
    
    def __init__(self):
        self.nic = network.WLAN(network.AP_IF)
        self.nic.active(True)
        self.nic.config(essid='wifi', authmode = 3, password = 'hesloheslo')
        print(self.nic.ifconfig())
        self.last_message = ''
        
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('192.168.4.1', 243))
        self.s.listen()
        self.led = RGBLED(26, 25, 27)
        self.led.set_color(0, 0, 0)
        self.serial_led = SerialRGBLed(Pin(13), 3)
        self.buzzer = Buzzer(33)
        self.buzzer.set_volume(0)
   
    def set_buzzer(self, buzzer):
        self.buzzer = buzzer
    
    def set_led(self, led):
        self.led = led
    
    def set_sled(self, sled):
        self.sled = sled
    
    def connect(self):
        self.conn, self.address = self.s.accept()
        print('Got a connection from %s' % str(self.address))
        
    def send(self, message):
        self.conn.write(message)
     
    def recieve(self):
        self.last_message = str(self.conn.recv(1023), 'UTF-8')
        print(self.last_message)
    
    def turn_led(self):
        self.send("message recieved")
        if self.last_message == "red":
            self.led.set_color_string(self.last_message)
            time.sleep(1)
            self.led.set_color(0, 0, 0)
        elif self.last_message == "blue":
            self.led.set_color_string(self.last_message)
            time.sleep(1)
            self.led.set_color(0, 0, 0)
        elif self.last_message == "yellow":
            self.led.set_color_string(self.last_message)
            time.sleep(1)
            self.led.set_color(0, 0, 0)
        elif self.last_message == "white":
            self.led.set_color_string(self.last_message)
            time.sleep(1)
            self.led.set_color(0, 0, 0)
        elif self.last_message == "green":
            self.led.set_color_string(self.last_message)
            time.sleep(1)
            self.led.set_color(0, 0, 0)
        elif self.last_message == "purple":
            self.led.set_color_string(self.last_message)
            time.sleep(1)
            self.led.set_color(0, 0, 0)
        elif self.last_message == "light blue":
            self.led.set_color_string(self.last_message)
            time.sleep(1)
            self.led.set_color(0, 0, 0)    
        else:
            self.send("invalid color")
    
    def check_message(self):
        self.send("message recieved")
        if self.last_message == "LED":
            self.led.set_color(0, 255, 0)
            time.sleep(1)
            self.led.set_color(0, 0, 0)
        elif self.last_message == "BUZZER":
            self.buzzer.set_volume(50)
            time.sleep(1)
            self.buzzer.set_volume(0)
        elif self.last_message == "SLED":
            self.serial_led.set_all_color(255, 0, 0)
            time.sleep(1)
            self.serial_led.set_all_color(0, 0, 0)
        else:
            self.send("invalid command")