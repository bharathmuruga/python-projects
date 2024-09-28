print("welcome to our game")
name=input("enter the your name: ")
print(f"hello {name} welcome")

user_input=input("do you want to play (yes/no): ").lower()
if user_input=="yes":
    print("you are  at center of forest")

    direction=input("enter which direction do you want to go(right/left): ").lower()
    if direction=="right":
        print("you see river")
        choice=input("do you want swim or use boat(swim/boat): ").lower()
        if choice=="swim":
          print("eaten by alligator ,you died, try again")
        else:
           print("found gold , won the game")
     
    elif direction=="left":
       print("you are eaten by a lion ")
    else:
      print("invalid input  game over ")

    
    
else:
    print("you are exiting the game")



