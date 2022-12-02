# Python
 This where my python scripts go

1: random story template, Idk what story I want to make yet but there is a template for one to exist. 

2: a Fibonacci Sequence solver that I made because I was board and thought that it would be funny. 

def apple_fall():
    global proper_list, index2
    #index2 = 0
    current_apple = proper_list[index2]
    proper_list.remove(current_apple)
    current_apple["turtle"].setheading(270)
    current_apple["turtle"].clear()
    current_apple["turtle"].goto(current_apple["turtle"].xcor(),-150)
    current_apple["turtle"].hideturtle()
    print(current_apple["letter"])
    proper_list = five_showing(5, proper_list, letters)
    
index2 = 0
def letterlisten():
    global index2
    wn.onkeypress(apple_fall, proper_list[0]["letter"])
    index2 = 1
    # wn.onkeypress(apple_fall(1), proper_list[1]["letter"])
    index2 = 2
    # wn.onkeypress(apple_fall(2), proper_list[2]["letter"])
    index2 = 3
    # wn.onkeypress(apple_fall(3), proper_list[3]["letter"])
    index2 = 4
    # wn.onkeypress(apple_fall(4), proper_list[4]["letter"])
    index2 = 0
    wn.listen()
