# Previous reditions

# 1st
from random import choice
while True:
    if (x := input("r,p,or s? ")) in (y := ("r","You WIN!","p","you TIED!","s","you LOSE!")):
         a = choice((("You won!",-1),("You tied!",0),("You tied!",1)))
         print(f"{a[0]} computer played: {y[y.index(x)+a[1]]}")   
    else: print("answer must be",y)
    
# 2nd
while input("Would you like to quit? y or n?") != "y": 
    if (x := input("r, p, or s? ")) in (y := ("r","p","s","You WON","you TIED","you LOST")):
        print((lambda a:f"{y[a]} against {y[(y.index(x)+a-4)%3]}")(__import__("random").choice((3,4,5))))
    else: print("answer must be r, p, or s.")
 
# 3rd
while input("quit y/n")!="y"and(x:=input("rps?"))in(y:=("r","p","s","won","tied","lost")):print((lambda a:f"{y[a]} against {y[(y.index(x)+a-4)%3]}")(__import__("random").choice((3,4,5))))

# 4th (Current Best)
while input("quit y/n ")!="y":print((lambda a,b:((f"{y[a]} against {y[(y.index(x)+a-4)%3]}")if b else"please enter r,p,s"))(__import__("random").choice((3,4,5)),((x:=input("r,p,s? "))in(y:=("r","p","s","won","tied","lost")))))
