# Python refresher exercises
# part 1 
# May 25, 2020

# - This set of exercises uses topics from refreshers 1 and 2: basic data types and flow control
# - But, you're free to use other python concepts (functions, OOP) as well
# - My solution is directly below, but with a visual buffer so you don't see it accidentally.

# You should have gotten this file by forking the python_ex_1 project from my github
# repo: https://github.com/ChHarding/python_ex_1

# How to work the exercises:
# - Use a debugger to set a break point at the print() at the top of the solution part so you
#  don't accidentally run beyond it and see the solution. This is the "end" breakpoint
# - Set another "start" breakpoint at the print() that shows the start of each part
#  write you code between those break points
# - To run your code, start the debugger (will stop at the "start" breakpoint) and
#  hit step or continue. Once you have your bug free solution, remove the start and
#  end breakpoints and move on to the next part. Here's an example:



# part 0
# This is just a simple example to demonstrate how the start and end
# breakpoint system works
# Task: create a variable with your name and print out Hello <name>
print("start of part 0") # set breakpoint here
# your code here
# Option 1: Creating my name as a variable. 
name = "ezequiel"
print("hello", name)

print("end of 0") # set breakpoint here 

# Option 2: Get Python to ask for my name and then print it. 
print("start of part 0") # set breakpoint here
name = input("Enter your name: ")
print("Hello", name + "!")

print("end of 0") # set breakpoint here 
'''























# solution 1
name = "Chris"
print("Hello", name)
'''

# Before we really start, a couple more things:
# - your solution may be different or even better than what I showed
# - Please get in the habit of documenting your code as you go along
#   You don't need to state the obvious but you should point out anything 
#   that could be interesting later.
# - After you've finished the code for a part (or even more often) you must
#   perform a commit! You should also push your commit to the remote master (Push)
#   once in a while

# Grading:
# - I will grade purely on effort based on your comments and commits!
# - Each part is worth 1 point
# - That means I don't really grade (judge you) by the quality of your code
# - Please give it your best shot and try to get a good result but it's up to you
#   you fancy you want to get. If you're stuck, you can't get a good result,
#   and you're out of time, just put in a (brief) comment about what you tried
#   and move on. If a part always produces an error (i.e. would stop execution)
#   use ''' ''' to comment out the entire part, that way your debugger won't stop!
#   I will still give you your point if I can see that you at least tried ... something!

# Handing in:
# - once you're done type this into your OS console in VS:
# python refresher_ex_1.py > results.txt
# this will run your file and put the output into results.txt.
# on Canvas hand in:
# - your version of this .py file
# - your results.txt
# - tell me the URL of your forked repo 






# part 1
# task:  L = [0, [], [1,2,3,4], [[5],[6,7]], [8,9,10]]
# using both, indexing and slicing on L, assemble and print a new list N that contains:
# [0,2,3,[5,6],8,10] 
# as an example, here's  how i've constructed a similar list X which contains [[2, 3], [10]] from L:
#
# L = [0, [], [1,2,3,4], [[5],[6,7]], [8,9,10]]
# X = [ L[2][1:-1], L[-1][2] ] 
# print(X)  => [[2, 3], [10]]
# You need to do something similar but end up with [0,2,3,[5,6],8,10] instead. One way to work 
# through this is to break the process down in small steps, store result of each step in a new variable
# and use these variables to assemble the final result.
# your code
print("start of part 1") # set breakpoint here
L = [0, [], [1,2,3,4], [[5],[6,7]], [8,9,10]]
LX = [L[0], L[2][1], L[2][2], [L[3][0][0], L[3][1][0]], L[-1][0], L[-1][2]]
print("The list is", LX)

L1 = [0,1,2,3,4,5,6,7,8,9,10]
tmp1 = L1[0]
tmp2 = L1[2]
tmp3 = L1[3]
tmp4 = [L1[5], L1[6]]
tmp5 = L1[-3]
tmp6 = L1[-1]
L2 = [tmp1, tmp2, tmp3, tmp4, tmp5, tmp6]
print("The alternative list is", L2)


  
print("end of 1") # set breakpoint here 
'''

























# solution 2
L = [0, [], [1,2,3,4], [[5],[6,7]], [8,9,10]]
print("L is", L)
tmp1 = L[0] # 0
tmp2 = L[2][1] # 2
tmp3 = L[2][2] # 3
tmp4 = [L[3][0][0], L[3][1][0]] # [5, 6]
tmp5 = L[4][0] # 8
tmp6 = L[4][-1] # 10 
newL = [tmp1, tmp2, tmp3, tmp4, tmp5, tmp6] # create final list
print(newL) # [0, 2, 3, [5, 6], 8, 10]
'''

