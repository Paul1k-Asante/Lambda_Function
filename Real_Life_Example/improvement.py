
from mk_dictionary import employees

get_older_40 = lambda emp: emp['name'] if emp['age'] >= 40 else None
# lambda {acting as input} And pass-in the argument {emp is a variable that we will declear}
# Means input emp at ['name'] if condition is True.

#Normaly;
#employees_over_40 = get_older_40(employees)   #( And pass-in employees dictionary)
# But we can't do that.

employees_over_40 = map(get_older_40, employees)
# For Map = we give the functionality first (get_older_40); 
# i.e Refer to the functionality Not calling it 
# AND then; pass the iterable (employees) ; That is the Value of emp = employees
#print(list(employees_over_40))  
#['John', None, None, 'Adam']

filtered_over_40 = list(filter(None, employees_over_40))
#This statement is important because we will get the {None Values} and 
#we have filter it out with the filter method;
# Therfore filter(None, ) from the Object (employees_over_40)
# Then we make it a {list} because of the map.

print(filtered_over_40)




get_older_40_2 = [emp['name'] for emp in employees if emp['age'] >= 40]
print(get_older_40_2)
# ['John', 'Adam']
































































































































