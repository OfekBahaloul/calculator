from operators import AllOperators
from operators import BaseOperator


class Calculator:
    def __init__(self):
        """

        set up the types of calculation the calculator can do or excepts
        """
        self.all_operators = {}

        # add the add operator
        self.__add_operator(AllOperators.AddOperator())

        # add the subtract operator
        self.__add_operator(AllOperators.SubtractOperator())

        # add the divide operator
        self.__add_operator(AllOperators.DivideOperator())

        # add the multiply operator
        self.__add_operator(AllOperators.MultOperator())

        # add the power operator
        self.__add_operator(AllOperators.PowerOperator())

        # add the avg operator
        self.__add_operator(AllOperators.AverageOperator())

        # add the max operator
        self.__add_operator(AllOperators.MaxOperator())

        # add the min operator
        self.__add_operator(AllOperators.MinOperator())

        # add the modulo operator
        self.__add_operator(AllOperators.ModuloOperator())

        # add the not operator
        self.__add_operator(AllOperators.NotOperator())

        # add the factorial operator
        self.__add_operator(AllOperators.FactorialOperator())

        # add the count numbers operator
        self.__add_operator(AllOperators.CountNumberOperator())

    def __add_operator(self, an_operator: BaseOperator.Operator):
        """

        :param an_operator: an instance of an operator
        :return: nothing, it adds the operator into a dictionary where the signature of the operator is the key
        """
        self.all_operators[an_operator.signature] = an_operator

    def calculate_expression(self, expression: str) -> float:
        """

        :param expression: a string representation of a math expression
        :return: the result of such expression
        """
        # first phase -> clean the expression and check for input errors
        expression = self.__clean_phase(expression)

        # second phase -> convert the expression into a list of floats and operators
        expression_list = []
        expression_list = self.__format_phase(expression)
        self.__print_expression_list(expression_list)

        # third phase -> convert the list of values and operators into a post fix expression
        expression_list = self.__covert_phase(expression_list)
        self.__print_expression_list(expression_list)

        # forth phase -> calc the post fix expression
        expression_list = self.__calc_phase(expression_list)
        self.__print_expression_list(expression_list)

        # return the calculation
        return expression_list[0]

    def __clean_phase(self, expression: str) -> str:
        """

        :param expression: a string representation of a math expression
        :return: a clean expression, without white spaces, without rows of --, without type error and more
        """
        if len(expression) == 0:
            raise TypeError("you did not any thing !")

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
        expression = expression.replace(' ', '')
        expression = expression.replace('\t', '')

        # check for paris of parenthesis and blanks parenthesis
        parenthesis_symmetric_counter = 0
        priv_char = " "
        for char in expression:
            if char == "(":
                parenthesis_symmetric_counter += 1

            elif char == ")":
                parenthesis_symmetric_counter -= 1

            if parenthesis_symmetric_counter < 0:
                raise ValueError("syntax error,  a parenthesis does not his counter part !")

            if priv_char == "(" and char == ")":
                raise TypeError("a blank parenthesis was enterd !")

            priv_char = char

        if parenthesis_symmetric_counter != 0:
            raise ValueError("syntax error,  a parenthesis does not his counter part !")

        # combine all combined operators -> (--- is -) and (---- is --)
        for operator in self.all_operators.values():
            if isinstance(operator, BaseOperator.AttributeOperator):
                expression = operator.combine_operator(expression)

        if len(expression) == 0:
            raise TypeError("you enterd nothing !")

        return expression

    def __format_phase(self, expression: str) -> list:

        current_value = 0
        expression_list = []
        index = 0
        while not index == len(expression):
            char = expression[index]

            # if it is an operator then push it
            if char in self.all_operators.keys():
                new_operator = self.all_operators[char].duplicate()
                expression_list.append(new_operator)



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

                    if expression[end_index] == ".":
                        count_dots += 1

                    end_index += 1

                # if the number had more than 1 dot, then it is not a number
                if count_dots > 1:
                    message = "there was a number that had " + str(count_dots) + " dots !!"
                    raise ValueError(message)

                # convert all the area of the number in the string into a number and move the index to its end
                value = float(expression[index: end_index])

                # if left is ) then error
                if len(expression_list) >= 1 and isinstance(expression_list[-1], str):
                    if expression_list[-1] == ")":
                        raise TypeError("you entered a ", value, "right next to a ) which is incorrecrt")

                expression_list.append(value)
                index = end_index

        for i in range(len(expression_list)):
            # if there is already sometihng on the expression list and its an atribute then check if you should
            # convert its type into an onary or remove complitly if doubled and onary
            if isinstance(expression_list[i], BaseOperator.AttributeOperator):
                attribute = expression_list[i]
                i = attribute.apply_attribute(expression_list, i)

        # check for directional operators if their direction is valide -> ~5 !=  5~
        for i in range(0, len(expression_list)):
            current_operator = expression_list[i]
            if isinstance(current_operator, BaseOperator.Operator):
                current_operator.check_direction_correct(expression_list, i)

        return expression_list

    def __covert_phase(self, expression_list: list) -> list:
        result_list = []
        operator_list = []

        for value in expression_list:
            # if its a number then push it to the result list
            if isinstance(value, float):
                result_list.append(value)

            # if it's a parenthesis then you should push it in (if its left)
            # or dump all the operators list until you meet the left (it is right)
            elif isinstance(value, str):
                if value == "(":
                    operator_list.append(value)

                elif value == ")":
                    result_list += self.__dump_container(operator_list, value)

            # it is an operator,
            # if len is 0 then push it into the stack
            elif len(operator_list) == 0:
                operator_list.append(value)

            # if not then check if should push it to the stack or dump the stack and push it after words
            elif self.__should_insert_operator(value, operator_list[-1]):
                operator_list.append(value)

            else:
                result_list += self.__dump_container(operator_list, value)
                operator_list.append(value)

        if len(operator_list) != 0:
            operator_list.reverse()
            result_list += operator_list

        return result_list

    def __calc_phase(self, expression_list: list) -> list:
        curr_index = 0
        while len(expression_list) > 1 and curr_index < len(expression_list):
            # if we are in an operator
            if isinstance(expression_list[curr_index], BaseOperator.Operator):
                curr_operator = expression_list[curr_index]
                curr_index = curr_operator.calc_operation(expression_list, curr_index)

            else:
                curr_index += 1

        if len(expression_list) != 1:
            raise ValueError("entered an extra number without an operator !")

        return expression_list

    def __dump_container(self, operation_stuck: list,  value: (str, BaseOperator.Operator)) -> list:
        """

        :param operation_stuck: a stack the containers a sequence of some operators represent by their signature
        :return: a list that contains part or all of the operation stack that shold be inserted into the result list,
        depend on the priority of the operators
        """
        result_list = []
        # dump the container and stop when you reached the bottom or when you incounterd '(' or when you hit
        # an operator that his priority is lower then yours.
        while (len(operation_stuck) != 0
               and self.__should_continue_dump(value, operation_stuck[-1])):
                result_list.append(operation_stuck.pop())


        # if there is a remnent of (,) we should delete it.
        if len(operation_stuck) != 0 and isinstance(operation_stuck[-1],str) and operation_stuck[-1] == "("\
                and isinstance(value, str) and value == ")":
            operation_stuck.pop()

        return result_list

    def __should_insert_operator(self, value_signature: (str, BaseOperator.Operator),
                                 last_signature: (str, BaseOperator.Operator)) -> bool:
        """

        :param value_signature: the signature of the current operator
        :param last_signature: the signatyre of the last operator
        :return: if we should insert the current operator or dump all into result
        """

        # if one of the above is ( then you should insert
        if isinstance(last_signature, str):
            if last_signature == "(":
                return False

        if isinstance(value_signature, str):
            if last_signature == "(":
                return False

        if isinstance(value_signature, BaseOperator.Operator) and isinstance(last_signature, BaseOperator.Operator):
            priority_current = value_signature.priority_level
            priority_last = last_signature.priority_level
            return priority_current > priority_last

        raise TypeError("in the operation stuck there was an instance of an object that was not ment to be there")

    def __should_continue_dump(self, value_signature: (str, BaseOperator.Operator),
                               last_signature: (str, BaseOperator.Operator)) -> bool:
        """

        :param value_signature: the signature of the current operator
        :param last_signature: the signatyre of the last operator
        :return: if we should insert the current operator or dump all into result
        """

        if isinstance(last_signature, str):
            if last_signature == "(":
                return False

        if isinstance(value_signature, str):
            if value_signature == ")":
                return True

        if isinstance(value_signature, BaseOperator.Operator) and isinstance(last_signature, BaseOperator.Operator):
            priority_current = value_signature.priority_level
            priority_last = last_signature.priority_level
            return priority_current <= priority_last

        raise TypeError("in the operation stuck there was an instance of an object that was not ment to be there")

    def __print_expression_list(self, expression_list: list):
        print("the expression list:\t", end="")
        for i in expression_list:
            if isinstance(i, BaseOperator.Operator):
                print("[", i.signature, " | ", i.priority_level, "] ", end="")
            else:
                print(i, " ", end="")
        print("")