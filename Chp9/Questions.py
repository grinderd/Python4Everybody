import os
os.chdir("'C:\\Users\\David\\PycharmProjects\\Python4Everybody\\Chp9'")
'''
Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn’t matter what the values are. Then you
can use the in operator as a fast way to check whether a string is in the
dictionary
'''

fhand = open("words.txt")

cnt = 0

di = dict()

for row in fhand:
    #print(row)
    row_s = row.split()
    #print(row_s)
    for wd in row_s:
        #print(wd)
        if wd not in di:
            cnt += 1
            di[wd] = cnt
'''
Exercise 2: Write a program that categorizes each mail message by
which day of the week the commit was done. To do this look for lines
that start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the program print
out the contents of your dictionary (order does not matter).

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Sample Execution:
python dow.py

Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}

'''

fhand = open("mbox-short.txt")
di = dict()

for line in fhand:
    print(line)
    #print(len(line))
    #print(line.startswith("From"))
    #line = line.rstrip()
    if len(line) >0 and line.startswith("From "):
        line_s = line.split()
        print(line_s[2])
        #print(line_s)
        di[line_s[2]] = di.get(line_s[2],0) + 1
'''
Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from
each email address, and print the dictionary
'''

fhand = open("mbox-short.txt")
di = dict()

for line in fhand:
    print(line)
    #print(len(line))
    #print(line.startswith("From"))
    #line = line.rstrip()
    if len(line) >0 and line.startswith("From "):
        line_s = line.split()
        print(line_s[1])
        #print(line_s)
        di[line_s[1]] = di.get(line_s[1],0) + 1

'''
Exercise 4: Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195\
'''

fhand = open("mbox-short.txt")
di = dict()

for line in fhand:
    print(line)
    #print(len(line))
    #print(line.startswith("From"))
    #line = line.rstrip()
    if len(line) >0 and line.startswith("From "):
        line_s = line.split()
        print(line_s[1])
        #print(line_s)
        di[line_s[1]] = di.get(line_s[1],0) + 1

ll = None
kll = None
for key in di:
    if ll is None or di[key] > ll:
        ll = di[key]
        kll = key

print(kll,' ', di[kll])


'''
Exercise 5: This program records the domain name (instead of the
address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary.

python schoolcount.py

Enter a file name: mbox-short.txt

{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
'''

fhand = open("mbox-short.txt")
di = dict()

for line in fhand:
    print(line)
    #print(len(line))
    #print(line.startswith("From"))
    #line = line.rstrip()
    if len(line) >0 and line.startswith("From "):
        line_s = line.split()
        email = line_s[1]
        #print(line_s[1])
        email = email.translate(email.maketrans('@',' ',''))
        email_s = email.split()
        dom = email_s[1]
        #print(line_s)
        di[dom] = di.get(dom,0) + 1


