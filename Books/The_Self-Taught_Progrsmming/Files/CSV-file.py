# csv - Comma Separated Values
import csv

with open('st.csv', 'w') as file:
    # the >writer< method which gets the file object and separator.
    w = csv.writer(file, delimiter=',')
    # the >writerow< method gets parameters as list, and can use to write in csv-file
    w.writerow(['one', 'two', 'three'])
    w.writerow(['four', 'five', 'six'])
    w.writerow(['seven', 'eight', 'nine'])


with open("st.csv", 'r') as file:
    # the >reader< method gets the file object and delimitor which separate values
    rd = csv.reader(file, delimiter=',')
    for row in rd:
        print(','.join(row))
        
    

