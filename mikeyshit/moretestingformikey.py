import random as rand, turtle as trtl

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
proper_list = []

wn = trtl.Screen()
apple_image = "apple.gif"
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)
wn.bgpic("background.gif")

def five_showing(number_of_apples, proper_list, letters): #make sure there are 5 apples
    while len(proper_list) < number_of_apples:
        #try to find a new letter and if that fails then return the proper list as is avoids running out of letters errors
        try:
            letter = letters.pop(rand.randint(0,len(letters))-1) #get a random letter 
        except:
            return proper_list
        current_apple = {"letter": letter, "turtle": create_apple(letter, "apple.gif", wn)} #make the apple, dict so there only needs to be 1 list
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
    return apple

def apple_fall(index2):
    global proper_list
    deactivate() 
    current_apple = proper_list.pop(index2) #get the current apple
    current_apple["turtle"].setheading(270)
    current_apple["turtle"].clear()
    current_apple["turtle"].goto(current_apple["turtle"].xcor(),-150)
    current_apple["turtle"].hideturtle()
    proper_list = five_showing(5, proper_list, letters) #make sure there is always 5 apples unless you are at win
    activate()

def deactivate(): #diactivate all the keypress conditionals so that what they are listen for updates
    global wn, proper_list
    try: wn.onkeypress(None, proper_list[0]["letter"])
    except: return
    try: wn.onkeypress(None, proper_list[1]["letter"])
    except: return
    try: wn.onkeypress(None, proper_list[2]["letter"])
    except: return
    try: wn.onkeypress(None, proper_list[3]["letter"])
    except: return
    try: wn.onkeypress(None, proper_list[4]["letter"])
    except: return
    
def activate(): #reactivate them
    global wn, proper_list
    #lambda so that you can send the arg though and not have it crash
    try: wn.onkeypress(lambda:apple_fall(0), proper_list[0]["letter"])
    except: return
    try: wn.onkeypress(lambda:apple_fall(1), proper_list[1]["letter"])
    except: return
    try: wn.onkeypress(lambda:apple_fall(2), proper_list[2]["letter"])
    except: return
    try: wn.onkeypress(lambda:apple_fall(3), proper_list[3]["letter"])
    except: return
    try: wn.onkeypress(lambda:apple_fall(4), proper_list[4]["letter"])
    except: return

def letterlisten():
    global proper_list
    activate()
    wn.listen()

#run the stuff
proper_list = five_showing(5, proper_list, letters)
letterlisten()
wn.update()
wn.mainloop()
