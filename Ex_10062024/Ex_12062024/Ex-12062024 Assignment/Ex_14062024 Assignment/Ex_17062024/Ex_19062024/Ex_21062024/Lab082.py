import time
def logs_function():
    time.sleep(3)
    print("logs of time taken")

start_time = time.time()
logs_function()
end_time = time.time()
print("Time taken - " + str(end_time - start_time))