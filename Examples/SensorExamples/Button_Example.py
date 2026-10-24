# Created by Aayush Iyengar on behalf on the ENGR 16X Teaching Team

# More info and instruction on using this sensor can be found in the basehat folder
# on your Pi's Desktop 

from basehat import Button  # Import the simplified Button class
import time
#connecting with the button for the button connected in pin 5 (this is customizable below)

def on_press():
    #Callback function for button press event
    print('Button is pressed')

def on_release():
    #Callback function for button release event
    print("Button is released")

def main():
    #Main function
    pin = 5  #Assuming pin 5 for the Button
    button = Button(pin)  #Create a Button instance

    #Assign the callback functions to the button instance
    button.when_pressed = on_press
    button.when_released = on_release
    try:
        #Main loop to continuously check button state
        while True:
            try:
                print("Button Value: {}".format(button.value))
                #The button events will trigger the callback functions
                time.sleep(1)
            except IOError:
                print ("\nError occurred while attempting to read values.")
                break
            
    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting...")

if __name__ == '__main__':
    main()
