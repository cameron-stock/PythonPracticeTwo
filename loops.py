colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

#looping through lists
for color in colors:
    if isinstance(color, int) and color > 50:
        print(color)


#looping through dictionaries
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("%s: %s" % (key, value))


#replacing values
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for value in phone_numbers.values():
    print(value.replace("+", "0"))