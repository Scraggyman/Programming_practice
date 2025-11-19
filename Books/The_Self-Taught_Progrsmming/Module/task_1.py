import statistics
import random

num_lst = []
def number_list(number, value):
    '''The function create a list of numbers. You choose the length of list,
and the value of numbers'''
    x = 0
    while x < number:
        num = random.randint(0,value)
        num_lst.append(num)
        x += 1
    print(num_lst)

while True:
    print("To start the program enter anything. To leave the program enter 'quit'")
    start = input("=>")
    if start == 'quit':
        break
    nmb = input("Enter times: ")
    vl = input("Enter a vaule of number: ")
    try:
        nmb = int(nmb)
        vl = int(vl)
    except:
        print("Error")
    number_list(nmb,vl)
    print(statistics.median_low(num_lst))

