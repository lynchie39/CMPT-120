#if you don't know how to play blackjack, tbh not super important but look it up anyway LOL
#this script is going to require some googling: I want you to practice using your resources with this one. But of course if you get stuck, reach out :)
'''instructions: randomly generate three values between 1 and 11. in the function bust: add these three numbers together. if they add up to or less than 21, return the sum. If it's over 21, return 0. If it's over 21 BUT there's an 11 as one of the values, return the sum - 10. '''

import random

def bust():
    print(threecards)
    total = sum(threecards)
    if total <= 21:
        return total
    elif 11 in threecards:
        return total - 10
    elif total > 21:
        return 0


    
def main():
    global threecards
    threecards = [random.randint(1, 11) for x in range(3)]
    print(bust())

main()
