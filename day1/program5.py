player1=int(input("enter the score of player 1"))
player2=int(input("enter the score of player 2"))
player3=int(input("enter the score of player 3"))
strike_player1=player1*100/60
strike_player2=player2*100/60
strike_player3=player3*100/60
print("the strike rate of player1",strike_player1)
print("the strike rate of player2",strike_player2)
print("the strike rate of player3",strike_player3)
print("runs scored by player1 for more than 60 balls:",player1*2)
print("runs scored by player2 for more than 60 balls:",player2*2)
print("runs scored by player3 for more than 60 balls:",player3*2)
print("maximum number of six player1 could hit:",player1//6)
print("maximum number of six player2 could hit:",player2//6)
print("maximum number of six player3 could hit:",player3//6)
