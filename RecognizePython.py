num1 = 42 #integer
num2 = 2.3 #float
boolean = True #Primitive data type, Boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, intiialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, intialize list
print(type(fruit)) #log statement
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') #list add value
print(person['name']) #log statement
person['name'] = 'George' #dictionary change value
person['eye_color'] = 'blue' #dictionary add value
print(fruit[2]) #list log statement

if num1 > 45: #if else condition
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5: #elseif condition
    print("It's a short word!")
elif len(string) > 15: 
    print("It's a long word!")
else: 
    print("Just right!")

for x in range(5): #function with parameter
    print(x)
for x in range(2,5): 
    print(x)
for x in range(2,10,3): 
    print(x)
x = 0
while(x < 5): #while loop
    print(x)
    x += 1

pizza_toppings.pop() #list delete value
pizza_toppings.pop(1) #list delete value

print(person) #log statement
person.pop('eye_color') #dictionary delete value
print(person)

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #if coniditional
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): #function declaration
    for num in range(10): #for loop
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #log statement
print_hello_x_or_ten_times(4) #log statement


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)