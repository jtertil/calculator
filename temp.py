

value1 = (input("value1? : "))
while type(float(value1)) == str:
    print("str!")
    value1 = (input("value1? : "))
value2 = (input("value2? : "))

print(type(float(value1)))
print(type(float(value2)))

print("type of calculation (1-add, 2-substract, 3-multiply, 4-divide: ")
select = float(input())

if select == 1:
    result = value1 + value2
    print("add result: ", result)
elif select == 2:
    result = value1 - value2
    print("substract result: ", result)
elif select == 3:
    result = value1 * value2
    print("multiply result: ", result)
elif select == 4:
    while value2 == 0:
        print("sorry I can't divide by 0")
        value2 = float(input("value2?: "))
    else:
        result = value1 / value2
        print("divide result: ", result)
else:
    print("error")
