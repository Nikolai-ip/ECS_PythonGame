import time

class Time:

    last_time = time.time()
    delta_time = 0

    @staticmethod
    def update():
        current_time = time.time()
        Time.delta_time = current_time - Time.last_time
        Time.last_time = current_time
