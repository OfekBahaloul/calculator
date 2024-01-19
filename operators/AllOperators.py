from operators.BaseOperator import Operator
from operators.BaseOperator import AttributeOperator


class AddOperator(Operator):
    def __init__(self):
        Operator.__init__(self, 1, '+', 2, "both")

    def calc_operation(self, expression_list: list, my_index: int) -> int:
        """

        :param expression_list: collection of all operations and operands
        :param my_index: the current index of the operator
        :return: the new index of the result
        """
        # base operation returns the extracted values and the new index position after extraction
        [values, my_index] = Operator.calc_operation(self, expression_list, my_index)

        # set the result of the operation in the new index
        expression_list.insert(my_index, values[0] + values[1])
        return my_index


class SubtractOperator(AttributeOperator):
    def __init__(self):
        AttributeOperator.__init__(self, 1, '-', 2, "both", 3.5)

    def calc_operation(self, expression_list: list, my_index: int) -> int:
        """

        :param expression_list: collection of all operations and operands
        :param my_index: the current index of the operator
        :return: the new index of the result
        """
        # base operation returns the extracted values and the new index position after extraction
        [values, my_index] = Operator.calc_operation(self, expression_list, my_index)

        # set the result of the operation in the new index
        # if i am normal then i should be a minus
        if self.direction == "both":
            expression_list.insert(my_index, values[0] - values[1])

        else:
            # if not then i shell negate the current value
            expression_list.insert(my_index, values[0] * -1)

        return my_index


class MultOperator(Operator):
    def __init__(self):
        Operator.__init__(self, 2, '*', 2, "both")

    def calc_operation(self, expression_list: list, my_index: int) -> int:
        """

        :param expression_list: collection of all operations and operands
        :param my_index: the current index of the operator
        :return: the index where the result is
        """
        # base operation returns the extracted values and the new index position after extraction
        [values, my_index] = Operator.calc_operation(self, expression_list, my_index)

        # set the result of the operation in the new index
        result = round(values[0] * values[1], 10)
        expression_list.insert(my_index, result)

        return my_index


class DivideOperator(Operator):
    def __init__(self):
        Operator.__init__(self, 2, '/', 2, "both")

    def calc_operation(self, expression_list: list, my_index: int) -> int:
        """

        :param expression_list: collection of all operations and operands
        :param my_index: the current index of the operator
        :return: the index where the result is
        """
        # base operation returns the extracted values and the new index position after extraction
        [values, my_index] = Operator.calc_operation(self, expression_list, my_index)

        # set the result of the operation in the new index

        if values[1] == 0:
            raise ZeroDivisionError("inserted a value that converted into a divide by zero !")

        result = round(values[0] / values[1], 10)
        expression_list.insert(my_index, result)
        return my_index


class PowerOperator(Operator):
    def __init__(self):
        Operator.__init__(self, 3, '^', 2, "both")

    def calc_operation(self, expression_list: list, my_index: int) -> int:
        """

        :param expression_list: collection of all operations and operands
        :param my_index: the current index of the operator
        :return: the index where the result is
        """
        # base operation returns the extracted values and the new index position after extraction
        [values, my_index] = Operator.calc_operation(self, expression_list, my_index)

        # set the result of the operation in the new index
        result = pow(values[0],values[1])

        if isinstance(result, complex):
            raise ValueError("result of power operation is imaginary !")

        result = round(result, 10)
        expression_list.insert(my_index, result)

        return my_index


class AverageOperator(Operator):
    def __init__(self):
        Operator.__init__(self, 5, '@', 2, "both")

    def calc_operation(self, expression_list: list, my_index: int) -> int:
        """

        :param expression_list: collection of all operations and operands
        :param my_index: the current index of the operator
        :return: the index where the result is
        """
        # base operation returns the extracted values and the new index position after extraction
        [values, my_index] = Operator.calc_operation(self, expression_list, my_index)

        # set the result of the operation in the new index
        result = round((values[0] + values[1]) / 2, 10)
        expression_list.insert(my_index, result)
        return my_index


