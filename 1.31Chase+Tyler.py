#----Imports and Initializations---#
import turtle as trtl
import time 
import random as rand
from functools import partial
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.cv._rootwindow.resizable(False, False)

Message0_4list = ["Every round is a new opportunity. Keep going!",
"You're doing great by giving it a try!",
"Keep practicing. There's always room to grow!",
"Take your time. You'll get there!",
"A little progress goes a long way. Keep it up!"]
Message5_9list = ["Very nice work! You're making great progress!",
"Excellent effort! You're getting closer!",
"Well done! Keep up the good work!",
"You're doing wonderfully! Almost there!",
"Great job! You're improving with every round!"]
Message10list = ["Perfect match! Outstanding work!",
"Fantastic! You got every single one right!",
"Excellent! Couldn't have done better!",
"Wonderful work! A perfect round!",
"Absolutely spot on! Congratulations!"]
number_list = [0,1,2,3,4,5,6,7,8,9]
code_list = []
entered_list = []
top_arrow_list =[]
bottom_arrow_list = []
number_writer_list =[]

#---Functions---#
def make_code(x,y):
  if -100 <= x <= 100 and -170 <= y <= -120:
    wn.onclick(None)
    global number_list, code_list
    writer.clear()
    start.clear()
    for number in range(5):
      number = rand.choice(number_list)
      number_list.remove(number)
      code_list.append(number)
    number_list = [0,1,2,3,4,5,6,7,8,9]
    #print(code_list)
    writer.goto(0,50)
    writer.write(str(code_list),align="center",font=("Arial", 50, "bold"))
    time.sleep(3)
    writer.clear()
    create_code_enter()

def create_code_enter():
  global entered_list
  wn.tracer(0)
  start_x = -200
  for number in code_list:
    number_writer = trtl.Turtle(shape="square")
    number_writer.shapesize(4)
    number_writer.speed(0)
    number_writer.fillcolor("white")
    number_writer.penup()
    number_writer.goto(start_x, 0)
    number_writer.stamp()
    number_writer.hideturtle()
    number_writer.goto(start_x, -35)
    number_writer.write("0",align="center",font=("Arial", 50, "bold"))
    top_arrow = trtl.Turtle(shape="arrow")
    bottom_arrow = trtl.Turtle(shape="arrow")
    top_arrow.speed(0)
    top_arrow.penup()
    top_arrow.setheading(90)
    top_arrow.goto(start_x, 50)
    top_arrow.onclick(partial(top_counter,top_arrow))
    top_arrow_list.append(top_arrow)
    bottom_arrow.speed(0)
    bottom_arrow.penup()
    bottom_arrow.setheading(-90)
    bottom_arrow.goto(start_x, -50)
    bottom_arrow_list.append(bottom_arrow)
    start_x += 100
  entered_list = [0,0,0,0,0]
  wn.tracer(1)

#--Counter go up thing--#
def top_counter(x,y, top_arrow):
  index = top_arrow_list.index(top_arrow)
  if index == 0:
    writer.goto(top_arrow.xcor(),-35)
    input = entered_list.pop(index)
    writer.write(str(input),align="center",font=("Arial", 50, "bold"))
  elif index == 1:
    writer.goto(top_arrow.xcor(),-35)
    input = entered_list.pop(index)
    writer.write(str(input),align="center",font=("Arial", 50, "bold"))
  elif index == 2:
    writer.goto(top_arrow.xcor(),-35)
    input = entered_list.pop(index)
    writer.write(str(input),align="center",font=("Arial", 50, "bold"))
  elif index == 3:
    writer.goto(top_arrow.xcor(),-35)
    input = entered_list.pop(index)
    writer.write(str(input),align="center",font=("Arial", 50, "bold"))
  elif index == 4:
    writer.goto(top_arrow.xcor(),-35)
    input = entered_list.pop(index)
    writer.write(str(input),align="center",font=("Arial", 50, "bold"))

def top_counter(top_arrow,x,y):
  index = top_arrow_list.index(top_arrow)
  if index == 0:
    print("0")
    writer.goto(top_arrow.xcor(),-35)
    input = entered_list.pop(index)
    input +=1
    writer.write(str(input),align="center",font=("Arial", 50, "bold"))
    entered_list.insert(input,index)
  elif index == 1:
    print("1")
    writer.goto(top_arrow.xcor(),-35)
    input = entered_list.pop(index)
    input +=1 
    writer.write(str(input),align="center",font=("Arial", 50, "bold"))
    entered_list.insert(input,index)
  elif index == 2:
    print("2")
    writer.goto(top_arrow.xcor(),-35)
    input = entered_list.pop(index)
    input +=1
    writer.write(str(input),align="center",font=("Arial", 50, "bold"))
    entered_list.insert(input,index)
  elif index == 3:
    print("3")
    writer.goto(top_arrow.xcor(),-35)
    input = entered_list.pop(index)
    input +=1
    writer.write(str(input),align="center",font=("Arial", 50, "bold"))
    entered_list.insert(input,index)
  elif index == 4:
    print("4")
    writer.goto(top_arrow.xcor(),-35)
    input = entered_list.pop(index)
    input +=1
    writer.write(str(input),align="center",font=("Arial", 50, "bold"))
    entered_list.insert(input,index)
    
#Drawing the How to play box
writer = trtl.Turtle()
writer.speed(0)
writer.penup()
writer.pencolor("grey")
writer.fillcolor("grey")
writer.goto(-600,-100)
writer.pendown()
writer.begin_fill()
writer.goto(600,-100)
writer.goto(600,200)
writer.goto(-600,200)
writer.goto(-600,-100)
writer.end_fill()
writer.penup()
writer.goto(0,220)
writer.pencolor("black")
writer.write("How to Play", align="center", font=("Arial", 40, "bold"))
writer.goto(0,-50)
writer.write("A string of 5 numbers will appear on the screen for 3 seconds. \n after those 3 seconds, it will disappear for 1 second. \n then 5 boxes will appear with arrows above and below them. \n these boxes are used to enter numbers, and the arrows change the number. \n Your goal is to enter the same string that appeared. \n tap the button below to begin.", align="center", font=("Arial", 25, "normal"))
writer.hideturtle()


#Start Button
start = trtl.Turtle()
start.hideturtle()
start.speed(0)
start.penup()
start.goto(-100,-120)
start.pendown()
start.fillcolor("green")
start.begin_fill()
start.goto(100,-120)
start.goto(100, -170)
start.goto(-100, -170)
start.end_fill()
start.penup()
start.goto(0, -170)
start.write("Begin", align="center",font=("Arial", 35, "bold"))
wn.onclick(make_code)










wn.mainloop()
