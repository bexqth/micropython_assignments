from machine import Timer, Pin
from zadanie_2.button_class import Button
from zadanie_2.buzzer_class import Buzzer
import time
from zadanie_2.rgb_led_class import RGBLED
from zadanie_3.serialrgbled_class import SerialRGBLed

timer = Timer(0)
button1Timer = Timer(1)
button2Timer = Timer(2)
note_timer = Timer(3)
printFlag = False
printDone = False
notePlayedDone = False
button1_pressed = False
button2_pressed = False
button1_released = False
button2_released = False
timer_expired = False
button1_count = 0
button2_count = 0

string = ""
button1 = Pin(16, Pin.IN, Pin.PULL_UP)
button2 = Pin(17, Pin.IN, Pin.PULL_UP)
button_boot = Button(0, Pin.PULL_UP, "Boot button")
led = serial_led = SerialRGBLed(Pin(13), 3)
led.set_all_color(0, 0, 0)
buzzer = Buzzer(33)
buzzer.set_volume(0)
led_rgb = RGBLED(26, 25, 27)
led_rgb.set_color(0, 0, 0)

REST = 0
NOTE_D4 = 294
NOTE_G4 = 392
NOTE_AS4 = 466
NOTE_A4 = 440
NOTE_D5 = 587
NOTE_C5 = 523
NOTE_F4 = 349
NOTE_GS4 = 415
NOTE_DS5 = 622
NOTE_B4 = 494
NOTE_CS5 = 554
NOTE_CS4 = 277
NOTE_AS4 = 466
NOTE_F5 = 698
NOTE_E5 = 659
NOTE_D5 = 587
NOTE_A4 = 440
NOTE_AS4 = 466
NOTE_CS5 = 554
NOTE_CS4 = 277
NOTE_D4 = 294
NOTE_D5 = 587

melody = [ 
  REST, NOTE_D4,
  NOTE_G4, NOTE_AS4, NOTE_A4,
  NOTE_G4, NOTE_D5,
  NOTE_C5, 
  NOTE_A4,
  NOTE_G4, NOTE_AS4, NOTE_A4,
  NOTE_F4, NOTE_GS4,
  NOTE_D4, 
  NOTE_D4,
  NOTE_G4, NOTE_AS4, NOTE_A4,
  NOTE_G4, NOTE_D5,
  NOTE_F5, NOTE_E5,
  NOTE_DS5, NOTE_B4,
  NOTE_DS5, NOTE_D5, NOTE_CS5,
  NOTE_CS4, NOTE_B4,
  NOTE_G4,
  NOTE_AS4,
  NOTE_D5, NOTE_AS4,
  NOTE_D5, NOTE_AS4,
  NOTE_DS5, NOTE_D5,
  NOTE_CS5, NOTE_A4,
  NOTE_AS4, NOTE_D5, NOTE_CS5,
  NOTE_CS4, NOTE_D4,
  NOTE_D5, 
  REST, NOTE_AS4,  
  NOTE_D5, NOTE_AS4,
  NOTE_D5, NOTE_AS4,
  NOTE_F5, NOTE_E5,
  NOTE_DS5, NOTE_B4,
  NOTE_DS5, NOTE_D5, NOTE_CS5,
  NOTE_CS4, NOTE_AS4,
  NOTE_G4]

durations = [
  2, 4,
  4, 8, 4,
  2, 4,
  2, 
  2,
  4, 8, 4,
  2, 4,
  1, 
  4,
  4, 8, 4,
  2, 4,
  2, 4,
  2, 4,
  4, 8, 4,
  2, 4,
  1,
  4,
  2, 4,
  2, 4,
  2, 4,
  2, 4,
  4, 8, 4,
  2, 4,
  1, 
  4, 4,  
  2, 4,
  2, 4,
  2, 4,
  2, 4,
  4, 8, 4,
  2, 4,
  1]

def irq_timer1(parameter):
    global button1
    global button1_pressed, button1_count
    if button1.value() == 0:
        button1_pressed = True
        button1_count = button1_count + 1
    button1.irq(trigger= Pin.IRQ_FALLING, handler= irq_button1)

def irq_timer2(parameter):
    global button2
    global button2_pressed, button2_count
    if button2.value() == 0:
        button2_pressed = True
        button2_count = button2_count + 1
    button2.irq(trigger= Pin.IRQ_FALLING, handler= irq_button2)

def irq_button1(parameter):
    global button1
    global button1Timer
    button1.irq(trigger= Pin.IRQ_FALLING, handler= None)
    button1Timer.init(period= 20, mode= Timer.ONE_SHOT, callback= irq_timer1)

