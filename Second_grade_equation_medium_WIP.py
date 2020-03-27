from random import randint

#generating the values for the equations
def values():
    a = randint(-9,9)
    b = randint(-9,9)
    c = randint(-9,9)
    b_sqr = b**2
    d = b_sqr - 4*a*c
    d_v2 = d**0.5
    ints = [a, b, c, d_v2]
    return ints

    
def printer():
    ints = values()
    a = ints[0]
    b = ints[1]
    c = ints[2]
    if c == 0:
        values()
    if b == 0:
        values()
    elif a == 0:
        values()
    elif b < 0:
        print(a,"x²", b,"x +", c,"= 0")
    else:
        print(a,"x² +", b,"x +", c, "= 0")


def quadratic_formula():
    ints = values()
    a = ints[0]
    b = ints[1]
    e = -b + ints[3]
    neg_e = -b - ints[3]   
    x = e/2*a
    y = neg_e/2*a
    print(x, y)
    if isinstance(x , complex):
        guess_2()
    x = round(x, 3)
    y = round(y, 3)
    return x, y


def guess_2():
    x, y = quadratic_formula()
    printer()
    print("The result needs to be aproximated to 3 decimal places.")
    guess = float(input("x ="))
    aprox_guess = (round(guess, 3))
    if aprox_guess == x:
        print("Congratulations, that's correct")
    elif aprox_guess == y:
        print("Congratulations, that's correct")
    else:
        print("Wrong, Here's the solution")       
        print("x₁ =", x, "      x₂ =", y)
    
guess_2()