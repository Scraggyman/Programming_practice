def convertor(enter = None):
	'''интерпетирует любой текст введенный в тип данных float'''
	enter = input('Enter something: ')
	try: 
		enter = float(enter)
	except: 
		print('Error! You couldn\'t ask me interpret string in float. It breaks all laws of logic. ')
	return enter
print(convertor())

