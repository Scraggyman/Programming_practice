file = open("st.txt", 'w') # the >open< function create the file 'st.txt'
# if the file doesn't exist, and open if file exists.
#'w' - mode of writing in the file, if the file doen't exist it creates one
# if it exists then delete all contents from the file.
#'r' - mode of reading the file.
#'w+' - mode of reading and writing in the file. Delete all contents in the file
# if it exists, if it doesn't exist then create the new file.

# using the method >write< to write something in the file.
file.write("Hello, world!")
for i in range(20):
    file.write("Python is powerful.\n")


# the method >close< closes the file and do writing in the file
file.close()
