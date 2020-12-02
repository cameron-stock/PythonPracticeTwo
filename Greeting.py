first_name = input("Please enter your first name:")
last_name = input("Now, please enter your last name:")

#for Python 2 
message = "Hello %s %s" % (first_name, last_name)


#for Python 3.6 +
message = f"Hello {first_name} {last_name}."
print(message) 

