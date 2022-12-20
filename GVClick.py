import mouse
import time
from os import system

def getCallButtonLocation():
    getCallButtonLocation = input("Hover mouse over call button and press 'a' " )
    if getCallButtonLocation == 'a':
        setCallButtonLocation = mouse.get_position()
        print("Call Button at " + str(setCallButtonLocation[0]) + " " + str(setCallButtonLocation[1]))
    else:
        print("try again.")
        getCallButtonLocation()
    return setCallButtonLocation

def getEndButtonLocation():   
    getEndButtonLoc = input("Hover mouse over end button and press 'a' ")
    if getEndButtonLoc == 'a':
        setEndButtonLocation = mouse.get_position()
        print("End button at " + str(setEndButtonLocation[0]) + " " + str(setEndButtonLocation[1]))
    else:
        print("try again.")
        getEndButtonLocation()
    return setEndButtonLocation
    
callButton = getCallButtonLocation()
endButton = getCallButtonLocation()

callTimes = input("How many times would you like to call? (use numbers only) ")
callTimes = int(callTimes)

while callTimes >= 0:
    print("Call number " + str(callTimes) + "\n")
    print("Press 'ctrl+c' at any time to stop this script..." + "\n")
    mouse.move(callButton[0], callButton[1])
    mouse.click('left')
    mouse.move(endButton[0], endButton[1])
    time.sleep(35)
    mouse.click('left')
    print("Call number " + str(callTimes))
    callTimes = callTimes - 1
    time.sleep(5)
    system('cls')