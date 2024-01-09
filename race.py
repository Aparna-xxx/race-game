import random
from turtle import Turtle,Screen


screen=Screen()
screen.setup(500,400)
my_bet=screen.textinput(title="Place a bet",prompt="Guess which turtle will win. Enter any colour of the rainbow: ")
winner=""
colours=["purple","blue","green","yellow","orange","red"]
y_pos=[-70,-40,-10,20,50,80]
my_players=[]
game_on=True
for i in range(0,6):
    tim=Turtle(shape="turtle")
    tim.color(colours[i])
    tim.penup()
    tim.goto(-230,y_pos[i])
    my_players.append(tim)

while game_on:
    for player in my_players:
        if player.xcor()>230:
            game_on=False
            winner=player.pencolor()
            if winner == my_bet:
                print(f"You have won, {winner} came first")
            else:
                print(f"You have lost, {winner} came first")
        rand_dist=random.randint(0,10)
        player.forward(rand_dist)

screen.exitonclick()




