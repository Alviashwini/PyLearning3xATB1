import time
def note_time_decorator(func):
    def wrapper():
        return wrapper()

@note_time_decorator
def logs_function():
        time.sleep(5)
        print("logs of time taken")
