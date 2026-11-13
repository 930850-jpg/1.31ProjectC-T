import random as rand
import time
import turtle as trtl
from functools import partial

# ---- Constants & Configuration ---- #
X_POSITIONS = [-200, -100, 0, 100, 200]

MESSAGES_LOW = [
    "Every round is a new opportunity. Keep going!",
    "You're doing great by giving it a try!",
    "Keep practicing. There's always room to grow!",
    "Take your time. You'll get there!",
    "A little progress goes a long way. Keep it up!",
]
MESSAGES_MID = [
    "Very nice work! You're making great progress!",
    "Excellent effort! You're getting closer!",
    "Good Try! Keep up the good work!",
    "You're doing wonderfully! Almost there!",
    "Great job! You're improving with every round!",
]
MESSAGES_HIGH = [
    "Perfect match! Outstanding work!",
    "Fantastic! You got every single one right!",
    "Excellent! Couldn't have done better!",
    "Wonderful work! A perfect round!",
    "Absolutely spot on! Congratulations!",
]

# ---- Screen Setup ---- #
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.cv._rootwindow.resizable(False, False)

# ---- Game State ---- #
code_list = []
entered_list = [0] * 5
number_writers = []


# ---- Helper Functions ---- #
def create_pen():
  pen = trtl.Turtle()
  pen.hideturtle()
  pen.penup()
  pen.speed(0)
  return pen


def build_button(label):
  btn = create_pen()
  btn.goto(-100, -120)
  btn.fillcolor("green")
  btn.begin_fill()
  for x, y in [(100, -120), (100, -170), (-100, -170), (-100, -120)]:
    btn.goto(x, y)
  btn.end_fill()

  btn.goto(0, -170)
  btn.write(label, align="center", font=("Arial", 35, "bold"))


def is_button_clicked(x, y):
  return -100 <= x <= 100 and -170 <= y <= -120


def calculate_score(secret, guess):
  score = 0
  for i in range(len(secret)):
    if guess[i] == secret[i]:
      score += 2
    elif guess[i] in secret:
      # Award 1 point once per misplaced digit, provided it wasn't already an exact match
      is_first_occurrence = guess.index(guess[i]) == i
      has_exact_match = any(
          guess[j] == secret[j] == guess[i] for j in range(len(secret))
      )
      if is_first_occurrence and not has_exact_match:
        score += 1
  return score


# ---- Game Flow Functions ---- #
def show_instructions():
  writer = create_pen()
  writer.pencolor("grey")
  writer.fillcolor("grey")
  writer.goto(-600, -100)
  writer.pendown()
  writer.begin_fill()
  for x, y in [(600, -100), (600, 200), (-600, 200), (-600, -100)]:
    writer.goto(x, y)
  writer.end_fill()
  writer.penup()

  writer.pencolor("black")
  writer.goto(0, 220)
  writer.write("How to Play", align="center", font=("Arial", 40, "bold"))
  writer.goto(0, -50)
  instructions = (
      "A string of 5 numbers will appear on the screen for 3 seconds.\n"
      "After those 3 seconds, it will disappear for 1 second.\n"
      "Then 5 boxes will appear with arrows above and below them.\n"
      "These boxes are used to enter numbers, and the arrows change the"
      " number.\n"
      "Your goal is to enter the same string that appeared.\n"
      "Tap the button below to begin."
  )
  writer.write(instructions, align="center", font=("Arial", 25, "normal"))

  build_button("Begin")
  wn.onclick(make_code)


def make_code(x, y):
  global code_list
  if not is_button_clicked(x, y):
    return

  wn.onclick(None)
  wn.clearscreen()

  # Sample 5 unique digits from 0-9
  code_list = rand.sample(range(10), 5)
  print(f"DEBUG - Secret code: {code_list}")

  writer = create_pen()
  writer.goto(0, 50)
  writer.write(str(code_list), align="center", font=("Arial", 50, "bold"))
  wn.update()
  time.sleep(3)

  writer.clear()
  wn.update()
  time.sleep(1)

  create_code_enter()


def create_code_enter():
  global entered_list, number_writers
  wn.tracer(0)

  entered_list = [0] * 5
  number_writers = []

  square_stamper = trtl.Turtle(shape="square")
  square_stamper.shapesize(4)
  square_stamper.fillcolor("white")
  square_stamper.penup()
  square_stamper.speed(0)

  for i, x_pos in enumerate(X_POSITIONS):
    # Stamp input box
    square_stamper.goto(x_pos, 0)
    square_stamper.stamp()

    # Up arrow
    top_arrow = trtl.Turtle(shape="arrow")
    top_arrow.speed(0)
    top_arrow.penup()
    top_arrow.setheading(90)
    top_arrow.goto(x_pos, 50)
    top_arrow.onclick(partial(update_digit, i, 1))

    # Down arrow
    bottom_arrow = trtl.Turtle(shape="arrow")
    bottom_arrow.speed(0)
    bottom_arrow.penup()
    bottom_arrow.setheading(-90)
    bottom_arrow.goto(x_pos, -50)
    bottom_arrow.onclick(partial(update_digit, i, -1))

    # Digit display
    digit_writer = create_pen()
    digit_writer.goto(x_pos, -35)
    digit_writer.write("0", align="center", font=("Arial", 50, "normal"))
    number_writers.append(digit_writer)

  square_stamper.hideturtle()
  build_button("Enter")
  wn.onclick(check)
  wn.tracer(1)


def update_digit(index, delta, x, y):
  entered_list[index] = (entered_list[index] + delta) % 10
  number_writers[index].clear()
  number_writers[index].write(
      str(entered_list[index]), align="center", font=("Arial", 50, "normal")
  )


def check(x, y):
  if not is_button_clicked(x, y):
    return

  wn.onclick(None)

  # Debug output runs before screen transitions, and entered_list is never mutated
  print(f"DEBUG - User entered: {entered_list}")
  score = calculate_score(code_list, entered_list)
  print(f"DEBUG - Score: {score}")

  wn.clearscreen()

  if score < 5:
    feedback = rand.choice(MESSAGES_LOW)
  elif score < 10:
    feedback = rand.choice(MESSAGES_MID)
  else:
    feedback = rand.choice(MESSAGES_HIGH)

  result_text = (
      f"{feedback}\n"
      f"The Code Was: {code_list}\n"
      f"  You Entered  : {entered_list}\n"
      "Would you like to go again?"
  )

  message_turtle = create_pen()
  message_turtle.goto(0, -20)
  message_turtle.write(result_text, align="center", font=("Arial", 32, "bold"))

  build_button("Again")
  wn.onclick(make_code)


# ---- Start Game ---- #
show_instructions()
wn.mainloop()
