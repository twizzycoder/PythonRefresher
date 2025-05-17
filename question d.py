def character_upper_lower(string):
    if string.isupper():
        return "uppercase"
    elif string.islower():
        return "lowercase"


string = input("enter a Letter: ") 

result = character_upper_lower(string)

print("Your letter is : ", result)

    
