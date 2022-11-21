from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 40, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.dashed_line()
        self.left_score = 0
        self.right_score = 0
        self.left_player_score()
        self.right_player_score()

    def dashed_line(self):
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        self.width(5)

        draw_line = True
        while draw_line:
            if self.ycor() > 280:
                draw_line = False
            else:
                self.forward(15)
                self.hideturtle()
                self.penup()
                self.forward(15)
                self.down()

    def left_player_score(self):
        self.hideturtle()
        self.penup()
        self.goto(-30, 240)
        self.write(arg=f"{self.left_score}", move=True, align=ALIGNMENT, font=FONT)

    def right_player_score(self):
        self.hideturtle()
        self.penup()
        self.goto(30, 240)
        self.write(arg=f"{self.right_score}", move=True, align=ALIGNMENT, font=FONT)

    def increase_score_left(self):
        self.clear()
        self.right_player_score()
        self.dashed_line()
        self.left_score += 1
        self.hideturtle()
        self.penup()
        self.goto(-30, 240)
        self.write(arg=f"{self.left_score}", move=True, align=ALIGNMENT, font=FONT)

    def increase_score_right(self):
        self.clear()
        self.left_player_score()
        self.dashed_line()
        self.right_score += 1
        self.hideturtle()
        self.penup()
        self.goto(30, 240)
        self.write(arg=f"{self.right_score}", move=True, align=ALIGNMENT, font=FONT)