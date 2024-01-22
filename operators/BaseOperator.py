class Operator:
    def __init__(self, priority_level: float, signature: str, uses_num_operands: int, direction: str):
        """

        :param priority_level: what is priority when calculating an expression, higher priority means he will be
        calculated first
        :param signature: how does the operator looks in a string format
        :param uses_num_operands: how many operands does the operator use
        :param direction: is it an operators that takes operands from his left, his right, or both?
        """

        self.priority_level = priority_level
        self.signature = signature
        self.uses_num_operands = uses_num_operands
        self.direction = direction

    def duplicate(self):
        """

        :return: a new instance with the same attribute values
        """
        return self.__class__()

    def calc_operation(self, expression_list: list, my_index: int):
        """

        :param expression_list: the list where all the operators and operands are
        :param my_index: the index of the operator
        :return: [list of values, the index of the result]
        """
        if my_index - self.uses_num_operands < 0:
            raise ArithmeticError("arithmetic error at operatnd: " + self.signature)

        values = self._get_operands(expression_list, my_index)
        my_index -= self.uses_num_operands

        return [values, my_index]

    def check_direction_correct(self, expression_list: list, index: int):
        """

        :param expression_list: a list that contains the formatted form of an expression
        :param index: the index of this current operator
        :return: nothing, checks if the operator is rounded from his left to right by correct values
        """
        # here checks for more specific type errors, for example directional error when 5! is writen as !5 ->
        # in post fix form such problem is not counted for !

        if self.direction == "right":
            # if there is no right then error because it cant be placed in the end !
            if len(expression_list)-1 == index:
                raise TypeError("cannot put ", self.signature, " in the end of the calculation !")

            value_right = expression_list[index + 1]
            # if the operator works from the right and the place where he should be operating is an operator then its
            # an error !
            if isinstance(value_right,Operator):
                # if the operator is of type attribute then its alright :)
                if not isinstance(value_right, AttributeOperator):
                    raise TypeError("at index: ", index, " there is a ", self.signature, " and to his right side "
                                                                                         "there is an"
                                                                                         "incorrect value!")

            # if to the left of me there is ) or onary left operator then its error !
            if index > 0:
                value_left =  expression_list[index - 1]
                if isinstance(value_left, str) and value_left == ")":
                    raise TypeError("at index: ", index, " there is a ", self.signature, " and to his left side "
                                                                                         "there is )"
                                                                                         "which is wrong !")

                if isinstance(value_left, Operator) and value_left.direction == "left":
                    raise TypeError("at index: ", index, " there is a ", self.signature, " and to his left side "
                                                                                         "there is an left onary"
                                                                                         "which is wrong !")

        # if from the left side of an right operator there is an

        if self.direction == "left":
            # if there is no left then error because it cant be placed in the end !
            if index == 0:
                raise TypeError("cannot put ", self.signature, " in the start of the calculation !")

            # if to the left of the operator there is something that is not ) and not a
            # number and not himself, its wrong !
            value_left = expression_list[index - 1]
            if isinstance(value_left, Operator):
                if value_left.signature == self.signature:
                    return
                if value_left.direction == "left":
                    return

                raise TypeError("at index: ", index, " there is a ", self.signature, " and at his left there is an"
                                                                                     "incorrect value!")

            if isinstance(value_left, str) and value_left == "(":
                raise TypeError("at index: ", index, " there is a ", self.signature, " and at his left there is an"
                                                                                     "incorrect value!")
            # if to the right of me there is ( then its error !
            if len(expression_list)-1 != index:
                value_right = expression_list[index + 1]
                if isinstance(value_right, str) and value_right == "(":
                    raise TypeError("at index: ", index, " there is a ", self.signature, " and to his right side "
                                                                                         "there is ("
                                                                                         "which is wrong !")

        # if to the left of the operator there is ( then its wrong !
        if self.direction == "both":
            if index != 0:
                to_left = expression_list[index - 1]
                if isinstance(to_left, str) and to_left == "(":
                    raise TypeError("at index: ", index, "there is a ", self.signature, "and to his left there is ( "
                                                                                        "which should not be there")

    def _get_operands(self, expression_list: list, my_index: int) -> list:
        """

        :param expression_list: the list where all the operators and operands are
        :param my_index: the index of the operator
        :return: all the operands the operator uses
        """

        to_return_list = []

        expression_list.pop(my_index)
        my_index -= 1

        for i in range(0, self.uses_num_operands):
            to_return_list.append(expression_list.pop(my_index))
            my_index -= 1

        to_return_list.reverse()
        return to_return_list


