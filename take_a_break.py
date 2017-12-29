import time
import webbrowser
index = 0
print "This program started on"+time.ctime()
while index < 3:
    time.sleep(2) # this function takes input in seconds only
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    index += 1