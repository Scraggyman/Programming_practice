def hangman(word):
        wrong = 0
	stages = ["",
	         "_______            ",
	         "|      |           ",
	         "|      |           ",
	         "|      0           ",
	         "|     /|\          ",
	         "|     / \          ",
	         "|                  ",
	         "|__________________"]
	rletters = list(word)
	board = ["_"] * len(word)
	win = False
	print("Welcome to Gallows!")
# loop make working program
        while wrong < len(stages) - 1:
                print("\n")
                msg = "Enter letter: "
                char = input(msg)
                if char in rletters:
                        cind = rletters.index(char)
                        board[cind] = char
                        rletters[cind] = '$'
                else:
                        wrong += 1
                print((" ".join(board)))
                e = wrong + 1
                print("\n".join(stages[0:e]))
                if "_" not in board:
                        print("You win! The word was: ")
                        print(" ".join(board))
                        win = True
                        break
                if not win:
                        print("\n".join(stages[0: wrong]))
                        print("You loose! The word was: {}.".format(word))
hangman("cat")

                    