class AttributeOperator(Operator):
    """
    operator that represent an attribute of a number -> for example if he is a positive or negative
    """
    def __init__(self, priority_level: float, signature: str, uses_num_operands: int, direction: str,
                 attribute_priority: float):
        """

        :param priority_level: the priority of the operator when its function as an operator
        :param signature: how does the operator looks in a string format
        :param uses_num_operands: how many operands does the operator use
        :param direction: is it an operators that takes operands from his left, his right, or both?
        :param attribute_priority: the priority of the operator when its function as an attribute
        """
        Operator.__init__(self, priority_level, signature, uses_num_operands, direction)
        self.attribute_priority = attribute_priority

    def combine_operator(self, expression: str) -> str:
        """

        :param expression: a string that represent a math expression
        :return: the same expression but without duplicates of the same attribute -> combines ------- to just -
        and combine  ---- to --, depends if the amount is odd or even
        """
        result_expression = ""

        combine_counter = 0
        for index in range(len(expression)):
            if expression[index] == self.signature:
                combine_counter += 1

            else:
                if combine_counter != 0:
                    result_expression = self.__add_signature(result_expression, combine_counter)
                    combine_counter = 0

                result_expression += expression[index]

        if combine_counter != 0:
            result_expression = self.__add_signature(result_expression, combine_counter)

        return result_expression

    def apply_attribute(self, expression_list: list, index: int) -> int:
        """

        :param expression_list: a math expression that is represented by a list of numbers and operator
        :param index: the current index of the attribute in the list
        :return: the new index of the attribute (in the case we delete it then the index moves back)
        """
        # if i am alone or double -> aka is there - or --
        # if i am double then check if i should delte myself
        if self.__is_double(expression_list, index):
            # sadly must check if to my right there is an onary type because when i delete the -- then
            # the bad expression becomed good
            if self.__check_if_right_is_onary(expression_list, index):
                raise TypeError("at index ", index, "there is ", self.signature, " and there is to his right an"
                                                                                 "operator")

            # if its the end then, change both to prime onary
            if index == 1:
                expression_list.pop(index)
                expression_list.pop(index - 1)
                return index - 2

            # the value after the double --
            far_value = expression_list[index - 2]

            # if the far value is an operator but not left you can delete it
            if isinstance(far_value, Operator):
                if not far_value.direction == "left":
                    expression_list.pop(index)
                    expression_list.pop(index - 1)
                    return index - 2

            # if its ( then remove
            if isinstance(far_value, str):
                if far_value == '(':
                    expression_list.pop(index)
                    expression_list.pop(index - 1)
                    return index - 2

        # if i am the first elemnt then i am onary
        if index == 0:
            self.priority_level = self.attribute_priority
            self.direction = "right"
            self.uses_num_operands = 1
            return index

        # there are at least 2 epxressions
        last_element = expression_list[index - 1]

        # if the priv element is a number then the attribute should be normal
        if isinstance(last_element, float):
            return index

        # if the last elemnt as ) you should be normal
        if last_element == ')':
            return index

        # if the last elemnt an ( then you should be a normal onary
        if last_element == '(':
            self.priority_level = self.attribute_priority
            self.direction = "right"
            self.uses_num_operands = 1
            return index

        # if the last element is an onary opereator that applay to left you should be normal
        if isinstance(last_element, Operator):
            if last_element.direction == "left":
                return index

            # if the last element is an opereator (not left onary) you should be a prime onary
            else:
                self.__change_to_prim_onary()
                return index

        raise TypeError("attribute | " + self.signature + " | could not be in sequence !")

    def __is_double(self, expression_list: list, index: int) -> bool:
        """

        :param expression_list: a math expression that is represented by a list of numbers and operator
        :param index: the index of the current attribute in the expression list
        :return: if there is to the left of this attribute another attribute like him
        """
        if index >= 1:
            before_me = expression_list[index - 1]
            if isinstance(before_me, Operator):
                if before_me.signature == self.signature:
                    return True

        return False

    def __check_if_right_is_onary(self, expression_list: list, index: int):
        """

        :param expression_list: the list that contains all the parts of the expression
        :param index: the current index of this operator in the list
        :return: if this attribute is to the right of an operator when
        """

        # if there isn't something to my right
        if index >= len(expression_list) + 1:
            return False

        # if its another type of operator then its a problem -> i am an atrribute so i should work on operands of ()
        next_to_me = expression_list[index + 1]
        if isinstance(next_to_me, Operator):
            if next_to_me.signature != self.signature:
                return True

        return False

    def __change_to_prim_onary(self):
        """

        :return: nothing, convert the current attribute to be an onary operators that will always be first
        """
        self.priority_level = 100
        self.direction = "right"
        self.uses_num_operands = 1

    def __add_signature(self,expression: str, counter: int) -> str:
        """

        :param expression: the expression string  that contains the function we want to calculate
        :param counter: the amount of operator attributes in a row
        :return: the expression string with the proper amount of operator attributes
        """
        is_even = counter % 2 == 0
        expression += self.signature

        if is_even:
            expression += self.signature

        return expression

