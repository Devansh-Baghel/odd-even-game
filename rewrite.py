# Date created: 04-01-2023

import random

runs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
player1 = [True, "player1"]
player2 = [False, "player2"]
toss_choices = [player1, player2]
toss_decision_choices = ["batting", "bowling"]

def play_game():
	# Toss
	toss_winning_player = random.choice(toss_choices)
	if toss_winning_player[0] == True:
		toss_loosing_player = [False, "player2"]
	else:
		toss_loosing_player = [True, "player1"]

	print("The toss has been won by:", toss_winning_player[1])
	print("The toss has been lost by:", toss_loosing_player[1])

	# Decision made by winning player
	toss_decision = random.choice(toss_decision_choices)
	print(f"And {toss_winning_player[1]} has decided to choose {toss_decision}")

	toss_winning_player.append(toss_decision)
	print(toss_winning_player)

	# First Inning
	if toss_winning_player[2] == "batting":
		toss_loosing_player.append("bowling")
		print()
		total = 0
		while True:
			run = random.choice(runs)
			ball = random.choice(runs)
			if run == ball:
				print(f"{toss_winning_player[1]} has been out!!")
				break
			else:
				print(f"Adding {run} to {toss_winning_player[1]}'s total")
				total += run
				print(f"Total runs are {total}")
		print(f"Final total score of {toss_winning_player[1]} is {total}")

	else: # toss winning player has chosen bowling first
		toss_loosing_player.append("batting")
		print()
		print(f"{toss_loosing_player[1]} is batting first")
		total = 0
		while True:
			run = random.choice(runs)
			ball = random.choice(runs)
			if run == ball:
				print(f"{toss_loosing_player[1]} has been out!!")
				break
			else:
				print(f"Adding {run} to {toss_loosing_player[1]}'s total")
				total += run
				print(f"Total runs are {total}")
		print(f"Final total score of {toss_loosing_player[1]} is {total}")


	# Second Inning
	if toss_winning_player[2] == "batting":
		toss_winning_player.append(total)

		print()
		print(f"{toss_loosing_player[1]} is batting second")
		total = 0
		while total < toss_winning_player[3]:
			run = random.choice(runs)
			ball = random.choice(runs)
			if run == ball:
				print(f"{toss_loosing_player[1]} has been out!!")
				break
			else:
				print(f"Adding {run} to {toss_loosing_player[1]}'s total")
				total += run
				print(f"Total runs are {total}")
		print(f"Final total score of {toss_loosing_player[1]} is {total}")
		toss_loosing_player.append(total)
	
	else:
		toss_loosing_player.append(total)

		print()
		print(f"{toss_winning_player[1]} is batting second")
		total = 0
		while total < toss_loosing_player[3]:
			run = random.choice(runs)
			ball = random.choice(runs)
			if run == ball:
				print(f"{toss_winning_player[1]} has been out!!")
				break
			else:
				print(f"Adding {run} to {toss_winning_player[1]}'s total")
				total += run
				print(f"Total runs are {total}")
		print(f"Final total score of {toss_winning_player[1]} is {total}")
		toss_winning_player.append(total)

	print(toss_winning_player)
	print(toss_loosing_player)

	print()
	print()
	print()

	if toss_winning_player[3] > toss_loosing_player[3]:
		print(f"{toss_winning_player[1]} has won the game !!!")
	elif toss_loosing_player[3] > toss_winning_player[3]:
		print(f"{toss_loosing_player[1]} has won the game !!!")
	else:
		print("The Game has been a draw, Playing again")
		play_game()

play_game()