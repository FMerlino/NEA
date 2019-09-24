import random
#generate a random linear equation
def equation_1():
    """Generate a linear equation that is random (eg. y = mx + b)
    """
    y = random.randint(-9,9)
    m = random.randint(-9,9)
    b = random.randint(-9,9)
    if b != 0:
        if m == 1:
            if b < 0:
                print(y,"= x",b)
            else:
                print(y,"= x +", b)
        elif m == -1:
            print(y, "= -x +", b)
        else:
             if b < 0:
                print(y,"=", m, "x", b )
             else:
                print(y,"=", m, "x +", b )
    else:
        equation_1()
    if m == 0:
        equation_1()
        
    x_v1 = y-b
    x_v2 = x_v1/m
    return y, m, b, x_v1, x_v2


#you need to type the value of x
def guess_1(func):
    y, m, b, x_v1, x_v2 = equation_1()
    x_v3 = (round(x_v2, 2))
    guess = float(input("x ="))
    if guess == x_v3:
        print("Congratulations, that's correct")
    else:
        print("Wrong, Here's the solution")
        print(y,"-",b,"=",m,"x")
        print(x_v1,"=",m,"x")
        print(x_v1,"/",m,"=",m,"x/",m)
        print(x_v3, "= x")
#type function to find the type of the value
guess_1(equation_1)
