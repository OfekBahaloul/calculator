import calculator


def get_input_loop():
    """
    get an expression from the user and calculate it
    stops when the user give the input "end"
    """
    my_calculator = calculator.Calculator()
    expression = input("give expression: ")
    while expression != "end":
        try:
            num = my_calculator.calculate_expression(expression)
            print("result: \t", num)


        except Exception as e:
            print(e)

        print("\n")
        expression = input("give expression: ")

    print("calculator ends !")


if __name__ == '__main__':
    get_input_loop()


