def number1(natural_number = 0):
	'''делит число на 2'''
	natural_number = int(input('Enter integer: '))
	natural_number //= 2 
	return natural_number
	
def number2(number = None):
	'''увеличивает число в 4 раза'''
	if number == None:
		number = int(input('Enter integer: '))
	number *= 4
	return number
n1 = number1()
print(n1)
n1 = int(n1)
print(number2(n1))
