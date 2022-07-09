import time

# Start time when hit enter
input("Press Enter to start")
start_time = time.time()

# Stop time when hit enter
input("Press Enter to stop")
end_time = time.time()

time_lapsed = end_time - start_time
print(time_lapsed)