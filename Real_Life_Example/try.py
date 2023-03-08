from mk_dictionary import employees

get_older_40 = lambda emp: emp['name'] if emp['age'] >= 40 else None

filtered_over_40 = list(filter(get_older_40, employees))

print(filtered_over_40)

[{'name': 'John', 'age': 46}, {'name': 'Adam', 'age': 42}]

