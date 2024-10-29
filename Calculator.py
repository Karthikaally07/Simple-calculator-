print("SIMPLE CALCULATOR")
def add(a,b):
    return a + b
def sub(a,b):
    return a - b 
def mul(a,b):
    return a * b 
def div(a,b):
    return a / b if b != 0 else 0 
def calculate():
    while True:
        a = float(input("Enter the number 1 :"))
        b = float(input("Enter the number 2 : "))
        x = int(input("Enter 1 to add, Enter 2 to subtract , Enter 3 to multiply , Enter 4 to divide  : "))
        if 1 <= x <= 4 :
            switch(x,a,b)
        else :
            print("Enter a Valid number")
            break 
def switch(key,a,b):
    if key == 1 :
        print("Addition of Two numbers", add(a,b))
    elif key == 2 :
        print("Subtraction of Two numbers " , sub(a,b))
    elif key == 3 :
        print("Multiplication of Two numbers ", mul(a,b))
    elif key == 4 :
        print("Division of Two numbers")
        s = div(a,b)
        if s==0:
            print("Zero")
        else :
            print(s)

calculate()