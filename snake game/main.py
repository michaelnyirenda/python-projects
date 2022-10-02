from turtle import Shape, Turtle, Screen, left, register_shape

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Danger Noodle: The Game")

segment_pos = [(0,0), (-20, 0), (-40, 0)] # list of segment positions

#3 turtle objects side by side
for i in segment_pos:
    segment = Turtle(shape = "square")
    segment.color("white")
    segment.setpos(i)
   




screen.exitonclick()


# s = Shape("compound")
# poly1 = ((0,0),(10,-5),(0,10),(-10,-5))
# s.addcomponent(poly1, "white", "blue")
# # poly2 = ((0,0),(10,-5),(-10,-5))
# # s.addcomponent(poly2, "blue", "red")

# register_shape("snake", s)
# snake =  Turtle(shape = "snake")
# snake.color = "white"
