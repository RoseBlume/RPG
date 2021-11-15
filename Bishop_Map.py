import time
import random
import sys
class word:
    def write(message):
        print("")
        for word in message:
            time.sleep(0.07)
            sys.stdout.write(word)
            sys.stdout.flush()
        time.sleep(.1)
        return ""
    def write2(message):
        for word in message:
            time.sleep(random.choice([0.3, 0.08, 0.07,   0.07, 0.07, 0.06, 0.06, 0.05, 0.01]))
            sys.stdout.write(word)
            sys.stdout.flush()
        time.sleep(.1)
#Work on increasing speed
#Increase speed by adding if statements to the monsters dictionary
#Add a false variable with a global scope if winning
class Bishop:
    def play():
        global Goblin
        Goblin = False
        global Elf
        Elf = False
        global Golem
        Golem = False
        global High_Gob
        High_Gob = False
        global Gatelord
        Gatelord = False
        global Sch
        Sch = False

        name = input(word.write("What is your name?"))
        game = True
        #Fight functions
        def Fight():
            global Goblin
            global Elf
            global Golem
            global High_Gob
            global Gatelord
            global Sch
            if mode == "easy" or mode == "Easy":
                if Goblin == True:
                    User = {
                        "Name": "User",
                        "Health": "400",
                        "Attack": "100"
                        }
                    Monster = {
                        "Name": "Goblin",
                        "Health": 150,
                        "Attack": 50,
                        "i2": "The "
                        }
                elif Elf == True:
                    User = {
                        "Name": "User",
                        "Health": "400",
                        "Attack": "100"
                        }
                    User["Name"] = name
                    a = User["Name"]
                    b = User["Health"]
                    c = User["Attack"]
                    Monster = {
                        "Name": "Elf",
                        "Health": 200,
                        "Attack": 50,
                        "i2": "The "
                        }
                    d = Monster["Name"]
                    e = Monster["Attack"]
                    f = Monster["Health"]
                    i2 = Monster["i2"]
                elif Golem == True:
                    User = {
                        "Name": "User",
                        "Health": "400",
                        "Attack": "100"
                        }
                    User["Name"] = name
                    a = User["Name"]
                    b = User["Health"]
                    c = User["Attack"]
                    Monster = {
                        "Name": "Golem",
                        "Health": 250,
                        "Attack": 75,
                        "i2": "The "
                        }
                    d = Monster["Name"]
                    e = Monster["Attack"]
                    f = Monster["Health"]
                    i2 = Monster["i2"]
                elif Gatelord == True:
                    User = {
                        "Name": "User",
                        "Health": "1000",
                        "Attack": "100"
                        }
                    User["Name"] = name
                    a = User["Name"]
                    b = User["Health"]
                    c = User["Attack"]

                    b = int(b)
                    c = int(c)
                    Monster = {
                        "Name": "Gatelord",
                        "Health": 400,
                        "Attack": 100,
                        "i2": "The "
                        }
                    d = Monster["Name"]
                    e = Monster["Health"]
                    f = Monster["Attack"]
                    i2 = Monster["i2"]
                elif High_Gob == True:
                    User = {
                        "Name": "User",
                        "Health": "400",
                        "Attack": "100"
                        }
                    User["Name"] = name
                    a = User["Name"]
                    b = User["Health"]
                    c = User["Attack"]

                    b = int(b)
                    c = int(c)
                    Monster = {
                        "Name": "High Goblin",
                        "Health": 250,
                        "Attack": 50,
                        "i2": "The "
                        }
                    d = Monster["Name"]
                    e = Monster["Attack"]
                    f = Monster["Health"]
                    i2 = Monster["i2"]
                elif Sch == True:
                    User = {
                        "Name": "User",
                        "Health": "400",
                        "Attack": "50"
                        }
                    User["Name"] = name
                    a = User["Name"]
                    b = User["Health"]
                    c = User["Attack"]

                    b = int(b)
                    c = int(c)
                    Sch = {
                        "Name": "Mrs.Schroeder",
                        "Health": 150,
                        "Attack": 25,
                        "i2": ""
                        }
                    d = Sch["Name"]
                    e = Sch["Health"]
                    f = Sch["Attack"]
                    i2 = Sch["i2"]
            else:
                if Goblin == True:
                    User = {
                        "Name": "User",
                        "Health": "200",
                        "Attack": "100"
                        }
                    User["Name"] = name
                    a = User["Name"]
                    b = User["Health"]
                    c = User["Attack"]
                    Monster = {
                        "Name": "Goblin",
                        "Health": 150,
                        "Attack": 50,
                        "i2": "The "
                        }
                    d = Monster["Name"]
                    e = Monster["Attack"]
                    f = Monster["Health"]
                    i2 = Monster["i2"]
                elif Elf == True:
                    User = {
                        "Name": "User",
                        "Health": "350",
                        "Attack": "100"
                        }
                    User["Name"] = name
                    a = User["Name"]
                    b = User["Health"]
                    c = User["Attack"]
                    Monster = {
                        "Name": "Elf",
                        "Health": 250,
                        "Attack": 50,
                        "i2": "The "
                        }
                    d = Monster["Name"]
                    e = Monster["Attack"]
                    f = Monster["Health"]
                    i2 = Monster["i2"]
                elif Golem == True:
                    User = {
                        "Name": "User",
                        "Health": "600",
                        "Attack": "200"
                        }
                    User["Name"] = name
                    a = User["Name"]
                    b = User["Health"]
                    c = User["Attack"]
                    Monster = {
                        "Name": "Golem",
                        "Health": 400,
                        "Attack": 200,
                        "i2": "The "
                        }
                    d = Monster["Name"]
                    e = Monster["Attack"]
                    f = Monster["Health"]
                    i2 = Monster["i2"]
                elif Gatelord == True:
                    User = {
                        "Name": "User",
                        "Health": "1000",
                        "Attack": "100",
                        "i2": "The "
                        }
                    User["Name"] = name
                    a = User["Name"]
                    b = User["Health"]
                    c = User["Attack"]

                    b = int(b)
                    c = int(c)
                    Monster = {
                        "Name": "Gatelord",
                        "Health": 400,
                        "Attack": 200,
                        "i2": "The "
                        }
                    d = Monster["Name"]
                    e = Monster["Health"]
                    f = Monster["Attack"]
                    i2 = Monster["i2"]
                elif High_Gob == True:
                    User = {
                        "Name": "User",
                        "Health": "350",
                        "Attack": "100 "
                        }
                    User["Name"] = name
                    a = User["Name"]
                    b = User["Health"]
                    c = User["Attack"]
                    b = int(b)
                    c = int(c)
                    Monster = {
                        "Name": "High Goblin",
                        "Health": 250,
                        "Attack": 50,
                        "i2": "The "
                        }
                    d = Monster["Name"]
                    e = Monster["Attack"]
                    f = Monster["Health"]
                    i2 = Monster["i2"]
                elif Sch == True:
                    User = {
                        "Name": "User",
                        "Health": "400",
                        "Attack": "50"
                        }
                    User["Name"] = name
                    a = User["Name"]
                    b = User["Health"]
                    c = User["Attack"]

                    b = int(b)
                    c = int(c)
                    Sch = {
                        "Name": "Mrs.Schroeder",
                        "Health": 250,
                        "Attack": 50,
                        "i2": ""
                        }
                    d = Sch["Name"]
                    e = Sch["Health"]
                    f = Sch["Attack"]
                    i2 = Sch["i2"]
            try:
                d = Monster["Name"]
                e = Monster["Attack"]
                f = Monster["Health"]
                i2 = Monster["i2"]
            except:
                d = Sch["Name"]
                e = Sch["Health"]
                f = Sch["Attack"]
                i2 = Sch["i2"]
            User["Name"] = name
            a = User["Name"]
            b = User["Health"]
            c = User["Attack"]
            b = int(b)
            e = int(e)
            ran = False
            action = "Ny"
            while f > 0 and b > 0 and ran == False:
                b = str(b)
                c = str(c)
                if action != "Check" or action != "check":
                    word.write("\nName:" + a + "\nHealth:" + b + "\nAttack:" + c)
                if Gatelord == True or Sch == True:
                    action = input(word.write("\nWould you like to fight or check?"))
                else:
                    action = input(word.write("\nWould you like to fight, check, or run?"))
                if action == "fight" or action == "Fight":
                    word.write("\nYou are attacking")
                    time.sleep(2)
                    atc = random.randint(1, 2)
                    if atc == 1:
                        word.write("\nYou attacked successfully")
                        time.sleep(2)
                        b = int(b)
                        c = int(c)

                        e = int(e)
                        f = int(f)
                        f -= c
                        f = str(f)
                        c = str(c)
                        word.write("\n"+ i2 + d + " took " + c + " damage")
                        time.sleep(2)
                        word.write("\n"+ i2 + d + " has " + f + " health remaining")
                        time.sleep(3)
                        f = int(f)
                        if f > 0:
                            word.write("\n"+ i2 + d + " is attacking")
                            atce = random.randint(1, 3)
                            if atce == 1:
                                word.write("\nYou dodged")
                                time.sleep(2)
                            elif atce == 2:
                                b = int(b)
                                c = int(c)

                                f = int(f)
                                b -= e
                                b = str(b)
                                e = str(e)
                                word.write("\nYou took " + e + " damage")
                                time.sleep(2)
                                word.write("\nYou have " + b + " health remaining")
                                time.sleep(2)
                            elif atce == 3:
                                b = int(b)
                                c = int(c)

                                e = int(e)
                                f = int(f)
                                b -= e
                                b = str(b)
                                e = str(e)
                                word.write("\nYou took " + e + " damage")
                                time.sleep(2)
                                word.write("\nYou have " + b + " health remaining")
                                time.sleep(2)
                            else:
                                word.write("\n" + i2 + d + " is dead")
                                time.sleep(2)
                    else:
                        word.write("\nYou missed")
                        time.sleep(2)
                        word.write("\n" + i2 + d + " is attacking")
                        atce = random.randint(1, 3)
                        if atce == 1:
                            word.write("\nYou dodged")
                            time.sleep(2)
                        elif atce == 2:
                            b = int(b)
                            c = int(c)

                            e = int(e)
                            f = int(f)
                            b -= e
                            b = str(b)
                            e = str(e)
                            word.write("\nYou took " + e + " damage")
                            time.sleep(2)
                            word.write("\nYou have " + b + " health remaining")
                            time.sleep(2)
                        elif atce == 3:
                            b = int(b)
                            c = int(c)

                            e = int(e)
                            f = int(f)
                            b -= e
                            b = str(b)
                            e = str(e)
                            word.write("\nYou took " + e + " damage")
                            time.sleep(2)
                            word.write("\nYou have " + b + " health remaining")
                            time.sleep(2)
                elif action == "Check" or action == "check":
                    e = str(e)
                    f = str(f)
                    word.write("\nName:" + d + "\nHealth:" + f + "\nAttack:" + e)
                elif action == "Run" or action == "run" and Gatelord != True and Sch != True:
                    if Gatelord == True or Sch == True:
                        word.write("\nYou cannot run")
                    else:
                        word.write("\nAttempting to run")
                        run = random.randint(1, 4)
                        if run == 1:
                            word.write("\nYou ran successfully")
                            time.sleep(2)
                            ran = True
                        else:
                            b = int(b)
                            c = int(c)

                            e = int(e)
                            f = int(f)
                            b -= e
                            b = str(b)
                            e = str(e)
                            word.write("\n" + i2 + d + " is attacking")
                            time.sleep(2)
                            word.write("\nYou took " + e + " damage")
                            time.sleep(2)
                            word.write("\nYou have " + b + " health remaining")
                            time.sleep(2)
                b = int(b)
                c = int(c)

                e = int(e)
                f = int(f)
            if f < 1:
                word.write("\nYou won")
                time.sleep(2)
                User["Health"] = 200
            elif b < 1:
                word.write("\nYou lost")
                global game
                game = False
                time.sleep(2)
            else:
                word.write("\nYou ran")
                time.sleep(2)
        #Text Functions
        def text1():
            word.write("\nYou are a Student in Bishop Smith Catholic Highschool.")
            time.sleep(2)
            word.write("\nYour day usually involves Computer Science in the morning and English in the Afternoon.")
            time.sleep(3)
            word.write("\nToday is different though.")
            time.sleep(2)
            word.write("\nToday when you enter the school you realize that it has transformed into a dungeon.")
            time.sleep(3)
            word.write("\nYou hear something approaching")
            time.sleep(3)
            word.write("\nYou turn around to see a small green creature blocking the exit")
            time.sleep(3)
            word.write("\nYou have no choice but to fight")
        def text2():
            word.write("\nYou hear a voice shouting \"Great Job!\"")
            time.sleep(2)
            word.write("\nIts Mr.Schroeder!")
            time.sleep(2)
            word.write("\nYou decide to ask him what happened")
            time.sleep(2)
            word.write("\nHe explains that while you were away strange portals opened up around the school and monsters began to pour out")
            time.sleep(4)
            word.write("\n\"You must defeat the gate lord or else the world will be overun by monsters\" He says")
            time.sleep(3)
            input(word.write("\nPress enter to continue"))
            word.write("\nYou find yourself at a corner")
            time.sleep(2)
            word.write("\nYou have the choice to go forward or left")
            time.sleep(2)
        def text3():
            input(word.write("\nPress Enter To Continue"))
            time.sleep(1)
            word.write("\nYou enter a dark room with stone walls")
            time.sleep(2)
            word.write("\nThis place would normally be the Grade 8 hall")
            time.sleep(3)
            word.write("\nYou quickly realize that the school is changing to fit the needs of the monsters")
            time.sleep(4)
            word.write("\nYou must stop the monsters quickly")
            time.sleep(4)
            input(word.write("\nPress Enter To Continue"))
            word.write2("\nYou enter another room that has transformed even more than the last")
            time.sleep(3)
            word.write("\nSuddenly out of the darkness a monster appears")
            time.sleep(2)
            word.write("\nIt looks like a Goblin except much larger")
            time.sleep(2)
            word.write("\nYou have no choice but to fight")
        def text4():
            word.write("\nYou continue walking through the school when you reach a corner")
            time.sleep(3)
            word.write("\nWhen you turn left you see Mrs.Schroeder")
            time.sleep(3)
            word.write("\nShe says \"In Order to pass you must prove your strength to me\"")
            time.sleep(4)
            word.write("\nProve your strength to Mrs.Schroeder by defeating her in a battle")
            time.sleep(4)
            word.write("\nYou have no choice but to fight")
            time.sleep(3)
        def text5():
            input(word.write("\nPress Enter To Continue"))
            word.write("\nAfter your fight with Mrs.Schroeder you have grown stronger")
            time.sleep(3)
            word.write("\nAs you continue through the school you take a turn and come face to face with a pointy eared monster with red eyes")
            time.sleep(5)
            word.write("\nThe monster looks suspiciously like a fellow student")
            time.sleep(4)
            word.write("\nYou have no choice but to fight")
            time.sleep(3)
        def text6():
            word.write("\nAfter defeating the elf you continue through the school")
            time.sleep(3)
            word.write("\nYou enter a room that looks exactly like a cave")
            time.sleep(3)
            word.write("\nYou think to yourself \"I must be getting closer to the boss\"")
            time.sleep(3)
            word.write("\nYou notice a creature emerging from the shadows")
            time.sleep(3)
            word.write("\nIts another elf")
            time.sleep(2)
            word.write("\nYou have no choice but to fight")
            time.sleep(3)
        def text7():
            input(word.write("\nPress Enter To Continue"))
            word.write("\nYou take a right turn and are faced with a choice")
            time.sleep(3)
        def text8():
            word.write("\nYou go back the way you came and turn")
            time.sleep(3)
            word.write("\nYou meet another elf that looks like a Student")
            time.sleep(3)
            word.write("\nYou have no choice but to fight")
        def text9():
            word.write("You take a left turn")
            time.sleep(2)
            word.write("\nYou meet another elf that looks like a Student")
            time.sleep(3)
            word.write("\nYou have no choice but to fight")
        def text10():
            word.write("\nYou continue down the hall and take a left turn")
            time.sleep(3)
            word.write("\nYou enter the next room")
            time.sleep(2)
            word.write("\nYou see a door")
            time.sleep(2)
            word.write("\nYou attempt to open it but are too weak")
            time.sleep(3)
            word.write("\nYou decide to continue down the hallway")
            time.sleep(3)
            input(word.write("\nClick enter to continue"))
            word.write("\nYou come face to face with a large creature")
            time.sleep(3)
            word.write("\nYou have no choice but to fight")
        def text11():
            word.write("\nYou continue down the hall and take a right turn and meet Mr.Solar")
            time.sleep(4)
            word.write("\nHe tells you that Mr.Kraftchick can help and all you have to do is step into the portal")
            time.sleep(4)
            input(word.write("\nPress Enter To Continue"))
            word.write("\nWhen you leave the portal Mr.Kraftchick is there with a potion in hand")
            time.sleep(4)
            word.write("\nHe says to open the door you need to drink the potion")
            time.sleep(3)
            input(word.write("\nPress enter to drink the potion"))
            word.write("\nHe says that you must enter another portal to fight the boss")
            time.sleep(4)
            word.write("\nYou have become stronger")
            time.sleep(2)
            input(word.write("\nClick enter to go through the portal"))
            word.write("\nWhen you reach the boss room a large shadowy creature shows up")
            time.sleep(4)
            word.write("\nHe calls himself the Gatelord")
            time.sleep(2)
            word.write("\nHe says that he wishes to stomp out the idea of rebellion")
            time.sleep(4)
            word.write("\nIn his mind teenagers are the most rebellious which is why he chose a highschool")
            time.sleep(4)
            word.write("\nYou have no choice but to fight")
        while game == True:
            mode = input(word.write("\nEasy or Hard Mode?"))
            c = time.localtime()
            time1 = c[4]
            text1()
            Goblin = True
            Fight()
            if game == False:
                break
            Goblin = False
            text2()
            contin = input(word.write("\nForward or left"))
            if contin == "left" or contin == "Left":
                word.write("You decide to go left")
                time.sleep(2)
                word.write("You enter the next room and find a green monster in front of you")
                time.sleep(3)
                Goblin = True
                Fight()
                if game == False:
                    break
                Goblin = False
                time.sleep(2)
                text3()
                High_Gob = True
                Fight()
                if game == False:
                    break
                High_Gob = False
                text4()
                Sch = True
                Fight()
                if game == False:
                    break
                Sch = False
                text5()
                Elf = True
                Fight()
                if game == False:
                    break
                Elf = False
                text6()
                Elf = True
                Fight()
                if game == False:
                    break
                Elf = False
                text7()
                loc = input(word.write("\nWould you like to go forward or left?"))
                if loc == "forward" or loc == "Forward":
                    word.write("You go forward and meet Mrs.Noble")
                    time.sleep(2)
                    word.write("She says \"If you continue this way you will fall to your death\"")
                    time.sleep(2)
                    ch = input(word.write("Would you like to go back? (y/n)"))
                    if ch == "n" or ch == "N" or ch == "No" or ch == "no":
                        word.write("You have died")
                        break
                    elif ch == "y" or ch == "Y" or ch == "Yes" or ch == "yes":
                        word.write("You go back the way you came and turn")
                        time.sleep(3)
                        word.write("You meet another elf that looks like a Student")
                        time.sleep(3)
                        word.write("You have no choice but to fight")
                        Elf = True
                        Fight()
                        if game == False:
                            break
                        Elf = False
                        text10()
                        Golem = True
                        Fight()
                        if game == False:
                            break

                        Golem = False
                        text11()
                        Gatelord = True
                        Fight()
                        if game == False:
                            break

                        Gatelord = False
                    else:
                        word.write("You go back the way you came and turn")
                        time.sleep(3)
                        word.write("You meet another elf that looks like a Student")
                        time.sleep(3)
                        word.write("You have no choice but to fight")
                        Elf = True
                        Fight()
                        if game == False:
                            break
                        Elf = False
                        text10()
                        Golem = True
                        Fight()
                        if game == False:
                            break
                        Golem = False
                        text11()
                        Gatelord = True
                        Fight()
                        if game == False:
                            break
                        Gatelord = False
            else:
                word.write("You continue going forward until you run into Mr.Briton")
                time.sleep(3)
                word.write("He says \"The ground is unstable this way, you should turn back.\"")
                time.sleep(3)
                tb = input(word.write("\nWould you like to turn back? (y/n)"))
                if tb == "n":
                    word.write("You continue past Mr.Briton and fall into a pit and die")
                    time.sleep(2)
                    word.write("You lost")
                    break
                else:
                    word.write("You go back to your previous position and turn right")
                    time.sleep(2)
                    word.write("You enter the next room and find a green monster in front of you")
                    time.sleep(3)
                    Goblin = True
                    Fight()
                    if game == False:
                        break
                    Goblin = False
                    text3()
                    High_Gob = True
                    Fight()
                    if game == False:
                        break

                    High_Gob = False
                    text4()
                    Sch = True
                    Fight()
                    if game == False:
                        break
                    Sch = False
                    text5()
                    Elf = True
                    Fight()
                    if game == False:
                        break
                    Elf = False
                    text6()
                    Elf = True
                    Fight()
                    if game == False:
                        break
                    Elf = False
                    text7()
                    loc = input(word.write("\nWould you like to go forward or left?"))
                    if loc == "forward" or loc == "Forward":
                        word.write("You go forward and meet Mrs.Noble")
                        time.sleep(2)
                        word.write("She says \"If you continue this way you will fall to your death\"")
                        time.sleep(2)
                        ch = input(word.write("Would you like to go back? (y/n)"))
                        if ch == "n" or ch == "N" or ch == "No" or ch == "no":
                            word.write("\nYou have died")
                            break
                        elif ch == "y" or ch == "Y" or ch == "Yes" or ch == "yes":
                            word.write("You go back the way you came and turn")
                            time.sleep(3)
                            word.write("You meet another elf that looks like a Student")
                            time.sleep(3)
                            word.write("You have no choice but to fight")
                            Elf = True
                            Fight()
                            if game == False:
                                break
                            Elf = False
                            text10()
                            Golem = True
                            Fight()
                            if game == False:
                                break
                            Golem = False
                            text11()
                            Gatelord = True
                            Fight()
                            if game == False:
                                break
                            Gatelord = False
                    else:
                        word.write("You go back the way you came and turn")
                        time.sleep(3)
                        word.write("You meet another elf that looks like a Student")
                        time.sleep(3)
                        word.write("You have no choice but to fight")
                        Elf = True
                        Fight()
                        if game == False:
                            break
                        Elf = False
                        text10()
                        Golem = True
                        Fight()
                        if game == False:
                            break

                        Golem = False
                        text11()
                        Gatelord = True
                        Fight()
                        if game == False:
                            break
                        Gatelord = False
            d = time.localtime()
            time2 = d[4]
            if time1 > time2:
                time1a = (60 - time1)
                time1a += time2
            else:
                time1a = (time2 - time1)
            time1a = str(time1a)
            word.write("It took you " + time1a + " minutes to beat the introduction")
            time.sleep(3)
            word.write("You see a portal and decide to walk into it")
            time.sleep(3)
        word.write("Ending")
Bishop.play()
