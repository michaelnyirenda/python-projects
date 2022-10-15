from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.sety(280)
        self.hideturtle()
        self.score = 0
        self.write(f"Score: {self.score}", False, align="center", font=("",10,""))
        
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, align="center")
        
    def game_over(self):
        self.setpos(0,0)
        self.write(f"GAME OVER", False, align="center")