(value1) = float(input("value1? : "))
(value2) = float(input("vailue2? : "))

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
    result = value1 / value2
    print("divide result: ", result)
else:
    print("error")
