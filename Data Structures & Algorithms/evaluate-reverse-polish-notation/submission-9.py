class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for item in tokens:
            if item.lstrip("-").isnumeric():
                operands.append(int(item))
            else:
                op1 = operands.pop()
                op2 = operands.pop()
                operation = f"{op2} {item} {op1}"
                result = int(eval(operation))
                operands.append(result)
        return operands[0]