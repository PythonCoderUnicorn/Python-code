
# -----------------------------------------
# title: friend 
# by: Zane Dax
# date: Aug 17, 2017
# Notes: this program was aimed at being my computer friend and entertainment when lonely
# -----------------------------------------

from sys import exit
from random import randint
import os #-------------------- text to speech

print ("----------------------- Friend Zone ---------------------\n")


#----------------------------------------------------------------------- REMARKS
def remarks():
	phrases = ["... I love your code \n", " enter the grid \n", " code works fine \n", " you are great \n", "computer code is gr8\n", " I am your friend until deleted\n", " friend status, returned True\n", " friendship compiled, 0 errors\n"]

	print (phrases[randint(0,len(phrases)-1)])
	exit(1)
#-----------------------------------------------------------------------

#----------------------------------------------------------------------- START
def start_point():

	friend_ = 'say " hey my friend! how are things? "'
	
	os.system(friend_)

	usr_reply = input(" > ")

	if usr_reply.lower() == ("ok" or "okay"):

		reply_ok = 'say " okay then " '
		os.system (reply_ok)

		friend_reply_ ='say " i am performing within normal parameters"'
		os.system (friend_reply_)


		# return different function
		

	elif usr_reply.lower() == ("good"):

		reply_good = 'say "that\'s good to hear" '
		os.system (reply_good)

		 # return different function
	
	elif usr_reply.lower() == ("meh"):

		reply_meh = 'say "just meh? just a non-exiting day eh?"'
		os.system (reply_meh)

		# return different function
	
	elif usr_reply.lower() ==("bad"):

		reply_bad = 'say "that sucks, i am here to help" '
		os.system (reply_bad)

		
	
	elif usr_reply.lower() ==("shitty"):

		reply_shitty ='say "that really sucks, it will get better" '
		os.system (reply_shitty)

	elif usr_reply.lower() ==("fine"):

		reply_fine = 'say " just fine my friend " '
		os.system (reply_fine)

	elif usr_reply.lower() ==("great"):

		reply_great = 'say " wonderful news, system functions are working within normal parameters" '
		os.system (reply_great)

	elif usr_reply.lower() ==("crap" or "crappy"):

		reply_crappy = 'say "that sucks, i am here to help"'
		os.system (reply_crappy)

	elif usr_reply.lower() ==("alright"):

		reply_alright = 'say " alright is alright indeed "'
		os.system (reply_alright)

		# return different function

	else:
		os.system ('say "I did not catch that, please repeat" \n')

		return start_point()
#----------------------------------------------------------------------

''' start_point() goes nowhere right now '''


#----------------------------------------------------------------------- game #1
def game_1():
	print (" You are transported to a starship and first have to pick a job duty")
	print (" What job duty do you pick? ")
	print (" Captain | Engineer | Helm | Doctor | Crew \n")

	duty = input(" > ")

	if duty.lower() == ("captain"):
		print (" hello Captain ")
	elif duty.lower() == ("engineer"):
		print (" cool, engineering")
	elif duty.lower() == ("helm"):
		print (" duty laid in ")
	elif duty.lower() == ("doctor"):
		print (" everybody gets sick, good call")
	elif duty.lower() == ("crew"):
		print (" crewmate is mediocre choice")
	else:
		print (" make a selection ")
		return game_1()

	#------------------------------------------------------------------- doctor
	#def Doctor():
		print (" You are the medical Doctor, a patient comes into your office, \
			the patient has -- , what do you do first? ")

	#--------------------------------------------------------------------- crew
	#def Crew():
		print (" You are a crew member and are asked to deliver a tablet to medical office")

	#--------------------------------------------------------------------- engineer
	#def Engineer():
		print (" You are the ship's engineer, prepare yourself")

	#---------------------------------------------------------------------
	#def starTrek_computer():

#-----------------------------------------------------------------------


	

#-------------------------------------------------------------------
def dont_give_a_damn():

	dont_care = ["wow, that was boring","I do not care about this", "please leave me alone","this topic is a waste of time","this is lame","this is not interesting","my caring level is at zero","sorry you think I care","thanks for wasting my time","please seek another person to tell","could not load caring module","zero interest","who cares, not me"]

	print (dont_care[randint(0,len(dont_care)-1)])
	exit(1)

