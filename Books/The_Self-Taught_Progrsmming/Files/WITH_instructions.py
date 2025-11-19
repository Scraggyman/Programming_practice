with open("st.txt", 'r') as file:
    for i in file:
        print(i)
 # or another way to do the same

with open("st.txt", 'r') as f:
     print(f.read())
