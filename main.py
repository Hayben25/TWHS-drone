import time
from codrone_edu.drone import *


drone = Drone()
drone.open()


def validColors(front, back):      # checks to see if colors are errors or are valid
   if (front == back) and (front == "Red" or front == "Blue" or front == "Green"):
       return True
   else:
       return False

def getColors():
   colorFront = "error"  # detect color
   colorBack = "error2"

   failCount = 0
   while not validColors(colorFront, colorBack):
      try:
         colorFront = drone.get_front_color()
         colorBack = drone.get_back_color()
         print(colorFront + " " + colorBack)
         failCount += 1
         if failCount == 100:
            colorFront = "Green"
            colorBack = "Green"
      except:
         print("error")
      print(colorFront)
      if colorFront == "Red":
         drone.set_controller_LED(255, 0, 0, 100)
         drone.set_drone_LED(255, 0, 0, 100)

      if colorFront == "Blue":
         drone.set_controller_LED(0, 0, 255, 100)
         drone.set_drone_LED(0, 0, 255, 100)

      if colorFront == "Green":
         drone.set_controller_LED(0, 255, 0, 100)
         drone.set_drone_LED(0, 255, 0, 100)


def figureEight(x):      # loops through the arch and keyhole
   arch_loop_count = x
   arch_looped = 0
   while arch_looped < arch_loop_count:  # arch loop, set archLoopCount to 0 until everything else works
       forward(.49)
       up(2)
       forward(.59)
       down(2)
       backward(.59)
       up(2)
       backward(.59)
       down(2)
       forward(.59)
       arch_looped = arch_looped + 1




def forward(x):         # moves drone forward; 1 second - 18-19 inches; use 0.1 for stabilization
   drone.set_yaw(0)
   drone.set_roll(0)
   drone.set_pitch(50)
   drone.move(x)
   drone.set_pitch(-100)
   drone.move(.1)
   drone.reset_move()
   return




def backward(x):        # moves drone backward; input seconds
   drone.set_yaw(0)
   drone.set_pitch(-50)
   drone.set_roll(0)
   drone.move(x)
   drone.set_pitch(100)
   drone.move(.1)
   drone.reset_move()
   return




def right(x):       # moves drone right; input seconds
   drone.set_yaw(0)
   drone.set_roll(50)
   drone.set_pitch(0)
   drone.move(x)
   drone.set_roll(-100)
   drone.move(.1)
   drone.reset_move()
   return




def left(x):        # moves drone left; input seconds
   drone.set_yaw(0)
   drone.set_roll(-50)
   drone.set_pitch(0)
   drone.move(x)
   drone.set_roll(100)
   drone.move(.1)
   drone.reset_move()
   return




def up(x):      # moves drone up; input seconds
   drone.set_pitch(0)
   drone.set_throttle(50)
   drone.move(x)
   drone.set_throttle(-100)
   drone.move(0.1)
   drone.set_throttle(0)
   drone.reset_move()
   return




def down(x):        # moves drone down; input seconds
   drone.set_throttle(-50)
   drone.move(x)
   drone.set_throttle(0)
   drone.move(0.1)
   drone.set_throttle(0)
   drone.reset_move()
   return




drone.takeoff()
# Type Code Here
#forward(1.932)
#figureEight(1)
#up(1.5)
#forward(.62)
#forward(1.975)
#getColors()
#drone.land()
#drone.takeoff()
#up(3)#SET AT PRACTICE
#right(2.52)
#up(2)#SET AT PRACTICE
#backward(1.225)
#drone.land()
#drone.close()
forward(.73)
drone.land()