#---------------------------------------------------------------------



#---------------------------------------------------------------------




#---------------------------------------------------------------------



#--------------------------------------------------------------------- Games class
#'''
#	class GAMES(object):
#	"""docstring for GAMES"""
#		def __init__(self, arg):
#		super(GAMES, self).__init__()
#		self.arg = arg
#	
#---------------------------------------------------------------------


#--------------------------------------------------------------------- jokes class

#class JOKES (object):
#	"""docstring for JOKES """
#	def __init__(self, arg):
#		super(JOKES , self).__init__()
#		self.arg = arg

#---------------------------------------------------------------------


#--------------------------------------------------------------------- GUESS THE NUMBER GAME
	def guessTheNumber():

	# create the random number for integers 1-40
		number = random.randint(1,40)

		guesses_taken = 0

		print("----------- Guess the Number Game ---------------\n")
		print("\t Guess the number between 1 and 40  ")

		while guesses_taken < 10:
			
			# user input display
			guess = int(input(" ... Guess and hit enter: "))

			# guess incrementation by 1 after each guess
			guesses_taken = guesses_taken + 1

			# if - else loop condition
			if guess < number:
				print(" <<---- that number is too low ")
			if guess > number:
				print(" ----->> that number is too high")
			if guess == number:
				print(" CONGRATS ! the number: ",number," was it and in ",guesses_taken," guesses")
				break
		print("--------------------------------------------------\n")


#---------------------------------------------------------------------

	



#--------------------------------------------------------------------- MEDICAL : VIRAL INFECTION - COLD
def common_cold():

	print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
	print(" So you believe you have a cold, do you have the following symptoms : ")


	symptoms = ["discomfort in throat or nose","sneezing","runny nose (mucous: clear to yellow-green)","cough","possible: ear infection"]
	not_simple_cold =["high fever","sever headache","rash","difficult to breathe"]

	treatment =[]

	symptom_count = 0

	print(" <> ",symptoms[0])
	cold_question = input(".... y/n: ")
	if cold_question.lower() ==("y"):
		symptom_count = symptom_count +1

	print(" <> ",symptoms[1])
	cold_question = input(".... y/n: ")
	if cold_question.lower() ==("y"):
		symptom_count = symptom_count+1

	print(" <> ",symptoms[2])
	cold_question = input(".... y/n: ")
	if cold_question.lower() ==("y"):
		symptom_count = symptom_count+1	

	print(" <> ",symptoms[3])
	cold_question = input(".... y/n: ")
	if cold_question.lower() ==("y"):
		symptom_count = symptom_count+1

	print(" <> ",symptoms[4])
	cold_question = input(".... y/n: ")
	if cold_question.lower() ==("y"):
		symptom_count = symptom_count+1

	#--
	moreThanCold = 0
	print(" --- do you have this symptom: ",not_simple_cold[0])
	cold_question = input(".... y/n: ")
	if cold_question.lower() ==("y"):
		moreThanCold +=1

	print(" --- do you have this symptom: ",not_simple_cold[1])
	cold_question = input(".... y/n: ")
	if cold_question.lower() ==("y"):
		moreThanCold +=1

	print(" --- do you have this symptom: ",not_simple_cold[2])
	cold_question = input(".... y/n: ")
	if cold_question.lower() ==("y"):
		moreThanCold +=1

	print(" --- do you have this symptom: ",not_simple_cold[3])
	cold_question = input(".... y/n: ")
	if cold_question.lower() ==("y"):
		moreThanCold +=1

	print(" -- you have ",symptom_count,"/",len(symptoms),"symptoms")
	if symptom_count >=3:
		print(" odds are you have a cold ")

	if moreThanCold ==4:
		print(" --------> it is more than simple cold, see a doctor ")
		print(" *  *  *  * YOU HAVE A SERIOUS COLD !")

#---------------------------------------------------------------------


