import random
import time

print("\tWELCOME TO SNAKE WATER GUN!!!\t")
t=0
while(t<=5):
    t = t + 1
    user_score=[]
    computer_score=[]
    print("Enter your choice:\n  snake\n  water\n  gun\n")
    user=input("MY CHOICE IS:")
    time.sleep(1)
    lst=["snake","water","gun"]
    c=random.choice(lst)
    print("computers choice is:",c)
    time.sleep(1)
    if user=="snake" and c=="snake":
        user_score.append("0")
        computer_score.append("0")
        print("the game is tied!!\nyou both are choose snake.")
        time.sleep(1)
    elif user=="snake" and c=="water":
        user_score.append("1")
        computer_score.append("0")
        print("yay!! you win.\nsnake is drink the water.")
        time.sleep(1)
    elif user=="snake" and c=="gun":
        user_score.append("0")
        computer_score.append("1")
        print("sorry! you lose and computer is winner.\ngun is killed the snake.")
        time.sleep(1)

    if user == "water" and c == "snake":
        user_score.append("0")
        computer_score.append("1")
        print("sorry! you lose and computer is winner.\nsnake drinks the water")
        time.sleep(1)
    elif user == "water" and c == "water":
        user_score.append("0")
        computer_score.append("0")
        print("the game is tied!!\nyou both are choose water.")
        time.sleep(1)
    elif user == "water" and c == "gun":
        user_score.append("1")
        computer_score.append("0")
        print("yay!! you win.\ngun is flowed in the water.")
        time.sleep(1)

    if user == "gun" and c == "snake":
        user_score.append("1")
        computer_score.append("0")
        print("yay!! you win.\ngun is killed the snake.")
        time.sleep(1)
    elif user == "gun" and c == "water":
        user_score.append("0")
        computer_score.append("1")
        print("sorry! you lose and computer is win.\ngun is flowed in the water.")
        time.sleep(1)
    elif user == "gun" and c == "gun":
        user_score.append(0)
        computer_score.append(0)
        print("the game is tied!!\nyou both are choose gun.")
        time.sleep(1)
        print(user_score)
        print(computer_score)

# game()
# time.sleep(1)
# game()
# time.sleep(1)
# game()
# time.sleep(1)
# game()
# time.sleep(1)
# game()
# time.sleep(1)
else:
    print("thats all!! thank you for playing the game.")
    print("printing score board...")
    time.sleep(2)
    print(f"your score is {user_score}")
    print(f"computers score is {computer_score}")




