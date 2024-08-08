def name_and_age (name, age):
    if age < 0: return "Error: Invalid Age"
    else:
        information = name + " is " + str(age) + " years old."
        return information