
num1, num2 = 2,0
try:
    print(num1 / num2)
except ZeroDivisionError:
    print("Exception! Division by Zero not permitted.")
finally:
    print("Finally block.")