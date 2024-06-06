"""Module for third assignment."""

from machine import Pin
from zadanie_2.rgb_led_class import RGBLED
from zadanie_2.button_class import Button
from zadanie_2.buzzer_class import Buzzer
from zadanie_3.photoresistor_class import Photoresistor
from zadanie_3.serialrgbled_class import SerialRGBLed


def main():
    """Control the code for assignment ."""
    led = RGBLED(26, 25, 27)
    led.set_dac(25, 26)
    led.set_color(0, 0, 0)
    serial_led = SerialRGBLed(Pin(13), 3)
    button2 = Button(17, Pin.PULL_UP, "button2")
    button1 = Button(16, Pin.PULL_UP, "button1")
    button_boot = Button(0, Pin.PULL_UP, "Boot button")
    photoresistor = Photoresistor(Pin(32))
    buzzer = Buzzer(33)
    buzzer.set_volume(0)
    while True:
        print("\n" + "-" * 70)
        print("Select option")
        print("1 - Select color of the chosen RGB SERIAL LED light")
        print("2 - Measure intensity of light using a photoresistor")
        print("3 - Set the color on the RGB LED diode using a DAC")
        print("4 - Change frequency and volume with buttons")
        option = input("Your choice: ")
        if option == '1':
            while True:
                print("\n" + "-" * 70)
                print("Which led lights:")
                print("(put in format - for example 1 and 2 is '1,2')")
                string = input("(or exit to go back): ")
                if string.lower() == 'exit':
                    serial_led.set_color(0, 0, 0, 0)
                    serial_led.set_color(0, 0, 0, 1)
                    serial_led.set_color(0, 0, 0, 2)
                    break
                red = input("red: ")
                green = input("green: ")
                blue = input("blue: ")
                values = string.split(',')
                led1 = 0
                led2 = 0
                led3 = 0
                if len(values) >= 1:
                    led1 = int(values[0])
                    serial_led.set_color(int(red), int(green), int(blue), led1)
                if len(values) >= 2:
                    led2 = int(values[1])
                    serial_led.set_color(int(red), int(green), int(blue), led2)
                if len(values) >= 3:
                    led3 = int(values[2])
                    serial_led.set_color(int(red), int(green), int(blue), led3)
        elif option == '2':
            while True:
                print("\n" + "-" * 70)
                print("Format n - number | v - voltage | p - percentage: ")
                string = input("(or exit to go back): ")
                if string.lower() == 'exit':
                    break
                photoresistor.read_light(string)
        elif option == '3':
            print("if u wanna go back write exit")
            intensity_red = input("Set the insensity of RED led light:")
            intensity_green = input("Set the insensity of GREEN led light:")
            if intensity_red == 'exit' or intensity_green == 'exit':
                break
            led.set_color_with_dac(intensity_red, intensity_green)
        elif option == '5':
            run_sequence(button1, button2, button_boot, led, serial_led)
            
        elif option == '4':
            buzzer.set_volume(20)
            buzzer.set_frequency(1000)
            while True:
                print("\n" + "-" * 70)
                print("To break please press the boot button")
                print("(then 'exit' to go back)")
                buzzer.vf(photoresistor, button2, button1, button_boot)
                string = input("Write 'exit' to go back: ")
                if string.lower() == 'exit':
                    break

def run_sequence(button1, button2, button_boot, led, serial_led):


main()