def irq_button2(parameter):
    global button2
    global button2Timer
    button2.irq(trigger= Pin.IRQ_FALLING, handler= None)
    button2Timer.init(period= 20, mode= Timer.ONE_SHOT, callback= irq_timer2)

def handle_button1_press(par):
    global button1Timer
    button1Timer.init(period=1500, mode=Timer.ONE_SHOT, callback=handle_button1_release)
    note_timer.init(period=3000, mode=Timer.ONE_SHOT, callback=handle_button1_3sec)

def handle_button1_3sec(par):
    global button1
    if button1.value() == 1:
        pass

def handle_button1_release(par):
    global led, timer, button1, button1_released
    if button1.value() == 0:
        led.set_color(0, 30, 220, 0)
        led.set_color(250, 25, 10, 1)
        led.set_color(100, 20, 250, 2)
        led_rgb.set_color(10, 80, 230)
    else:
        led.set_color(200, 0, 20, 0)
        led.set_color(50, 250, 10, 1)
        led.set_color(10, 30, 230, 2)
        led_rgb.set_color(30, 10, 240)
    button1_released = True
    timer.init(period=2000, mode=Timer.ONE_SHOT, callback=turn_off_leds)

def handle_button2_press(par):
    global button2Timer
    button2Timer.init(period=1500, mode=Timer.ONE_SHOT, callback=handle_button2_release)
    note_timer.init(period=3000, mode=Timer.ONE_SHOT, callback=handle_button2_3sec)

def handle_button2_3sec(par):
    global button2
    if button2.value() == 1:
        pass

def handle_button2_release(par):
    global button2, timer, led
    if button2.value() == 0:
        led.set_color(255, 0, 0, 0)
        led.set_color(0, 255, 0, 1)
        led.set_color(0, 0, 255, 2)
        led_rgb.set_color(10, 200, 10)
    else:
        led.set_color(20, 200, 0, 0)
        led.set_color(210, 30, 20, 1)
        led.set_color(230, 180, 0, 2)
        led_rgb.set_color(20, 250, 150)
    button1_released = True    
    timer.init(period=2000, mode=Timer.ONE_SHOT, callback=turn_off_leds)

def turn_off_leds(par):
    global led
    led.set_all_color(0, 0, 0)
    led_rgb.set_color(0, 0, 0)

def play_tone(note, duration):
    global buzzer, note_timer, timer_expired
    buzzer.set_volume(200)
    if note == 0:
        buzzer.set_volume(0)
    else:    
        buzzer.set_frequency(note)
    timer_expired = False
    note_timer.init(period=round(duration * 1.30), mode=Timer.ONE_SHOT, callback=stop_tone)
    
def play_melody():
    for i in range(len(melody)):
        note = melody[i]
        duration = 1000 / durations[i]
        notePlayed = False
        play_tone(note, round(duration))
        while timer_expired == False:
            pass
        
def stop_tone(timer):
    global buzzer, timer_expired
    buzzer.set_volume(0)
    timer_expired = True

def main():
    global button1_pressed, button2_pressed, button1_released, button2_released
    button1.irq(trigger=Pin.IRQ_FALLING, handler=handle_button1_press)
    button2.irq(trigger=Pin.IRQ_FALLING, handler=handle_button2_press)
    while True:
        print("\n" + "-" * 70)
        print("Select option")
        print("1 - Print input after time")
        print("2 - Info about pressed buttons")
        print("3 - play a song")
        print("4 - light up leds by the buttons being pressed")
        option = input("Your choice: ")
        if option == '1':
            while True:
                print("\n" + "-" * 70)
                global string, printDone
                string = input("enter input (or exit to go back): ")
                time = int(input("enter time:"))
                if string.lower() == 'exit':
                    break
                printFlag = True
                if printFlag == True:
                    printFlag = False
                    timer.init(period= time*1000, mode=Timer.ONE_SHOT, callback=toString)
                    while printDone == False:
                        pass
                    break

        elif option == '2':
            button1.irq(trigger=Pin.IRQ_FALLING, handler=irq_button1)
            button2.irq(trigger=Pin.IRQ_FALLING, handler=irq_button2)
            while button_boot.pin.value() == 1:
                if button1_pressed == True:
                    print("button 1 cout: " + str(button1_count))
                    button1_pressed = False
                elif button2_pressed == True:
                    print("button 2 count: " + str(button2_count))
                    button2_pressed = False
        elif option == '3':
            while True:
                play_melody()
                break

        elif option == '4':
            while button_boot.pin.value() == 1:
                 if button1_released == True:
                     button1_released = False
                 elif button2_released == True:
                     button2_released = False

def toString(timer):
    global printFlag, printDone
    printFlag = False
    printDone = True
    print("your input was: " + string)

main()

