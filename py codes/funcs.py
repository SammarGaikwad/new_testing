def calculate(a ,b):
    if(a <= 0 or b <= 0):
        print("Please enter positive numbers only.")
        return
    elif(a > b):
        print("The first number is greater than the second number.")
        print("The sum of", a, "and", b, "is", a + b)
        if(a < b):
            print("The first number is less than the second number.")
            print("The sum of", a, "and", b, "is", a + b)
    else:
        print("The first number is equal to the second number.")
        print("The sum of", a, "and", b, "is", a + b)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
calculate(a, b)

jenjwkwdkjebjkfbbkfbkfbhkjwfkfbkf