class MaxOperator(Operator):
    def __init__(self):
        Operator.__init__(self, 5, '$', 2, "both")

    def calc_operation(self, expression_list: list, my_index: int) -> int:
        """

        :param expression_list: collection of all operations and operands
        :param my_index: the current index of the operator
        :return: the index where the result is
        """
        # base operation returns the extracted values and the new index position after extraction
        [values, my_index] = Operator.calc_operation(self, expression_list, my_index)

        # set the result of the operation in the new index
        result = values[0]
        if values[1] > result:
            result = values[1]

        expression_list.insert(my_index, result)
        return my_index


class MinOperator(Operator):
    def __init__(self):
        Operator.__init__(self, 5, '&', 2, "both")

    def calc_operation(self, expression_list: list, my_index: int) -> int:
        """

        :param expression_list: collection of all operations and operands
        :param my_index: the current index of the operator
        :return: the index where the result is
        """
        # base operation returns the extracted values and the new index position after extraction
        [values, my_index] = Operator.calc_operation(self, expression_list, my_index)

        # set the result of the operation in the new index
        result = values[0]
        if values[1] < result:
            result = values[1]

        expression_list.insert(my_index, result)
        return my_index


class ModuloOperator(Operator):
    def __init__(self):
        Operator.__init__(self, 4, '%', 2, "both")

    def calc_operation(self, expression_list: list, my_index: int) -> int:
        """

        :param expression_list: collection of all operations and operands
        :param my_index: the current index of the operator
        :return: the index where the result is
        """
        # base operation returns the extracted values and the new index position after extraction
        [values, my_index] = Operator.calc_operation(self, expression_list, my_index)

        # set the result of the operation in the new index
        result = round(values[0] % values[1],10)
        expression_list.insert(my_index, result)
        return my_index


class NotOperator(Operator):
    def __init__(self):
        Operator.__init__(self, 6, '~', 1, "right")

    def calc_operation(self, expression_list: list, my_index: int) -> int:
        """

        :param expression_list: collection of all operations and operands
        :param my_index: the current index of the operator
        :return: the index where the result is
        """
        # base operation returns the extracted values and the new index position after extraction
        [values, my_index] = Operator.calc_operation(self, expression_list, my_index)

        # set the result of the operation in the new index
        result = values[0] * -1
        expression_list.insert(my_index, result)
        return my_index


class FactorialOperator(Operator):
    def __init__(self):
        Operator.__init__(self, 6, '!', 1, "left")

    def calc_operation(self, expression_list: list, my_index: int) -> int:
        """

        :param expression_list: collection of all operations and operands
        :param my_index: the current index of the operator
        :return: the index where the result is
        """
        # base operation returns the extracted values and the new index position after extraction
        [values, my_index] = Operator.calc_operation(self, expression_list, my_index)

        # set the result of the operation in the new index
        if values[0] < 0:
            raise ValueError("you cant factorial a negative number !")

        if not values[0].is_integer():
            raise ValueError("you can factorial only integer number !")

        to_compute = int(values[0])
        result = 1.0
        for i in range(2, to_compute + 1):
            result *= i
            if result >= float('inf'):
                raise ValueError("value is too large !")

        expression_list.insert(my_index, result)
        return my_index


class CountNumberOperator(Operator):
    def __init__(self):
        Operator.__init__(self, 6, '#', 1, "left")

    def calc_operation(self, expression_list: list, my_index: int) -> int:
        """

        :param expression_list: collection of all operations and operands
        :param my_index: the current index of the operator
        :return: the index where the result is
        """
        # base operation returns the extracted values and the new index position after extraction
        [values, my_index] = Operator.calc_operation(self, expression_list, my_index)

        result = 0.0
        to_compute = str(values[0])

        # Add the digit to the sum
        for char in to_compute:
            if char.isdigit():
                result += int(char)

        expression_list.insert(my_index, result)
        return my_index