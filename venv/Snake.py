from turtle import Turtle, Screen

WIDTH = Screen().window_width()
HEIGHT = Screen().window_height()
class Snake:
    def __init__(self):
        #body of the snake, first cube is always the head
        self.cubes = []
        #spawns three parts of the snake
        for i in range(3):
            self.cubes.append(Snake.make_turtle(self))
        Snake.init_pos(self)


    def make_turtle(self):
        #snake bodies are turtles from Turtle library
        #shapes as squares and colored white to represent snake body
        turtle = Turtle()
        turtle.shape("square")
        turtle.color("white")
        turtle.penup()
        return turtle


    def init_pos(self):
        for i in range(len(self.cubes)):
            if i >= 1:
                #to spawn a body we take body part before it, and
                #take away the offset
                self.cubes[i].setx(self.cubes[(i - 1)].xcor() - 30)


    def move(self):
        #to move the snake, we move every individual part forward by x amount
        for i in range(len(self.cubes) - 1, 0, -1):
            self.cubes[i].setx(self.cubes[i - 1].xcor())
            self.cubes[i].sety(self.cubes[i - 1].ycor())
        self.cubes[0].forward(30)


    def check_for_collision(self):
        if self.cubes[0].xcor() >= 315 or self.cubes[0].xcor() <= -315:
            return False
        if self.cubes[0].ycor() >= 315 or self.cubes[0].ycor() <= -315:
            return False
        for i in range(1, len(self.cubes)):
            if self.cubes[0].distance(self.cubes[i]) < 10:
                return False
        return True

    def clear_snake(self):
        for x in self.cubes:
            x.ht()
            x.clear()

    def grow(self):
        self.cubes.append(self.make_turtle())
        self.cubes[
            len(self.cubes) - 1].setx(self.cubes[len(self.cubes) - 2
                    ].xcor())
        self.cubes[
            len(self.cubes) - 1].sety(self.cubes[len(self.cubes) - 2
                    ].ycor())

    #to change the direction of the snake, we just rotate
    #head by x degrees, the rest will follow it with the use of move()
    def up(self):
        if self.cubes[0].heading() != 270:
            self.cubes[0].setheading(90)


    def down(self):
        if self.cubes[0].heading() != 90:
            self.cubes[0].setheading(270)


    def right(self):
        if self.cubes[0].heading() != 180:
            self.cubes[0].setheading(0)


    def left(self):
        if self.cubes[0].heading() != 0:
            self.cubes[0].setheading(180)
