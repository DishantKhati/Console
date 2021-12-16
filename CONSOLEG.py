import os
import random
import pyttsx3
from os import system, name

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    pass


def CAT_GAME():
    system("cls")
    print("\t\tOPENING CATEGORY MENU : DB GAMES \n ACTION & SHOOTING(T) \n\t ADVENTURE(A) \n\t\t ARCADE & PUZZLE(P) \n\t\t\t COOKING , HIDDEN OBJECTS & FARMING(C) \n\t MULTIPLAYER(M) \n\t\t RACING(R) \n\t\t\t STRATEGY(S) \n")
    speak("\t\tOPENING CATEGORY MENU : DB GAMES \n ACTION & SHOOTING(T) \n\t ADVENTURE(A) \n\t\t ARCADE & PUZZLE(P) \n\t\t\t COOKING , HIDDEN OBJECTS & FARMING(C) \n\t MULTIPLAYER(M) \n\t\t RACING(R) \n\t\t\t STRATEGY(S) \n ENTER YOUR CHOICE")
    IN = input("ENTER YOUR CHOICE: ")
    if IN == "T" or IN == "t":
        system("cls")
        print("YOU HAVE CHOSEN ACTION AND SHOOTING GAMES CATEGORY \n\n OPENING GAMES MENU FOR THIS CATEGORY")
        speak("YOU HAVE CHOSEN ACTION AND SHOOTING GAMES CATEGORY \n\n OPENING GAMES MENU FOR THIS CATEGORY")
        print("\n\n\t\t\t GAMES MENU \n\t ASSASSIN'S CREED(A) \n\t\t COUNTER STRIKE CONDITION ZERO(C) \n\t\t\t LEGO MARVEL (L) \n\t\t\t\t PROTOTYPE 2(P) \n\t\t\t\t\t IRON MAN(I) \n\t\t\t\t\t\t THE HULK(H) \n\t\t\t\t\t\t\t TOMB RAIDER(R) \n\t\t\t\t\t\t\t\t TRANSFORMERS(T) \n\n SUB-CAT GAMES : \n\t GTA SERIES(G) \n\t\t PRINCE OF PERSIA SERIES(O) \n\t\t\t PROJECT IGI SERIES(J) \n\t\t\t HALF LIFE(F) \n")
        speak("\n\t PRESS A FOR ASSASSIN'S CREED \n\t\tC FOR COUNTER STRIKE CONDITION ZERO \n\t\t\t L FOR LEGO MARVEL\n\t\t\t\t P FOR PROTOTYPE 2\n\t\t\t\t\t I FOR IRON MAN \n\t\t\t\t\t\tH FOR THE HULK \n\t\t\t\t\t\t\tR FOR TOMB RAIDER \n\t\t\t\t\t\t\t\tT FOR TRANSFORMERS \n\n SUB-CAT GAMES : \n\tG FOR GTA SERIES \n\t\tO FOR PRINCE OF PERSIA SERIES\n\t\t\tJ FOR PROJECT IGI SERIES\n\t\t\tF FOR HALF LIFE\n ENTER YOUR CHOICE ")
        ST = input("ENTER YOUR CHOICE: ")
        if ST == "A" or ST == "a":
            print("YOU HAVE CHOSEN ASSASSIN'S CREED")
            speak("YOU HAVE CHOSEN ASSASSIN'S CREED")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\ASSASSIN'S CREED\Assassin's Creed- Brotherhood.exe")
        elif ST == "C" or ST == "c":
            print("YOU HAVE CHOSEN COUNTER STRIKE CONDITION ZERO")
            speak("YOU HAVE CHOSEN COUNTER STRIKE CONDITION ZERO")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\COUNTER STRIKE CONDITION ZERO\czero.exe")
        elif ST == "F" or ST == "F":
            print("YOU HAVE CHOSEN HALF LIFE")
            speak("YOU HAVE CHOSEN HALF LIFE")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\COUNTER STRIKE CONDITION ZERO\hl.exe")
        elif ST == "L" or ST == "l":
            print("YOU HAVE CHOSEN LEGO MARVEL SUPER HEROES")
            speak("YOU HAVE CHOSEN LEGO MARVEL SUPER HEROES")
            speak("LAUNCHING GAME...")
            print("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\MULTIPLAYER\LEGO MARVEL SUPER HEROES\LEGOMarvel.exe")
        elif ST == "P" or ST == "p":
            print("YOU HAVE CHOSEN PROTOTYPE 2")
            speak("YOU HAVE CHOSEN PROTOTYPE 2")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\PROTOTYPE 2\prototype2.exe")
        elif ST == "I" or ST == "i":
            print("YOU HAVE CHOSEN IRON MAN")
            speak("YOU HAVE CHOSEN IRON MAN")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\IRON MAN\GameLauncher.exe")
        elif ST == "H" or ST == "h":
            print("YOU HAVE CHOSEN THE HULK")
            speak("YOU HAVE CHOSEN THE HULK")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\THE HULK\hulk.exe")
        elif ST == "r" or ST == "R":
            print("YOU HAVE CHOSEN TOMB RAIDER")
            speak("YOU HAVE CHOSEN TOMB RAIDER")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\TOMB RAIDER\tra.exe")
        elif ST == "T" or ST == "t":
            print("YOU HAVE CHOSEN TRANSFORMERS")
            speak("YOU HAVE CHOSEN TRANSFORMERS")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\56")
        elif ST == "G" or ST == "g":
            system("cls")
            print("YOU HAVE CHOSEN GTA SERIES \n IT HAS 2 GAMES")
            speak("YOU HAVE CHOSEN GTA SERIES \n IT HAS 2 GAMES")
            print("\t\tGTA MENU \n GTA VICE CITY(V) \n\t GTA SAN ANDREAS(S)")
            speak(
                "\t\tGTA MENU \n GTA VICE CITY(V) \n\t GTA SAN ANDREAS(S) \nENTER YOUR CHOICE")
            SC = input(
                "\nV FOR GTA VICE CITY\n\t S FOR GTA SAN ANDREAS\nENTER YOUR CHOICE: ")
            if SC == "V" or SC == "v":
                print("YOU HAVE CHOSEN GTA VICE CITY")
                speak("YOU HAVE CHOSEN GTA VICE CITY")
                print("LAUNCHING GAME...")
                speak("LAUNCHING GAME...")
                os.startfile(
                    r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\GTA SERIES\GTA VICE CITY\GTA Vice ultimate Trainer.exe")
            elif SC == "S" or SC == "s":
                print("YOU HAVE CHOSEN GTA SAN ANDREAS")
                speak("YOU HAVE CHOSEN GTA SAN ANDREAS")
                print("LAUNCHING GAME...")
                speak("LAUNCHING GAME...")
                os.startfile(
                    r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\GTA SERIES\GTA SAN ANDREAS\gta_sa.exe")
        elif ST == "O" or ST == "o":
            system("cls")
            print("YOU HAVE CHOSEN PRINCE OF PERSIA SERIES \n IT HAS 3 GAMES")
            speak("YOU HAVE CHOSEN PRINCE OF PERSIA SERIES \n IT HAS 3 GAMES")
            print(
                "\t\tPOP MENU \n PRINCE OF PERSIA 1(1) \n\t PRINCE OF PERSIA 2(2) \n\t\t PRINCE OF PERSIA 3(3)")
            speak("\nPRESS 1 FOR PRINCE OF PERSIA 1 \n\t2 FOR PRINCE OF PERSIA 2 \n\t\t3 FOR PRINCE OF PERSIA 3\nENTER YOUR CHOICE: ")
            SC = input("ENTER YOUR CHOICE: ")
            if SC == "1":
                print("YOU HAVE CHOSEN PRINCE OF PERSIA 1 : SANDS OF TIME ")
                speak("YOU HAVE CHOSEN PRINCE OF PERSIA 1 : SANDS OF TIME ")
                print("LAUNCHING GAME...")
                speak("LAUNCHING GAME...")
                os.startfile(
                    r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\PRINCE OF PERSIA\PRINCE OF PERSIA 1\POP.exe")
            elif SC == "2":
                print("YOU HAVE CHOSEN PRINCE OF PERSIA 2 : THE WARRIOR WITHIN")
                speak("YOU HAVE CHOSEN PRINCE OF PERSIA 2 : THE WARRIOR WITHIN")
                print("LAUNCHING GAME...")
                speak("LAUNCHING GAME...")
                os.startfile(
                    r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\PRINCE OF PERSIA\PRINCE OF PERSIA 2\POP2.exe")
            elif SC == "3":
                print("YOU HAVE CHOSEN PRINCE OF PERSIA 3 : THE TWO THRONES")
                speak("YOU HAVE CHOSEN PRINCE OF PERSIA 3 : THE TWO THRONES")
                print("LAUNCHING GAME...")
                print("PLEASE HOLD CTRL TO LAUNCH THE GAME")
                speak("LAUNCHING GAME...")
                os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\34")
                print("                                                                                                                                                                                                                                                                                                                                                                                                           ")
                os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\34G")
        elif ST == "J" or ST == "j":
            system("cls")
            print("YOU HAVE CHOSEN PROJECT IGI SERIES \n IT HAS 2 GAMES")
            speak("YOU HAVE CHOSEN PROJECT IGI SERIES \n IT HAS 2 GAMES")
            print("\t\tIGI MENU \n PROJECT IGI 1(1) \n\t PROJECT IGI 2(2)")
            speak("\nPRESS 1 FOR PROJECT IGI 1\n\t2 FOR PROJECT IGI 2\nENTER YOUR CHOICE")
            SC = input("ENTER YOUR CHOICE: ")
            if SC == "1":
                print("YOU HAVE CHOSEN PROJECT IGI : I'M GOING IN ")
                speak("YOU HAVE CHOSEN PROJECT IGI : I'M GOING IN ")
                print("LAUNCHING GAME...")
                speak("LAUNCHING GAME...")
                os.startfile(
                    r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\PROJECT IGI SERIES\PROJECT IGI I'M GOING IN\IGI.exe")
            elif SC == "2":
                print("YOU HAVE CHOSEN PROJECT IGI 2 : COVERT STRIKE")
                speak("YOU HAVE CHOSEN PROJECT IGI 2 : COVERT STRIKE")
                print("LAUNCHING GAME...")
                speak("LAUNCHING GAME...")
                os.startfile(
                    r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\PROJECT IGI SERIES\IGI 2 COVERT STRIKE\pc\igi2.exe")
    elif IN == "A" or IN == "a":
        system("cls")
        print(
            "YOU HAVE CHOSEN ADVENTURE CATEGORY \n\n OPENING GAMES MENU FOR THIS CATEGORY")
        speak(
            "YOU HAVE CHOSEN ADVENTURE CATEGORY \n\n OPENING GAMES MENU FOR THIS CATEGORY")
        print("\n\n\t\t\t GAMES MENU \n\t ALEX GORDON(A) \n\t\t ALONE IN WINTER(I) \n\t\t\t DUNGEON RIDER(D) \n\t\t\t\t SKY RUNNERS(R) \n\t\t\t\t\t SONIC ADDVENTURE DEMO(S) \n\t TARZAN(T)  \n\t\t ROLLER COASTER TYCOON 3(3) \n\n SUB-CAT GAMES : \n\t MARIO SERIES(M) \n\t\t CHICKEN INVADERS SERIES(C) \n\t\t\t POKEMON SERIES(P) \n\t\t\t\t SCRAP GARDEN SERIES(SC)")
        speak("n\tPRESS A FOR ALEX GORDON \n\t\tI FOR ALONE IN WINTER\n\t\t\tD FOR DUNGEON RIDER\n\t\t\t\tR FOR SKY RUNNERS\n\t\t\t\t\tS FOR SONIC ADDVENTURE DEMO\n\tT FOR TARZAN\n\t\t3 FOR ROLLER COASTER TYCOON 3\n\n SUB-CAT GAMES : \n\tM FOR MARIO SERIES\n\t\tC FOR CHICKEN INVADERS SERIES\n\t\t\tP FOR POKEMON SERIES\n\t\t\t\tSC FOR SCRAP GARDEN SERIES\n ENTER YOUR CHOICE: ")
        ST = input("ENTER YOUR CHOICE: ")
        if ST == "A" or ST == "a":
            print("YOU HAVE CHOSEN ALEX GORDON")
            speak("YOU HAVE CHOSEN ALEX GORDON")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\88")
        elif ST == "C" or ST == "c":
            system("cls")
            print("YOU HAVE CHOSEN CHICKEN INVADERS SERIES \n IT HAS 2 GAMES")
            speak("YOU HAVE CHOSEN CHICKEN INVADERS SERIES \n IT HAS 2 GAMES")
            print("\t\tCI MENU \n CHICKEN INVADERS 3(3) \n\t CHICKEN INVADERS 4(4)")
            speak(
                "\nPRESS 3 FOR CHICKEN INVADERS 3\n\t4 FOR CHICKEN INVADERS 4\nENTER YOUR CHOICE")
            SC = input("ENTER YOUR CHOICE: ")
            if SC == "3":
                print("YOU HAVE CHOSEN CHICKEN INVADERS 3 : REVENGE OF THE YOLK")
                speak("YOU HAVE CHOSEN CHICKEN INVADERS 3 : REVENGE OF THE YOLK")
                print("LAUNCHING GAME...")
                speak("LAUNCHING GAME...")
                os.startfile(
                    r"E:\DB DRIVE\DB games\ADVENTURE\CHICKEN INVADERS\CHICKEN INVADERS 3\CI3.exe")
            elif SC == "4":
                print("YOU HAVE CHOSEN CHICKEN INVADERS 4 : ULTIMATE OMELETTE")
                speak("YOU HAVE CHOSEN CHICKEN INVADERS 4 : ULTIMATE OMELETTE")
                print("LAUNCHING GAME...")
                speak("LAUNCHING GAME...")
                os.startfile(
                    r"E:\DB DRIVE\DB games\ADVENTURE\CHICKEN INVADERS\CHICKEN INVADERS 4\CI4.exe")
        elif ST == "D" or ST == "d":
            print("YOU HAVE CHOSEN DUNGEON RIDER")
            speak("YOU HAVE CHOSEN DUNGEON RIDER")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ADVENTURE\DUNGEON RIDER\Dungeon Rider.exe")
        elif ST == "3":
            print("YOU HAVE CHOSEN ROLLER COASTER TYCOON 3")
            speak("YOU HAVE CHOSEN ROLLER COASTER TYCOON 3")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ADVENTURE\ROLLER COASTER TYCOON 3\RCT3.exe")
        elif ST == "r" or ST == "R":
            print("YOU HAVE CHOSEN SKY RUNNERS")
            speak("YOU HAVE CHOSEN SKY RUNNERS")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\74")
        elif ST == "S" or ST == "s":
            print("YOU HAVE CHOSEN SONIC ADVENTURE DEMO")
            speak("YOU HAVE CHOSEN SONIC ADVENTURE DEMO")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ADVENTURE\SONIC ADVENTURE\sonic.exe")
        elif ST == "I" or ST == "i":
            print("YOU HAVE CHOSEN ALONE IN WINTER")
            speak("YOU HAVE CHOSEN ALONE IN WINTER")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ADVENTURE\ALONE IN WINTER\engine.exe")
        elif ST == "T" or ST == "t":
            print("YOU HAVE CHOSEN TARZAN")
            speak("YOU HAVE CHOSEN TARZAN")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(r"E:\DB DRIVE\DB games\ADVENTURE\TARZAN\tarzan.exe")
        elif ST == "SC" or ST == "sc":
            system("cls")
            print("YOU HAVE CHOSEN SCRAP GARDEN SERIES \n IT HAS 2 GAMES")
            speak("YOU HAVE CHOSEN SCRAP GARDEN SERIES \n IT HAS 2 GAMES")
            print("\t\tSG MENU \n SCRAP GARDEN THE DAY BEFORE(T) \n\t SCRAP GARDEN(S)")
            speak(
                "\nPRESS T FOR SCRAP GARDEN THE DAY BEFORE\n\tS FOR SCRAP GARDEN\nENTER YOUR CHOICE")
            SC = input("ENTER YOUR CHOICE: ")
            if SC == "T" or SC == "t":
                print("YOU HAVE CHOSEN SCRAP GARDEN THE DAY BEFORE")
                speak("YOU HAVE CHOSEN SCRAP GARDEN THE DAY BEFORE")
                print("LAUNCHING GAME...")
                speak("LAUNCHING GAME...")
                os.startfile(
                    r"E:\DB DRIVE\DB games\ADVENTURE\SCRAP GARDEN SERIES\SCRAP GARDEN THE DAY BEFORE\game.exe")
            elif SC == "S" or SC == "s":
                print("YOU HAVE CHOSEN SCRAP GARDEN")
                speak("YOU HAVE CHOSEN SCRAP GARDEN")
                print("LAUNCHING GAME...")
                speak("LAUNCHING GAME...")
                os.startfile(
                    r"E:\DB DRIVE\DB games\ADVENTURE\SCRAP GARDEN SERIES\SCRAP GARDEN\game.exe")
        elif ST == "M" or ST == "m":
            system("cls")
            print("YOU HAVE CHOSEN MARIO SERIES \n IT HAS 3 GAMES")
            speak("YOU HAVE CHOSEN MARIO SERIES \n IT HAS 3 GAMES")
            print(
                "\t\tMARIO MENU \n MARIO FOREVER(1) \n\t MARIO GALAXY(2) \n\t\t NEW MARIO BROS(3)")
            speak(
                "\nPRESS 1 FOR MARIO FOREVER\n\t2 FOR MARIO GALAXY\n\t\t3 FOR NEW MARIO BROS\nENTER YOUR CHOICE")
            SC = input("ENTER YOUR CHOICE: ")
            if SC == "1":
                print("YOU HAVE CHOSEN MARIO FOREVER ")
                speak("YOU HAVE CHOSEN MARIO FOREVER ")
                print("LAUNCHING GAME...")
                speak("LAUNCHING GAME...")
                os.startfile(
                    r"E:\DB DRIVE\DB games\ADVENTURE\MARIO\MARIO FOREVER\Mario Forever 5.0.exe")
            elif SC == "2":
                print("YOU HAVE CHOSEN MARIO GALAXY ")
                speak("YOU HAVE CHOSEN MARIO FOREVER ")
                print("LAUNCHING GAME...")
                speak("LAUNCHING GAME...")
                os.startfile(
                    r"E:\DB DRIVE\DB games\ADVENTURE\MARIO\MARIO GALAXY\Mario Forever Galaxy.exe")
            elif SC == "3":
                print("YOU HAVE CHOSEN NEW MARIO BROS")
                speak("YOU HAVE CHOSEN NEW MARIO BROS")
                print("LAUNCHING GAME...")
                speak("LAUNCHING GAME...")
                os.startfile(
                    r"E:\DB DRIVE\DB games\ADVENTURE\MARIO\NEW MARIO BROS\New Super Mario Bros.exe")
        elif ST == "P" or ST == "p":
            system("cls")
            print("YOU HAVE CHOSEN POKEMON SERIES \n IT HAS 3 GAMES")
            speak("YOU HAVE CHOSEN POKEMON SERIES \n IT HAS 3 GAMES")
            print("\t\tPOKEMON MENU \n POKEMON GLOBAL REVOLUTION(1) \n\t POKEMON MEGA ADVENTURE(2) \n\t\t POKEMON URANIUM(3)")
            speak("\nPRESS 1 FOR POKEMON GLOBAL REVOLUTION\n\t2 FOR POKEMON MEGA ADVENTURE\n\t\t3 FOR POKEMON URANIUM\nENTER YOUR CHOICE")
            SC = input("ENTER YOUR CHOICE: ")
            if SC == "1":
                print("YOU HAVE POKEMON GLOBAL REVOLUTION ")
                speak("YOU HAVE POKEMON GLOBAL REVOLUTION ")
                print("LAUNCHING GAME...")
                speak("LAUNCHING GAME...")
                os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\96")
            elif SC == "2":
                print("YOU HAVE POKEMON MEGA ADVENTURE ")
                speak("YOU HAVE POKEMON GLOBAL REVOLUTION ")
                print("LAUNCHING GAME...")
                speak("LAUNCHING GAME...")
                os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\98")
            elif SC == "3":
                print("YOU HAVE CHOSEN POKEMON URANIUM ")
                speak("YOU HAVE CHOSEN POKEMON URANIUM ")
                print("LAUNCHING GAME...")
                speak("LAUNCHING GAME...")
                os.startfile(
                    r"E:\DB DRIVE\DB games\ADVENTURE\POKEMON\POKEMON URANIUM\Uranium.exe")
    elif IN == "P" or IN == "p":
        system("cls")
        print("YOU HAVE CHOSEN ARCADE AND PUZZLE GAMES CATEGORY \n\n OPENING GAMES MENU FOR THIS CATEGORY")
        speak("YOU HAVE CHOSEN ARCADE AND PUZZLE GAMES CATEGORY \n\n OPENING GAMES MENU FOR THIS CATEGORY")
        print("\n\n\t\t\t GAMES MENU \n\t BATTLE RANCH(B) \n\t\t CARROM(C) \n\t\t\t DE BLOB(D) \n\t\t\t\t DX BALL 2(X) \n\t\t\t\t\t HARD HAT III(H) \n\t\t\t\t\t\t HEROES OF HELLAS 3(O) \n\t\t\t\t\t\t\t JARDINAINS!(J) \n\t\t\t\t\t\t\t KBC(K)\n\t MACHINARIUM(M) \n\t\t NAMARIEL LEGENDS(N) \n\t\t\t PARANORMAL PURSUIT(P) \n\t\t\t\t PORTAL OF EVIL(E) \n\t\t\t\t\t PUZZLE PUPPERS(U) \n\t\t\t\t\t\t TEKKEN 3(T) \n\t\t\t\t\t\t\t VOID(V) \n\t\t\t\t\t\t\t WEIRD PARK SCARY TALES(W) \n\t\t\t\t\t\t\t FOOTBALL(F)")
        speak("\n\tPRESS B FOR BATTLE RANCH\n\t\tC FOR CARROM\n\t\t\tD FOR DE BLOB\n\t\t\t\tX FOR DX BALL 2\n\t\t\t\t\tH FOR HARD HAT III\n\t\t\t\t\t\tO FOR HEROES OF HELLAS 3\n\t\t\t\t\t\t\tJ FOR JARDINAINS!\n\t\t\t\t\t\t\tK FOR KBC\n\tM FOR MACHINARIUM\n\t\tN FOR NAMARIEL LEGENDS\n\t\t\tP FOR PARANORMAL PURSUIT\n\t\t\t\tE FOR PORTAL OF EVIL\n\t\t\t\t\tU FOR PUZZLE PUPPERS\n\t\t\t\t\t\tT FOR TEKKEN 3\n\t\t\t\t\t\t\tV FOR VOID\n\t\t\t\t\t\t\tW FOR WEIRD PARK SCARY TALES\n\t\t\t\t\t\t\tF FOR FOOTBALL\n ENTER YOUR CHOICE")
        ST = input("ENTER YOUR CHOICE: ")
        if ST == "B" or ST == "b":
            print("YOU HAVE CHOSEN BATTLE RANCH ")
            speak("YOU HAVE CHOSEN BATTLE RANCH ")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\BATTLE RANCH\BATTLE RANCH.exe")
        elif ST == "C" or ST == "c":
            print("YOU HAVE CHOSEN CARROM")
            speak("YOU HAVE CHOSEN CARROM")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\20")
        elif ST == "C" or ST == "c":
            print("YOU HAVE CHOSEN KAUN BANEGA CROREPATI")
            speak("YOU HAVE CHOSEN KAUN BANEGA CROREPATI")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\KBC\KBC.exe")
        elif ST == "D" or ST == "d":
            print("YOU HAVE CHOSEN DE BLOB")
            speak("YOU HAVE CHOSEN DE BLOB")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\DE BLOB\DE BLOB.exe")
        elif ST == "X" or ST == "x":
            print("YOU HAVE CHOSEN DX BALL 2")
            speak("YOU HAVE CHOSEN DX BALL 2")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\31")
        elif ST == "P" or ST == "p":
            print("YOU HAVE CHOSEN PARANORMAL PURSUIT - THE GIFTED ONE")
            speak("YOU HAVE CHOSEN PARANORMAL PURSUIT - THE GIFTED ONE")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\PARANORMAL PURSUIT - THE GIFTED ONE\Game.exe")
        elif ST == "O" or ST == "o":
            print("YOU HAVE CHOSEN HEROES OF HELLAS 3 : ATHENS")
            speak("YOU HAVE CHOSEN HEROES OF HELLAS 3 : ATHENS")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\HEROES OF HELLAS 3 - ATHENS\HOH 3.exe")
        elif ST == "H" or ST == "h":
            print("YOU HAVE CHOSEN HARD HAT III")
            speak("YOU HAVE CHOSEN HARD HAT 3")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\HARD HAT III\Hard Hat 3.exe")
        elif ST == "r" or ST == "R":
            print("YOU HAVE CHOSEN JARDINAINS! ")
            speak("YOU HAVE CHOSEN JARDINAINS! ")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\91")
        elif ST == "T" or ST == "t":
            print("YOU HAVE CHOSEN TEKKEN 3 ")
            speak("YOU HAVE CHOSEN TEKKEN 3 ")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\TEKKEN 3\Tekken_3.exe")
        elif ST == "M" or ST == "m":
            print("YOU HAVE CHOSEN MACHINARIUM - KAO'S ")
            speak("YOU HAVE CHOSEN MACHINARIUM - KAO'S ")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\TEKKEN 3\Tekken_3.exe")
        elif ST == "N" or ST == "n":
            print("YOU HAVE CHOSEN NAMARIEL LEGENDS - IRON LORD COLLECTORS REDITION  ")
            speak("YOU HAVE CHOSEN NAMARIEL LEGENDS - IRON LORD COLLECTORS REDITION  ")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\NAMARIEL LEGEND - IRON LORD COLLECTORS EDITION\Game.exe")
        elif ST == "E" or ST == "e":
            print("YOU HAVE CHOSEN PORTAL OF EVIL - STOLEN RUNES")
            speak("YOU HAVE CHOSEN PORTAL OF EVIL - STOLEN RUNES")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\PORTAL OF EVIL - STOLEN RUNES\Game.exe")
        elif ST == "U" or ST == "u":
            print("YOU HAVE CHOSEN PUZZLE PUPPERS")
            speak("YOU HAVE CHOSEN PUZZLE PUPPERS")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\PUZZLE PUPPERS\PP.exe")
        elif ST == "V" or ST == "v":
            print("YOU HAVE CHOSEN VOID")
            speak("YOU HAVE CHOSEN VOID")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\VOID\game.exe")
        elif ST == "W" or ST == "w":
            print("YOU HAVE CHOSEN WEIRD PARK - SCARY TALES")
            speak("YOU HAVE CHOSEN WEIRD PARK - SCARY TALES")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\WEIRD PARK - SCARY TALES\Game.exe")
        elif ST == "F" or ST == "f":
            print("YOU HAVE CHOSEN FOOTBALL")
            speak("YOU HAVE CHOSEN FOOTBALL")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\FOOTBALL\game.exe")
    elif IN == "C" or IN == "c":
        system("cls")
        print("YOU HAVE CHOSEN COOKING , HIDDEN OBJECTS AND FARMING GAMES CATEGORY \n\n OPENING GAMES MENU FOR THIS CATEGORY")
        speak("YOU HAVE CHOSEN COOKING , HIDDEN OBJECTS AND FARMING GAMES CATEGORY \n\n OPENING GAMES MENU FOR THIS CATEGORY")
        print("\n\n\t\t\t GAMES MENU \n\t CAKE SHOP 3(3) \n\t\t COOKING TRIP(C) \n\t\t\t GARDENSCAPES 2(2) \n\t\t\t\t JANE'S REALTY(J) \n\t\t\t\t\t KATY AND BOB(K) \n\t MAGIC FARM 2(M) \n\n SUB-CAT GAMES : \n\t FARM FRENZY SERIES(F)")
        speak("\n\tPRESS 3 FOR CAKE SHOP 3 \n\t\tC FOR COOKING TRIP\n\t\t\t2 FOR GARDENSCAPES 2\n\t\t\t\tJ FOR JANE'S REALTY\n\t\t\t\t\tK FOR KATY AND BOB\n\tM FOR MAGIC FARM 2\n\n SUB-CAT GAMES : \n\tF FOR FARM FRENZY SERIES\n ENTER YOUR CHOICE")
        ST = input("ENTER YOUR CHOICE: ")
        if ST == "3":
            print("YOU HAVE CHOSEN CAKE SHOP 3")
            speak("YOU HAVE CHOSEN CAKE SHOP 3")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\COOKING , HIDDEN OBJECTS AND FARMING\CAKE SHOP 3\CS3.exe")
        elif ST == "C" or ST == "c":
            print("YOU HAVE CHOSEN COOKING TRIP - BACK ON THE ROAD")
            speak("YOU HAVE CHOSEN COOKING TRIP - BACK ON THE ROAD")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\COOKING , HIDDEN OBJECTS AND FARMING\COOKING TRIP\CT.exe")
        elif ST == "2":
            print("YOU HAVE CHOSEN GARDENSCAPES 2 : MANISON MAKEOVER")
            speak("YOU HAVE CHOSEN GARDENSCAPES 2 : MANISON MAKEOVER")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\COOKING , HIDDEN OBJECTS AND FARMING\GARDENCAPES 2 MANISON MAKEOVER\G2.exe")
        elif ST == "J" or ST == "j":
            print("YOU HAVE CHOSEN JANE'S REALTY")
            speak("YOU HAVE CHOSEN JANE'S REALTY")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\COOKING , HIDDEN OBJECTS AND FARMING\JANE'S REALTY\game.exe")
        elif ST == "K" or ST == "k":
            print("YOU HAVE CHOSEN KATY AND BOB")
            speak("YOU HAVE CHOSEN KATY AND BOB")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\COOKING , HIDDEN OBJECTS AND FARMING\KATY AND BOB\KAB.exe")
        elif ST == "H" or ST == "h":
            print("YOU HAVE CHOSEN MAGIC FARM 2 - FAIRYLAND")
            speak("YOU HAVE CHOSEN MAGIC FARM 2 - FAIRYLAND")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\COOKING , HIDDEN OBJECTS AND FARMING\MAGIC FARM 2 - FAIRYLAND\MF 2.exe")
        elif ST == "F" or ST == "f":
            system("cls")
            print("YOU HAVE CHOSEN FARM FRENZY SERIES \n IT HAS 2 GAMES")
            speak("YOU HAVE CHOSEN FARM FRENZY SERIES \n IT HAS 2 GAMES")
            print("\t\tFF MENU \n FARM FRENZY 2(2) \n\t FARM FRENZY 4(4)")
            speak(
                "\nPRESS 2 FOR FARM FRENZY 2 \n\tPRESS 4 FOR FARM FRENZY 4\nENTER YOUR CHOICE")
            SC = input("ENTER YOUR CHOICE: ")
            if SC == "2":
                print("YOU HAVE CHOSEN FARM FRENZY 2 ")
                speak("YOU HAVE CHOSEN FARM FRENZY 2 ")
                print("LAUNCHING GAME...")
                speak("LAUNCHING GAME...")
                os.startfile(
                    r"E:\DB DRIVE\DB games\COOKING , HIDDEN OBJECTS AND FARMING\FARM FRENZY SEIRES\FARM FRENZY 2\FF2.exe")
            elif SC == "4":
                print("YOU HAVE CHOSEN FARM FRENZY 4")
                speak("YOU HAVE CHOSEN FARM FRENZY 4")
                print("LAUNCHING GAME...")
                speak("LAUNCHING GAME...")
                os.startfile(
                    r"E:\DB DRIVE\DB games\COOKING , HIDDEN OBJECTS AND FARMING\FARM FRENZY SEIRES\FARM FRENZY 4\FF4.exe")
    elif IN == "M" or IN == "m":
        system("cls")
        print(
            "YOU HAVE CHOSEN MULTPLAYER CATEGORY \n\n OPENING GAMES MENU FOR THIS CATEGORY")
        speak(
            "YOU HAVE CHOSEN MULTPLAYER CATEGORY \n\n OPENING GAMES MENU FOR THIS CATEGORY")
        print("\n\n\t\t\t GAMES MENU \n\t AIR FORCE MISSION(A) \n\t\t BATTLE PAINTERS(B) \n\t\t\t BRAWLHALLA(R) \n\t\t\t\t BUG BITS(U) \n\t\t\t\t\t CHICKEN INVADERS 2(C) \n\t\t\t\t\t\t BUNHILATION(N) \n\n\n\t\t\t\t\t DON'T GET ANGRY 3(D) \n\t\t\t\t\t\t\t\t HANDY DANDY(H) \n\t\t\t\t\t\t\t\t\t MARVEL SUPERHEROES(M) \n\t\t\t\t\t\t\t\t\t\t OVERPOWERED(O) \n\t POCKET TANKS(P) \n\t\t POOL PRO(L) \n\t\t\t RISE OF NATIONS(I) \n\t\t\t\t STRATEGY WARGAME COLLECTION(S) \n\t\t\t\t\t BUILDING HORIZON(Z) \n\t\t\t\t\t\t SUPER TUX KART(K)")
        speak("\n\n\t\t\t GAMES MENU \n\t AIR FORCE MISSION(A) \n\t\t BATTLE PAINTERS(B) \n\t\t\t BRAWLHALLA(R) \n\t\t\t\t BUG BITS(U) \n\t\t\t\t\t CHICKEN INVADERS 2(C) \n\t\t\t\t\t\t BUNHILATION(N) \n\n\n\t\t\t\t\t DON'T GET ANGRY 3(D) \n\t\t\t\t\t\t\t\t HANDY DANDY(H) \n\t\t\t\t\t\t\t\t\t MARVEL SUPERHEROES(M) \n\t\t\t\t\t\t\t\t\t\t OVERPOWERED(O) \n\t POCKET TANKS(P) \n\t\t POOL PRO(L) \n\t\t\t RISE OF NATIONS(I) \n\t\t\t\t STRATEGY WARGAME COLLECTION(S) \n\t\t\t\t\t BUILDING HORIZON(Z) \n\t\t\t\t\t\t SUPER TUX KART(K)\n ENTER YOUR CHOICE")
        ST = input("\n\tPRESS A FOR AIR FORCE MISSION\n\t\tB FOR BATTLE PAINTERS\n\t\t\tR FOR BRAWLHALLA\n\t\t\t\tU FOR BUG BITS\n\t\t\t\t\tC FOR CHICKEN INVADERS 2\n\t\t\t\t\t\tN FOR BUNHILATION\n\n\n\t\t\t\t\tD FOR DON'T GET ANGRY 3\n\t\t\t\t\t\t\t\tH FOR HANDY DANDY\n\t\t\t\t\t\t\t\t\tM FOR MARVEL SUPERHEROES\n\t\t\t\t\t\t\t\t\t\tO FOR OVERPOWERED\n\tP FOR POCKET TANKS\n\t\tL FOR POOL PRO\n\t\t\tI FOR RISE OF NATIONS\n\t\t\t\tS FOR STRATEGY WARGAME COLLECTION\n\t\t\t\t\tZ FOR BUILDING HORIZON \n\t\t\t\t\t\tK FOR SUPER TUX KART\n ENTER YOUR CHOICE: ")
        if ST == "A" or ST == "a":
            print("YOU HAVE CHOSEN AIR FORCE MISSION")
            speak("YOU HAVE CHOSEN AIR FORCE MISSION")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\MULTIPLAYER\AIR FORCE MISSION\AFM.exe")
        elif ST == "K" or ST == "k":
            print("YOUR HAVE CHOSEN SUPER TUX KART 1.2.0")
            speak("YOUR HAVE CHOSEN SUPER TUX KART 1.2.0")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\78.exe")
        elif ST == "B" or ST == "b":
            print("YOU HAVE CHOSEN BATTLE PAINTERS")
            speak("YOU HAVE CHOSEN BATTLE PAINTERS")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\MULTIPLAYER\BATTLE PAINTERS\Battle Painters.exe")
        elif ST == "U" or ST == "u":
            print("YOU HAVE CHOSEN BUG BITS")
            speak("YOU HAVE CHOSEN BUG BITS")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\16")
        elif ST == "R" or ST == "r":
            print("YOU HAVE CHOSEN BRAWLHALLA")
            speak("YOU HAVE CHOSEN BRAWLHALLA")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\Steam\steamapps\common\Brawlhalla\Brawlhalla.exe")
        elif ST == "C" or ST == "c":
            print("YOU HAVE CHOSEN CHICKEN INVADERS 2 : THE NEXT WAVE REMASTERED")
            speak("YOU HAVE CHOSEN CHICKEN INVADERS 2 : THE NEXT WAVE REMASTERED")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\MULTIPLAYER\CHICKEN INVADERS 2\CI2.exe")
        elif ST == "N" or ST == "n":
            print("YOU HAVE CHOSEN BUNIHILATION")
            speak("YOU HAVE CHOSEN BUNIHILATION")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\MULTIPLAYER\BUNNIHILATION\Bunnihilation.exe")
        elif ST == "D" or ST == "d":
            print("YOU HAVE CHOSEN DON'T GET ANGRY 3")
            speak("YOU HAVE CHOSEN DON'T GET ANGRY 3")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\29")
        elif ST == "H" or ST == "h":
            print("YOU HAVE CHOSEN HANDY DANDY")
            speak("YOU HAVE CHOSEN HANDY DANDY")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\MULTIPLAYER\BUNNIHILATION\Handy Dandy")
        elif ST == "M" or ST == "m":
            print("YOU HAVE CHOSEN MARVEL SUPERHEROES")
            speak("YOU HAVE CHOSEN MARVEL SUPERHEROES")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\MULTIPLAYER\MARVEL SUPERHEROES\MSH.exe")
        elif ST == "O" or ST == "o":
            print("YOU HAVE CHOSEN OVERPOWERED")
            speak("YOU HAVE CHOSEN OVERPOWERED")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\MULTIPLAYER\OVERPOWERED\Overpowered.exe")
        elif ST == "Z" or ST == "z":
            print("YOU HAVE CHOSEN BUILDING HORIZON")
            speak("YOU HAVE CHOSEN BUILDING HORIZON")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\MULTIPLAYER\BUILDING HORIZON\BH.exe")
        elif ST == "P" or ST == "p":
            print("YOU HAVE CHOSEN POCKET TANKS")
            speak("YOU HAVE CHOSEN POCKET TANKS")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\MULTIPLAYER\POCKET TANKS\pockettanks.exe")
        elif ST == "L" or ST == "l":
            print("YOU HAVE CHOSEN POOL PRO")
            speak("YOU HAVE CHOSEN POOL PRO")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(r"E:\DB DRIVE\DB games\MULTIPLAYER\POOL PRO\PP.exe")
        elif ST == "I" or ST == "i":
            print("YOU HAVE CHOSEN RISE OF NATIONS")
            speak("YOU HAVE CHOSEN RISE OF NATIONS")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\MULTIPLAYER\RISE OF NATIONS\RON.exe")
        elif ST == "S" or ST == "s":
            print("YOU HAVE CHOSEN STRATEGY AND WARGAME COLLECTION")
            speak("YOU HAVE CHOSEN STRATEGY AND WARGAME COLLECTION")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\MULTIPLAYER\STRATEGY WARGAME COLLECTION\S&T.exe")
    elif IN == "R" or IN == "r":
        system("cls")
        print("YOU HAVE CHOSEN RACING GAMES CATEGORY \n\n OPENING GAMES MENU FOR THIS CATEGORY")
        speak("YOU HAVE CHOSEN RACING GAMES CATEGORY \n\n OPENING GAMES MENU FOR THIS CATEGORY")
        print("\n\n\t\t\t GAMES MENU \n\t CARTOON RACER 3D(C) \n\t\t CRAZY CARS(R) \n\t\t\t NEED FOR SPEED MOST WANTED(N) \n\t\t\t\t NITRO RACERS(I) \n\t\t\t\t\t SKY TRACK(S)")
        speak("\n\tPRESS C FOR CARTOON RACER 3D\n\t\tR FOR CRAZY CARS\n\t\t\tN FOR NEED FOR SPEED MOST WANTED\n\t\t\t\tI FOR NITRO RACERS\n\t\t\t\t\tS FOR SKY TRACK\n ENTER YOUR CHOICE")
        ST = input("ENTER YOUR CHOICE: ")
        if ST == "C" or ST == "c":
            print("YOU HAVE CHOSEN CARTOON RACER 3D")
            speak("YOU HAVE CHOSEN CARTOON RACER 3D")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\RACING\CARTOON HOT RACER 3D\Cartoon Hot Racer 3D.exe")
        elif ST == "R" or ST == "r":
            print("YOU HAVE CHOSEN CRAZY CARS")
            speak("YOU HAVE CHOSEN CRAZY CARS")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(r"E:\DB DRIVE\DB games\RACING\CRAZY CARS\CC.exe")
        elif ST == "N" or ST == "n":
            print("YOU HAVE CHOSEN NEED FOR SPEED MOST WANTED")
            speak("YOU HAVE CHOSEN NEED FOR SPEED MOST WANTED")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\RACING\NEED FOR SPEED MOST WANTED\NFS13.exe")
        elif ST == "I" or ST == "i":
            print("YOU HAVE CHOSEN NITRO RACERS")
            speak("YOU HAVE CHOSEN NITRO RACERS")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(r"E:\DB DRIVE\DB games\RACING\NITRO RACERS\NR.exe")
        elif ST == "S" or ST == "s":
            print("YOU HAVE CHOSEN SKY TRACK")
            speak("YOU HAVE CHOSEN SKY TRACK")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\102")
    elif IN == "S" or IN == "s":
        system("cls")
        print("YOU HAVE CHOSEN STRATEGY GAMES CATEGORY \n\n OPENING GAMES MENU FOR THIS CATEGORY")
        speak("YOU HAVE CHOSEN STRATEGY GAMES CATEGORY \n\n OPENING GAMES MENU FOR THIS CATEGORY")
        print("\n\n\t\t\t GAMES MENU \n\t AFTER(A) \n\t\t AGE OF MYTHOLOGY(M) \n\t\t\t ANCIENT ROME 2(N) \n\t\t\t\t BATTLE REALMS DEMO(B) \n\t\t\t\t\t FLYING ISLAND CHRONICLES(F) \n\t\t\t\t\t\t FRONTLINE TACTICS(O) \n\t\t\t\t\t\t\t JACK OF ALL TRIBES(J) \n\t\t\t\t\t\t\t\t LANDGRABBERS(L) \n\t\t\t\t\t\t\t\t\t TOTAL WAR SHOGUN 2(T) \n\t\t\t\t\t\t\t\t\t\t TOY DEFENSE 3(Y) \n\t\t\t\t\t\t\t\t\t\t WARCRAFT III DEMO(W) \n\n SUB-CAT GAMES : \n\t AGE OF EMPIRES SERIES(G)")
        speak("\n\n\t\t\t GAMES MENU \n\t AFTER(A) \n\t\t AGE OF MYTHOLOGY(M) \n\t\t\t ANCIENT ROME 2(N) \n\t\t\t\t BATTLE REALMS DEMO(B) \n\t\t\t\t\t FLYING ISLAND CHRONICLES(F) \n\t\t\t\t\t\t FRONTLINE TACTICS(O) \n\t\t\t\t\t\t\t JACK OF ALL TRIBES(J) \n\t\t\t\t\t\t\t\t LANDGRABBERS(L) \n\t\t\t\t\t\t\t\t\t TOTAL WAR SHOGUN 2(T) \n\t\t\t\t\t\t\t\t\t\t TOY DEFENSE 3(Y) \n\t\t\t\t\t\t\t\t\t\t WARCRAFT III DEMO(W) \n\n SUB-CAT GAMES : \n\t AGE OF EMPIRES SERIES(G) \n ENTER YOUR CHOICE")
        ST = input("\n\tPRESS A FOR AFTER\n\t\tM FOR AGE OF MYTHOLOGY\n\t\t\tN FOR ANCIENT ROME 2\n\t\t\t\tB FOR BATTLE REALMS DEMO\n\t\t\t\t\tF FOR FLYING ISLAND CHRONICLES\n\t\t\t\t\t\tO FOR FRONTLINE TACTICS\n\t\t\t\t\t\t\tJ FOR JACK OF ALL TRIBES\n\t\t\t\t\t\t\t\tL FOR LANDGRABBERS\n\t\t\t\t\t\t\t\t\tT FOR TOTAL WAR SHOGUN 2\n\t\t\t\t\t\t\t\t\t\tY FOR TOY DEFENSE 3\n\t\t\t\t\t\t\t\t\t\tW FOR WARCRAFT III DEMO\n\n SUB-CAT GAMES : \n\tG FOR AGE OF EMPIRES SERIES\n ENTER YOUR CHOICE")
        if ST == "A" or ST == "a":
            print("YOU HAVE CHOSEN AFTER")
            speak("YOU HAVE CHOSEN AFTER")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\68")
        elif ST == "M" or ST == "m":
            print("YOU HAVE CHOSEN AGE OF MYTHOLOGY")
            speak("YOU HAVE CHOSEN AGE OF MYTHOLOGY")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\6")
        elif ST == "B" or ST == "b":
            print("YOU HAVE CHOSEN BATTLE REALMS DEMO")
            speak("YOU HAVE CHOSEN BATTLE REALMS DEMO")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\STRATEGY\BATTLE REALMS\Battle_Realms_Demo.exe")
        elif ST == "F" or ST == "f":
            print("YOU HAVE CHOSEN FLYING ISLAND CHRONICLES")
            speak("YOU HAVE CHOSEN FLYING ISLAND CHRONICLES")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\STRATEGY\FLYING ISLAND CHRONICLES\FIC.exe")
        elif ST == "O" or ST == "o":
            print("YOU HAVE CHOSEN FRONTLINE TACTICS")
            speak("YOU HAVE CHOSEN FRONTLINE TACTICS")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\39")
        elif ST == "J" or ST == "j":
            print("YOU HAVE CHOSEN JACK OF ALL TRIBES")
            speak("YOU HAVE CHOSEN JACK OF ALL TRIBES")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\STRATEGY\JACK OF ALL TRIBES\JOAT.exe")
        elif ST == "L" or ST == "l":
            print("YOU HAVE CHOSEN LANDGRABBERS")
            speak("YOU HAVE CHOSEN LANDGRABBERS")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(r"E:\DB DRIVE\DB games\STRATEGY\LANDGRABBERS\LG.exe")
        elif ST == "T" or ST == "t":
            print("YOU HAVE CHOSEN TOTAL WAR : SHOGUN 2")
            speak("YOU HAVE CHOSEN TOTAL WAR : SHOGUN 2")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\STRATEGY\SHOGUN 2\Total War SHOGUN 2")
        elif ST == "T" or ST == "t":
            print("YOU HAVE CHOSEN TOY DEFENSE 3 : FANTASY")
            speak("YOU HAVE CHOSEN TOY DEFENSE 3 : FANTASY")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\STRATEGY\TOY DEFENSE 3 - FANTASY\TD3.exe")
        elif ST == "T" or ST == "t":
            print("YOU HAVE CHOSEN WARCRAFT III DEMO")
            speak("YOU HAVE CHOSEN WARCRAFT III DEMO")
            print("LAUNCHING GAME...")
            speak("LAUNCHING GAME...")
            os.startfile(
                r"E:\DB DRIVE\DB games\STRATEGY\WARCRAFT III\Warcraft III Demo.exe")
        elif ST == "g" or ST == "G":
            system("cls")
            print("YOU HAVE CHOSEN AGE OF EMPIRES SERIES \n IT HAS 3 GAMES")
            speak("YOU HAVE CHOSEN AGE OF EMPIRES SERIES \n IT HAS 3 GAMES")
            print(
                "\t\tAOE MENU \n AGE OF EMPIRES 1(1) \n\t PRINCE OF PERSIA 2(2) \n\t\t PRINCE OF PERSIA 3(3)")
            speak("\nPRESS 1 FOR AGE OF EMPIRES 1\n\t2 FOR AGE OF EMPIRES 2\n\t\t3 FOR AGE OF EMPIRES 3\nENTER YOUR CHOICE")
            SC = input("ENTER YOUR CHOICE: ")
            if SC == "1":
                print("YOU HAVE CHOSEN AGE OF EMPIRES : RISE OF THE ROME")
                speak("YOU HAVE CHOSEN AGE OF EMPIRES : RISE OF THE ROME")
                print("LAUNCHING GAME...")
                speak("LAUNCHING GAME...")
                os.startfile(
                    r"E:\DB DRIVE\DB games\STRATEGY\AGE OF EMPIRES I\EMPIRESX.exe")
            elif SC == "2":
                print(
                    "YOU HAVE CHOSEN AGE OF EMPIRES II PRESS 1 FOR THE CONQUERERS AND PRESS 2 FOR AGE OF KINGS")
                speak(
                    "YOU HAVE CHOSEN AGE OF EMPIRES II PRESS 1 FOR THE CONQUERERS AND PRESS 2 FOR AGE OF KINGS ENTER YOUR CHOICE")
                NUT = input("ENTER YOUR CHOICE: ")
                print("LAUNCHING GAME...")
                speak("LAUNCHING GAME...")
                if NUT == "1":
                    os.startfile(
                        r"E:\DB DRIVE\DB games\STRATEGY\AGE OF EMPIRES II\EMPIRES2.exe")
                elif NUT == "2":
                    os.startfile(
                        r"E:\DB DRIVE\DB games\STRATEGY\AGE OF EMPIRES II\age2_x1t.exe")
            elif SC == "3":
                print("YOU HAVE CHOSEN AGE OF EMPIRES III")
                speak("YOU HAVE CHOSEN AGE OF EMPIRES III")
                print("LAUNCHING GAME...")
                speak("LAUNCHING GAME...")
                os.startfile(
                    r"E:\DB DRIVE\DB games\STRATEGY\AGE OF EMPIRES III\age3.exe")


def LIST_GAME():
    print("OPENING GAME LIST")
    speak("OPENING GAME LIST")
    os.startfile(r"E:\DB DRIVE\FILES\DOWNLOADS\LIST.docx")


def RAND_GAME():
    system("cls")
    speak("OPENING RANDOM MENU")
    print("\t\tRANDOM MENU")
    print("\tPRESS 1 FOR USER SELECTION \n\tPRESS 2 FOR COMPUTER SELECTION\n")
    speak("PRESS 1 FOR USER SELECTION \nPRESS 2 FOR COMPUTER SELECTION\nENTER YOUR CHOICE")
    RES = input("ENTER YOUR CHOICE : ")
    if RES == "1":
        system("cls")
        speak("ENTER A RANDOM NUMBER FROM 1 TO 135")
        GT = input("ENTER A RANDOM NO. FROM 1 TO 135 : ")
    elif RES == "2":
        GT = random.randint(1, 135)
    else:
        GT = 1000
    ST = str(GT)
    print("CHOOSING RANDOM NO.")
    speak("CHOOSING RANDOM NUMBER")
    speak("YOUR RANDOM NUMBER IS")
    speak(ST)
    system("cls")
    print("YOUR RANDOM NUMBER IS: ", ST)
    if ST == "11":
        print("YOUR RANDOM GAME IS : ASSASSIN'S CREED")
        speak("YOUR RANDOM GAME IS : ASSASSIN'S CREED")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\ASSASSIN'S CREED\Assassin's Creed- Brotherhood.exe")
    elif ST == "70":
        print("YOUR RANDOM GAME IS : ROLLER COASTER TYCOON 3")
        speak("YOUR RANDOM GAME IS : ROLLER COASTER TYCOON 3")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ADVENTURE\ROLLER COASTER TYCOON 3\RCT3.exe")
    elif ST == "26":
        print("YOUR RANDOM GAME IS : COUNTER STRIKE CONDITION ZERO")
        speak("YOUR RANDOM GAME IS : COUNTER STRIKE CONDITION ZERO")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\COUNTER STRIKE CONDITION ZERO\czero.exe")
    elif ST == "59":
        print("YOUR RANDOM GAME IS : HALF LIFE")
        speak("YOUR RANDOM GAME IS : HALF LIFE")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\COUNTER STRIKE CONDITION ZERO\hl.exe")
    elif ST == "92":
        print("YOUR RANDOM GAME IS : LEGO MARVEL")
        speak("YOUR RANDOM GAME IS : LEGO MARVEL")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\LEGO MARVEL\LEGOMarvel.exe")
    elif ST == "66":
        print("YOUR RANDOM GAME IS : PROTOTYPE 2")
        speak("YOUR RANDOM GAME IS : PROTOTYPE 2")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\PROTOTYPE 2\prototype2.exe")
    elif ST == "1":
        print("YOUR RANDOM GAME IS : SCRAP GARDEN")
        speak("YOUR RANDOM GAME IS : SCRAP GARDEN")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ADVENTURE\SCRAP GARDEN SERIES\SCRAP GARDEN\game.exe")
    elif ST == "40":
        print("YOUR RANDOM GAME IS : IRON MAN")
        speak("YOUR RANDOM GAME IS : IRON MAN")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\IRON MAN\GameLauncher.exe")
    elif ST == "90":
        print("YOUR RANDOM GAME IS : THE HULK")
        speak("YOUR RANDOM GAME IS : THE HULK")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\THE HULK\hulk.exe")
    elif ST == "82":
        print("YOUR RANDOM GAME IS : TOMB RAIDER")
        speak("YOUR RANDOM GAME IS : TOMB RAIDER")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\TOMB RAIDER\tra.exe")
    elif ST == "85":
        print("YOUR RANDOM GAME IS : TRANSFORMERS")
        speak("YOUR RANDOM GAME IS : TRANSFORMERS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\85")
    elif ST == "58":
        print("YOUR RANDOM GAME IS : GTA VICE CITY")
        speak("YOUR RANDOM GAME IS : GTA VICE CITY")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\GTA SERIES\GTA VICE CITY\GTA Vice ultimate Trainer.exe")
    elif ST == "60":
        print("YOUR RANDOM GAME IS : PRINCE OF PERSIA 1 : SANDS OF TIME ")
        speak("YOUR RANDOM GAME IS : PRINCE OF PERSIA 1 : SANDS OF TIME ")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\PRINCE OF PERSIA\PRINCE OF PERSIA 1\POP.exe")
    elif ST == "65":
        print("YOUR RANDOM GAME IS : PRINCE OF PERSIA 2 : THE WARRIOR WITHIN")
        speak("YOUR RANDOM GAME IS : PRINCE OF PERSIA 2 : THE WARRIOR WITHIN")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ACTION AND SHOOTING\PRINCE OF PERSIA\PRINCE OF PERSIA 2\POP2.exe")
    elif ST == "34":
        print("YOUR RANDOM GAME IS : PRINCE OF PERSIA 3 : THE TWO THRONES")
        speak("YOUR RANDOM GAME IS : PRINCE OF PERSIA 3 : THE TWO THRONES")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        print("PLEASE HOLD CTRL TO LAUNCH THE GAME")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\34")
        print("                                                                                                                                                                                                                                                                       ")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\34G")
    elif ST == "50":
        print("YOUR RANDOM GAME IS : PROJECT IGI : I'M GOING IN ")
        speak("YOUR RANDOM GAME IS : PROJECT IGI : I'M GOING IN ")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\50")
    elif ST == "93":
        print("YOUR RANDOM GAME IS : PROJECT IGI 2 : COVERT STRIKE")
        speak("YOUR RANDOM GAME IS : PROJECT IGI 2 : COVERT STRIKE")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\93")
    elif ST == "88":
        print("YOUR RANDOM GAME IS : ALEX GORDON")
        speak("YOUR RANDOM GAME IS : ALEX GORDON")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\88")
    elif ST == "23":
        print("YOUR RANDOM GAME IS : CHICKEN INVADERS 3 : REVENGE OF THE YOLK")
        speak("YOUR RANDOM GAME IS : CHICKEN INVADERS 3 : REVENGE OF THE YOLK")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ADVENTURE\CHICKEN INVADERS\CHICKEN INVADERS 3\CI3.exe")
    elif ST == "35":
        print("YOUR RANDOM GAME IS : PIKUNIKU ")
        speak("YOUR RANDOM GAME IS : PIKUNIKU ")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\35")
    elif ST == "103":
        print("YOUR RANDOM GAME IS : CHICKEN INVADERS 4 : ULTIMATE OMELETTE")
        speak("YOUR RANDOM GAME IS : CHICKEN INVADERS 4 : ULTIMATE OMELETTE")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ADVENTURE\CHICKEN INVADERS\CHICKEN INVADERS 4\CI4.exe")
    elif ST == "30":
        print("YOUR RANDOM GAME IS : DUNGEON RIDER")
        speak("YOUR RANDOM GAME IS : DUNGEON RIDER")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ADVENTURE\DUNGEON RIDER\Dungeon Rider.exe")
    elif ST == "74":
        print("YOUR RANDOM GAME IS : SKY RUNNERS")
        speak("YOUR RANDOM GAME IS : SKY RUNNERS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\74")
    elif ST == "76":
        print("YOUR RANDOM GAME IS : SONIC ADVENTURE DEMO")
        speak("YOUR RANDOM GAME IS : SONIC ADVENTURE DEMO")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ADVENTURE\SONIC ADVENTURE\sonic.exe")
    elif ST == "9":
        print("YOUR RANDOM GAME IS : ALONE IN WINTER")
        speak("YOUR RANDOM GAME IS : ALONE IN WINTER")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ADVENTURE\ALONE IN WINTER\engine.exe")
    elif ST == "79":
        print("YOUR RANDOM GAME IS : TARZAN")
        speak("YOUR RANDOM GAME IS : TARZAN")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\ADVENTURE\TARZAN\tarzan.exe")
    elif ST == "73":
        print("YOUR RANDOM GAME IS : SCRAP GARDEN THE DAY BEFORE")
        speak("YOUR RANDOM GAME IS : SCRAP GARDEN THE DAY BEFORE")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\73")
    elif ST == "48":
        print("YOUR RANDOM GAME IS : GTA SAN ANDREAS")
        speak("YOUR RANDOM GAME IS : GTA SAN ANDREAS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ADVENTURE\SCRAP GARDEN SERIES\SCRAP GARDEN\game.exe")
    elif ST == "52":
        print("YOUR RANDOM GAME IS : MARIO FOREVER ")
        speak("YOUR RANDOM GAME IS : MARIO FOREVER ")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ADVENTURE\MARIO\MARIO FOREVER\Mario Forever 5.0.exe")
    elif ST == "53":
        print("YOUR RANDOM GAME IS : MARIO GALAXY ")
        speak("YOUR RANDOM GAME IS : MARIO GALAXY ")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\53")
    elif ST == "57":
        print("YOUR RANDOM GAME IS : NEW MARIO BROS")
        speak("YOUR RANDOM GAME IS : NEW MARIO BROS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ADVENTURE\MARIO\NEW MARIO BROS\New Super Mario Bros.exe")
    elif ST == "96":
        print("YOUR RANDOM GAME IS : POKEMON GLOBAL REVOLUTION")
        speak("YOUR RANDOM GAME IS : POKEMON GLOBAL REVOLUTION")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\96")
    elif ST == "98":
        print("YOUR RANDOM GAME IS : POKEMON MEGA ADVENTURE")
        speak("YOUR RANDOM GAME IS : POKEMON MEGA ADVENTURE")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\98")
    elif ST == "89":
        print("YOUR RANDOM GAME IS : POKEMON URANIUM ")
        speak("YOUR RANDOM GAME IS : POKEMON URANIUM ")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ADVENTURE\POKEMON\POKEMON URANIUM\Uranium.exe")
    elif ST == "13":
        print("YOUR RANDOM GAME IS : BATTLE RANCH ")
        speak("YOUR RANDOM GAME IS : BATTLE RANCH ")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\BATTLE RANCH\BATTLE RANCH.exe")
    elif ST == "20":
        print("YOUR RANDOM GAME IS : CARROM")
        speak("YOUR RANDOM GAME IS : CARROM")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\20")
    elif ST == "94":
        print("YOUR RANDOM GAME IS : KAUN BANEGA CROREPATI")
        speak("YOUR RANDOM GAME IS : KAUN BANEGA CROREPATI")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\KBC\KBC.exe")
    elif ST == "28":
        print("YOUR RANDOM GAME IS : DE BLOB")
        speak("YOUR RANDOM GAME IS : DE BLOB")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\DE BLOB\DE BLOB.exe")
    elif ST == "31":
        print("YOUR RANDOM GAME IS : DX BALL 2")
        speak("YOUR RANDOM GAME IS : DX BALL 2")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\31")
    elif ST == "46":
        print("YOUR RANDOM GAME IS : PARANORMAL PURSUIT - THE GIFTED ONE")
        speak("YOUR RANDOM GAME IS : PARANORMAL PURSUIT - THE GIFTED ONE")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\PARANORMAL PURSUIT - THE GIFTED ONE\Game.exe")
    elif ST == "71":
        print("YOUR RANDOM GAME IS : HEROES OF HELLAS 3 : ATHENS")
        speak("YOUR RANDOM GAME IS : HEROES OF HELLAS 3 : ATHENS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\HEROES OF HELLAS 3 - ATHENS\HOH 3.exe")
    elif ST == "61":
        print("YOUR RANDOM GAME IS : HARD HAT III")
        speak("YOUR RANDOM GAME IS : HARD HAT 3")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\HARD HAT III\Hard Hat 3.exe")
    elif ST == "91":
        print("YOUR RANDOM GAME IS : JARDINAINS! ")
        speak("YOUR RANDOM GAME IS : JARDINAINS! ")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\91")
    elif ST == "80":
        print("YOUR RANDOM GAME IS : TEKKEN 3 ")
        speak("YOUR RANDOM GAME IS : TEKKEN 3 ")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\TEKKEN 3\Tekken_3.exe")
    elif ST == "51":
        print("YOUR RANDOM GAME IS : MACHINARIUM - KAO'S ")
        speak("YOUR RANDOM GAME IS : MACHINARIUM - KAO'S ")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\51")
    elif ST == "55":
        print("YOUR RANDOM GAME IS : NAMARIEL LEGENDS - IRON LORD COLLECTORS EDITION  ")
        speak("YOUR RANDOM GAME IS : NAMARIEL LEGENDS - IRON LORD COLLECTORS EDITION  ")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\NAMARIEL LEGENDS - IRON LORD COLLECTORS EDITION\Game.exe")
    elif ST == "63":
        print("YOUR RANDOM GAME IS : PORTAL OF EVIL - STOLEN RUNES")
        speak("YOUR RANDOM GAME IS : PORTAL OF EVIL - STOLEN RUNES")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\PORTAL OF EVIL - STOLEN RUNES\Game.exe")
    elif ST == "67":
        print("YOUR RANDOM GAME IS : PUZZLE PUPPERS")
        speak("YOUR RANDOM GAME IS : PUZZLE PUPPERS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\PUZZLE PUPPERS\PP.exe")
    elif ST == "86":
        print("YOUR RANDOM GAME IS : VOID")
        speak("YOUR RANDOM GAME IS : VOID")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\VOID\game.exe")
    elif ST == "87":
        print("YOUR RANDOM GAME IS : WEIRD PARK - SCARY TALES")
        speak("YOUR RANDOM GAME IS : WEIRD PARK - SCARY TALES")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\WEIRD PARK - SCARY TALES\Game.exe")
    elif ST == "38":
        print("YOUR RANDOM GAME IS : FOOTBALL")
        speak("YOUR RANDOM GAME IS : FOOTBALL")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\ARCADE AND PUZZLE\FOOTBALL\game.exe")
    elif ST == "19":
        print("YOUR RANDOM GAME IS : CAKE SHOP 3")
        speak("YOUR RANDOM GAME IS : CAKE SHOP 3")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\COOKING , HIDDEN OBJECTS AND FARMING\CAKE SHOP 3\CS3.exe")
    elif ST == "25":
        print("YOUR RANDOM GAME IS : COOKING TRIP - BACK ON THE ROAD")
        speak("YOUR RANDOM GAME IS : COOKING TRIP - BACK ON THE ROAD")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\COOKING , HIDDEN OBJECTS AND FARMING\COOKING TRIP\CT.exe")
    elif ST == "43":
        print("YOUR RANDOM GAME IS : GARDENSCAPES 2 : MANISON MAKEOVER")
        speak("YOUR RANDOM GAME IS : GARDENSCAPES 2 : MANISON MAKEOVER")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\COOKING , HIDDEN OBJECTS AND FARMING\GARDENCAPES 2 MANISON MAKEOVER\G2.exe")
    elif ST == "42":
        print("YOUR RANDOM GAME IS : JANE'S REALTY")
        speak("YOUR RANDOM GAME IS : JANE'S REALTY")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\42")
    elif ST == "47":
        print("YOUR RANDOM GAME IS : KATY AND BOB")
        speak("YOUR RANDOM GAME IS : KATY AND BOB")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\COOKING , HIDDEN OBJECTS AND FARMING\KATY AND BOB\KAB.exe")
    elif ST == "37":
        print("YOUR RANDOM GAME IS : MAGIC FARM 2 - FAIRYLAND")
        speak("YOUR RANDOM GAME IS : MAGIC FARM 2 - FAIRYLAND")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\COOKING , HIDDEN OBJECTS AND FARMING\MAGIC FARM 2 - FAIRYLAND\MF 2.exe")
    elif ST == "32":
        print("YOUR RANDOM GAME IS : FARM FRENZY 2 ")
        speak("YOUR RANDOM GAME IS : FARM FRENZY 2 ")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\COOKING , HIDDEN OBJECTS AND FARMING\FARM FRENZY SEIRES\FARM FRENZY 2\FF2.exe")
    elif ST == "33":
        print("YOUR RANDOM GAME IS : FARM FRENZY 4")
        speak("YOUR RANDOM GAME IS : FARM FRENZY 4")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\COOKING , HIDDEN OBJECTS AND FARMING\FARM FRENZY SEIRES\FARM FRENZY 4\FF4.exe")
    elif ST == "7":
        print("YOUR RANDOM GAME IS : AIR FORCE MISSION")
        speak("YOUR RANDOM GAME IS : AIR FORCE MISSION")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\MULTIPLAYER\AIR FORCE MISSION\AFM.exe")
    elif ST == "12":
        print("YOUR RANDOM GAME IS : BATTLE PAINTERS")
        speak("YOUR RANDOM GAME IS : BATTLE PAINTERS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\MULTIPLAYER\BATTLE PAINTERS\Battle Painters.exe")
    elif ST == "16":
        print("YOUR RANDOM GAME IS : BUG BITS")
        speak("YOUR RANDOM GAME IS : BUG BITS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\16")
    elif ST == "100":
        print("YOUR RANDOM GAME IS : POCKET TANKS")
        speak("YOUR RANDOM GAME IS : POCKET TANKS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\MULTIPLAYER\POCKET TANKS\pockettanks.exe")
    elif ST == "15":
        print("YOUR RANDOM GAME IS : BRAWLHALLA")
        speak("YOUR RANDOM GAME IS : BRAWLHALLA")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\Steam\steamapps\common\Brawlhalla\Brawlhalla.exe")
    elif ST == "22":
        print("YOUR RANDOM GAME IS : CHICKEN INVADERS 2 : THE NEXT WAVE REMASTERED")
        speak("YOUR RANDOM GAME IS : CHICKEN INVADERS 2 : THE NEXT WAVE REMASTERED")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\MULTIPLAYER\CHICKEN INVADERS 2\CI2.exe")
    elif ST == "18":
        print("YOUR RANDOM GAME IS : BUNIHILATION")
        speak("YOUR RANDOM GAME IS : BUNIHILATION")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\MULTIPLAYER\BUNNIHILATION\Bunnihilation.exe")
    elif ST == "29":
        print("YOUR RANDOM GAME IS : DON'T GET ANGRY 3")
        speak("YOUR RANDOM GAME IS : DON'T GET ANGRY 3")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\29")
    elif ST == "64":
        print("YOUR RANDOM GAME IS : HANDY DANDY")
        speak("YOUR RANDOM GAME IS : HANDY DANDY")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\MULTIPLAYER\BUNNIHILATION\Handy Dandy")
    elif ST == "54":
        print("YOUR RANDOM GAME IS : MARVEL SUPERHEROES")
        speak("YOUR RANDOM GAME IS : MARVEL SUPERHEROES")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\54")
    elif ST == "45":
        print("YOUR RANDOM GAME IS : OVERPOWERED")
        speak("YOUR RANDOM GAME IS : OVERPOWERED")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\MULTIPLAYER\OVERPOWERED\Overpowered.exe")
    elif ST == "17":
        print("YOUR RANDOM GAME IS : BUILDING HORIZON")
        speak("YOUR RANDOM GAME IS : BUILDING HORIZON")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\MULTIPLAYER\BUILDING HORIZON\BH.exe")
    elif ST == "R":
        print("YOUR RANDOM GAME IS : POCKET TANKS")
        speak("YOUR RANDOM GAME IS : POCKET TANKS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\MULTIPLAYER\POCKET TANKS\pockettanks.exe")
    elif ST == "62":
        print("YOUR RANDOM GAME IS : POOL PRO")
        speak("YOUR RANDOM GAME IS : POOL PRO")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\MULTIPLAYER\POOL PRO\PP.exe")
    elif ST == "69":
        print("YOUR RANDOM GAME IS : RISE OF NATIONS")
        speak("YOUR RANDOM GAME IS : RISE OF NATIONS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\MULTIPLAYER\RISE OF NATIONS\RON.exe")
    elif ST == "77":
        print("YOUR RANDOM GAME IS : STRATEGY AND WARGAME COLLECTION")
        speak("YOUR RANDOM GAME IS : STRATEGY AND WARGAME COLLECTION")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\MULTIPLAYER\STRATEGY WARGAME COLLECTION\S&T.exe")
    elif ST == "21":
        print("YOUR RANDOM GAME IS : CARTOON RACER 3D")
        speak("YOUR RANDOM GAME IS : CARTOON RACER 3D")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\RACING\CARTOON HOT RACER 3D\Cartoon Hot Racer 3D.exe")
    elif ST == "27":
        print("YOUR RANDOM GAME IS : CRAZY CARS")
        speak("YOUR RANDOM GAME IS : CRAZY CARS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\RACING\CRAZY CARS\CC.exe")
    elif ST == "56":
        print("YOUR RANDOM GAME IS : NEED FOR SPEED MOST WANTED")
        speak("YOUR RANDOM GAME IS : NEED FOR SPEED MOST WANTED")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\56")
    elif ST == "44":
        print("YOUR RANDOM GAME IS : NITRO RACERS")
        speak("YOUR RANDOM GAME IS : NITRO RACERS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\44")
    elif ST == "102":
        print("YOUR RANDOM GAME IS : SKY TRACK")
        speak("YOUR RANDOM GAME IS : SKY TRACK")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\102")
    elif ST == "68":
        print("YOUR RANDOM GAME IS : AFTER")
        speak("YOUR RANDOM GAME IS : AFTER")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\68")
    elif ST == "6":
        print("YOUR RANDOM GAME IS : AGE OF MYTHOLOGY")
        speak("YOUR RANDOM GAME IS : AGE OF MYTHOLOGY")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\6")
    elif ST == "14":
        print("YOUR RANDOM GAME IS : BATTLE REALMS DEMO")
        speak("YOUR RANDOM GAME IS : BATTLE REALMS DEMO")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\STRATEGY\BATTLE REALMS\Battle_Realms_Demo.exe")
    elif ST == "36":
        print("YOUR RANDOM GAME IS : FLYING ISLAND CHRONICLES")
        speak("YOUR RANDOM GAME IS : FLYING ISLAND CHRONICLES")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\36")
    elif ST == "39":
        print("YOUR RANDOM GAME IS : FRONTLINE TACTICS")
        speak("YOUR RANDOM GAME IS : FRONTLINE TACTICS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\39")
    elif ST == "41":
        print("YOUR RANDOM GAME IS : JACK OF ALL TRIBES")
        speak("YOUR RANDOM GAME IS : JACK OF ALL TRIBES")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\STRATEGY\JACK OF ALL TRIBES\Wrapgame.exe")
    elif ST == "49":
        print("YOUR RANDOM GAME IS : LANDGRABBERS")
        speak("YOUR RANDOM GAME IS : LANDGRABBERS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\49")
    elif ST == "83":
        print("YOUR RANDOM GAME IS : TOTAL WAR : SHOGUN 2")
        speak("YOUR RANDOM GAME IS : TOTAL WAR : SHOGUN 2")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\STRATEGY\SHOGUN 2\Total War SHOGUN 2")
    elif ST == "84":
        print("YOUR RANDOM GAME IS : TOY DEFENSE 3 : FANTASY")
        speak("YOUR RANDOM GAME IS : TOY DEFENSE 3 : FANTASY")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\STRATEGY\TOY DEFENSE 3 - FANTASY\TD3.exe")
    elif ST == "81":
        print("YOUR RANDOM GAME IS : WARCRAFT III DEMO")
        speak("YOUR RANDOM GAME IS : WARCRAFT III DEMO")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\STRATEGY\WARCRAFT III\Warcraft III Demo.exe")
    elif ST == "2":
        print("YOUR RANDOM GAME IS : AGE OF EMPIRES : RISE OF THE ROME")
        speak("YOUR RANDOM GAME IS : AGE OF EMPIRES : RISE OF THE ROME")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\2")
    elif ST == "3":
        print("YOUR RANDOM GAME IS : AGE OF EMPIRES 2 : THE CONQUERER DEMO")
        speak("YOUR RANDOM GAME IS : AGE OF EMPIRES 2 : THE CONQUERER DEMO")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\STRATEGY\AGE OF EMPIRES II\EMPIRES2.exe")
    elif ST == "4":
        print("YOUR RANDOM GAME IS : AGE OF EMPIRES 2 : THE AGE OF KINGS DEMO")
        speak("YOUR RANDOM GAME IS : AGE OF EMPIRES 2 : THE AGE OF KINGS DEMO")
        print("LAUNCHING GAME")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\STRATEGY\AGE OF EMPIRES II\age2_x1t.exe")
    elif ST == "5":
        print("YOUR RANDOM GAME IS : AGE OF EMPIRES III DEMO")
        speak("YOUR RANDOM GAME IS : AGE OF EMPIRES III DEMO")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(
            r"E:\DB DRIVE\DB games\STRATEGY\AGE OF EMPIRES III\age3.exe")
    elif ST == "97":
        speak("NO RANDOM GAME")
        print("NO RANDOM GAME")
        os.startfile(r"E:\DB DRIVE\FILES\DOWNLOADS\97.docx")
    elif ST == "10":
        speak("NO RANDOM GAME")
        print("NO RANDOM GAME")
        os.startfile(r"E:\DB DRIVE\FILES\DOWNLOADS\97.docx")
    elif ST == "101":
        speak("NO RANDOM GAME")
        print("NO RANDOM GAME")
        os.startfile(r"E:\DB DRIVE\FILES\DOWNLOADS\97.docx")
    elif ST == "72":
        print("YOUR RANDOM GAME IS : 20XX")
        speak("YOUR RANDOM GAME IS : 20XX")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\72")
    elif ST == "75":
        speak("NO RANDOM GAME")
        print("NO RANDOM GAME")
        os.startfile(r"E:\DB DRIVE\FILES\DOWNLOADS\97.docx")
    elif ST == "99":
        speak("NO RANDOM GAME")
        print("NO RANDOM GAME")
        os.startfile(r"E:\DB DRIVE\FILES\DOWNLOADS\97.docx")
    elif ST == "24":
        speak("NO RANDOM GAME")
        print("NO RANDOM GAME")
        os.startfile(r"E:\DB DRIVE\FILES\DOWNLOADS\97.docx")
    elif ST == "75":
        speak("NO RANDOM GAME")
        print("NO RANDOM GAME")
        os.startfile(r"E:\DB DRIVE\FILES\DOWNLOADS\97.docx")
    elif ST == "78":
        print("YOUR RANDOM GAME IS : SUPER TUX KART 1.2.0")
        speak("YOUR RANDOM GAME IS : SUPER TUX KART 1.2.0")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\78")
    elif ST == "104":
        print("YOUR RANDOM GAME IS : ANCIENT ROME")
        speak("YOUR RANDOM GAME IS : ANCIENT ROME")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\104")
    elif ST == "105":
        speak("NO RANDOM GAME")
        print("NO RANDOM GAME")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\105")
    elif ST == "106":
        print("YOUR RANDOM GAME IS : NAISSANCE")
        speak("YOUR RANDOM GAME IS : NAISSANCE")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\106")
    elif ST == "108":
        print("YOUR RANDOM GAME IS : KINGDOM")
        speak("YOUR RANDOM GAME IS : KINGDOM")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\108")
    elif ST == "109":
        print("YOUR RANDOM GAME IS : TOTEMORI")
        speak("YOUR RANDOM GAME IS : TOTEMORI")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\109")
    elif ST == "110":
        print("YOUR RANDOM GAME IS : COMMAND ANT CONQUER")
        speak("YOUR RANDOM GAME IS : COMMAND ANT CONQUER")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\110")
    elif ST == "8":
        speak("NO RANDOM GAME")
        print("NO RANDOM GAME")
        os.startfile(r"E:\DB DRIVE\FILES\DOWNLOADS\97.docx")
    elif ST == "111":
        print("YOUR RANDOM GAME IS : DON'T BITE ME BRO !")
        speak("YOUR RANDOM GAME IS : DON'T BITE ME BRO !")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\111")
    elif ST == "112":
        print("YOUR RANDOM GAME IS : DRAGON BALL ARCADE")
        speak("YOUR RANDOM GAME IS : DRAGON BALL ARCADE")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\112")
    elif ST == "113":
        print("YOUR RANDOM GAME IS : DYO")
        speak("YOUR RANDOM GAME IS : DYO")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\113")
    elif ST == "114":
        print("YOUR RANDOM GAME IS : SUPER CLASH BROS")
        speak("YOUR RANDOM GAME IS : SUPER CLASH BROS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\114")
    elif ST == "115":
        print("YOUR RANDOM GAME IS : DRAGON BALL Z SAGAS")
        speak("YOUR RANDOM GAME IS : DRAGON BALL ZEE SAGAS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\115")
    elif ST == "116":
        print("YOUR RANDOM GAME IS : EGGNOG PLUS")
        speak("YOUR RANDOM GAME IS : EGGNOG PLUS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\116")
    elif ST == "117":
        print("YOUR RANDOM GAME IS : SUPER TOY CARS")
        speak("YOUR RANDOM GAME IS : SUPER TOY CARS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\117")
    elif ST == "118":
        print("YOUR RANDOM GAME IS : HYPER DRAGON BALL Z")
        speak("YOUR RANDOM GAME IS : HYPER DRAGON BALL ZEE")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\118")
    elif ST == "119":
        print("YOUR RANDOM GAME IS : JUST ME AND ONLY ME AGAINST THE WORLD")
        speak("YOUR RANDOM GAME IS : JUST ME AND ONLY ME AGAINST THE WORLD")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\119")
    elif ST == "120":
        print("YOUR RANDOM GAME IS : KEY CARS")
        speak("YOUR RANDOM GAME IS : KEY CARS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\120")
    elif ST == "121":
        print("YOUR RANDOM GAME IS : KNIGHT CLUB")
        speak("YOUR RANDOM GAME IS : KNIGHT CLUB")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\121")
    elif ST == "125":
        print("YOUR RANDOM GAME IS : NEVER APART")
        speak("YOUR RANDOM GAME IS : NEVER APART")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\125")
    elif ST == "123":
        print("YOUR RANDOM GAME IS : ADVENTURE MACHINE")
        speak("YOUR RANDOM GAME IS : ADVENTURE MACHINE")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\123")
    elif ST == "124":
        print("YOUR RANDOM GAME IS : SUPER PILOT")
        speak("YOUR RANDOM GAME IS : SUPER PILOT")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\124")
    elif ST == "122":
        speak("NO RANDOM GAME")
        print("NO RANDOM GAME")
        os.startfile(r"E:\DB DRIVE\FILES\DOWNLOADS\97.docx")
    elif ST == "126":
        print("YOUR RANDOM GAME IS : SUPERHEROES 2000")
        speak("YOUR RANDOM GAME IS : SUPERHEROES 2000")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\126")
    elif ST == "107":
        print("YOUR RANDOM GAME IS : ISLAND SAVER")
        speak("YOUR RANDOM GAME IS : ISLAND SAVER")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\107")
    elif ST == "127":
        print("YOUR RANDOM GAME IS : COSTUME QUEST 2")
        speak("YOUR RANDOM GAME IS : COSTUME QUEST 2")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\127")
    elif ST == "130":
        print("YOUR RANDOM GAME IS : GAME OF LIFE")
        speak("YOUR RANDOM GAME IS : GAME OF LIFE")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\130")
    elif ST == "128":
        print("YOUR RANDOM GAME IS : ATTACK ON TOYS")
        speak("YOUR RANDOM GAME IS : ATTACK ON TOYS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\128")
    elif ST == "129":
        print("YOUR RANDOM GAME IS : PLANTS VS ZOMBIES")
        speak("YOUR RANDOM GAME IS : PLANTS VS ZOMBIES")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\129")
    elif ST == "131":
        print("YOUR RANDOM GAME IS : ULTIMATE MARVEL VS CAPCOM 3")
        speak("YOUR RANDOM GAME IS : ULTIMATE MARVEL VS CAPCOM 3")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\131")
    elif ST == "132":
        print("YOUR RANDOM GAME IS : HALO COMBAT EVOLVED")
        speak("YOUR RANDOM GAME IS : HALO COMBAT EVOLVED")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\132")
    elif ST == "133":
        print("YOUR RANDOM GAME IS : DORAEMON STORY OF SEASONS")
        speak("YOUR RANDOM GAME IS : DORAEMON STORY OF SEASONS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\133")
    elif ST == "134":
        print("YOUR RANDOM GAME IS : FREEDOM FIGHTERS")
        speak("YOUR RANDOM GAME IS : FREEDOM FIGHTERS")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\134")
    elif ST == "135":
        print("YOUR RANDOM GAME IS : DE BLOB 2")
        speak("YOUR RANDOM GAME IS : DE BLOB 2")
        print("LAUNCHING GAME...")
        speak("LAUNCHING GAME...")
        os.startfile(r"E:\DB DRIVE\DB games\Z FOLDER\135")
    else:
        print("WRONG INPUT , ERROR !!!!")
        speak("WRONG INPUT , ERROR !!!!")


if __name__ == "__main__":
    print("\t\t\tTHIS PROGRAM IS CREATED BY DK\n\n\n")
    speak("\t\t\tTHIS PROGRAM IS CREATED BY DK\n\n\n")
    QU = "n"
    XU = "n"
    while QU == "N" or QU == "n":
        system("cls")
        print("\t\tGAME MENU \n\n\tRANDOM GAME(R) \n\n\t CATEGORY GAMES(C) \n\n\t  GAMES LIST(G)")
        speak("OPENING GAME MENU \n\tPRESS R FOR RANDOM GAME, \n\t\tPRESS C FOR CATEGORY GAMES,\n\t\t\tPRESS G FOR GAMES LIST,\n ENTER YOUR CHOICE")
        PU = input("\n\nENTER YOUR CHOICE: ")
        if PU == "C" or PU == "c":
            CAT_GAME()
        elif PU == "G" or PU == "g":
            LIST_GAME()
        elif PU == "R" or PU == "r":
            while XU == "n" and QU == "n" or XU == "N" and QU == "N" or QU == "N" and XU == "n" or QU == "n" and XU == "N":
                RAND_GAME()
                XU = input("WANT TO EXIT RANDOM MENU ?(Y/N) :")
        else:
            speak("YOU HAVE ENTERED WRONG INPUT : ERROR!!!")
            print("YOU HAVE ENTERED WRONG INPUT : ERROR!!!")
        speak("WANT TO QUIT MAIN MENU ? YES OR NO :")
        QU = input("WANT TO QUIT MAIN MENU ?(Y/N) :")
    speak("EXITING PROGRAM \n BYE")