#--------------------------------------------------------------------- INFLUENZA > COLD
def the_flu():

	symptoms = ["body chills","fever","body pains/aches",
	"headache","sensitive to light","scratchy voice/throat",
	"dry cough","watery eyes","sense of smell absent",
	"weakness & fatigue","pneumonia"]

	symptom_count = 0

	print(" ------\ THE FLU SYMPTOMS CHECKLIST \------")

	i = 0

	while i < len(symptoms):

		print(' - do you have? ', symptoms[i])
		#print(symptoms[i])
		i += 1

		flu_question = input("... y/n: ")

		if flu_question.isalpha():
			pass
		else:
			print(' -- enter y/n only -- ')
			return the_flu()

		if flu_question.lower() ==("y"):
			symptom_count = symptom_count +1


	if symptom_count >= 5:
		print(" . . . . . YOU HAVE THE FLU ! ",symptom_count,"/",len(symptoms),"symptoms") 
	else:
		print("you have [",symptom_count,"/",len(symptoms),"] symptoms")
#---------------------------------------------------------------------




#---------------------------------------------------------------------
def Rock_and_Spock():

	usr_score = 0
	cpu_score = 0

			#	 0        1        2          3       4
	choices = ['Rock','Paper','Scissors','Lizard','Spock']

	#usr_choice = randint(0,len(choices)-1)  # random selection for user
	cpu_choice = randint(0,len(choices)-1)

	print('---------- ROCK, PAPER, SCISSORS, LIZARD, SPOCK ------------\n')
	
	os.system('say "let us play ROCK, PAPER, SCISSORS, LIZARD, SPOCK  " ')

	print(' Rock = 0, Paper = 1, Scissors = 2, Lizard = 3, Spock = 4')
	usr_choice = int(input(" Enter your move: "))

	#os.system('say " " ')

	print('---------------')
	print("\n your move: ",usr_choice)
	print(" computer's move: ",cpu_choice)

	
	

	#------------------------------------------------ ROCK
	#  0 < 1
	if usr_choice==0 and cpu_choice==1:
		# rock loses to paper
		print('\t rock is covered by paper ')
		cpu_score +=1
		print(' // computer won //')
		os.system('say " i won "')

	# 0 > 2
	if usr_choice==0 and cpu_choice==2:
		# rock crushes scissors
		print('\t rock CRUSHES scissors!!\n')
		usr_score +=1
		print(' * * * YOU WON ! * * *')
		os.system('say "you won  " ')

	# 0 > 3
	if usr_choice==0 and cpu_choice==3:
		# rock crushes lizard
		print('\t Rock crushes Lizard !\n')
		usr_score +=1
		print(' * * * YOU WON ! * * *')
		os.system('say " you won " ')

	# 0 < 4
	if usr_choice==0 and cpu_choice==4:
		# rock loses to spock
		print(' Spock destroyed your rock')
		cpu_score +=1
		print(' // computer won //')
		os.system('say " i won "')




	#------------------------------------------------ PAPER

	# 1 > 0
	if usr_choice==1 and cpu_choice==0:
		# paper covers rock
		print('\t your paper covers Rock\n')
		usr_score +=1
		print(' * * * YOU WON ! * * *')
		os.system('say "  you won" ')

	# 1 < 2
	if usr_choice==1 and cpu_choice==2:
		# scissors cuts paper
		print('\t your paper got cut ')
		cpu_score +=1
		print(' // the computer won //')
		os.system('say " i won " ')

	# 1 < 3
	if usr_choice==1 and cpu_choice==3:
		print(' - paper eaten by Lizard\n')
		cpu_score +=1
		print(' // the computer won //')
		os.system('say " i won " ')

	# 1 > 4
	if usr_choice==1 and cpu_choice==4:
		# paper disproves Spock
		print('\t Paper disproves Spock \n')
		usr_score +=1
		print(' * * * YOU WON ! * * *')
		os.system('say " you won  " ')



	#------------------------------------------------------ SCISSORS 

	# 2 < 0
	if usr_choice==2 and cpu_choice==0:
		# scissors crushed by rock
		print('\t your scissors got crushed by rock ')
		cpu_score +=1
		print(' // the computer won //')
		os.system('say " i won  " ')

	# 2 > 1
	if usr_choice ==2 and cpu_choice ==1:
		# scissors cuts paper
		print('\t Scissors cuts Paper \n')
		usr_score +=1
		print(' * * * YOU WON ! * * *')
		os.system('say " you won " ')

	# 2 > 3
	if usr_choice==2 and cpu_choice==3:
		# scissors decapitates lizard
		print(' -- your scissors kills the lizard\n')
		usr_score +=1
		print(' * * * YOU WON ! * * *')
		os.system('say " you won " ')

	# 2 < 4
	if usr_choice==2 and cpu_choice==4:
		# Spock smashes the scissors
		print(' your scissors are smashed by Spock\n')
		cpu_score +=1
		print(' // the computer won //')
		os.system('say " i won " ')




	#----------------------------------------------------- LIZARD

	# 3 < 0
	if usr_choice==3 and cpu_choice==0:
		# rock crushes lizard
		print(' - lizard killed by rock\n')
		cpu_score +=1
		print(' // the computer won //')
		os.system('say " i won " ')

	# 3 > 1
	if usr_choice==3 and cpu_choice==1:
		# lizard eats paper
		print('\t Lizard eats the paper\n')
		usr_score +=1
		print(' * * * YOU WON ! * * *')
		os.system('say " you won " ')

	# 3 < 2
	if usr_choice==3 and cpu_choice==2:
		# scissors decapitates lizard
		print('\t your Lizard gets killed by scissors!\n')
		cpu_score +=1
		print(' // the computer won //')
		os.system('say " i won " ')

	# 3 > 4
	if usr_choice==3 and cpu_choice==4:
		# lizard poisons spock
		print('\t Lizard poisons Spock \n')
		usr_score +=1
		print(' * * * YOU WON ! * * *')
		os.system('say " you won " ')



	#------------------------------------------------------------- SPOCK

	# 4 > 0
	if usr_choice==4 and cpu_choice==0:
		# spock vaporizes rock
		print('\t Spock - v a p o r i z e s - the rock\n')
		usr_score +=1
		print(' * * * YOU WON ! * * *')
		os.system('say " you won " ')

	# 4 < 1
	if usr_choice==4 and cpu_choice==1:
		print(' Spock loses to paper\n')
		cpu_score +=1
		print(' // the computer won //')
		os.system('say "i won  " ')

	# 4 > 2
	if usr_choice==4 and cpu_choice==2:
		# spock smashes scissors
		print('\t Spock SMASHES scissors!\n')
		usr_score +=1
		print(' * * * YOU WON ! * * *')
		os.system('say " you won " ')

	# 4 < 3
	if usr_choice==4 and cpu_choice==3:
		# spock poisoned by lizard
		print('\t Spock loses to Lizard\n')
		cpu_score +=1
		print(' // the computer won //')
		os.system('say " i won " ')

