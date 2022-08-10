import random as rd
import os

score = 0
score_ai = 0

ai_play =[]

try:
	from training_saves import *
	print('importing training_saves succesfully.\n')
	progress = open('training_saves.py', 'w')
	Box1
except:
	print('failed importing training_saves, creating file...')
	progress = open('training_saves.py', 'w')
	progress.write("Box1 = ['draw']"+"\nBox2 = ['draw']"+"\nBox3 = ['draw']"+"\nBox4 = ['draw']"+"\nBox5 = ['draw']"+"\nBox6 = ['draw']"+"\nBox7 = ['draw']"+"\nBox8 = ['draw']"+"\nBox9 = ['draw']"+"\nBox10 = ['draw']"+"\nBox11 = " + rd.choice(['["draw"]',
'["pass"]'])+"\nBox12 = " + rd.choice(['["draw"]',
'["pass"]'])+"\nBox13 = " + rd.choice(['["draw"]',
'["pass"]'])+"\nBox14 = " + rd.choice(['["draw"]',
'["pass"]'])+"\nBox15 = " + rd.choice(['["draw"]',
'["pass"]'])+"\nBox16= " + rd.choice(['["draw"]',
'["pass"]'])+"\nBox17 = " + rd.choice(['["draw"]',
'["pass"]'])+"\nBox18 = " + rd.choice(['["draw"]',
'["pass"]'])+"\nBox19 = " + rd.choice(['["draw"]',
'["pass"]'])+"\nBox20 = " + rd.choice(['["draw"]',
'["pass"]']))

	print('creating training_saves succesfully.\nPlease rerun.')
	exit()

from training_saves import *

def draw(user):
	global score_ai
	global score
	if user == "ai":
		score_ai += rd.randint(1, 11)
		print(score_ai)
	elif user == "player":
		score += rd.randint(1, 11)
		print('Your score is: ', score)

print("Box1 = " + str(Box1) + "\nBox2 = " + str(Box2) + "\nBox3 = " + str(Box3) + "\nBox4 = " + str(Box4) + "\nBox5 = " + str(Box5) + "\nBox6 = " + str(Box6) + "\nBox7  = " + str(Box7) + "\nBox8 = " + str(Box8) + "\nBox9 = " + str(Box9) + "\nBox10 = " + str(Box10) + "\nBox11 = " + str(Box11) + "\nBox12 = " + str(Box12) + "\nBox13 = " + str(Box13) + "\nBox14 = " + str(Box14) + "\nBox15 = " + str(Box15) + "\nBox16 = " + str(Box16) + "\nBox17 = " + str(Box17) + "\nBox18 = " + str(Box18) + "\nBox19 = " + str(Box19) + "\nBox20 = " + str(Box20))

print('\n')

#MatchboxAI is playing blackjack

