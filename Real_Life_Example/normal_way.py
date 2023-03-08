
from mk_dictionary import employees


def get_older_40(employees_list):
    main_list = []
    for employee in employees_list:
        if employee['age'] >= 40:      #
            main_list.append(employee['name'])

    return main_list

over_40 = get_older_40(employees) 
print(over_40)

'''
            NOTE
    Sine the Object that am iterating on is a dictionary 

if for each in employees
if employee['age'] > 40:   #we used ['age]= means employee at age;
    that is search for the Key at age AND if it Value is {>= 40}

Then append each employees at ['name]
Then we; .append(employee['name']) 


'''
































































































































































