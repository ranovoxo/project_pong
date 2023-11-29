from turtle import Turtle
ALIGNMENT = "center"
FONT = ('COURIER', 24, 'normal')

class Scoreboad(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def right_point(self):
        self.right_score += 1
        self.update_score()

    def left_point(self):
        self.left_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(
            self.left_score,
            self.right_score,
            align="center",
            font=("Courier", 80, "normal")
            )
        self.goto(100, 200)
        self.write(
            self.right_score,
            self.right_score,
            align="center",
            font=("Courier", 80, "normal")
            )

    def game_over(self, winner):
        self.goto(0,0)
        self.write(f"GAMEOVER, {winner}, won!", move=False, align=ALIGNMENT, font=FONT)

       
