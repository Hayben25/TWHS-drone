from codrone_edu.drone import *


def validColors(front,back):
    if (front == back) and (front == "Red" or front == "Blue" or front == "Green"):
        return True
    else:
        return False


def forward(x):  # forward 1 - 18-19 inches. use 0.1 for stabilization
    drone.set_yaw(0)
    drone.set_roll(0)
    drone.set_pitch(50)
    drone.move(x)
    drone.set_pitch(-100)
    drone.move(.1)
    return

def backward(x):
    drone.set_yaw(0)
    drone.set_pitch(-50)
    drone.set_roll(0)
    drone.move(x)
    drone.set_pitch(100)
    drone.move(.1)
    drone.set_yaw(0)
    drone.set_pitch(0)
    drone.set_roll(0)
    return


def right(x):
    drone.set_yaw(0)
    drone.set_roll(50)
    drone.set_pitch(0)
    drone.move(x)
    drone.set_roll(-100)
    drone.move(.1)
    drone.set_yaw(0)
    drone.set_pitch(0)
    drone.set_roll(0)
    return


def left(x):
    drone.set_yaw(0)
    drone.set_roll(-50)
    drone.set_pitch(0)
    drone.move(x)
    drone.set_roll(100)
    drone.move(.1)
    drone.set_yaw(0)
    drone.set_pitch(0)
    drone.set_roll(0)
    return


def up(x):
    drone.set_pitch(0)
    drone.set_throttle(50)
    drone.move(x)
    drone.set_throttle(-100)
    drone.move(0.1)
    drone.set_throttle(0)
    drone.set_yaw(0)
    drone.set_pitch(0)
    drone.set_roll(0)
    return


def down(x):
    drone.set_throttle(-50)
    drone.move(x)
    drone.set_throttle(100)
    drone.move(0.1)
    drone.set_throttle(0)
    drone.set_yaw(0)
    drone.set_pitch(0)
    drone.set_roll(0)
    return


print("MAIN")
drone = Drone()
drone.pair()

drone.takeoff()  # height - 20-30 inches
forward(1)       # move 36 inches forward
up(0.5)
left(.30)
"""archLoopCount = 0;
archLooped = 0;
while archLooped < archLoopCount: # arch loop, set archLoopCount to 0 until everything else works
    up(2)
    backward(3)
    down(2)
    forward(3)
    archLooped = archLooped+1"""

up(.65)       # total height - 48 inches
forward(1.75)  # move 72 inches forward

"""keyholeLoopCount = 0
keyholeLooped = 0
while keyholeLooped < keyholeLoopCount: # keyhole loop, set keyholeLoopCount to 0 until everything else works
    up(5)
    backward(5)
    down(5)
    forward(5)
    keyholeLooped = keyholeLooped+1"""

forward(1)  # forward 18 inches
up(.25)       # up 8 inches
left(2)    # the bigger part of 90 inches. Through green keyhole loop.

down(4)     # down 30 inches, total height 26 inches
left(.85)     # the smaller part of 90 inches, through the second arch
drone.land()

colorFront = "error"  # detect color
colorBack = "error2"

failCount = 0
while not validColors(colorFront,colorBack):
    try:
        colorFront = drone.get_front_color()
        colorBack = drone.get_back_color()
        print(colorFront+" "+colorBack)
        failCount += 1
        if failCount == 100:
            colorFront = "Green"
            colorBack = "Green"
    except:
        print("error")

drone.takeoff()
print(colorFront)
if colorFront == "Red":
    drone.set_controller_LED(255,0,0,100)
    drone.set_drone_LED(255,0,0,100)
    backward(1.4)
if colorFront == "Blue":
    drone.set_controller_LED(0,0,255,100)
    drone.set_drone_LED(0,0,255,100)
    forward(1.2)
if colorFront == "Green":
    drone.set_controller_LED(0,255,0,100)
    drone.set_drone_LED(0,255,0,100)
    right(1)


drone.land()
drone.close()
