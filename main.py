import calculator


def get_input_loop():
    """
    get an expression from the user and calculate it
    stops when the user give the input "end"
    """
    my_calculator = calculator.Calculator()
    expression = ""

    while expression != "end":

        try:
            expression = input("give expression: ")
            num = my_calculator.calculate_expression(expression)
            print("result: \t", num)

        except EOFError as e:
            print("there is end of file !")
            expression = "end"

        except KeyboardInterrupt as e:
            print("interrupted")
            expression = "end"

        except ValueError as e:
            print("value error: ", e)

        except TypeError as e:
            print("type error: ", e)

        except ZeroDivisionError as e:
            print("division by zero error: ", e)

        except ArithmeticError as e:
            print("calculation error: ", e)


        #except Exception as e:
        #    print(e)

    print("calculator ends !")


if __name__ == '__main__':
    get_input_loop()


