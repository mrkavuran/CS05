# CS5, hw1pr1
# Filename: hw1pr1.py
# Name: İsmail Kavuran
# Problem description: Second Python lab, problem 1!

#################################
#        PLEASE
#         READ
# Note for Part-1
# I prefered confusing and long answers in the comment section because I wanted to convert this homework to game, something like four four. 
# I tried do not use the numbers directly. You can find them as a comment right next to the answers. 
# I hope you like it, have great day!
#################################

#PART-1, NUMBERS
pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example problem (problem 0):  [2, 7, 5, 9]
answer0 = e[0:2] + pi[-2:]  
print("answer0:", answer0)

#Problem 1: Use pi and e to create the list [7, 1]. Store this list in the variable answer1.
answer1 = e[1:] #or, [pi[2]+pi[0],e[1] % e[0]] 
print('Answer1: ', answer1)

#Problem 2: Use pi and/or e to create the list [9, 1, 1]. Store this list in the variable answer2.
answer2 = pi[::-2] #or, [e[1]+e[0], e[1] % e[0], pi[2] - pi[0]]
print('Answer2: ', answer2)

#Problem 3: Use pi and/or e to create the list [1, 4, 1, 5, 9]. Store this list in the variable answer3.
answer3 = pi[1:] #or, [e[1] % e[0], pi[5] // e[0], pi[2] - pi[0], e[1]-e[0],e[1]+e[0]]
print('Answer3: ', answer3)

#Problem 4:Use pi and/or e to create the list [1, 2, 3, 4, 5]. Store this list in the variable answer4.
answer4 = e[::-2]+ pi[::2]  #or, [pi[2] - pi[0], pi[0]-pi[1], e[1] // e[0], pi[5] // e[0], e[1]-e[0]]
print('Answer4: ', answer4)






#PART-2, WORDS
# Lab1 string practice

h = 'harvey'
m = 'mudd'
c = 'college'

# Problem 5:  'hey'
answer5 = h[0] + h[4:6]    
print("answer5:", answer5)

#Problem 6: Create collude and store this string in the variable answer6.   (Our best: 5 ops.)
answer6 = c[0:4]+m[1:3]+h[4]
print(answer6)

#Problem 7: Create arveyudd and store this string in the variable answer7.   (Our best: 3 ops.)
answer7 = h[1:6]+m[1:4]
print(answer7)

#Problem 8: Create hardeharharhar and store this string in the variable answer8. (Our best: 7)  using the crazy construction (h+m)[-2:3:-4]
answer8 = h[0:3] + (h+m)[-2:3:-4] + h[0:3] * 3
print(answer8)

#Problem 9: Create legomyego and store this string in the variable answer9. 
answer9 = c[3:6]+c[1]+m[0]+h[5:]+h[4]+c[5]+c[1]
print(answer9)

#Problem 10: Create clearcall and store this string in the variable answer10.
answer10 = c[::2][0:3] + h[1:3] + c[0] + h[1] + c[2:4]
print(answer10)