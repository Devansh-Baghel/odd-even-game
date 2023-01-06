# Date created: 04-01-2023
import random
from time import sleep

# imports for creating better UI
from rich import print
from rich.traceback import install
from rich.console import Console
from rich.padding import Padding
# from pyfiglet import Figlet

# UI elements 
console = Console()
install() # provides better looking errors
input_style = "[bold blue]"
rule_style = "[bold red]"
print_style = "bold green"

# Header Text
'''
f = Figlet(font="doom", justify="center", width=150)
console.print(f.renderText('Odd Even Game'), style="bold blue")
'''
console.rule("[bold red]Enter Player Names")
print()

runs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
player1_name = console.input(f"{input_style}Enter Player 1's Name :right_arrow: :right_arrow: ")
player2_name = console.input(f"{input_style}Enter Player 2's Name :right_arrow: :right_arrow: ")
player1 = [True, player1_name]
player2 = [False, player2_name]
toss_choices = [player1, player2]
toss_decision_choices = ["batting", "bowling"]

def play_game():
	# Toss
	print()
	console.rule(f"{rule_style}Toss")
	print()
	with console.status("[bold green]Tossing...") as status:
		for i in range(1,5):
			sleep(1)
	toss_winning_player = random.choice(toss_choices)
	if toss_winning_player[0] == True:
		toss_loosing_player = [False, player2_name]
	else:
		toss_loosing_player = [True, player1_name]

	console.print("The toss has been won by:", toss_winning_player[1], style=print_style, justify="center")
	# print("The toss has been lost by:", toss_loosing_player[1])

	# Decision made by winning player
	print()
	console.rule(f"{rule_style}Toss Decision")
	print()
	with console.status(f"[bold green]{toss_winning_player[1]} deciding what to choose...") as status:
		for i in range(1,7):
			sleep(1)
	toss_decision = random.choice(toss_decision_choices)
	console.print(f"And {toss_winning_player[1]} has decided to choose {toss_decision}", style=print_style, justify="center")
	print()
	toss_winning_player.append(toss_decision)
	# print(toss_winning_player)

	console.rule(f"{rule_style}First Inning")
	# First Inning
	if toss_winning_player[2] == "batting":
		toss_loosing_player.append("bowling")
		sleep(2)
		print()
		console.print(f"{toss_winning_player[1]} is batting", style="bold blue", justify="center")
		total = 0
		while True:
			sleep(2)
			run = random.choice(runs)
			ball = random.choice(runs)
			if run == ball:
				console.print(f"{toss_winning_player[1]} has been out!!", style="bold red", justify="center")
				print()
				break
			else:
				console.print(f"Adding {run} to {toss_winning_player[1]}'s total", justify="center")
				total += run
				# print(f"Total runs are {total}")
				print()
		console.print(f"Final total score of {toss_winning_player[1]} is {total}", justify="center")

	else: # toss winning player has chosen bowling first
		toss_loosing_player.append("batting")
		sleep(2)
		print()
		console.print(f"{toss_loosing_player[1]} is batting first", style="bold blue", justify="center")
		total = 0
		while True:
			sleep(2)
			run = random.choice(runs)
			ball = random.choice(runs)
			if run == ball:
				console.print(f"{toss_loosing_player[1]} has been out!!", style="bold red", justify="center")
				print()
				break
			else:
				console.print(f"Adding {run} to {toss_loosing_player[1]}'s total", justify="center")
				total += run
				# print(f"Total runs are {total}")
				print()
		console.print(f"Final total score of {toss_loosing_player[1]} is {total}", justify="center")

	print()
	console.rule(f"{rule_style}Second Inning")
	print()
	with console.status(f"[bold green]Waiting for second inning to start...") as status:
		for i in range(1,11):
			sleep(1)
	# Second Inning
	if toss_winning_player[2] == "batting":
		toss_winning_player.append(total)
		sleep(2)
		print()
		console.print(f"{toss_loosing_player[1]} is batting second", style="bold blue", justify="center")
		total = 0
		while total <= toss_winning_player[3]:
			sleep(2)
			run = random.choice(runs)
			ball = random.choice(runs)
			if run == ball:
				console.print(f"{toss_loosing_player[1]} has been out!!", style="bold red", justify="center")
				print()
				break
			else:
				console.print(f"Adding {run} to {toss_loosing_player[1]}'s total", justify="center")
				total += run
				# print(f"Total runs are {total}")
				print()
		console.print(f"Final total score of {toss_loosing_player[1]} is {total}", justify="center")
		toss_loosing_player.append(total)
	
	else:
		toss_loosing_player.append(total)
		sleep(2)
		print()
		console.print(f"{toss_winning_player[1]} is batting second", style="bold blue", justify="center")
		total = 0
		while total <= toss_loosing_player[3]:
			sleep(2)
			run = random.choice(runs)
			ball = random.choice(runs)
			if run == ball:
				console.print(f"{toss_winning_player[1]} has been out!!", style="bold red", justify="center")
				print()
				break
			else:
				console.print(f"Adding {run} to {toss_winning_player[1]}'s total", justify="center")
				total += run
				# print(f"Total runs are {total}")
				print()
		console.print(f"Final total score of {toss_winning_player[1]} is {total}", justify="center")
		toss_winning_player.append(total)


	print()
	print()
	print()

	if toss_winning_player[3] > toss_loosing_player[3]:
		console.print(f"{toss_winning_player[1]} has won the game !!!", style="bold green", justify="center")
	elif toss_loosing_player[3] > toss_winning_player[3]:
		console.print(f"{toss_loosing_player[1]} has won the game !!!", style="bold green", justify="center")
	else:
		console.print("The Game has been a draw, Playing again", style="bold blue")
		play_game()

play_game()

wait = input("Enter any key to exit...")