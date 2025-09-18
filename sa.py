def calculation(a, b, c):
    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)
    elif c == "/":
        if b != 0:
            print(a / b)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Enter a valid operator (+, -, *, /).")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = input("Enter your choice (+, -, *, /): ")
calculation(a, b, c)
