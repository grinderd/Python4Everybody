'''
Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first
character in the string, printing each letter on a separate line, except backwards
'''

inputstring = input("Please write a string")

index = 1
while index < len(inputstring)+1:
    print(inputstring[(-1)*index])
    index = index +1


'''
Exercise 2: Given that fruit is a string, what doe fruit[:] mean?

'''

#This would be the whole string. 'fruit'

'''
Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the 
letter as arguments.
'''

def count(t_string,t_letter):
    count = 0
    for letter in t_string:
        if letter == t_letter:
            count = count + 1

    print(count)

'''
Exercise 4: There is a string method called count that is similar to the function in the previous exercise.  Read the 
documentation of the method at:

https://docs.python.org/library/stdtypes.html#string-methonds

Write an invocation that counts the number of times the letter a occurs in "banana". 
'''

'banana'.count('a')


'''
Exercise 5: Take the following Python code that stores a string:

str = 'X=DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the string after the colon character and then use the float 
function to convert into a floating point number.
'''

str = 'X=DSPAM-Confidence:0.8475'

conf = str[str.find(':')+1:]

conf = float(conf)
print(conf)

'''
Exercise 6: Read the documentation of the string methods at https;//docs.python.org/library/stdtypes.html#string-methods
You might way to experiment with some of them to make sure you understand how they work.  strip and replace are 
particularly useful.
'''
