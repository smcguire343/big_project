
#number of domitrains
#status, health
#spend money or take action

import random

#setting up the names for targets to kill
domitrian_names = ["Tyrus", "Cygna", "Gannex", "Lotharias", "Randevald", "Evdoxia"]

#setting up the number of targets to kill to win
count = random.randint(2, 8)

#basic intro
print "Welcome to my game! You must kill all " + str(count) + " of your rivals for the throne"

#determine first target to kill
def determine_target(list):
	to_kill = random.choice(domitrian_names)
	domitrian_names.remove(to_kill)
	return to_kill

#calling upon the determine target function
targeted = determine_target(domitrian_names)

#setting up the player stat that must reach zero for death
player_health = 10

#setting up the player attack strength
might = random.randint(3, 9)

#asking the palyer if they wish to attack or wait
global_question = raw_input("Do you care to attack *a*? Do you care to wait *b*?")

#this was going to be about buying stuff to enhance likelihood you can kill someone
# def primary_interface(user_choice):
# 	if user_choice == "spend" or "Spend" or "SPEND":
# 		spend_money()
# 	elif user_choice == "action" or "Action" or "ACTION":
# 		take_action()
# 	else:
# 		print "You must choose action or spend"
# 		primary_interface(raw_input("Do you want to take *action* or *spend* money?"))


#the basi game interface
def play_game(count, targeted):
	if count >= 0 and player_health >= 0:
		#insert choice option
		#attack
		target_stats(targeted)
		#player picks attack, spend
	elif count >= 0 and player_health == 0:
		print "Sorry, you have died."
	else:
		print "Congratulations! You have killed all opposition!"

#the polayer if they live learns target's strength
#or is updated on target's strength
#unless target is dead
def target_stats(targeted):
	if  might >= 0:
		print "Your target is %s. Your target's might is %i" % (targeted, might)
		approach(global_question)
	else:
		print "You have killed your first target!"
		count =- 1
		play_game(count, random.choice(domitrian_names))

#the player decides if they attack or wait
#I cannot for the life of me get this to work!
def approach(global_question):
	if global_question == "a":
		attack_move(might, count, targeted)
	elif global_question == "b":
		print "You are waiting."
		play_game(count, targeted)
	else:
		print "You must type an 'a' or a 'w'."
		target_stats(targeted)

#this is how you attack a target and randomly determines if you hurt them or take damage
def attack_move(might, count, targeted):	
	dice = random.randint(1, 2)
	if dice == 1:		
		print "You hit them!"
		might -= 1
		target_stats(targeted)
		#functiun that takes tihs away from target
	else:
		print "You missed!"
		player_health -= 1
		if player_health >= 0:
			target_stats(targeted)
		else:
			play_game(count, targeted)

#calling upon the playing game functions
play_game(count, targeted)

# def spend_money():
# 	print "moeny being spent"


# def take_action():
# 	print "action being taken"


# play_game(count, targeted)

# primary_interface(raw_input("Do you want to take *action* or *spend* money?"))
