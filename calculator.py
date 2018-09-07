x = y = z = 0

com1 = "Please use only numbers and dot (.) as decimal separator"
com2 = "Please select: 1-add, 2-substract, 3-multiply, 4-divide: "
com_e = "Sorry, I can't do this. "

while type(x) != float:
    try:
        x = float(input("x: "))
    except ValueError:
        print (com_e + com1)

while type(y) != float:
    try:
        y = float(input("y: "))
    except ValueError:
        print (com_e + com1)

while type(z) != float or ((z<1) or (z>4)):
    try:
        z = float(input(com2))
    except ValueError:
        print (com_e)

class calculator:
    def addition(x,y):
        print("Add result for %d and %d is: " % (x, y), x+y)

    def subtraction(x,y):
        print("Substract result for %d and %d is: " % (x, y), x-y)

    def multiplication(x,y):
        print("Multiply result for %d and %d is: " % (x, y), x*y)

    def division(x,y):
        try:
            print("Divide result for %d and %d is: " % (x, y), x/y)
        except ZeroDivisionError as err:
            print(com_e + "(" + str(err) + ")")

if z == 1:
    calculator.addition(x,y)
elif z == 2:
    calculator.subtraction(x,y)
elif z == 3:
    calculator.multiplication(x,y)
elif z == 4:
    calculator.division(x,y)
else:
    print("Something goes wrong")