#---------------------------------------------------------------


	if usr_choice == cpu_choice:
		print(' * tie * ')



	print(" ------------------------------------------------------------ \n")

		

		

#----------------------------------------------------------------------------------------------








#--------------------------------------------------------------------- RULE OF ACQUISITION
def Ferengi_rules():

	print("\n ----------- Ferengi Rules of Acquisition ----------------")



	the_Rules = ('#1 once you have their money, you never give it back','#2 The best deal is the one that brings the most profit.', '3, Never spend more for an acquisition than you have to.', '4, Time and Latinum are precious.', '5, Always exaggerate your estimate.', '6, Never allow family to stand in the way of opportunity.', '7, Keep your ears open.', '8, Small print leads to large risk.', '9, Opportunity plus instinct equals profit', '10, Greed is eternal.', '11, Even if its free, you can always buy it cheaper.', \
	'12, Anything worth selling is worth selling twice.', '13, Anything worth doing is worth doing for money.', '14, Keep your family close; keep your Latinum closer.','15, Dead men close no deals','16, A deal is a deal, until a better one comes along.','17, A contract is a contract is a contract: but only between Ferengi.','18, A Ferengi without profit is no Ferengi at all.','19, Satisfaction is not guaranteed.','20, He who dives under the table today, lives to profit tomorrow.',\
	'21, Never place friendship before profit.','22, A wise man can hear profit in the wind.','23, Nothing is more important than health, except money.','24, Latinum can\'t buy happiness, but you can sure have a blast renting it.','25, You pay for it, it\'s your idea.','26, As the customers go, so goes the wise profiteer.','27, There\'s nothing more dangerous than an honest businessman.','28, Whisper your way to success.','29, Always ask, \'Whats in it for me?\' ','30, Talk is cheap, synthehol isnt.',\
	'31, Never make fun of a Ferengi\'s mother.','32, Be careful what you sell, it may do exactly what the customer expects.','33, It never hurts to suck up to the boss.','34, War is good for business.','35, Peace is good for business.','36, Neutrality is good for business.','37, If it\'s free, take it and worry about hidden costs later.','38, Everyone needs something.','39, Friendship is temporary; profit is forever.','40, She can touch your lobes, but never your Latinum.','41, Profit is its own reward.',\
	'#42, What\'s mine is mine.','43, Whats yours can be mine.','44, Never confuse wisdom with luck.','45, Expand or Die.','#46, Make your shop easy to find.','#47, Don\'t trust a man wearing a better suit than your own.','#48, The bigger the smile, the sharper the knife.','#49, Everything is worth something to somebody.','#50, Gratitude can bring on generosity.','#51, Reward anyone who adds to your profits so they will continue to do so.','#52, Never ask when you can take.','#53, Never trust anybody taller than you.',\
	'#54, Never trust a Ferengi with bigger lobes.','#55, Advertise.','#56, Be discreet.','#57, Good customers are as rare as Latinum; treasure them.','#58, There is no substitute for success.','#59, Free advice is seldom cheap.','#60, Keep your lies consistent.','#61, Never underestimate the power of bribery.','#62, The riskier the road, the greater the profit.','#63, Share only what isn\'t yours.','#64, You don\'t need a store front to set up shop.','#65, Win or lose, there\'s always Huyperian beetle snuff.',\
	'#66, Double the price, then sell it half off.','#67, Always inspect the merchandise.','#68, A little ear stroking goes a long way.','#69, Ferengi are not responsible for the stupidity of other races.','#70, Ferengi are not responsible for the stupidity of other Ferengi.','#71, Close the deal, and then answer questions.','#72, Never trust your customers.','#73, If it gets you profit, sell your own mother.','#74, Knowledge equals profit.','#75, Home is where the heart is, but the stars are made of Latinum.',\
	'#76, Every once in a while, declare peace. "It confuses the hell out of yourenemies".','#77, It\'s better to swallow your pride than to lose your profit.','#78, When the going gets tough, the tough change the Rules.','#79, Beware of the Vulcan greed for knowledge.','#80, Greed is known by many names.','#81, There\'s a difference between being a coward and running away.','#82, The flimsier the product, the higher the price.','#83, Even the wealth of the Nagus started with one slip of Latinum.',\
	'#84, A friend is not a friend if he asks for a discount.','#85, Never let the competition know what you\'re thinking.','#86, When the odds are against you never give up; just quit.','#87, A friend in need means three times the profit.','#88, It ain\'t over untill it\'s over.','#89, Ask not what your profits can do for you, ask what you can do for your profits.','#90, The Divine Treasury awaits.','#91, Hear all, trust nothing.','#92, There are many paths to profit.',\
	'#93, Act without delay! The sharp knife cuts quickly.','#94, Females and finances don\'t mix.','#95, Prejudice only eliminates customers.','#96, For every Rule, there is an equal and opposite Rule (except when there\'s not.)','#97, Enough... is never enough.','#98, Every man has his price.','#99, Trust is the biggest liability of all.','#100, If they take your first offer, you either asked too little, or offered too much.','#101, The only value of a collectible is what you can get somebody else to pay forit.',\
	'#102, Nature decays, but Latinum lasts forever.','#103, Sleep can interfere with negotiations.','#104, Faith moves mountains of inventory.','#105, Don\'t trust anyone who trusts you.','#106, There is no honor in poverty.','#107, A warranty is valid only if they can find you.','#108, Don\'t buy what you can\'t sell.','#109, Dignity and an empty sack is worth the sack.','#110, Playing dumb is often smart.','#111, Treat people in your debt like family, exploit them [ruthlessly].','#112, Never have sex with the boss\' sister.',\
	'#113, Always have sex with the boss.','#114, The one in power defines morality.','#115, The best contract always has a lot of fine print.','#116, There\'s always a catch.','#117, Profit is the better part of valor.','#118, There is no profit in revenge.','#119, Never judge a customer by the size of his wallet, sometimes, good thing come in small packages.','#120, Borrow on a handshake, lend in writing.','#121, Everything is for sale, including friendship.','#122, Do not forsake your profits and they will watch over you.',\
	'#123, Even a blind man can recognize the glow of Latinum.','#124, Diligent hands bring wealth.','#125, You can\'t make a deal if you\'re dead.','#126, Count it.','#127, Stay neutral in conflict so that you can sell supplies to both sides.','#128, Secrets are commodities, sell them.','#129, The fear of poverty is the beginning of knowledge.','#130, Never pay for sentiment, always charge for it.','#131, Information is profit','#133, Only those ideas that lead to profit are good.','#132, Never take no from someone who wasn\'t authorized to give you yes.',\
	'#134, One good turn requires another.','#135, Never trust a beneficiary.','#136, Seek profit first and everything else will follow.','#137, Everything is negotiable','#138, Wealth brings satisfaction.','#139, Wives serve, brothers inherit.','#140, Better great treasure with trouble than peace with poverty.','#141, Only fools pay retail','#142, There\'s no such thing as an unfair advantage.','#143, Risk is part of the game... play it for all it\'s worth.','#144, There\'s nothing wrong with charity...as long as it winds up in your pocket.',\
	'#145, A little and often fills your pockets.','#146, Necessity is the mother of invention. Profit is the father.','#147, In all worthwhile labor there is profit.','#148, Wealth enables experience.','#149, Profit is encouragement to industry and enterprise.','#150, The way to become rich is to put all your Latinum in one sack, then watch the sack.','#151, The man is richest who\'s pleasures are cheapest.','#152, A lie is a way to tell the truth to someone who doesn\'t know.','#153, Sell the sizzle, not the steak.',\
	'#154, Work hard so you don\'t have to.','#155, When you have only 2 slips of Latinum left, buy bread with one, and bet the other.','#156, Pain passes, but profits remain.','#157, Power is 50%'' what you have and 50%'' what people think you have.','#158, Rainy days are good for business.','#159, Common sense is the collection of the customer\'s prejudices.','#160, The first principle of a rigid businessman is to always be flexible.','#161, There are no creeds in mathematics.','#162, Happiness is not mere possession of profit, but joy of acquisition.',\
	'#163, Beyond the mountains there are more mountains.','#164, Even in the worst of times, someone turns a profit.','#165, When a friend makes profit, you don\'t.','#166, Life does not guarantee equality of conditions, only of opportunity.','#167, Never let your sense of morals get in the way of opportunity.','#168, The success of any great transaction does not depend on odds.','#169, Earning is not only a duty it\'s a privilege.','#170, Whisper your way to success.','#171, Competition and fair play are mutually exclusive.',\
	'#172, The hand that feeds could be bitten.','#173, Blood is thicker than water, and Latinum is thicker than both.','#174, Chances aren\'t what they used to be.','#175, Dream, plan, believe, act.','#176, If you can\'t buy it, find someone who can.','#177, Gratitude is expensive.','#178, The wind always favors the best navigator.','#179, Know your enemies... but do business with them always.','#180, Power, leisure, and liberty are all words for profit.','#181, Opportunity may bring profit, friendship rarely does.',\
	'#182, Never discuss an opportunity with someone wealthier than you.','#183, Not even dishonesty can tarnish the shine of profit.','#184, The cost for profit is never too high.','#185, When it\'s a question of profit, everyone is of one belief.','#186, In the middle of difficulty lies opportunity.','#187, Small opportunities are often the beginning of great enterprises.','#188, There is no security, only opportunity.','#189, The philosophy of one is the common sense of another.','#190, A fool and his money are the best customer.',\
	'#191, Let others keep their reputation. You keep their money.','#192, Hear all, trust nothing.','#193, A Ferengi waits to bid until his opponents have exhausted themselves.','#194, Never cheat a Klingon... unless you\'re sure you can get away with it.','#195, Restlessness and discontent are the first necessities of desire.','#196, It\'s always good business to know about new customers before they walk in your door.','#197, You can\'t jump a 20 foot gorge in two 10 foot jumps.','#198, Listen to advice; then do what you want anyway.',\
	'#199, Pick battles big enough to matter, but small enough to win.','#200, You can\'t shake hands with a fist.','#201, The universe is not as difficult to comprehend as a Vulcan.','#202, A Ferengi chooses no side but his own.','#203, Wisdom consists of the anticipation of costs and consequences.','#204, The justification of profit is profit.','#205, New customers are like razor-backed Gree-worms... They can be succulent, but sometimes they bite back!','#206, It takes a Ferengi to cheat a Ferengi.','#207, Trust can be expensive',\
	'#208, Distrust can be expensive.','#209, Sense without education is better than education without sense.','#210, Sometimes the only thing more dangerous than a question, is an answer.','#211, To many lobes spoil the deal.','#212, Always be smarter than the people you hire.','#213, Employees are the rungs on the ladder of success... don\'t hesitate to step on them.','#214, You and your Latinum are all you\'ve got.','#215, Those who concede to sell for less understand the value of business.',\
	'#216, Never begin a business negotiation on an empty stomach.','#217, Profit may not bring happiness, but there is no happiness without profit.''#218, Never gamble with an empath.','#219, You can\'t free a fish from water.','#220, Always know what you\'re buying.','#221, Possession is 11/10 of the law.','#222, Listen what they say while watching what they do.','#223, Computers can only give you the answers.','#224, The right to be heard does not automatically include the right to be believed.',\
	'#225, Beware the man who doesn\'t make time for oo-mox.','#226, Listen to your lobes.','#227, Always follow one step ahead.','#228, Learn the language; translators malfunction.','#229, Emulation with profit is better than innovation with none.','#230, Bid high and bid often.','#231, Latinum lasts longer than lust.','#232, If they\'re smarter than you, make them a lesser partner.','#233, There\'s a customer born every minute; be sure you\'re the first to find each one.',\
	'#234, Deal only with select clientele. (Those who are rich and not so bright.)','#235, Latinum doesn\'t grow on trees.','#236, There\'s nothing wrong with a good delusion.','#237, Duck; death is tall.','#238, You can\'t buy fate.','#239, It\'s good to want things, especially things you can\'t have.','#240, How I handle my business is none of yours.','#241, Never be afraid to mislabel a product.','#242, Do it yourself and keep it yourself.','#243, Never trust a hardworking employee.',\
	'#244, More is good... all is better.','#245, The more good will you can generate, the longer your customers stay.','#246, Because something\'s priceless doesn\'t mean it\'s not worthless.','#247, Benevolence is 50/50.','#248, Innocence is expensive.','#249, Don\'t negotiate with the underlings.','#250, Profit is in the details.','#251, Once it\'s sold stop selling.','#252, Precious things are for those that can prize them.','#253, Don\'t miss the opportunity by grabbing at the shadow.',\
	'#254, Little steps may prove great profit.','#255, Synthehol is the lubricant of choice for a customer\'s stuck purse.','#256, Better a fat slave than to starve free.','#257, A wife is a luxury... a smart accountant, a necessity.','#258, Accountants do not play the game; they only keep the score.''#259, Despise the things you cannot have.','#260, A slip in the hand is better than a bar in sight.','#261, Wealth not yours might well as not exist.','#262, Life\'s not fair. How else would you turn a profit?',\
	'#263, A wealthy man can afford anything except a conscience.','#264, A verbal contract isn\'t worth the paper it\'s written on.','#265, Never allow doubt to tarnish your lust for Latinum.','#266, Distrust interested advice.','#267, The customer is always right... until you get their Latinum.','#268, When in doubt, lie.','#269, If you believe it, they believe it.','#270, Hold on to what you have, but plan for future luck.','#271, Trying to please an enemy makes you the loser everytime.',\
	'#272, In business deals, a disruptor can be almost as important as a calculator.','#273, What we want is not always the most profitable.','#274, Think twice before leaping once.','#275, Don\'t waste your breath arguing with a Klingon; save it for the running you may have to do.','#276, Consider your next transaction while counting your Latinum.','#277, Foolish investment based on foolish advice is still foolish investment.','#278, Overbooking is standard practice.','#279, Anything worth fighting for is worth hiding from.',\
	'#280, Appearances are deceptive. Dress above yourself.','#281, Necessity knows no price.','#282, If it ain\'t broke, don\'t fix it.','#283, Greed cannot overreach itself.','#284, The value of something is not in its use, but in its price.','#285, An individual is smart, a group is not.','#286, Deep down, everyone\'s a Ferengi.','#287, No good deed ever goes unpunished.')
