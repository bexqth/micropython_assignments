from machine import Pin
from zadanie_2.button_class import Button
import esp32
import time
from machine import lightsleep
from machine import wake_reason
from zadanie_2.rgb_led_class import RGBLED
from zadanie_3.serialrgbled_class import SerialRGBLed
from zadanie_2.buzzer_class import Buzzer
from zadanie_5.sender import Sender
#from zadanie_5.node import Node
from zadanie_5.reciever import Reciever

led = RGBLED(26, 25, 27)
led.set_color(0, 0, 0)
serial_led = SerialRGBLed(Pin(13), 3)
buzzer = Buzzer(33)
buzzer.set_volume(0)


sender = Sender(1)
node = Node(1)
reciever = Reciever(1, buzzer, led, serial_led)


button_boot = Pin(0, Pin.IN, Pin.PULL_UP)
esp32.wake_on_ext0(button_boot, esp32.WAKEUP_ALL_LOW)
lightsleep()
print("the esp32 woke up")

while True:
    print("---------------------------")
    print("A - Sender")
    print("B - Node")
    print("C - Reciever")
    print("D - light sleep")
    print("E - change UART settings")
    option = input("your choice: ")
    
    if option == 'A':
        while True:
            print("Enter text u would like to send: ")
            print("(or exit to go back) ")
            text = input("your choice: ")
            if text == 'exit':
                break
            sender.send(text)
    elif option == 'C':
        while True:
            reciever.recieve()
            reciever.check_message()
            break
    elif option == 'B':
        uart_num_sender = int(input("Enter UART number for sender: "))
        uart_num_reciever = int(input("Enter UART number for receiver: "))
        sender = Sender(uart_num_sender)
        reciever = Reciever(uart_num_reciever, buzzer, led, serial_led)
        node = Node(sender, reciever)
        while True:
            print("Relaying message...")
            print("(or exit to go back) ")
            if input("your choice: ") == 'exit':
                break
            node.relay_message()
        
    elif option == 'D':
        print("1 - by seconds")
        print("2 - by pressing a boot button")
        print("(or exit to go back)")
        number = input("select number: ")
        while True:
            if number == 'exit':
                break
            if number == '1':
                sec = input("select number: ")
                print("the esp32 is going into light sleep for " + sec + " seconds")
                time.sleep(0.1)
                if sec == 'exit':
                    break
                lightsleep(int(sec)*1000 - 100)
                print(sec + " passed - esp32 woke up")
            elif number == '2':
                esp32.wake_on_ext0(button_boot, esp32.WAKEUP_ALL_LOW)
                lightsleep()
                print("esp32 woke up by the boot button being pressed")
                break
    elif option == 'E':
        while True:
            print("1 - pin")
            print("2 - baudrate")
            print("3 - bits")
            print("4 - parity")
            print("5 - stop")
            print("6 - rx")
            print("7 - tx")
            print("8 - txbuf")
            print("9 - rxbuf")
            print("(or exit to go back)")
            number = input("Your choice: ")
            if number == 'exit':
               break
            if number == '1':
                value = input("Enter new value: ")
                sender.change_pin(value)
                reciever.change_pin(value)
            elif number == '2':
                value = input("Enter new value: ")
                sender.change_baudrate(int(value))
                reciever.change_baudrate(int(value))
            elif number == '3':
                value = input("Enter new value: ")
                sender.change_bits(int(value))
                reciever.change_bits(int(value))
            elif number == '4':
                value = input("Enter new value: ")
                sender.change_parity(value)
                reciever.change_parity(value)
            elif number == '5':
                value = input("Enter new value: ")
                sender.change_stop(int(value))
                reciever.change_stop(int(value))
            elif number == '6':
                value = input("Enter new value: ")
                sender.change_rx(int(value))
                reciever.change_rx(int(value))
            elif number == '7':
                value = input("Enter new value: ")
                sender.change_tx(int(value))
                reciever.change_tx(int(value))
            elif number == '8':
                value = input("Enter new value: ")
                sender.change_txbuf(int(value))
                reciever.change_txbuf(int(value))
            elif number == '9':
                value = input("Enter new value: ")
                sender.change_rxbuf(int(value))
                reciever.change_rxbuf(int(value))


            













