from datetime import datetime


def print_time(string):
    time_string = datetime.now().strftime("%H:%M:%S")
    print(time_string, string)


class Elapsed:
    def __init__(self):
        self.time_start = datetime.now()

    def end(self):
        time_end = datetime.now() - self.time_start
        print_time(f"Process ended after {time_end}")