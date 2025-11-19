import csv

lst = [["Star Wars", "Terminator", "Artificial Intelegence"],
       ["fool", "Matilda", "Leviafan"],
       ["Men in Black", "I am robot", "Evolution"]]


with open("task_3.csv", 'w') as file:
    fl = csv.writer(file, delimiter=',')
    fl.writerow(lst[0])
    fl.writerow(lst[1])
    fl.writerow(lst[2])
    
