
# This is a list of dictionary in a container

# Here; There are Four dictionary with same Keys but diff Values

employees = [
    {
        'name' : 'John',
        'age'  : 46 
    },
    {
        'name' : 'Jay',
        'age'  : 39
    },
    {
        'name' : 'Marcus',
        'age'  : 36
    },
    {
        'name' : 'Adam',
        'age'  : 42 
    }
]

#NOTE : it is a list of Dictionaries, We can't print it this way.
'''
print(employees['name'])
print(employees['age'])
'''


            #For test cases Run This.
'''
for employee in employees :
    print(employee['name'])
    print(employee['age'])
print()


print(len(employees)) # This gives as 4
for emp in range(len(employees)): #So for range(len(employees)) = a number.
    print(emp)
print()


print(len(employees))
for emp in range(len(employees)):
    print(employees[emp])
print()


print(len(employees))
for emp in range(len(employees)):
    print(employees[emp]['name'])
print()


for emp in range(len(employees)):
    print(employees[emp]['name'])
    print(employees[emp]['age'])
    print()
'''























































































































































