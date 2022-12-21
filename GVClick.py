import mouse
import time
from os import system

def getCallButtonLocation():
    getCallButtonLocation = input("Hover mouse over call button and press 'a' \n" )
    if getCallButtonLocation == 'a':
        setCallButtonLocation = mouse.get_position()
        print("Call Button at " + str(setCallButtonLocation[0]) + " " + str(setCallButtonLocation[1]))
    else:
        system("cls")
        print("try again.")
        getCallButtonLocation()
    return setCallButtonLocation

def getEndButtonLocation():   
    getEndButtonLoc = input("Hover mouse over end button and press 'a' \n")
    if getEndButtonLoc == 'a':
        setEndButtonLocation = mouse.get_position()
        print("End button at " + str(setEndButtonLocation[0]) + " " + str(setEndButtonLocation[1]))
    else:
        system("cls")
        print("try again.")
        getEndButtonLocation()
    return setEndButtonLocation

def setCallRingTime():
    ringTime = input("How long would you like the phone to ring in seconds? (15 - 30 is recommended) \n")
    ringTime = int(ringTime)
    return ringTime

def setCallNumber():    
    numberOfCalls = input("How many times would you like to call? (use numbers only) \n")
    numberOfCalls = int(numberOfCalls)
    return numberOfCalls

def setWaitBetweenCalls():
    waitBetweenCalls = input("How long would you like to wait between phone calls? (give it something between 3 and 10) \n")
    waitBetweenCalls = int(waitBetweenCalls)
    return waitBetweenCalls


callButton = getCallButtonLocation()
endButton = getCallButtonLocation()
ringTime = setCallRingTime()
numberOfCalls = setCallNumber()
waitBetweenCalls = setWaitBetweenCalls()
totalCalls = numberOfCalls
incrementer = 0

system('cls')

while numberOfCalls >= 0:
    incrementer = incrementer + 1
    print("Call number " + str(incrementer) + " of " + str(totalCalls) + "\n")
    print("Press 'ctrl+c' at any time to stop this script..." + "\n")
    mouse.move(callButton[0], callButton[1])
    mouse.click('left')
    time.sleep(ringTime)
    mouse.move(endButton[0], endButton[1])
    mouse.click('left')
    # print("Call number " + str(numberOfCalls))
    numberOfCalls = numberOfCalls - 1
    time.sleep(5)
    system('cls')