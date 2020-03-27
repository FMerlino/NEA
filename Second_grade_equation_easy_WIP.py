from random import randint

#generating the values for the equations
def values():
    b = randint(-9,9)
    c = randint(-9,9)
    d = b**2 - 4*c
    d_v2 = d**0.5
    if b == 0:
        values()
    elif b < 0:
        print("x² ", b,"x+", c, "= 0")
    else:
        print("x² +", b,"x+", c, "= 0")
    ints = [b, d_v2]
    return ints

def quadratic_formula():
    ints = values()
    b = ints[0]
    e = -b + ints[1]
    neg_e = -b - ints[1]   
    x = e/2
    y = neg_e/2
    x = round(x, 3)
    y = round(y, 3)
    return x, y

def guess_2():
    x, y = quadratic_formula()
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

    #a_str = values()
    #b_str = values()
    #c_str = values() 