'''print("Hello World")'''

#LIST
'''friends = ["mike" , "jane" , "kevin" , "surya"]
friends[2] = "Atul"
print(friends[2])
'''
'''print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
'''

#LIST FUNCTIONS
'''
lucky_number = ["42","6","4","5","80","1"]
friends = ["Mike" , "Jane" , "Oscar","Oscar" ,"Toby" ,"Atul","Atul", "Atul"]
friends2 = friends.copy()'''
'''friends.extend(lucky_number)'''
'''friends.append("Saloni")'''
'''friends.insert(5, "Saloni")'''
'''friends.clear()'''
'''friends.pop()'''
'''print(friends.index("Mike"))'''
'''print(friends.count("Atul"))'''
'''#lucky_number.sort()
#print(lucky_number)
print(friends2)'''

#TRUPLES
'''coordinates = [(4,32),(6,90), (90,23)]

coordinates

print(coordinates[1])
'''

#FUNCTIONS
'''def say_hi(name, age):
     print("Hello " + name + ", you are " + str(age) + " years old.")

say_hi("Atul", 17)
say_hi("Saloni", 21)
'''
#RETURN STATEMENT

'''def square(num):
    return num * num

results = square(12)
print(results)
'''
#IF STATEMENTS

'''is_male = True
is_tall = True

if is_male and is_tall :
    print("You are a tall male")

elif is_male and not(is_tall):
    print("You are a short male")

elif not(is_male) and is_tall:
    print("You are not a male but are tall")

else:
    print("You are not a male and not tall")'''

#IF STATEMENT AND COMPARISIONS

'''def min_num(num1 , num2 , num3):
    if num1 <= num2 and num1 <= num3 :
        return num1
    elif num2 <= num1 and num2 <= num3 :
        return num2
    else :
        return num3

print(min_num(300,34,3))

def max_num(num1 , num2 , num3):
    if num1 >= num2 and num1 >= num3 :
        return num1
    elif num2 >= num1 and num2 >= num3 :
        return num2
    else :
        return num3

print(max_num(300,34,3))'''

#BUILDING A BETTER CALCULATOR

num1 = float(input("Enter a first number: "))
op = input("Enter a opeartor: ")
num2 = float(input("Enter a second number: "))

if op == "+":
    print(num1 + num2)

elif op == "-":
    print(num1 - num2)

elif op == "/":
    print(num1 / num2)

elif op == "*":
    print(num1 * num2)

else :
    print("Invalid operator")









