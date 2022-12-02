
import random
import turtle as trtl

letters = [
  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
  "P", "Q", "R", "S", "T", "U", "V", "W", "Y", "X", "Z"
]


#-----setup-----
apple_image = "apple.gif"  # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)  # Make the screen aware of the new file
wn.bgpic("background.gif")

current_turtle = trtl.Turtle()
current_turtle2 = trtl.Turtle()
current_turtle3 = trtl.Turtle()
current_turtle4 = trtl.Turtle()
current_turtle5 = trtl.Turtle()

drawer = trtl.Turtle()
drawer2 = trtl.Turtle()
drawer3 = trtl.Turtle()
drawer4 = trtl.Turtle()
drawer5 = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_a_letter():
  global letter_used
  global current_turtle
  letter_used = letters[random.randint(0, len(letters) - 1 )]
  letters.remove(letter_used)
  apple_xcord = current_turtle.xcor()
  apple_ycord = current_turtle.ycor()
  drawer.penup()
  drawer.color("white")
  drawer.goto(apple_xcord - 15, apple_ycord - 35)
  drawer.pendown()
  drawer.write(letter_used, font=("Arial", 35, "bold"))
  drawer.hideturtle()


def draw_apple():
  global current_turtle
  #wn.tracer(False)
  current_turtle.shape(apple_image)
  draw_a_letter()
  wn.update()


def apple_fall_on_letter():
  global current_turtle
  #wn.tracer(True)
  drawer.clear()
  ycord = current_turtle.ycor()
  if ycord > -20:
    current_turtle.penup()
    current_turtle.right(90)
    current_turtle.forward(100)
    reset()

def reset():
  global current_turtle
  global letter_used
  current_turtle.hideturtle()
  #wn.clear()
  wn.bgpic("background.gif")
  x_turtle_cord = random.randint(-200,200)
  y_turtle_cord = random.randint(-20, 150)
  current_turtle = trtl.Turtle()
  current_turtle.hideturtle()
  current_turtle.penup()
  current_turtle.goto(x_turtle_cord, y_turtle_cord)
  current_turtle.showturtle()
  draw_apple()
  print (letter_used.lower())
  wn.onkeypress(apple_fall_on_letter, letter_used.lower())
 
def draw_a_letter2():
  global letter_used2
  global current_turtle2
  letter_used2 = letters[random.randint(0, len(letters) - 1 )]
  letters.remove(letter_used2)
  apple_xcord2 = current_turtle2.xcor()
  apple_ycord2 = current_turtle2.ycor()
  drawer2.penup()
  drawer2.color("green")
  drawer2.goto(apple_xcord2 - 15, apple_ycord2 - 35)
  drawer2.pendown()
  drawer2.write(letter_used2, font=("Arial", 35, "bold"))
  drawer2.hideturtle()


def draw_apple2():
  global current_turtle2
  #wn.tracer(False)
  current_turtle2.shape(apple_image)
  draw_a_letter2()
  wn.update()


def apple_fall_on_letter2():
  global current_turtle2
  #wn.tracer(True)
  drawer2.clear()
  ycord2 = current_turtle2.ycor()
  if ycord2 > -20:
    current_turtle2.penup()
    current_turtle2.right(90)
    current_turtle2.forward(100)
    reset2()

def reset2():
  global current_turtle2
  global letter_used2
  current_turtle2.hideturtle()
  #wn.clear()
  wn.bgpic("background.gif")
  x_turtle_cord2 = random.randint(-30,30)
  y_turtle_cord2 = random.randint(-10, 100)
  current_turtle2 = trtl.Turtle()
  current_turtle2.hideturtle()
  current_turtle2.penup()
  current_turtle2.goto(x_turtle_cord2, y_turtle_cord2)
  current_turtle2.showturtle()
  draw_apple2()
  print (letter_used2.lower())
  wn.onkeypress(apple_fall_on_letter2, letter_used2.lower())

def draw_a_letter3():
  global letter_used3
  global current_turtle3
  letter_used3 = letters[random.randint(0, len(letters) - 1 )]
  letters.remove(letter_used3)
  apple_xcord3 = current_turtle3.xcor()
  apple_ycord3 = current_turtle3.ycor()
  drawer3.penup()
  drawer3.color("blue")
  drawer3.goto(apple_xcord3 - 15, apple_ycord3 - 35)
  drawer3.pendown()
  drawer3.write(letter_used3, font=("Arial", 35, "bold"))
  drawer3.hideturtle()


