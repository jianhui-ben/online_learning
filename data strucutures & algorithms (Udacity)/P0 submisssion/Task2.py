"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

all_phone=dict()
for i in calls:
    if i[0] in all_phone.keys():
        all_phone[i[0]]+=int(i[3])
    else: all_phone[i[0]]=int(i[3])
    if i[1] in all_phone.keys():
        all_phone[i[1]]+=int(i[3])
    else: all_phone[i[1]]=int(i[3])

sort_phone = sorted(all_phone.items(), key=lambda x: x[1], reverse=True)
print("{} spent the longest time, {} seconds, on the phone during \
September 2016.".format(sort_phone[0][0], sort_phone[0][1]))

#import pandas as pd
#all_phone=[[i[0], int(i[3])] for i in calls]+[[i[1], int(i[3])] for i in calls]
#df = pd.DataFrame(all_phone, columns = ['number', 'duration'])
#longest= df.groupby('number').duration.sum().reset_index().sort_values("duration", ascending=False)
#print(longest['number'][0]
#      + " spent the longest time, "
#      + str(longest['duration'][0]) +" seconds, on the phone during September 2016.")
##O(n)
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

