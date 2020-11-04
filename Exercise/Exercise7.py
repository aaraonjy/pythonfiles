def add(num1, num2):
    sum = num1 + num2
    print(sum)

def subtract(num1, num2):
    subtract = num1 - num2
    print(subtract)

def multiply(num1, num2):
    multiply = num1 * num2
    print(multiply)

def divide(num1, num2):
    divide = num1 / num2
    print(divide)

print("1.Add 2.Subtract 3.Multiply 4.Divide")
select = int(input())

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
		add(number_1, number_2)

elif select == 2:
		subtract(number_1, number_2)

elif select == 3:
		multiply(number_1, number_2)

elif select == 4:
	    divide(number_1, number_2)

else:
	print("Invalid input")
