
#Normal Functions

#lambda : allows creating functions quicker that are commonly used/defined
'''
def square(num):
    return num ** 2                 # The ** is for square a number

result = square(5)
print(result)
'''

                                    # The Lambda Function is a built-in; Allows creating functions quicker that are commonly
                                    # used/defined.
                                    # It allows you to create functions without the def
square = lambda num : num ** 2
result2 = square(6)
print(result2)
                                    #After we write lambda; The Next arguments that you want
                                    #to receive within that function {e.g num }
                                    # Then used; [ : ] After This is the we Write the logic


                                    #How to accept more than one parameter in your lambda function.
multiply = lambda x,y : x * y
ten_by_ten = multiply(10, 10)
print(ten_by_ten)




































































































































































