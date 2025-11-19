def power():
	'''it powers a number in 2'''
	number = input('Enter the number please: ')
	try:
                number = int(number)
        except:
                print('Enter a number please, for example: 73')
	number = number ** 2
	return number
print(power())


loop = True
while loop:
        power()
