from art import logo, vs
from game_data import data
import random
from replit import clear

def account_format(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"

def check(choice, A_followers, B_followers):
    if A_followers > B_followers:
        return choice == "a"
    else: 
        return choice == "b"

print(logo)
score = 0
game_continue = True
random_B = random.choice(data)

while game_continue:
    random_A = random_B
    random_B = random.choice(data)
    if random_A == random_B:
        random_B = random.choice(data)
    print(f"Compare A: {account_format(random_A)}.")
    print(vs)
    print(f"Against B: {account_format(random_B)}.")

    random_A_followers = random_A['follower_count']
    # print(random_A_followers)
    random_B_followers = random_B['follower_count']
    # print(random_B_followers)

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    random_A_followers = random_A['follower_count']
    # print(random_A_followers)
    random_B_followers = random_B['follower_count']
    # print(random_B_followers)
    is_correct = check(choice, random_A_followers, random_B_followers)
    clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"You're right! Current Score: {score}.")
    
    else: 
        game_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")