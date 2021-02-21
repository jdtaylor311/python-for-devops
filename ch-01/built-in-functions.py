#print built in function
print('print() is a built in function. It prints whatever is evaluated between the parantheses to the console')

'''
range built in function
creates a range of numbers given a set of parameters
range can take in multiple parameters
in the paramters below, the first one represents the starting point for the range,
the second parameter represents the ending point for the range not including the number itself,
and the third parameter represents the steps to take for each iteration
etc... [3, 6, 9, 12, 15, 18, 21, 24]
'''
result = range(3,25,3)
print(list(result))
