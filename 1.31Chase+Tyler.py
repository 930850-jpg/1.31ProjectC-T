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
checking = 0

def number_writers():
  global number_writer0, number_writer1, number_writer2, number_writer3, number_writer4
  number_writer0 = trtl.Turtle()
  number_writer0.hideturtle()
  number_writer0.penup()
  number_writer0.goto(-200,-35)
  number_writer1 = trtl.Turtle()
  number_writer1.hideturtle()
  number_writer1.penup()
  number_writer1.goto(-100,-35)
  number_writer2 = trtl.Turtle()
  number_writer2.hideturtle()
  number_writer2.penup()
  number_writer2.goto(0,-35)
  number_writer3 = trtl.Turtle()
  number_writer3.hideturtle()
  number_writer3.penup()
  number_writer3.goto(100,-35)
  number_writer4 = trtl.Turtle()
  number_writer4.hideturtle()
  number_writer4.penup()
  number_writer4.goto(200,-35)

#---Functions---#
#Start Button
def build_button():
  global start
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
    square_writer = trtl.Turtle(shape="square")
    square_writer.shapesize(4)
    square_writer.speed(0)
    square_writer.fillcolor("white")
    square_writer.penup()
    square_writer.goto(start_x, 0)
    square_writer.stamp()
    square_writer.hideturtle()
    square_writer.goto(start_x, -35)
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
    bottom_arrow.onclick(partial(bottom_counter,bottom_arrow))
    bottom_arrow_list.append(bottom_arrow)
    start_x += 100
  build_button()
  start.write("Enter", align="center",font=("Arial", 35, "bold"))
  wn.onclick(check)
  number_writers()
  number_writer0.write(0, align="center", font=("arial", 50, "normal"))
  number_writer1.write(0, align="center", font=("arial", 50, "normal"))
  number_writer2.write(0, align="center", font=("arial", 50, "normal"))
  number_writer3.write(0, align="center", font=("arial", 50, "normal"))
  number_writer4.write(0, align="center", font=("arial", 50, "normal"))
  entered_list = [0,0,0,0,0]
  wn.tracer(1)

def check(x,y):
  global entered_list, code_list, checking
  if -100 <= x <= 100 and -170 <= y <= -120:
    wn.onclick(None)
    wn.clearscreen()
    i=0
    while i <= 4:
      if entered_list[i] == code_list[i]:
        checking += 2
      elif entered_list[i] in code_list:
          checking +=1
      i += 1
    message_turtle = trtl.Turtle()
    message_turtle.hideturtle()
    if checking < 5:
      message_turtle.write(rand.choice(Message0_4list)+"\n"+ "The Code Was: "+ str(code_list)+ "\n"+"You Entered: "+ str(entered_list)+ "\n" + "Would you like to go again?", align="center", font=("arial", 50, "bold"))
    if checking > 4 and checking != 10:
      message_turtle.write(rand.choice(Message5_9list)+"\n"+ "The Code Was: "+ str(code_list)+ "\n"+"You Entered: "+ str(entered_list)+ "\n" + "Would you like to go again?", align="center", font=("arial", 50, "bold"))
    if checking == 10:
      message_turtle.write(rand.choice(Message10list)+"\n"+ "The Code Was: "+ str(code_list)+ "\n"+"You Entered: "+ str(entered_list)+ "\n" + "Would you like to go again?", align="center", font=("arial", 50, "bold"))
    build_button()
    start.write("Again", align="center",font=("Arial", 35, "bold"))
    wn.onclick(make_code)

def bottom_counter(bottom_arrow, x, y):
  writer.clear()
  index = bottom_arrow_list.index(bottom_arrow)
  #print(index)
  if index == 0:
    input = entered_list.pop(index)
    input -=1
    if input < 0:
      input = 9
    entered_list.insert(index,input)
    number_writer0.clear()
    number_writer0.write(str(input), align="center", font=("arial", 50, "normal"))
  elif index == 1:
    input = entered_list.pop(index)
    input -=1
    if input < 0:
      input = 9
    entered_list.insert(index,input)
    number_writer1.clear()
    number_writer1.write(str(input), align="center", font=("arial", 50, "normal"))
  elif index == 2:
    input = entered_list.pop(index)
    input -=1
    if input < 0:
      input = 9
    entered_list.insert(index,input)
    number_writer2.clear()
    number_writer2.write(str(input), align="center", font=("arial", 50, "normal"))
  elif index == 3:
    input = entered_list.pop(index)
    input -=1
    if input < 0:
      input = 9
    entered_list.insert(index,input)
    number_writer3.clear()
    number_writer3.write(str(input), align="center", font=("arial", 50, "normal"))
  elif index == 4:
    input = entered_list.pop(index)
    input -=1
    if input < 0:
      input = 9
    entered_list.insert(index,input)
    number_writer4.clear()
    number_writer4.write(str(input), align="center", font=("arial", 50, "normal"))

def top_counter(top_arrow,x,y):
  index = top_arrow_list.index(top_arrow)
  if index == 0:
    #print("0")
    #print(entered_list)
    input = entered_list.pop(index)
    input +=1
    if input > 9:
          input = 0
    entered_list.insert(index,input)
    number_writer0.clear()
    number_writer0.write(str(input), align="center", font=("arial", 50, "normal"))
  elif index == 1:
    #print("1")
    input = entered_list.pop(index)
    input +=1
    if input > 9:
          input = 0
    entered_list.insert(index,input)
    number_writer1.clear()
    number_writer1.write(str(input), align="center", font=("arial", 50, "normal"))
  elif index == 2:
    #print("2")
    input = entered_list.pop(index)
    input +=1
    if input > 9:
          input = 0
    entered_list.insert(index,input)
    number_writer2.clear()
    number_writer2.write(str(input), align="center", font=("arial", 50, "normal"))
  elif index == 3:
    #print("3")
    input = entered_list.pop(index)
    input +=1
    if input > 9:
          input = 0
    entered_list.insert(index,input)
    number_writer3.clear()
    number_writer3.write(str(input), align="center", font=("arial", 50, "normal"))
  elif index == 4:
    #print("4")
    input = entered_list.pop(index)
    input +=1
    if input > 9:
      input = 0
    entered_list.insert(index,input)
    number_writer4.clear()
    number_writer4.write(str(input), align="center", font=("arial", 50, "normal"))
  #print(entered_list)
    
    
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

build_button()
start.write("Begin", align="center",font=("Arial", 35, "bold"))
wn.onclick(make_code)










wn.mainloop()
