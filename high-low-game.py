from game import data
from art import logo, vs
import random
import time
print(logo)
time.sleep(5)


#generating a random opponent
score = 0

while True:

    opponenet1 = random.choice(data)
    opponenet2 = random.choice(data)
    if opponenet1 == opponenet2:
        opponenet2 = random.choice(data)





    def formating(op):
        op_name = op["name"]
        op_des = op["description"]
        op_country = op["country"]
        return (f"{op_name}, {op_des}, {op_country}")

    print(f"Compare A: {formating(opponenet1)}")
    print(vs)
    print(f"Against B: {formating(opponenet2)}")






    user = input("which celebrity has more followers? a/b ").lower()





    if opponenet1["follower_count"] > opponenet2["follower_count"] and user == "a":
        print("you guessed right, yey!")
        score = score + 1
        print(f"score is {score}")

    elif opponenet1["follower_count"] > opponenet2["follower_count"] and user == "b":
        print("incorrect guess, sorry!")
        print(f"score is {score}")
        break


    elif opponenet1["follower_count"] < opponenet2["follower_count"] and user == "a":
        print("incorrect guess, sorry!")
        print(f"score is {score}")
        break

    elif opponenet1["follower_count"] < opponenet2["follower_count"] and user == "b":
        print("you guessed right, yey!")
        score = score + 1
        print(f"score is {score}")
    time.sleep(8)
    print("___________***********************************************_________________________________________________________")
    print("___________***********************************************_________________________________________________________")



print(f"score is {score}")