def Matchbox():
	global ai_play
	global score_ai
	global Box1, Box2, Box3, Box4, Box5, Box6, Box7, Box8, Box9, Box10, Box11, Box12, Box13, Box14, Box15, Box16, Box17, Box18, Box19, Box20
	score_ai = rd.randint(1, 11)
	print('Start AI score: ', score_ai)
	
	while score_ai <= 21:
		if score_ai == 1:
			ai_play.append('1')
			if rd.choice(Box1) == "draw":
				draw('ai')
			else:
				print("Final AI score: ", score_ai)
				break
		if score_ai == 2:
			ai_play.append('2')
			if rd.choice(Box2) == "draw":
				draw('ai')
			else:
				print("Final AI score: ", score_ai)
				break
		if score_ai == 3:
			ai_play.append('3')
			if rd.choice(Box3) == "draw":
				draw('ai')
			else:
				print("Final AI score: ", score_ai)
				break
		if score_ai == 4:
			ai_play.append('4')
			if rd.choice(Box4) == "draw":
				draw('ai')
			else:
				print("Final AI score: ", score_ai)
				break
		if score_ai == 5:
			ai_play.append('5')
			if rd.choice(Box5) == "draw":
				draw('ai')
			else:
				print("Final AI score: ", score_ai)
				break
		if score_ai == 6:
			ai_play.append('6')
			if rd.choice(Box6) == "draw":
				draw('ai')
			else:
				print("Final AI score: ", score_ai)
				break
		if score_ai == 7:
			ai_play.append('7')
			if rd.choice(Box7) == "draw":
				draw('ai')
			else:
				print("Final AI score: ", score_ai)
				break
		if score_ai == 8:
			ai_play.append('8')
			if rd.choice(Box8) == "draw":
				draw('ai')
			else:
				print("Final AI score: ", score_ai)
				break
		if score_ai == 9:
			ai_play.append('9')
			if rd.choice(Box9) == "draw":
				draw('ai')
			else:
				print("Final AI score: ", score_ai)
				break
		if score_ai == 10:
			ai_play.append('10')
			if rd.choice(Box10) == "draw":
				draw('ai')
			else:
				print("Final AI score: ", score_ai)
				break
		if score_ai == 11:
			ai_play.append('11')
			if rd.choice(Box11) == "draw":
				draw('ai')
			else:
				print("Final AI score: ", score_ai)
				break
		if score_ai == 12:
			ai_play.append('12')
			if rd.choice(Box12) == "draw":
				draw('ai')
			else:
				print("Final AI score: ", score_ai)
				break
		if score_ai == 13:
			ai_play.append('13')
			if rd.choice(Box13) == "draw":
				draw('ai')
			else:
				print("Final AI score: ", score_ai)
				break
		if score_ai == 14:
			ai_play.append('14')
			if rd.choice(Box14) == "draw":
				draw('ai')
			else:
				print("Final AI score: ", score_ai)
				break
		if score_ai == 15:
			ai_play.append('15')
			if rd.choice(Box15) == "draw":
				draw('ai')
			else:
				print("Final AI score: ", score_ai)
				break
		if score_ai == 16:
			ai_play.append('16')
			if rd.choice(Box16) == "draw":
				draw('ai')
			else:
				print("Final AI score: ", score_ai)
				break
		if score_ai == 17:
			ai_play.append('17')
			if rd.choice(Box17) == "draw":
				draw('ai')
			else:
				print("Final AI score: ", score_ai)
				break
		if score_ai == 18:
			ai_play.append('18')
			if rd.choice(Box18) == "draw":
				draw('ai')
			else:
				print("Final AI score: ", score_ai)
				break
		if score_ai == 19:
			ai_play.append('19')
			if rd.choice(Box19) == "draw":
				draw('ai')
			else:
				print("Final AI score: ", score_ai)
				break
		if score_ai == 20:
			ai_play.append('20')
			if rd.choice(Box20) == "draw":
				draw('ai')
			else:
				print("Final AI score: ", score_ai)
				break
		if score_ai == 21:
			print("Final AI score:", score_ai)
			break


def play():
	global score
	playerend = False
	draw('player')
	while playerend == False:
		dop = input('Would you like to draw or pass? [d/p]')
		if dop == 'd':
			draw('player')
			print('\n')
			if score >= 22:
				print('You have scored over 21 points.\n')
				playerend = True
		if dop == 'p':
			print('Your final score is: ', score)
			playerend = True