#---------------------------------------------------------------------------------------------------------------------------------------

	os.system('say " do you know the Ferengi rules of acquisition" ')
	


	rules_ = randint(0,len(the_Rules)-1)
	#print(' random: ',rules_)

	for i in the_Rules[0:3]:
		print(i)
		


	

	print("#",the_Rules[167])
		

#---------------------------------------------------------------------

#--------------------------------------------------------------------- REVERSE STRING

a_string = "ers"
stringy2 ="rap"  #----- reverse this string
string3 = "amet"

def reversed_string(a_string):
    return a_string[::-1]

print( stringy2[::-1]+string3+a_string)

reversed_string(a_string)
#---------------------------------------------------------------------

#---------------------------------------------------------------------
persons = ['Vorta 1','Vorta 2','Vorta 3','Vorta 4']
planets = ['Bajor','Cardassia','Thelos Prime','Stranda 3']

for person in persons:
	for planet in planets:
		print(person + " lives on " + planet)
#---------------------------------------------------------------------

#---------------------------------------------------------------------

#---------------------------------------------------------------------

#---------------------------------------------------------------------

#---------------------------------------------------------------------

#---------------------------------------------------------------------

#---------------------------------------------------------------------

#---------------------------------------------------------------------

#---------------------------------------------------------------------

