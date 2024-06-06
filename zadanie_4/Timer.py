class Timer:
    def __init__(self, timer_number):
        self.timer = Timer(timer_number)

    def start(self, period, mode, callback):
        self.timer.init(period=period, mode=mode, callback=callback)

    def stop(self):
        self.timer.deinit()