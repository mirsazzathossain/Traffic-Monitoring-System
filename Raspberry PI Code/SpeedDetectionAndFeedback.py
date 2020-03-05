#libraries
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER_ONE = 18
GPIO_ECHO_ONE = 24
GPIO_TRIGGER_TWO = 23
GPIO_ECHO_TWO = 16

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER_ONE, GPIO.OUT)
GPIO.setup(GPIO_ECHO_ONE, GPIO.IN)
GPIO.setup(GPIO_TRIGGER_TWO, GPIO.OUT)
GPIO.setup(GPIO_ECHO_TWO, GPIO.IN)

def distance_one():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER_ONE, True)
    
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_ONE, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO_ONE) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO_ONE) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    
    return distance


def distance_two():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER_TWO, True)
    
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_TWO, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO_TWO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO_TWO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    
    return distance


if __name__ == '__main__':
    try:
        while True:
            dist_one = distance_one()
            
            if dist_one<25:
                StartTime = time.time()
                
                while True:
                    dist_two = distance_two()
                    
                    if dist_two < 25:
                        StopTime = time.time()
                        print("Speed is %.1f cm/sec." %(15/(StopTime-StartTime)))
                        break
                    
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
        

