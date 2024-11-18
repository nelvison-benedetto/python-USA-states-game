import turtle
import pandas
from score import Scoreboard

screen = turtle.Screen()
screen.title("U.S.A States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

point = turtle.Turtle()
point.color("green")
point.penup()
point.hideturtle()

scoreboard = Scoreboard()

#screen.exitonclick()
# def getmouse_coords(x, y):
#     print(x, y)
# turtle.onscreenclick(getmouse_coords)

isPlaying = True
while (isPlaying is True):
    scoreboard.update_scoreboard()
    answer_state = screen.textinput("State Game","Insert the state: ").lower()
    states_Data = pandas.read_csv("50_states.csv")
    #states_Dict = states_Data.to_dict()
    isFoundstate = False
    state_list = states_Data["state"].to_list()   #["state"] is the column in the table
    for state in state_list:
        if state.lower() == answer_state:
            correct_state = states_Data[states_Data.state == state]
            correct_state_X = correct_state.x.iloc[0]  #senza iloc è una pandas series, non puoi metterla nel goto
            correct_state_Y = correct_state.y.iloc[0]  #ILOC PRENDE DALLA PANDAS SERIES IL VALORE CHE VUOI but select index!
            isFoundstate = True
            scoreboard.increase_score()
            break
    if (isFoundstate is False):
        print("state not found")
        point.goto(0,0)
        point.color("red")
        point.write("Game Over", align="center", font=("Times New Roman", 40, "normal"))
        isPlaying = False


    else:
        point.goto(correct_state_X, correct_state_Y)
        point.write(correct_state.state.iloc[0], align= "center")

screen.exitonclick()
turtle.mainloop()






