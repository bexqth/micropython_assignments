"""Module for controlling a photoresistor."""

from machine import Pin, ADC


class Photoresistor:
    """A class to represent a photoresistor."""

    def __init__(self, pin):
        """Initialize the photoresistor with the given pin."""
        self.adc = ADC(Pin(pin))
        self.adc.width(ADC.WIDTH_12BIT)
        self.adc.atten(ADC.ATTN_11DB)

    def read_light(self, display_format):
        """Read measured value."""
        measured_value = self.adc.read()
        voltage = (3.3 / 4095) * measured_value
        one_percent = 4095 / 100
        percentage = measured_value / one_percent

        if display_format == 'n':
            print("measured value is " + str(measured_value))
        elif display_format == 'v':
            print("voltage is " + str(voltage))
        elif display_format == 'p':
            print("percentage is " + str(percentage))

    def get_light_intensity(self):
        """Return measured value."""
        return self.adc.read()
