"""Module for controlling an RGB LED."""

from machine import Pin, PWM, DAC


class RGBLED:
    """A class to represent an RGB LED."""

    def __init__(self, pin_g, pin_r, pin_b):
        """Initialize the RGB LED with the given pins."""
        self.pwm_g = PWM(Pin(pin_g))
        self.pwm_r = PWM(Pin(pin_r))
        self.pwm_b = PWM(Pin(pin_b))

    def set_dac(self, pin_r, pin_g):
        """Set the pins of the DAC."""
        self.dac_r = DAC(Pin(pin_r))
        self.dac_g = DAC(Pin(pin_g))

    def set_color_with_dac(self, dac_r, dac_g):
        """Set the color using DAC."""
        self.dac_r.write(int(dac_r))
        self.dac_g.write(int(dac_g))

    def set_color(self, g, r, b):
        """Set the color of the RGB LED."""
        self.pwm_g.duty(g)
        self.pwm_r.duty(r)
        self.pwm_b.duty(b)

    def set_color_string(self, string):
        """Set the color of the RGB LED using a string."""
        if string == "blue":
            self.set_color(0, 0, 255)
        elif string == "red":
            self.set_color(0, 255, 0)
        elif string == "green":
            self.set_color(255, 0, 0)
        elif string == "yellow":
            self.set_color(255, 255, 0)
        elif string == "purple":
            self.set_color(30, 200, 240)
        elif string == "white":
            self.set_color(255, 255, 255)
        elif string == "light blue":
            self.set_color(30, 30, 255)
