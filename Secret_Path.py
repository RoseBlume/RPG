import time
import random
import sys
from os import system, name
Gatelord = False
Sch = False
name = input("What is your name")
speed = 0.05
mode = "Easy"
class screen:
    def clear():
        if name == 'nt':
            system('cls')
        else:
            system('clear')
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
class Secret_Path:
    def play():
        game = True
        Skele = False
        Skelek = False
        MagiSkele = False
        Sarge = False
        Necromancer = False
        def Fight():
            global Skele
            global MagiSkele
            global Skelek
            global High_Gob
            global Gatelord
            global Sch
            global name
            if mode == "easy" or mode == "Easy":
                if Skele == True:
                    User = {
                        "Name": "User",
                        "Health": "400",
                        "Attack": "100"
                        }
                    Monster = {
                        "Name": "Skeleton",
                        "Health": 150,
                        "Attack": 50,
                        "i2": "The "
                        }
                elif MagiSkele == True:
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
                        "Name": "Skeleton Magician",
                        "Health": 200,
                        "Attack": 50,
                        "i2": "The "
                        }
                    d = Monster["Name"]
                    e = Monster["Attack"]
                    f = Monster["Health"]
                    i2 = Monster["i2"]
                elif Sarge == True:
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
                        "Name": "Sargent Bones",
                        "Health": 250,
                        "Attack": 75,
                        "i2": ""
                        }
                    d = Monster["Name"]
                    e = Monster["Attack"]
                    f = Monster["Health"]
                    i2 = Monster["i2"]
                elif Necromancer == True:
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
                        "Name": "Necromancer",
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
                if Skele == True:
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
                        "Name": "Skeleton",
                        "Health": 150,
                        "Attack": 50,
                        "i2": "The "
                        }
                    d = Monster["Name"]
                    e = Monster["Attack"]
                    f = Monster["Health"]
                    i2 = Monster["i2"]
                elif MagiSkele == True:
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
                        "Name": "Skeleton Magician",
                        "Health": 250,
                        "Attack": 50,
                        "i2": "The "
                        }
                    d = Monster["Name"]
                    e = Monster["Attack"]
                    f = Monster["Health"]
                    i2 = Monster["i2"]
                elif Skelek == True:
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
                        "Name": "Skeleton Knight",
                        "Health": 400,
                        "Attack": 200,
                        "i2": "The "
                        }
                    d = Monster["Name"]
                    e = Monster["Attack"]
                    f = Monster["Health"]
                    i2 = Monster["i2"]
                elif Necromancer == True:
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
                        "Name": "Necromancer",
                        "Health": 400,
                        "Attack": 200,
                        "i2": "The "
                        }
                    d = Monster["Name"]
                    e = Monster["Health"]
                    f = Monster["Attack"]
                    i2 = Monster["i2"]
                elif Sarge == True:
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
                        "Name": "Sargent Bones",
                        "Health": 250,
                        "Attack": 50,
                        "i2": ""
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
                screen.clear()
                if action != "Check" or action != "check":
                    print("\nName:" + a + "\nHealth:" + b + "\nAttack:" + c)
                if Gatelord == True or Sch == True:
                    action = input("\nWould you like to fight or check?")
                else:
                    action = input("\nWould you like to fight, check, or run?")
                if action == "fight" or action == "Fight":
                    print("\nYou are attacking")
                    time.sleep(2)
                    atc = random.randint(1, 2)
                    if atc == 1:
                        print("\nYou attacked successfully")
                        time.sleep(2)
                        b = int(b)
                        c = int(c)

                        e = int(e)
                        f = int(f)
                        f -= c
                        f = str(f)
                        c = str(c)
                        print("\n"+ i2 + d + " took " + c + " damage")
                        time.sleep(2)
                        print("\n"+ i2 + d + " has " + f + " health remaining")
                        time.sleep(3)
                        f = int(f)
                        if f > 0:
                            print("\n"+ i2 + d + " is attacking")
                            atce = random.randint(1, 3)
                            if atce == 1:
                                print("\nYou dodged")
                                time.sleep(2)
                            elif atce == 2:
                                b = int(b)
                                c = int(c)

                                f = int(f)
                                b -= e
                                b = str(b)
                                e = str(e)
                                print("\nYou took " + e + " damage")
                                time.sleep(2)
                                print("\nYou have " + b + " health remaining")
                                time.sleep(2)
                            elif atce == 3:
                                b = int(b)
                                c = int(c)

                                e = int(e)
                                f = int(f)
                                b -= e
                                b = str(b)
                                e = str(e)
                                print("\nYou took " + e + " damage")
                                time.sleep(2)
                                print("\nYou have " + b + " health remaining")
                                time.sleep(2)
                            else:
                                print("\n" + i2 + d + " is dead")
                                time.sleep(2)
                    else:
                        print("\nYou missed")
                        time.sleep(2)
                        print("\n" + i2 + d + " is attacking")
                        atce = random.randint(1, 3)
                        if atce == 1:
                            print("\nYou dodged")
                            time.sleep(2)
                        elif atce == 2:
                            b = int(b)
                            c = int(c)

                            e = int(e)
                            f = int(f)
                            b -= e
                            b = str(b)
                            e = str(e)
                            print("\nYou took " + e + " damage")
                            time.sleep(2)
                            print("\nYou have " + b + " health remaining")
                            time.sleep(2)
                        elif atce == 3:
                            b = int(b)
                            c = int(c)

                            e = int(e)
                            f = int(f)
                            b -= e
                            b = str(b)
                            e = str(e)
                            print("\nYou took " + e + " damage")
                            time.sleep(2)
                            print("\nYou have " + b + " health remaining")
                            time.sleep(2)
                    screen.clear()
                elif action == "Check" or action == "check":
                    e = str(e)
                    f = str(f)
                    print("\nName:" + d + "\nHealth:" + f + "\nAttack:" + e)
                elif action == "Run" or action == "run" and Gatelord != True and Sch != True:
                    if Gatelord == True or Sch == True:
                        print("\nYou cannot run")
                    else:
                        print("\nAttempting to run")
                        run = random.randint(1, 4)
                        if run == 1:
                            print("\nYou ran successfully")
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
                            print("\n" + i2 + d + " is attacking")
                            time.sleep(2)
                            print("\nYou took " + e + " damage")
                            time.sleep(2)
                            print("\nYou have " + b + " health remaining")
                            time.sleep(2)
                    screen.clear()
                b = int(b)
                c = int(c)

                e = int(e)
                f = int(f)
            if f < 1:
                print("\nYou won")
                time.sleep(2)
                User["Health"] = 200
                screen.clear()
            elif b < 1:
                print("\nYou lost")
                global game
                game = False
                time.sleep(2)
            else:
                print("\nYou ran")
                time.sleep(2)
        def Text1():
            word.write("\nAfter leaving the portal you find yourself in a maze")
            time.sleep(3)
            word.write("\nYou decide to try and escape")
            time.sleep(3)
            input(word.write("\nPush Enter To Continue"))
            screen.clear()
        def Text2():
            word.write("\nYou walk forward and find a strange new monster in front of you")
            time.sleep(4)
            word.write("\nIts a Skeleton!")
            time.sleep(2)
            word.write("\nSuddenly you hear a scream")
            time.sleep(2)
            word.write("\nIt sounds like some sort of warcry")
            time.sleep(3)
            word.write("\nYou have no choice but to fight")
            time.sleep(3)
            screen.clear()
        def Text3():
            global loc
            input(word.write("Press Enter To Continue"))
            time.sleep(2)
            word.write("\nYou find yourself at a corner")
            time.sleep(3)
            loc = input(word.write("Would you like to go left or right?"))
            time.sleep(4)
            screen.clear()
        def Text4():
            word.write("\nYou decided to turn right and end up at a corner")
            time.sleep(2)
            word.write("\nYou take a left and continue until you find yourself face to face with another Skeleton")
            time.sleep(4)
            word.write("\nThe Skeleton notices you and lets out a warcry")
            time.sleep(3)
            print("\nYou have no choice but to fight")
            time.sleep(3)
            screen.clear()
        def Text45():
            word.write("\nYou decided to turn left and end up at a corner")
            time.sleep(3)
            screen.clear()
        def Text5():
            word.write("\nYou continue along the path and take a right turn")
            time.sleep(3)
            word.write("\nYou find a Skeleton dressed in a robe blocking your path")
            time.sleep(3)
            word.write("\nYou have no choice but to fight")
            time.sleep(3)
            screen.clear()
        def Text6():
            word.write("You continue down the path and turn left")
            time.sleep(3)
            word.write("You meet a skeleton covered in armor")
            time.sleep(3)
            word.write("The skeleton starts charging at you")
            time.sleep(3)
            word.write("You have no choice but to fight")
            time.sleep(3)
            screen.clear()
        def Text7():
            word.write("Once again you start down the path and turn left")
            time.sleep(3)
            word.write("You meet another skeleton covered in armor")
            time.sleep(3)
            word.write("It lets out a warcry")
            time.sleep(3)
            word.write("You have no choice but to fight")
            time.sleep(3)
            screen.clear()
        def Text8():
            word.write("You continue down the path")
            time.sleep(3)
            word.write("You meet a third skeleton covered in armor")
            time.sleep(3)
            word.write("It lets out a warcry")
            time.sleep(3)
            word.write("You have no choice but to fight")
            time.sleep(3)
            screen.clear()
        def Text9():
            global loc
            word.write("You take a left and continue down the path")
            time.sleep(3)
            word.write("You are faced with a choice")
            time.sleep(3)
            word.write("You can either go forward or take a right")
            time.sleep(3)
            screen.clear()
            loc = input(word.write("Left or forward?"))
            time.sleep(3)
            screen.clear()
        def Text95():
            word.write("You continue forward and come face to face with another Magician")
            time.sleep(3)
            word.write("You have no choice but to fight")
            time.sleep(3)
            screen.clear()
        def Text10():
            word.write("You continue down the path")
            time.sleep(3)
            word.write("You meet a skeleton dressed in a military uniform with a red sash")
            time.sleep(3)
            word.write("The skeleton charges at you with an axe")
            time.sleep(3)
            word.write("You have no choice but to fight")
            time.sleep(3)
            screen.clear()
        def Text11():
            word.write("You take a right and continue down the path")
            time.sleep(3)
            word.write("You meet a dark figure in dressed in a robe")
            time.sleep(3)
            word.write("He summons a skeleton")
            time.sleep(3)
            word.write("You have no choice but to fight")
            time.sleep(3)
            screen.clear()
        def Text12():
            word.write("The Necromancer shrieks")
            time.sleep(3)
            word.write("In an attempt to escape with his life the necromancer opens a portal")
            time.sleep(3)
            word.write("As he walks through the portal he screams you will never defeat our leader")
            time.sleep(3)
            word.write("He managed to escape")
            time.sleep(3)
            screen.clear()
        while game == True:
            Text1()
            Text2()
            Skele = True
            Fight()
            if game == False:
                break
            Skele = False
            Text3()
            if loc == "Right" or loc == "right":
                Text4()
                Skele = True
                Fight()
                if game == False:
                    break
                Skele = False
            elif loc == "left" or loc == "Left":
                Text45()
            Text5()
            MagiSkele = True
            Fight()
            if game == False:
                break
            Skele = False
            Text6()
            Skelek = True
            Fight()
            if game == False:
                break
            Skelek = False
            Text7()
            Skelek = True
            Fight()
            if game == False:
                break
            Skelek = False
            Text8()
            Skelek = True
            Fight()
            if game == False:
                break
            Skelek = False
            Text9()
            if loc == "forward" or loc == "Forward":
                Text95()
                MagiSkele = True
                Fight()
                if game == False:
                    break
            Text10()
            Sarge = True
            Fight()
            if game == False:
                break
            Sarge = False
            Text11()
            Necromancer = True
            Fight()
            if game == False:
                break
            Necromancer = False
            Text12()
