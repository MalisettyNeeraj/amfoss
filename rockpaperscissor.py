from random import randint
z=1
print('''Enter the thing from
          . rock
          . paper
          . scissor''')
list=["rock", "paper", "scissor"]
while(z!=0):
    computer=list[randint(0,2)]
    user=input()
    if(user==computer):
        print("same score")
    elif(user=="rock"):
        if(computer=="paper"):
            print("user wins")
        else:
            print("computer wins")
    elif(user=="paper"):
        if(computer=="scissor"):
            print("user wins")
        else:
            print("computer wins")
    elif(user=="scissor"):
        if(computer=="rock"):
            print("computer wins")
        else:
            print("user wins")
    else:
        print("enter the spelling correctly")
    
