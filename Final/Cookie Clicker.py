import time
import threading

totalcookies = 0
oven = 0
kitchen = 0
persec = 0

def cps():
    global totalcookies
    while oven > 0:
        totalcookies = 1 + totalcookies
        print(totalcookies)
        time.sleep(3)

    while kitchen > 0:
        totalcookies = 15 + totalcookies
        print(totalcookies)
        time.sleep(5)

def shop():
    global oven
    global totalcookies
    global kitchen
    global persec
    while True:
        buysell = input("Welcome to the building shop! Here you can buy buildings with your cookies to create cookies for you! These are the buildings we have to offer: \nOven (0.3cps) - 10 cookies \nKitchen (1.5cps) - 100 cookies \nType buy (building name) to purchase a building: ").lower()
        if buysell == ("buy oven"):
            if totalcookies >= 10:
                print("You have bought 1 oven")
                oven = oven + 1
                persec = persec + 0.3
                totalcookies = totalcookies - 10
                cps_thread = threading.Thread(target=cps)
                cps_thread.start()
                break
            else:
                print("You do not have enough cookies")
        elif buysell == ("buy kitchen"):
            if totalcookies >= 100:
                print("You have bought 1 kitchen")
                kitchen = kitchen + 1
                persec = persec + 1.5
                totalcookies = totalcookies - 100
                cps_thread = threading.Thread(target=cps)
                cps_thread.start()
                break
        elif buysell == ("home"):
            print("Returning to home")
            break
        else:
            print("Invalid input")

def main():
    global totalcookies
    global oven
    global kitchen
    global persec

    print("Welcome to Cookie Clicker! Press enter to generate a Cookie! \nType \"help\" if you need help")


    while True:

        interact = input().lower()
        if interact == (""):
            totalcookies = 1 + totalcookies
            print(totalcookies)
        elif interact == ("help"):
            print("Press enter to generate a cookie \ntype help for help \ntype shop for the shop \ntype total for total amount of cookies \ntype cps for your cookies per second\ntype home to go back to the main page \ntype buildings to see how many of each building you have")
        elif interact == ("shop"):
            shop()
        elif interact == ("total"):
            print("You have", totalcookies, "cookies!")
        elif interact == ("cps"):
            print("You are generating", persec, "cookies per second!")
        elif interact == ("buildings"):
            print("Ovens:", oven)
            print("Kitchens:", kitchen)
        else:
            print("Invalid input")



main()
