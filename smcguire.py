
#number of domitrains
#status, health
#spend money or take action

import random

domitrian_names = ["Tyrus", "Cygna", "Gannex", "Lotharias", "Randevald", "Evdoxia"]

count = random.randint(2, 8)

print "Welcome to my game! You must kill all " + str(count) + " of your rivals for the throne"

def determine_target(list):
	to_kill = random.choice(domitrian_names)
	domitrian_names.remove(to_kill)
	return to_kill

targeted = determine_target(domitrian_names)

player_health = 10

might = random.randint(3, 9)

global_question = raw_input("Do you care to attack *a*? Do you care to wait *b*?")

# def primary_interface(user_choice):
# 	if user_choice == "spend" or "Spend" or "SPEND":
# 		spend_money()
# 	elif user_choice == "action" or "Action" or "ACTION":
# 		take_action()
# 	else:
# 		print "You must choose action or spend"
# 		primary_interface(raw_input("Do you want to take *action* or *spend* money?"))


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

def target_stats(targeted):
	if  might >= 0:
		print "Your target is %s. Your target's might is %i" % (targeted, might)
		approach(global_question)
	else:
		print "You have killed your first target!"
		count =- 1
		play_game(count, random.choice(domitrian_names))

def approach(global_question):
	if global_question == "a":
		attack_move(might, count, targeted)
	elif global_question == "b":
		print "You are waiting."
		play_game(count, targeted)
	else:
		print "You must type an 'a' or a 'w'."
		target_stats(targeted)
	
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

play_game(count, targeted)

# def spend_money():
# 	print "moeny being spent"


# def take_action():
# 	print "action being taken"


# play_game(count, targeted)

# primary_interface(raw_input("Do you want to take *action* or *spend* money?"))
