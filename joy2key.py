import keyboard
#import uinput
#import time

from inputs import get_gamepad

def main():
    while 1:
        events = get_gamepad()
        for event in events:
            #keyboard.press_and_release('enter')
            if event.code == "ABS_X" and event.state > 127:
                #print ("right")
                keyboard.press_and_release('right')

            if event.code == "ABS_X" and event.state < 127:
                #print ("left")
                keyboard.press_and_release('left')

            if event.code == "ABS_Y" and event.state > 127:
                #print ("down")
                keyboard.press_and_release('down')

            if event.code == "ABS_Y" and event.state < 127:
                keyboard.press_and_release('up')
                #print ("up")

            if event.code == "BTN_THUMB2" and event.state > 0:
                keyboard.press_and_release('enter')
                #print ("SNES B")
                exit()

            if event.code == "BTN_THUMB" and event.state > 0:
                print ("SNES A")
            if event.code == "BTN_TOP" and event.state > 0:
                print ("SNES Y")
            if event.code == "BTN_TOP2" and event.state > 0:
                print ("SNES L")
            if event.code == "BTN_TRIGGER" and event.state > 0:
                print ("SNES X")
            if event.code == "BTN_BASE" and event.state > 0:
                print ("SNES R")
            if event.code == "BTN_BASE3" and event.state > 0:
                print ("SNES SELECT")
            if event.code == "BTN_BASE4" and event.state > 0:
                print ("SNES START")

            #print ("Code: " + event.code)
            #print ("State: ") 
            #print (event.state)


if __name__=="__main__":
    main()
