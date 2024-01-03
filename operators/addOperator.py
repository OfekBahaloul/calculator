from operators.BaseOperator import Operator
from operators.BaseOperator import FirstOperator


class AddOperator(Operator, FirstOperator):
    def __init__(self):
        Operator.__init__(self, 4, '+', 2)
        FirstOperator.__init__(self, "0")

    def calc_operation(self, expression_list: list, my_index: int):
        Operator.calc_operation(self, expression_list, my_index)
        values = Operator._get_operands(self, expression_list, my_index)

        # the list is now shorter by all the operands you used + the operator itself
        my_index -= self.uses_num_operands + 1

        expression_list.insert(my_index, values[0] + values[1])

