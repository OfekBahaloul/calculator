from operators import addOperator
from operators import BaseOperator


class Calculator:
    def __init__(self):
        """

        set up the types of calculation the calculator can do or excepts
        """
        self.all_operators = {}

        # add the add operator
        add_operator = addOperator.AddOperator()
        self.all_operators[add_operator.signature] = add_operator

        # add the minus operator

        # add the divide operator

        # add the multiply operator

        # add the sum operator

        # add the ! operator

        # add the avg operator

        # add the delta operator

    def calculate_expression(self, expression: str) -> float:
        """

        :param expression: a string representation of a math expression
        :return: the result of such expression
        """
        # first phase -> clean the expression and check for input errors
        expression = self.__clean_phase(expression)

        # second phaze -> convert the expression into a list of floats and operators
        expression_list = []
        expression_list = self.__format_phase(expression)
        print("the expression list in inner form: ", expression_list)

        # third phase -> convert the list of values and operators into a post fix expression
        print("the expression list in postfix form: ", "--------")

        # forth phase -> calc the post fix expression
        print("the expression list after calculation: ", "--------")

        # return the calculation
        return expression_list[0]

    def __clean_phase(self, expression: str)->str:
        """

        :param expression: a string representation of a math expression
        :return: a clean expression, without white spaces, without rows of --, without type error and more
        """

        # check if the expression is a string
        if not isinstance(expression, str):
            raise TypeError("the expression should be in a string form")

        # check there are no invalid letters in the expression
        for char in expression:
            is_number = '0' <= char <= '9'  # is this char a number ?
            is_dot = char == '.'  # is this char a dot ?
            is_parenthesis = char == ')' or char == '('  # is this char a parenthesis ?
            is_operator = char in self.all_operators.keys()  # is this char a valid operator ?
            is_space = char == ' ' or char == '\t'  # is this char a space or a tab ?

            # a letter is valid if it's one of the following chars
            # if he is not one of those then he in invalid
            is_valid = is_number or is_dot or is_parenthesis or is_operator or is_space
            if not is_valid:
                messege = "this is not a valid letter: " + char
                raise ValueError(messege)

        # remove all white spaces
        expression.replace(' ', '')
        expression.replace('\t', '')

        # combine all combined operators

        # if the first operator is from start type operator add a 0 to the expression
        is_first_a_key = expression[0] in self.all_operators.keys()
        if is_first_a_key and isinstance(self.all_operators[expression[0]], BaseOperator.FirstOperator):
            the_operator = self.all_operators[expression[0]]
            expression = the_operator.get_sub_str() + expression

        return expression

    def __format_phase(self, expression: str) -> list:

        current_value = 0
        expression_list = []
        index = 0
        while not index == len(expression):
            char = expression[index]

            # if it is an operator then push it
            if char in self.all_operators.keys():
                expression_list.append(char)
                index += 1

            # if it is a parenthesis
            elif char == ")" or char == "(":
                expression_list.append(char)
                index += 1

            # if it is a part of a number, calc the number
            elif "0" <= char <= "9" or char == ".":
                end_index = index

                # go to the index where the number end, and count the number of dots it has
                count_dots = 0
                while (end_index < len(expression) and
                       ("0" <= expression[end_index] <= "9" or expression[end_index] == ".")):

                    if char == ".":
                        count_dots = 1

                    end_index += 1

                # if the number had more than 1 dot, then it is not a number
                if count_dots > 1:
                    raise ValueError("there was a number that had- ", count_dots, " dots !!")

                # convert all the area of the number in the string into a number and move the index to its end
                expression_list.append(float(expression[index: end_index]))
                index = end_index

        return expression_list
