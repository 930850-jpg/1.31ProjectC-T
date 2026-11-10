#----Imports and Initializations---#
import turtle as trtl
import time 
import random as rand
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

#Drawing the How to play box
font = ("Arial", 15, "normal")
writer = trtl.Turtle()
writer.speed(0)
writer.penup()
writer.pencolor("grey")
writer.fillcolor("grey")
writer.goto(-350,-100)
writer.pendown()
writer.begin_fill()
writer.goto(350,-100)
writer.goto(350,200)
writer.goto(-350,200)
writer.goto(-350,-100)
writer.end_fill()

writer.penup()
writer.goto(0,220)
writer.pencolor("black")
writer.write("How to Play", align="center", font=("Arial", 24, "bold"))
writer.goto(0,0)
writer.write("A string of 5 numbers will appear on the screen for 3 seconds. \n after those 3 seconds, it will disappear for 1 second. \n then 5 boxes will appear with arrows above and below them. \n these boxes are used to enter numbers, and the arrows change the number. \n Your goal is to enter the same string that appeared. \n tap the button below to begin.", align="center", font=font)
writer.hideturtle()









wn.mainloop()
