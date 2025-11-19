def contact():
    name = input("Enter your name: ")
    with open("contact.txt", 'w') as file:
        file.write(name)

while True:
    start = input("Enter anything to start the program.\nEnter 'quit' to leave the program.\n=>")
    if start == 'quit':
        break
    else:
        contact()
        
