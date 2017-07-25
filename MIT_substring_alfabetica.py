'''
 Alphabetical Substrings (15/15 pontos)

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s
in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

For problems such as these, do not include raw_input statements
or define the variable s in any way. Our automated testing will
provide a value of s for you - so the code you submit in the
following box should assume s is already defined.
If you are confused by this instruction, please review L4
Problems 10 and 11 before you begin this problem set.
'''


s = 'zyxwvutsrqponmlkjihgfedcba'
temp = s[0]
answer = s[0]
for char in range(len(s) - 1):
    if ord(s[char]) <= ord(s[char + 1]):
        temp += s[char + 1]
    else:
        temp = s[char + 1]
    if len(temp) > len(answer):
        answer = temp

print 'Longest substring in alphabetical order is: ', answer
        
        
    
