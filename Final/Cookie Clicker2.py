import time
import threading

totalcookies = 0
oven = 0

def cps():
    global totalcookies
    while oven > 0:
        totalcookies = 1 + totalcookies
        print(totalcookies)
        time.sleep(3)

def shop():
    global oven
    global totalcookies
    while True:
        buysell = input("Welcome to the building shop! Here you can buy buildings with your cookies to create cookies for you!These are the buildings we have to offer: \nOven (0.3cps) - 10 cookies \nType buy (building name) to purchase a building: ")
        if buysell == ("buy oven"):
            if totalcookies >= 10:
                print("You have bought 1 oven")
                oven = oven + 1
                totalcookies = totalcookies - 10
                cps_thread = threading.Thread(target=cps)
                cps_thread.start()
                break
            else:
                print("You do not have enough cookies")
        elif buysell == ("buy kitchen"):
            pass
        elif buysell == ("home"):
            print("Returning to home")
            break
        else:
            print("Invalid input")


def main():
    global totalcookies
    global oven

    print("Welcome to Cookie Clicker! Press enter to generate a Cookie! \nType \"help\" if you need help")

    # Start the cps thread in the background

    while True:

        interact = input()
        if interact == (""):
            totalcookies = 1 + totalcookies
            print(totalcookies)
        elif interact == ("help"):
            print("Press enter to generate a cookie \ntype help for help \ntype shop for the shop \ntype upgrade for the upgrade shop \ntype total for total amount of cookies \ntype cps for your cookies per second \ntype home to go back to the main page \ntype buildings to see how many of each building you have")
        elif interact == ("shop"):
            shop()
        elif interact == ("upgrade"):
            pass
        elif interact == ("total"):
            print("You have", totalcookies, "cookies!")
        elif interact == ("cps"):
            pass  # You can add functionality here if needed
        elif interact == ("buildings"):
            print("Ovens:", oven)
        else:
            print("Invalid input")


# Run the main program
main()