# part 2
# Task: Break s into sentences (which end in a .), count them and print them out using a loop:
# result: (I truncated them with ...)
# there are 4 sentences:
# Python is an interpreted, high-level, general-purpose programming language
#  Created by Guido van Rossum and first released in 1991, Python ...
#  Its language constructs and object-oriented approach aim to help programmers ...
print("start of part 2") # set breakpoint here
#Option 1. Split the string using the split() function
s = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."

sentences = s.split(".")

print(sentences)
print("This passage has", (len(sentences)-sentences.count("")), "sentences") #fixed the sentence count problem by using the string.count() function and substracting the spaces from the sentences. 


#Option 2. Use NLTK tokens
from nltk.tokenize import sent_tokenize, word_tokenize
s = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."
sent_tokenize(s)
print(sent_tokenize(s))
print("This package has", len(sent_tokenize(s)), "sentences")
print("end of 2") # set breakpoint here 
#I used a natural language processing tool, NLTK, to manage the sentences. This tool does identify the three sentences correctly. 

























# part 3
# Task: 
# - break s into a list of words (i.e. now separated by space)
# - print out the word list (with a loop) so that every 2. word is in full uppercase.
# - optionally remove all periods and commas
# result:
# Python
# IS
# an
# INTERPRETED
# high-level
# GENERAL-PURPOSE
# programming
# LANGUAGE
print("start of part 3") # set breakpoint here
# your code here
s = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."
wordbyword = s.split()



print("end of 3") # set breakpoint here 
'''



























# solution 3
# version 1 - using 1/-1
s = "Python is an interpreted, high-level, general-purpose programming language."
words = s.split()
make_upper = -1  # we start with 1 for normal print-out, then flip -1 for uppercase, then back, etc.
for w in words:
    w = w.replace('.', '') # replace . with empty list
    w = w.replace(',', '') # replace , with empty list
    if make_upper == 1:
        print(w.upper())
    else:
        print(w)
    make_upper *= -1 # flip from 1 to -1 or vice versa

# version 2 - using a flag
s = "Python is an interpreted, high-level, general-purpose programming language."
words = s.split()
make_upper = False  # we start with False for normal print-out, then flip to True for uppercase, then back, etc.
for w in words:
    w = w.replace('.', '') # replace . with empty list
    w = w.replace(',', '') # replace , with empty list
    if make_upper == True:
        print(w.upper())
        make_upper = False # it's currently True, so set to False
    else:
        print(w)
        make_upper = True # it must currently be False, so set to True
'''

# part 4
# task: abbreviate a potentially long string s to have only the x first and x last chars with ... in between.
# for x = 5 this would be: "A very long description" => "A ver...ption" (... is called filler).
# In a loop, set x from 5 to and to 15 and print out x and the abbreviated version 
# there'll be an issue where the result would actually be longer(!) than the un-abbreviated s. 
# For these cases, do not perform your abbreviation, simply print out s. Note that this
# should work for any other string a or filler as well, so don't hardcode things!
# 
# Optional:
# write a general function abbr(s, filler="...", total_width=15) which abbreviates s
# to total_width chars and uses the string filler in between them. Again, make sure the
# result would not be longer than s!
# call your function a couple of times with different parameters and also test edge cases
print("start of part 4") # set breakpoint here
s = "A very long description" # a long string
filler = "..."
# your code here


print("end of 4") # set breakpoint here 
'''






























# solution 4
s = "A very long description" # a long string
filler = "..."
for x in range(5, 15):
    # check if abbreviation would be longer than s
    if x * 2 + len(filler) > len(s):
        print(x, s)
    else:
        abb_str = s[0:x] + filler + s[-x:] # slice off ends and glue together with filler chars
        print(x, abb_str)



def abbr(s, filler="...", total_width=15):
    "returns a copy of s abbreviated to total_width with filler in the middle" 
    x = total_width // 2 # integer division
    rem = total_width % 2 # remainder will be 1 if width is odd
    abb_str = s[0:x+rem] + filler + s[-x:] # for odd width, add one to front
    if len(abb_str) > len(s):
        return s
    return abb_str

# Test
s = "A very long description"
for tw in range(5, len(s)+1):
    print(tw, abbr(s, "...", tw))

# Edge cases
print(abbr("", "...", 0))
print(abbr("", "...", 999))
print(abbr("", "", 0))
print(abbr("", "", 999))
print(abbr("test", "...", 0))
print(abbr("test", "...", 999))
print(abbr("test", "", 0))
print(abbr("test", "", 999))
print(abbr("A very long description", "....................................", 999))
print(abbr("A very long description", "....................................", 0))
'''
