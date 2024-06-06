"""Module for controlling an RGB LED, buttons and a buzzer."""

from machine import Pin
from zadanie_2.rgb_led_class import RGBLED
from zadanie_2.button_class import Button
from zadanie_2.buzzer_class import Buzzer


def main():
    """Control the RGB LED, buttons and buzzer."""
    led = RGBLED(26, 25, 27)
    button2 = Button(17, Pin.PULL_UP, "button2")
    button1 = Button(16, Pin.PULL_UP, "button1")
    button_boot = Button(0, Pin.PULL_UP, "Boot button")

    buzzer = Buzzer(33)
    buzzer.set_volume(0)

    while True:
        print("\n" + "-" * 70)
        print("Select option")
        print("1 - Select color of the RGB LED light")
        print("2 - Print status of pressed buttons")
        print("3 - Change the frequency and volume of the buzzer")
        print("4 - Set custom color of the RGB LED light")
        print("5 - Change the volume of the buzzer with buttons")
        option = input("Your choice: ")

        if option == '1':
            while True:
                print("\n" + "-" * 70)
                print("Write string")
                print("'blue', 'red', 'green', 'yellow'")
                print("'purple', 'white', 'light blue' (or 'exit' to go back)")
                string = input("your input: ")
                if string.lower() == 'exit':
                    led.set_color(0, 0, 0)
                    break
                led.set_color_string(string)

        elif option == '2':
            while True:
                print("\n" + "-" * 70)
                print("Write string")
                print("'button1', 'button2'")
                print("to break please press the boot button")
                print("(then 'exit' to go back")
                button_string = input("your input: ")
                if button_string.lower() == 'button1':
                    button1.print_status(button_boot)
                elif button_string.lower() == 'button2':
                    button2.print_status(button_boot)
                elif button_string.lower() == 'exit':
                    break

        elif option == '3':
            while True:
                print("\n" + "-" * 70)
                print("Write string")
                print("'f' (for frequency) , 'v' (for volume)")
                print("(or 'exit' to go back)")
                string = input("your input: ")
                if string.lower() == 'f':
                    freq = int(input("Enter frequency: "))
                    buzzer.set_frequency(freq)
                elif string.lower() == 'v':
                    volume = int(input("Enter volume: "))
                    buzzer.set_volume(volume)
                elif string.lower() == 'exit':
                    buzzer.set_volume(0)
                    break

        elif option == '4':
            while True:
                print("\n" + "-" * 70)
                print("Write string")
                print("'custom' (or 'exit' to go back)")
                string = input("your input: ")
                if string.lower() == 'custom':
                    red = int(input("Enter red: "))
                    green = int(input("Enter green: "))
                    blue = int(input("Enter blue: "))
                    led.set_color(green, red, blue)
                elif string.lower() == 'exit':
                    led.set_color(0, 0, 0)
                    break

        elif option == '5':
            while True:
                print("\n" + "-" * 70)
                print("To break please press the boot button")
                print("(then 'exit' to go back)")
                buzzer.manage_volume(button2, button1, button_boot)
                string = input("Write string - 'exit' to go back: ")
                if string.lower() == 'exit':
                    break


main()
