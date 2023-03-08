
'''
def even_numbers(list_of_numbers):
    even = []
    for number in list_of_numbers:
        if number % 2 == 0:
            even.append(number)

    return even

even_digits = even_numbers(range(1,10,1))
print(even_digits)
'''


#The Map as the first argument is going to accept the functionality that
#you want to apply for an iterable

def even_number(number):
    if number % 2 == 0:
        return number

#Normally we would have useed below.
'''
even_digits2 = even_number(range(1, 10+1))
'''

#NOTE : map is a way to call your function.
even_digits2 = map(even_number, range(1, 20,1))
#The map First argument is going to accept the functionality that you want
#to apply for an iterable . map(even_number)
#NOTE But Not Calling The Function since calling it is Like = map(even_number(10))

#Then we can pass-in our iterable argument (range(1, 20,1)). iterable argument is a Value.

print(even_digits2) 
# This gave as a map object = <map object at 0x0000016C2A83BF10>
# So in order to reture a list with all of the values;
#Then NOTE : We Used The {List}.
'''
# print(list(even_digits2))
'''
    #This Ptinted = [None, 2, None, 4, None, 6, None, 8, None, 10, None, 12, None, 14, None, 16, None, 18, None]
    #The None are numbers that are not even numbers

# So in order to avoid this; NOTE: Is By Using A Function called Filter
even_digits2_filtered = filter(None, even_digits2)
#The first argument The filter =it search for an expression to filter out.
#And the second argument it expect for an iterable
print(even_digits2_filtered)
# So this also returns a fiter object = <filter object at 0x000002656B6CBF10>
        #  NOTE : BEFORE
    #IT is important to remember that { everything that is a built in function that is
    # going to Return some iterable; at the begining will Return the object }
print(list(even_digits2_filtered))


















