# 🧮 Simple Python Calculator  

This is a beginner-friendly **Python calculator program** that performs basic arithmetic operations ➕ ➖ ✖️ ➗.  

## ✨ Features  
- Add two numbers ➕  
- Subtract two numbers ➖  
- Multiply two numbers ✖️  
- Divide two numbers ➗ (with zero-division check ⚡)  
- Error handling for invalid operators 🚫  

## 📌 Code  

```python
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
