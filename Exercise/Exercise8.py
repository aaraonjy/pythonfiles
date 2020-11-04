def calculate(input1,input2):

    result = pow(input1, input2)
    print(input1, "raises to the power of", input2, "is:", result)

base = int(input("Enter base:"))
power = int(input("Enter power:"))

calculate(base,power)
