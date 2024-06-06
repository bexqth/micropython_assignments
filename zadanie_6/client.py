import network
import socket

class Client:
    
    def __init__(self):
        self.nic = network.WLAN(network.STA_IF)
        self.nic.active(True)
        self.last_message = ''
    
    def connect(self, wifi, password, ip, port):
        self.nic.connect(wifi, password)
        while self.nic.isconnected()==False:
            pass
        print(nic.status())
        self.s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))
        
    def send(self, message):
       self.s.write(str(message))
     
    def recieve(self):
        self.last_message = str(s.recv(1023),'UTF-8')
        print(self.last_message)