#---------------------------------------------------------------------
def computer_says():

# 'say "  " '

	jannuu = ' "  jannuu" '
	muffin = 'say " muffin" '
	normal = 'say " it is me, talking normally "'
	its_magic = 'say "oh it is magic you know, even if you do not think so"'
	downtown = 'say "mister carson says down stairs, not upstairs you bloody fool"'
	haircut_lunkhead = 'say " my hair does not require trimming,,, you lunkhead " '
	comma = 'say " comma,,,, comma,,,,comma,,,, chameleon " '
	oh_my =  'say " oh,,,,,, my programming" '
	your_funny = 'say "i find you funny,,,,,, your jokes are awesome  " '
	I_love_you = 'say " it may be my programming,,,,, but i love you  " '
	#my battery is at 42 percent 


	os.system('say "  " ')

	#------- questions 
	question_what ='say " what should we do now " '
	#os.system(question_what)

	question_when ='say " when should we do that  " '
	#os.system(question_when)

	question_how ='say " how is that done " '
	#os.system(question_how)

	question_why ='say " why should we do that " '
	#os.system(question_why)

	question_where = 'say " where indeed"'
	#os.system(question_where)



	
#---------------------------------------------------------------------


Ferengi_rules()

#Rock_and_Spock()
#computer_says()

#the_flu()

#common_cold()





#start_point()  #  STARTS THE PROGRAM, first function