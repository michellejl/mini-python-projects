import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program started running at: " + time.ctime())

while break_count < total_breaks:
    time.sleep(2 * 60 * 60) # Number of seconds in 2 hours
    url = "https://www.youtube.com/watch?v=LCDgJiPBxfI"
    print("Break Time!")
    webbrowser.open(url)
    break_count += 1

print("This program finished running at: " + time.ctime())