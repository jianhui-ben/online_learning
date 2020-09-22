"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
all_number=[i[0] for i in texts] + [i[1] for i in texts] + [i[0] for i in calls] +[i[1] for i in calls]
print("There are "+ str(len(set(all_number))) + " different telephone numbers in the records.")
# O(n)
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
