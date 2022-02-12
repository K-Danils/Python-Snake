from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.highScore = self.read_highscore_file()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.sety(250)
        self.write(
            ("Score: "+ str(self.score)+
             "| HighScore: "+ str(self.highScore)),
            move=False,
            align="center",
            font=("Arial", 20, "normal")
            )

    def read_highscore_file(self):
        with open("HighScore.txt") as file:
            return int(file.read())
        
    def write_to_highscore_file(self, score):
        with open("HighScore.txt", "w") as file:
                file.write(str(score))
                
    def increase_score(self):
        self.clear()
        self.score += 1
        if self.score > self.highScore:
            self.highScore += 1
            
        self.write(
            ("Score: "+ str(self.score)+
             "| HighScore: "+
             str(self.highScore)
             ),
            move=False,
            align="center",
            font=("Arial", 20, "normal")
            )

    def reset_score(self):
        if self.score >= self.highScore:
            self.write_to_highscore_file(self.score)
            
        self.clear()
        self.score = 0
        self.write(("Score: " + str(self.score) + "| HighScore: " + str(self.highScore)), move=False, align="center",
                   font=("Arial", 20, "normal"))

