import calculator


def rapper_calculator(calc: calculator.Calculator, expression: str) -> str:
    """

    :param calc: the calculator
    :param expression: the expression you wished to calculate
    :return: the result of the calculation or an error
    """
    try:
        value = calc.calculate_expression(expression)
        return str(value)

    except Exception as e:
        return "error"


def test_calculator():
    """

    :param expression:
    :return:
    """
    my_calculator = calculator.Calculator()

    # calc errors -> count 25
    assert rapper_calculator(my_calculator, "(1/3)#4") == "error"
    assert rapper_calculator(my_calculator, "!5") == "error"
    assert rapper_calculator(my_calculator, "5()-7") == "error"
    assert rapper_calculator(my_calculator, "--~--5") == "error"
    assert rapper_calculator(my_calculator, "~~4") == "error"
    assert rapper_calculator(my_calculator, "5+-3!") == "error"
    assert rapper_calculator(my_calculator, "(-10)^0.5") == "error"
    assert rapper_calculator(my_calculator, "(10 / (5-5)#)") == "error"
    assert rapper_calculator(my_calculator, "hello") == "error"
    assert rapper_calculator(my_calculator, "pqoiweuryt;alskdjfhg.z,mncvb") == "error"
    assert rapper_calculator(my_calculator, "~3!") == "error"
    assert rapper_calculator(my_calculator, "3.3.3.3 - 7") == "error"
    assert rapper_calculator(my_calculator, "-~1") == "error"
    assert rapper_calculator(my_calculator, "5**6") == "error"
    assert rapper_calculator(my_calculator, "(--~5+4)") == "error"
    assert rapper_calculator(my_calculator, "--~5") == "error"
    assert rapper_calculator(my_calculator, "6)-4") == "error"
    assert rapper_calculator(my_calculator, "5+()4") == "error"
    assert rapper_calculator(my_calculator, "((5)-7") == "error"
    assert rapper_calculator(my_calculator, ")(5)-7(") == "error"
    assert rapper_calculator(my_calculator, "(0.3)!") == "error"
    assert rapper_calculator(my_calculator, "2^243214235342") == "error"
    assert rapper_calculator(my_calculator, "3!!!!!") == "error"
    assert rapper_calculator(my_calculator, "1 (%24)") == "error"
    assert rapper_calculator(my_calculator, "1(!)") == "error"
    assert rapper_calculator(my_calculator, "5(4)") == "error"

    # calc edge cases -> count 24
    assert rapper_calculator(my_calculator, "(3/5/3)") == "0.2"
    assert rapper_calculator(my_calculator, " ") == "0.0"
    assert rapper_calculator(my_calculator, "~--5") == "-5.0"
    assert rapper_calculator(my_calculator, "5*~-5") == "25.0"
    assert rapper_calculator(my_calculator, "~(~(5))") == "5.0"
    assert rapper_calculator(my_calculator, "(1/3)#") == "30.0"
    assert rapper_calculator(my_calculator, "5  7-3") == "54.0"
    assert rapper_calculator(my_calculator, "5+-3") == "2.0"
    assert rapper_calculator(my_calculator, "--5!") == "120.0"
    assert rapper_calculator(my_calculator, "-5!") == "-120.0"
    assert rapper_calculator(my_calculator, "6-(--4^2*--3)") == "-42.0"
    assert rapper_calculator(my_calculator, "6-(-4^2*3)") == "-42.0"
    assert rapper_calculator(my_calculator, "6-( -4^3*3)") == "198.0"
    assert rapper_calculator(my_calculator, "3!!") == "720.0"
    assert rapper_calculator(my_calculator, "0.1##") == "1.0"
    assert rapper_calculator(my_calculator, "-3^2") == "9.0"
    assert rapper_calculator(my_calculator, " -3^3") == "-27.0"
    assert rapper_calculator(my_calculator, "5--4") == "9.0"
    assert rapper_calculator(my_calculator, "5     8") == "58.0"
    assert rapper_calculator(my_calculator, "(-(3*6)-~(3*6))") == "0.0"
    assert rapper_calculator(my_calculator, "-(5*7)") == "-35.0"
    assert rapper_calculator(my_calculator, "0-~-5") == "-5.0"
    assert rapper_calculator(my_calculator, "~-3") == "3.0"
    assert rapper_calculator(my_calculator, "3.2#!") == "120.0"


    # calc general expressions -> count 20
    assert rapper_calculator(my_calculator, "3.+3-5*9.4-12345679#") == "-78.0"
    assert rapper_calculator(my_calculator, "(.05 * 5)# - 7! +(1/3)#") == "-5003.0"
    assert rapper_calculator(my_calculator, "5&-3 * -10 + 5%7 + ~4") == "31.0"
    assert rapper_calculator(my_calculator, "15---3$(-3 ^3) * 5 -- 5") == "5.0"
    assert rapper_calculator(my_calculator, "--7+~-5+~--5*(--3^2+--3^3)--4") == "-164.0"
    assert rapper_calculator(my_calculator, "3  &-6^ 2- (17# * 4 + 4@-3)*5") == "-126.5"
    assert rapper_calculator(my_calculator, " ~(3!! * -0.5 * (0.5 % 0.2))") == "36.0"
    assert rapper_calculator(my_calculator, "15 !&7 *(4 7) -15 4") == "175.0"
    assert rapper_calculator(my_calculator, "~ (1 5%4 /10) # * 20") == "60.0"
    assert rapper_calculator(my_calculator, "9 !$ 1 0!&-5^ 5 / 5 ^ 5 ") == "-1.0"
    assert rapper_calculator(my_calculator, "(12341234*0.001--147&-200)/1000") == "12.541234"
    assert rapper_calculator(my_calculator, "90 % 5 * (25 -- 7&4 ^3$-8 +4)") == "0.0"
    assert rapper_calculator(my_calculator, "(43 *(4!)&( 4+(-3^10) -53)*6 44)") == "664608.0"
    assert rapper_calculator(my_calculator, "1!!!!! %( 25 ^ (5 / 25))") == "1.0"
    assert rapper_calculator(my_calculator, "867--12 34^((-1)$ (16 -16)   )") == "866.0"
    assert rapper_calculator(my_calculator, "(~-75 / 75 + 5 * 0.2 ^ 1.000)#") == "2.0"
    assert rapper_calculator(my_calculator, "25 25 25 ^ 2 / 25 25 25 ^ 1.5") == "502.5186563701"
    assert rapper_calculator(my_calculator, "((17-(5+4^3*0.8 / (10 + 5))) * (2/3))#") == "50.0"
    assert rapper_calculator(my_calculator, "680-(~15 * 20 & 1) -95 - 400 @ 600") == "100.0"
    assert rapper_calculator(my_calculator, "(1 -- (17*  1 / 17) - 25 % 4)*(25)") == "25.0"
