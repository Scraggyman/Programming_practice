# call the >read< method, not close and not open the file next time,
# can do just ONE time, so if we need to use the file some times,
# we have to assign it to variable

my_list = list()
with open("st.txt", "r") as file:
    my_list.append(file.read())

print(my_list)
