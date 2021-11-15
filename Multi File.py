import time
import sys
import random
from os import system, name
from Screen import screen
speed = 0.02
class word:
    def write(message):
        global speed
        print("")
        for word in message:
            time.sleep(speed)
            sys.stdout.write(word)
            sys.stdout.flush()
        time.sleep(.1)
        return ""
    def write2(message):
        for word in message:
            global speed
            time.sleep(speed)
            sys.stdout.write(word)
            sys.stdout.flush()
        time.sleep(.1)
        return ""
speed = int(input(word.write2("Type text speed (1-5)")))
if speed == 5:
    speed = 0.01
elif speed == 4:
    speed = 0.02
elif speed == 3:
    speed = 0.03
elif speed == 2:
    speed = 0.04
elif speed == 1:
    speed = 0.05
names = input(word.write("What is your name?"))
mode = input(word.write("Easy or Hard Mode?"))
while playing == True:
    speed = 0.02
    speed = int(input(word.write2("Type text speed (1-5)")))
    if speed == 5:
        speed = 0.01
    elif speed == 4:
        speed = 0.02
    elif speed == 3:
        speed = 0.03
    elif speed == 2:
        speed = 0.04
    elif speed == 1:
        speed = 0.05
    names = input(word.write("What is your name?"))
    mode = input(word.write("Easy or Hard Mode?"))
    level = int(input(word.write2("\nWhat level would you like to play?\n1. Bishop\n2. Secret Path\n3. Castle\n4. \n5. \nNumber: ")))
    screen.clear()
    if level == 1:
        from Bishop_Map import Bishop
        Bishop.play()
        screen.clear()
    elif level == 2:
        from level2V1 import Secret_Path
        Secret_Path.play()
        screen.clear()
        time.sleep(2)
    elif level == 3:
        word.write("\nLevel not out yet")
        time.sleep(2)
        screen.clear()
        time.sleep(2)
    elif level == 4:
        word.write("\nLevel not out yet")
        time.sleep(2)
        screen.clear()
        time.sleep(2)
    elif level == 5:
        word.write("\nLevel not out yet")
        time.sleep(2)
        screen.clear()
        time.sleep(2)
    elif level > 5:
        level = str(level)
        word.write("There is no level " + level)
        time.sleep(2)
        screen.clear()
