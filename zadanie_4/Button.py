class Button:
    def __init__(self, pin_number, led):
        self.pin = Pin(pin_number, Pin.IN, Pin.PULL_UP)
        self.led = led
        self.timer = MyTimer(1)
        self.note_timer = MyTimer(3)
        self.pin.irq(trigger=Pin.IRQ_FALLING, handler=self.irq_button)

    def irq_button(self, parameter):
        self.pin.irq(trigger=Pin.IRQ_FALLING, handler=None)
        self.timer.start(period=20, mode=Timer.ONE_SHOT, callback=self.irq_timer)

    def irq_timer(self, parameter):
        if self.pin.value() == 0:
            self.pin.irq(trigger=Pin.IRQ_FALLING, handler=self.irq_button)
        self.handle_press()

    def handle_press(self):
        self.timer.start(period=1500, mode=Timer.ONE_SHOT, callback=self.handle_release)
        self.note_timer.start(period=3000, mode=Timer.ONE_SHOT, callback=self.handle_3sec)

    def handle_3sec(self, par):
        if self.pin.value() == 1:
            pass

    def handle_release(self, par):
        if self.pin.value() == 0:
            self.led.set_color(0, 30, 220, 0)
            self.led.set_color(250, 25, 10, 1)
            self.led.set_color(100, 20, 250, 2)
            led_rgb.set_color(10, 80, 230)
        else:
            self.led.set_color(200, 0, 20, 0)
            self.led.set_color(50, 250, 10, 1)
            self.led.set_color(10, 30, 230, 2)
            led_rgb.set_color(30, 10, 240)
        timer.start(period=2000, mode=Timer.ONE_SHOT, callback=turn_off_leds)

def turn_off_leds(par):
    global led
    led.set_all_color(0, 0, 0)
    led_rgb.set_color(0, 0, 0)

