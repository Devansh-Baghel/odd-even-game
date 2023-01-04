import random

runs = [1,2,3,4,5,6,7,8,9,10]
toss_choice = ["odd", "even"]
bat_or_ball = ["batting", "bowling"]

#### ----- Toss ----- ####

a_toss_runs = random.choice(runs)
a_toss_choice = random.choice(toss_choice)

a_toss_final = [a_toss_runs, a_toss_choice]

b_toss_runs = random.choice(runs)

toss_sum = a_toss_runs + b_toss_runs

if a_toss_choice == "odd":
    b_toss_final = [b_toss_runs, "even"]

    if toss_sum % 2 == 1:
        toss_winner = "a"
        toss_losser = "b"
    else:
        toss_winner = "b"
        toss_losser = "a"
else:
    b_toss_final = [b_toss_runs, "odd"]

    if toss_sum % 2 == 1:
        toss_winner = "a"
    else:
        toss_winner = "b"

print(f"The winner of the toss is {toss_winner}")

#### ----- Toss decision ----- ####

bat_or_ball = random.choice(["bat", "bowl"])

print(f"And {toss_winner} choses to {bat_or_ball}")

#### ----- First ining ----- ####

# The Winner will always chose to bat.
toss_winner_runs = int()
def batting():
    toss_winner_runs = [random.choice(runs)]
    toss_losser_bowl = random.choice(runs)
    c = random.choice(runs)
    if toss_winner_runs == toss_losser_bowl:
        print(f"{toss_winner} is out")
        print(f"The total score of {toss_winner} is {sum(toss_winner_runs)}")
    else:
        toss_winner_runs.append(c)
        batting()

batting()

#### ----- Second ining ----- ####
toss_losser_runs = int()

def bowling():
    toss_losser_runs = [random.choice(runs)]
    toss_winner_bowl = random.choice(runs)
    d = random.choice(runs)
    if toss_losser_runs == toss_winner_bowl:
        print(f"{toss_losser} is out")
        print(f"The total score of {toss_losser} is {sum(toss_losser_runs)}")
    else:
        toss_losser_runs.append(d)
        bowling()

bowling()

if toss_winner_runs > toss_losser_runs :
    print(f"The winner of the match is {toss_winner}")
elif toss_losser_runs > toss_winner_runs :
    print(f"The winner of the match is {toss_losser}")
elif toss_winner_runs == toss_losser_runs :
    print("Draw")