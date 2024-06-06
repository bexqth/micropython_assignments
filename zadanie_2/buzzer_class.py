"""Module for controlling a buzzer."""

from machine import Pin, PWM
import time


class Buzzer:
    """A class to represent a buzzer."""

    def __init__(self, pin):
        """Initialize the buzzer with the given pin."""
        self.pwm = PWM(Pin(pin), freq=1000, duty=20)

    def set_frequency(self, freq):
        """Set the frequency of the buzzer."""
        self.pwm.freq(freq)

    def set_volume(self, volume):
        """Set the volume of the buzzer."""
        self.pwm.duty(volume)

    def manage_volume(self, button2, button1, button_boot):
        """Manage the volume of the buzzer."""
        volume = self.pwm.duty()
        print("Volume is " + str(volume))
        while button_boot.pin.value() == 1:
            if button2.pin.value() == 0:
                volume += 5
                self.set_volume(volume)
                print("Volume is " + str(volume))
                time.sleep(0.2)
            elif button1.pin.value() == 0 and volume > 0:
                volume -= 5
                self.set_volume(volume)
                print("Volume is " + str(volume))
                time.sleep(0.2)
        self.set_volume(0)

    def vf(self, photoresistor, button2, button1, button_boot):
        """Change the frequency and volume with light."""
        while button_boot.pin.value() == 1:
            if button1.pin.value() == 0:
                light_intensity = photoresistor.get_light_intensity()
                if 10 <= light_intensity <= 10000:
                    self.pwm.freq(int(light_intensity))
                time.sleep(0.2)
            elif button2.pin.value() == 0:
                light_intensity = photoresistor.get_light_intensity()
                if 0 <= light_intensity <= 512:
                    self.pwm.duty(int(light_intensity))
                time.sleep(0.2)
        self.set_volume(0)
