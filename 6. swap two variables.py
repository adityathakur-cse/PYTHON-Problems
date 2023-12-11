# 1. using third variable
x = int(input("num1: "))
y = int(input("num2: "))
temp = x
print("value of temporary variable is now",x)
x = y
print("the value of x is:",x)
y = temp
print("the value of y is:",y)

# 2. without using third variable
x = int(input("num1: "))
y = int(input("num2: "))
x, y = y, x
print("the value of x is:",x)
print("the value of y is:",y)