import random

a = random.randint(1,10)

guess = 0
tries = 3

while guess!=a:
	
	print (f'you have {tries} tries')
	guess = int(input("guess: "))
	
	if guess > a:
		print ('too high')
	elif guess < a:
		print ('too low')
	else: 
		print("just right")
		break
	if tries == 1:
		print ('unfortunately, you lost')
		break
	tries-=1
	