def draw_apple3():
  global current_turtle3
  #wn.tracer(False)
  current_turtle3.shape(apple_image)
  draw_a_letter3()
  wn.update()


def apple_fall_on_letter3():
  global current_turtle3
  #wn.tracer(True)
  drawer3.clear()
  ycord3 = current_turtle3.ycor()
  if ycord3 > -20:
    current_turtle3.penup()
    current_turtle3.right(90)
    current_turtle3.forward(100)
    reset3()

def reset3():
  global current_turtle3
  global letter_used3
  current_turtle3.hideturtle()
  #wn.clear()
  wn.bgpic("background.gif")
  x_turtle_cord3 = random.randint(-30,30)
  y_turtle_cord3 = random.randint(-10, 100)
  current_turtle3 = trtl.Turtle()
  current_turtle3.hideturtle()
  current_turtle3.penup()
  current_turtle3.goto(x_turtle_cord3, y_turtle_cord3)
  current_turtle3.showturtle()
  draw_apple3()
  print (letter_used3.lower())
  wn.onkeypress(apple_fall_on_letter3, letter_used3.lower())
 
def draw_a_letter4():
  global letter_used4
  global current_turtle4
  letter_used4 = letters[random.randint(0, len(letters) - 1 )]
  letters.remove(letter_used4)
  apple_xcord4 = current_turtle4.xcor()
  apple_ycord4 = current_turtle4.ycor()
  drawer4.penup()
  drawer4.color("yellow")
  drawer4.goto(apple_xcord4 - 15, apple_ycord4 - 35)
  drawer4.pendown()
  drawer4.write(letter_used4, font=("Arial", 35, "bold"))
  drawer4.hideturtle()


def draw_apple4():
  global current_turtle4
  #wn.tracer(False)
  current_turtle4.shape(apple_image)
  draw_a_letter4()
  wn.update()


def apple_fall_on_letter4():
  global current_turtle4
  #wn.tracer(True)
  drawer4.clear()
  ycord4 = current_turtle4.ycor()
  if ycord4 > -20:
    current_turtle4.penup()
    current_turtle4.right(90)
    current_turtle4.forward(100)
    reset4()

def reset4():
  global current_turtle4
  global letter_used4
  current_turtle4.hideturtle()
  #wn.clear()
  wn.bgpic("background.gif")
  x_turtle_cord4 = random.randint(-30,30)
  y_turtle_cord4 = random.randint(-10, 100)
  current_turtle4 = trtl.Turtle()
  current_turtle4.hideturtle()
  current_turtle4.penup()
  current_turtle4.goto(x_turtle_cord4, y_turtle_cord4)
  current_turtle4.showturtle()
  draw_apple4()
  print (letter_used4.lower())
  wn.onkeypress(apple_fall_on_letter4, letter_used4.lower())


def draw_a_letter5():
  global letter_used5
  global current_turtle5
  letter_used5 = letters[random.randint(0, len(letters) - 1 )]
  letters.remove(letter_used5)
  apple_xcord5 = current_turtle5.xcor()
  apple_ycord5 = current_turtle5.ycor()
  drawer5.penup()
  drawer5.color("orange")
  drawer5.goto(apple_xcord5 - 15, apple_ycord5 - 35)
  drawer5.pendown()
  drawer5.write(letter_used5, font=("Arial", 35, "bold"))
  drawer5.hideturtle()


def draw_apple5():
  global current_turtle5
  #wn.tracer(False)
  current_turtle5.shape(apple_image)
  draw_a_letter5()
  wn.update()


def apple_fall_on_letter5():
  global current_turtle5
  #wn.tracer(True)
  drawer5.clear()
  ycord5 = current_turtle5.ycor()
  if ycord5 > -20:
    current_turtle5.penup()
    current_turtle5.right(90)
    current_turtle5.forward(100)
    reset5()

def reset5():
  global current_turtle5
  global letter_used5
  current_turtle5.hideturtle()
  #wn.clear()
  wn.bgpic("background.gif")
  x_turtle_cord5 = random.randint(-30,30)
  y_turtle_cord5 = random.randint(-10, 100)
  current_turtle5 = trtl.Turtle()
  current_turtle5.hideturtle()
  current_turtle5.penup()
  current_turtle5.goto(x_turtle_cord5, y_turtle_cord5)
  current_turtle5.showturtle()
  draw_apple5()
  print (letter_used5.lower())
  wn.onkeypress(apple_fall_on_letter5, letter_used5.lower())
#-----function calls-----
reset()
reset2()
reset3()
reset4()
reset5()
wn.listen()
wn.mainloop()


