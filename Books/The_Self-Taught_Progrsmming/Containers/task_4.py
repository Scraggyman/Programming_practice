profiles = {}
while True:
	weight = input('Enter your weight: ')
	try:
		weight = float(weight)
		break
	except: 
		print('Enter the number pls: ')
		continue
favorite_colour = input('Enter your favorite_colour: ')
favorite_actor = input('Enter your favorite actor: ')
profiles['weight'] = weight
profiles['favorite colour'] = favorite_colour
profiles['favorite actor'] = favorite_actor
for i in profiles:
	print(i, profiles[i], sep = "(^.^)")

