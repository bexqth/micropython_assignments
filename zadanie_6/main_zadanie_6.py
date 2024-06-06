from zadanie_6.server import Server
from zadanie_6.client import Client
from machine import Pin
from zadanie_2.rgb_led_class import RGBLED
from zadanie_2.button_class import Button
from zadanie_2.buzzer_class import Buzzer
from zadanie_3.serialrgbled_class import SerialRGBLed

button_boot = Button(0, Pin.PULL_UP, "Boot button")

while True:
    
    print("1 - comunication with SocketTest")
    print("2 - communication with another ESP")
    option = input("select your option: ")
    
    if option == "1":
        while True:
            print("S - act as a server")
            print("C - act as a client")
            print("E - to exit and go back")
            d = input("select option: ")
            if d == "S":
                server = Server()
                server.connect()
                while button_boot.pin.value() == 1:
                    server.recieve()
                    server.check_message()
               
            elif d == "C":
                client = Client()
                wifi = input("wifi name: ")
                password = input("wifi password: ")
                port = input("port: ")
                ip = input("ip: ")
                client.connect(wifi, password, ip, port)
                while button_boot.pin.value() == 1:
                    mess = input("enter a message: ")
                    client.send(mess)    
                    client.recieve()
            elif d == "E":
                break
    
    elif option == "2":
        print("S - act as a server")
        print("C - act as a client")
        print("E - to exit and go back")
        print("to terminate communication press the boot button")
        d = input("select option: ")
        
        if d == "S":
            server = Server()
            server.connect()
            while button_boot.pin.value() == 1:
                server.recieve()
                server.check_message()
        elif d == "C":
            client = Client()
            wifi = input("wifi name: ")
            password = input("wifi password: ")
            port = input("port: ")
            ip = input("ip: ")
            cliet.connect(wifi, password, ip, port)
            while button_boot.pin.value() == 1:
                mess = input("enter a message: ")
                client.send(mess)    
                client.recieve()
                
          
            
            
            