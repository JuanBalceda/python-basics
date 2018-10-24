import webbrowser
import time

# Take a break every hours

num = 0

while num < 3:
    print('Begin at: ' + time.ctime())
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=dlFA0Zq1k2A&list=RDdlFA0Zq1k2A")
    num += 1

print('End at: ' + time.ctime())
