from random import randint
#generate a random linear equation
def equation_1():
    """Generate a linear equation that is random (eg. y = mx + b)
    """
    seperator = ""
    y = randint(-9,9)
    m = randint(-9,9)
    b = randint(-9,9)
    y_str = str(y)
    m_str = str(m)
    b_str = str(b)
    if b != 0:
        if m == 1:
            if b < 0:
                e_q1 = [y_str," = x ",b_str]
                (seperator.join(e_q1))
            else:
                e_q2 = [y_str," = x + ", b_str]
                (seperator.join(e_q2))
        elif m == -1:
            e_q3 = [y_str, " = -x + ", b_str]
            print (seperator.join(e_q3))
        else:
             if b < 0:
                e_q4 = [y_str," = ", m_str, "x ", b_str]
                print(seperator.join(e_q4))
             else:
                e_q5 = [y_str," = ", m_str, "x + ", b_str]
                print(seperator.join(e_q5))
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
    x_v3 = (round(x_v2, 3))
    print("The result needs to be aproximated to 3 decimal places")
    guess = float(input("x ="))
    aprox_guess = (round(guess, 3))
    if aprox_guess == x_v3:
        print("Congratulations, that's correct")
    else:
        print("Wrong, Here's the solution")
        print(y,"-",b,"=",m,"x")
        print(x_v1,"=",m,"x")
        print(x_v1,"/",m,"=",m,"x/",m)
        print(x_v3, "= x")
        print("")

guess_1(equation_1)
