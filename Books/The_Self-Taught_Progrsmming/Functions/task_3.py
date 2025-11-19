def SomeName(age, sex, name, greeting = 'morning' , language = 'Python' ):
	'''общение с компьютерм'''
	age = input('Please, Enter your age: ')
	sex = input('Please, Enter your sex: ')
	name = input('Please, Enter your name: ')
	greeting = input('Please, write a part of day: ')
	language = input('Please, Enter a language which you use for programming')
	print('Good {}, {}. {} is very simple languge for programming.'.format(greeting, name, language))
	print('I\'m {} year old and i\'m programmer. I\'m {}.'.format(age,sex))
SomeName(1,1,1)
	
