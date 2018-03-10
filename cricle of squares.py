# draw one square
# change the starting angle
# and repeat it


import turtle

def circle_of_squars():
    #opening screen
    window = turtle.Screen()

    # changing the background color
    window.bgcolor('red')

    # idenfing the brad turtle
    brad = turtle.Turtle()

    # reset some prop.s

    brad.shape('turtle')
    brad.color('white',"yellow")
    brad.speed('fastest')
    brad.pensize(5)
    #drowing cricle of squares
    squares_number = 35
    drawed = 0
    while drawed <= squares_number:  
        #drowing square by brad
        sides_number = 3
        side_counts = 0
        while side_counts <= sides_number:
            brad.forward(100)
            brad.right(90)
            side_counts+=1
        brad.right(10)
        drawed += 1
  
    
    #closing the screen by clicking on it
    window.exitonclick()

circle_of_squars()