def Conclusion():
	global score
	global score_ai
	global ai_play
	global Box1, Box2, Box3, Box4, Box5, Box6, Box7, Box8, Box9, Box10, Box11, Box12, Box13, Box14, Box15, Box16, Box17, Box18, Box19, Box20
	
	if score_ai > 21:
		if ai_play[-1] == '1':
			Box1.append('pass')
		if ai_play[-1] == '2':
			Box2.append('pass')
		if ai_play[-1] == '3':
			Box3.append('pass')
		if ai_play[-1] == '4':
			Box4.append('pass')
		if ai_play[-1] == '5':
			Box5.append('pass')
		if ai_play[-1] == '6':
			Box6.append('pass')
		if ai_play[-1] == '7':
			Box7.append('pass')
		if ai_play[-1] == '8':
			Box8.append('pass')
		if ai_play[-1] == '9':
			Box9.append('pass')
		if ai_play[-1] == '10':
			Box10.append('pass')
		if ai_play[-1] == '11':
			Box11.append('pass')
		if ai_play[-1] == '12':
			Box12.append('pass')
		if ai_play[-1] == '13':
			Box13.append('pass')
		if ai_play[-1] == '14':
			Box14.append('pass')
		if ai_play[-1] == '15':
			Box15.append('pass')
		if ai_play[-1] == '16':
			Box16.append('pass')
		if ai_play[-1] == '17':
			Box17.append('pass')
		if ai_play[-1] == '18':
			Box18.append('pass')
		if ai_play[-1] == '19':
			Box19.append('pass')
		if ai_play[-1] == '20':
			Box20.append('pass')

	elif score_ai < score and score < 22:
		if ai_play[-1] == '1':
			Box1.append('draw')
		if ai_play[-1] == '2':
			Box2.append('draw')
		if ai_play[-1] == '3':
			Box3.append('draw')
		if ai_play[-1] == '4':
			Box4.append('draw')
		if ai_play[-1] == '5':
			Box5.append('draw')
		if ai_play[-1] == '6':
			Box6.append('draw')
		if ai_play[-1] == '7':
			Box7.append('draw')
		if ai_play[-1] == '8':
			Box8.append('draw')
		if ai_play[-1] == '9':
			Box9.append('draw')
		if ai_play[-1] == '10':
			Box10.append('draw')
		if ai_play[-1] == '11':
			Box11.append('draw')
		if ai_play[-1] == '12':
			Box12.append('draw')
		if ai_play[-1] == '13':
			Box13.append('draw')
		if ai_play[-1] == '14':
			Box14.append('draw')
		if ai_play[-1] == '15':
			Box15.append('draw')
		if ai_play[-1] == '16':
			Box16.append('draw')
		if ai_play[-1] == '17':
			Box17.append('draw')
		if ai_play[-1] == '18':
			Box18.append('draw')
		if ai_play[-1] == '19':
			Box19.append('draw')
		if ai_play[-1] == '20':
			Box20.append('draw')
	
	
	if score_ai == score or score > 21 and score_ai > 21:
		print('\nIts a tie!\n')
		
	if score < 22 and score > score_ai or score < 22 and score_ai > 21:
		print('\nCongrats, you won!\n')
		
	if score_ai < 22 and score_ai > score or score_ai < 22 and score > 21:
		print('\nYou lost, the AI outplayed you.\n')


play()
Matchbox()
Conclusion()

print("Box1 = " + str(Box1) + "\nBox2 = " + str(Box2) + "\nBox3 = " + str(Box3) + "\nBox4 = " + str(Box4) + "\nBox5 = " + str(Box5) + "\nBox6 = " + str(Box6) + "\nBox7  = " + str(Box7) + "\nBox8 = " + str(Box8) + "\nBox9 = " + str(Box9) + "\nBox10 = " + str(Box10) + "\nBox11 = " + str(Box11) + "\nBox12 = " + str(Box12) + "\nBox13 = " + str(Box13) + "\nBox14 = " + str(Box14) + "\nBox15 = " + str(Box15) + "\nBox16 = " + str(Box16) + "\nBox17 = " + str(Box17) + "\nBox18 = " + str(Box18) + "\nBox19 = " + str(Box19) + "\nBox20 = " + str(Box20))

progress.write("Box1 = " + str(Box1) + "\nBox2 = " + str(Box2) + "\nBox3 = " + str(Box3) + "\nBox4 = " + str(Box4) + "\nBox5 = " + str(Box5) + "\nBox6 = " + str(Box6) + "\nBox7  = " + str(Box7) + "\nBox8 = " + str(Box8) + "\nBox9 = " + str(Box9) + "\nBox10 = " + str(Box10) + "\nBox11 = " + str(Box11) + "\nBox12 = " + str(Box12) + "\nBox13 = " + str(Box13) + "\nBox14 = " + str(Box14) + "\nBox15 = " + str(Box15) + "\nBox16 = " + str(Box16) + "\nBox17 = " + str(Box17) + "\nBox18 = " + str(Box18) + "\nBox19 = " + str(Box19) + "\nBox20 = " + str(Box20))


progress.close()