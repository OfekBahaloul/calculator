class Operator:
    def __init__(self, priority_level: int, signature: str, uses_num_operands: int):
        """

        :param priority_level: what is priority when calculating an expression, higher priority means he will be
        calculated first
        :param signature: how does the operator looks in a string format
        :param uses_num_operands: how many operands does the operator use
        """

        self.priority_level = priority_level
        self.signature = signature
        self.uses_num_operands = uses_num_operands

    def calc_operation(self, expression_list: list, my_index: int):
        """

        :param expression_list: the list where all the operators and operands are
        :param my_index: the index of the operator
        :return: nothing, it does the operation on the list
        """
        if my_index - self.uses_num_operands < 0:
            raise ArithmeticError("arithmetic error at operatnd: " + self.signature)

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

        return to_return_list


class FirstOperator:
    """
    any operator that takes 2 or more operands and can be in the start of the string
    for example, in the start of the string there can be +5 but not *5
    """
    def __init__(self, what_should_appear_first: str):
        self._sub_str = what_should_appear_first

    def get_sub_str(self) -> str:
        """

        :return: the sub string that should appear before this operator when he is the first char in the string
        """
        return self._sub_str
