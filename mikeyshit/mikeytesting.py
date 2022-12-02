#   a123_apple_1.py
import turtle as trtl
import random as rand
import time
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
proper_list = []
number_of_apples = 5

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

writer = trtl.Turtle()
writer.penup()
writer.hideturtle()

def five_showing(number_of_apples, proper_list, letters):
  while len(proper_list) < number_of_apples:
    letter = letters.pop(rand.randint(0,len(letters))-1) #get a random letter
    current_apple = {"letter": letter, "turtle": create_apple(letter, "apple.gif", wn)} #make the apple
    proper_list.append(current_apple)
  return proper_list

def create_apple(letter, apple_image, wn):
  apple = trtl.Turtle() #Make a new object
  apple.shape(apple_image) #give it an image
  apple.penup() #so it doesn't draw
  apple.goto(rand.randint(-300,300),rand.randint(-150,150)) #give location
  wn.tracer(False) #so screen doesn't update
  apple.goto(apple.xcor()-10,apple.ycor()-28) #set location for text
  apple.write(letter, font=("Arial", 40, "bold")) #print letter
  apple.goto(apple.xcor()+10,apple.ycor()+28) #rest the location #set the turtle part in the current apple
  wn.tracer(True) #make it so screen updates again
  wn.update()
  return apple

def display_letter(active_apple):
  global current_letter, x
  letter_xcor = float(active_apple.xcor()) - 10
  letter_ycor = float(active_apple.ycor()) - 28
  writer.goto(letter_xcor,letter_ycor)
  writer.write(current_letter, font=("Arial", 40, "bold"))


def apple_fall():
  global listen_letter, current_letter
  print(listen_letter)
  correct_place = proper_list["letters"].index(listen_letter)
  proper_list["letters"].pop(correct_place)
  print(correct_place)
  print(proper_list["letters"])
  proper_list["turtle"][correct_place].setheading(270)
  proper_list["turtle"][correct_place].clear()
  proper_list["turtle"][correct_place].goto(proper_list["turtle"][correct_place].xcor(),-150)
  proper_list["turtle"][correct_place].hideturtle()
  proper_list["turtle"].pop(correct_place)
  print(proper_list["turtle"])
  five_showing()


five_showing()
wn.listen()
wn.mainloop()