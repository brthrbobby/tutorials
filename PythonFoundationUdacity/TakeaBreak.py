#TODO: Docstring

#TODO: keep a timer for 2 hours

#TODO: open a browser to video

import time
import webbrowser

loopVar = True
while(loopVar == True): # Loop forever until program is broken by window close or ctrl C
    
    time.sleep(10) # set sleep timer to pause program in seconds
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

