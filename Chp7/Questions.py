'''
Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case.
Executing the program will look as follows:

python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
    BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
    SAT, 05 JAN 2008 09:14:16 -0500

You can download the file from: www.py4e.com/code3/mbox-short.txt
'''

shout_it = input("Please enter a valid file name:")

filename = 0
while filename == 0:
    try:
        if shout_it == "done":
            exit()
        fshout = open(shout_it)
    except FileNotFoundError:
        print("\nThe file name you entered \'%s\' is invalid.\n" % shout_it)
        shout_it = input("Please enter a valid file name:")
    else:
        filename = 1

for line in fshout:
    print(line.rstrip().upper())

#C:\Users\David\PycharmProjects\Python4Everybody\Chp7\mbox-short.txt


'''
Exercise 2: Write a program to prompt for a file name, and then read through the file and look for a lines of hte form:

X-DSPAM-Confidence: 0.8475

When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the floating-point 
number of the line.  Count these lines and then compute the total of the spam confidence values from these lines.  When 
you rach the end of the file, print out the average spam confidence.

'''

confid = input("Please enter a valid file name:")

filename = 0
while filename == 0:
    try:
        if confid == "done":
            exit()
        fcon = open(confid)
    except FileNotFoundError:
        print("\nThe file name you entered \'%s\' is invalid.\n" % confid)
        confid = input("Please enter a valid file name:")
    else:
        filename = 1
count = 0
tlt_conf = 0
for line in fcon:
    if not line.lower().startswith('x-dspam-confidence:'):
        continue
    #print(line)
    conf = line[(line.find(':')+1):]
    conf = float(conf)
    tlt_conf = tlt_conf + conf
    count = count +1
    print("Total:", tlt_conf)

avgconf = tlt_conf/count*1.0

#print(tlt_conf)
#print(count)
print("The average confidence is %f." % avgconf)

'''
Exercise 3: Sometimes when programmers get bored or want to have a
bit of fun, they add a harmless Easter Egg to their program. Modify
the program that prompts the user for the file name so that it prints a
funny message when the user types in the exact file name “na na boo
boo”. The program should behave normally for all other files which
exist and don’t exist. Here is a sample execution of the program:

'''

confid = input("Please enter a valid file name:")

filename = 0
while filename == 0:
    try:
        if confid == "done":
            exit()
        if confid == "na na boo boo":
            print("I find you lack of seriousness disturbing.")
            exit()

        fcon = open(confid)
    except FileNotFoundError:
        print("\nThe file name you entered \'%s\' is invalid.\n" % confid)
        confid = input("Please enter a valid file name:")
    else:
        filename = 1
count = 0
tlt_conf = 0
for line in fcon:
    if not line.lower().startswith('x-dspam-confidence:'):
        continue
    #print(line)
    conf = line[(line.find(':')+1):]
    conf = float(conf)
    tlt_conf = tlt_conf + conf
    count = count +1
    print("Total:", tlt_conf)

avgconf = tlt_conf/count*1.0

#print(tlt_conf)
#print(count)
print("The average confidence is %f." % avgconf)


