import random

c1=["rock","paper","scissors"]
score=0
time=0
freq = {"rock": 0, "paper": 0, "scissors": 0}

transition = {
    "rock": {"rock": 0, "paper": 0, "scissors": 0},
    "paper": {"rock": 0, "paper": 0, "scissors": 0},
    "scissors": {"rock": 0, "paper": 0, "scissors": 0}
}

reaction = {
    "win": {"rock": 0, "paper": 0, "scissors": 0},
    "lose": {"rock": 0, "paper": 0, "scissors": 0},
    "tie": {"rock": 0, "paper": 0, "scissors": 0}
}

last_user_move = None
last_result = None

def counter(move):
    if move == "rock":
        return "paper"
    elif move == "paper":
        return "scissors"
    elif move == "scissors":
        return "rock"
    

while True:
    #comp=random.choice(c1)
    user = input("Enter your choice(rock,paper,scissors) : ").lower()
    if user not in c1:
        print("invalid input") 
        continue
    time += 1
    freq[user] += 1
    if last_user_move:
        transition[last_user_move][user] += 1

    if last_result:
        reaction[last_result][user] += 1
    #1
    predict1 = max(freq, key=freq.get)   
    #2
    if last_user_move:
        predict2 = max(transition[last_user_move], key=transition[last_user_move].get)
    else:
        predict2 = random.choice(c1)
    #3
    if last_result:
        predict3 = max(reaction[last_result], key=reaction[last_result].get)
    else:
        predict3 = random.choice(c1)
    votes = {"rock": 0, "paper": 0, "scissors": 0}
    votes[predict1] += 1
    votes[predict2] += 1
    votes[predict3] += 1

    predicted_move = max(votes, key=votes.get)   
    comp = counter(predicted_move)
    print(f"Computer chose {comp} and You chose {user}")
    if comp == user:
        print("It was a tie ! ")
    elif comp == "rock":
        if  user == "paper":
            print("You Win ! ")
            score += 1
        elif user == "scissors": 
            print("You Lose :(") 
    elif comp == "paper":
        if  user == "scissors":
            print("You Win ! ")
            score += 1
        elif user == "rock":   
            print("You Lose :(") 
    elif comp == "scissors":
        if  user == "rock":
            print("You Win ! ")
            score += 1
        elif user == "paper":   
            print("You Lose :(") 
    last_user_move = user        
    choice = input("Type any to proceed and 's' to stop : ").lower()
    if choice == "s":
        break                   
print(f"You won {score} times out of {time} ! ")        

        



    
    