from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        stack = []
        result = []

        op = {
            "+": lambda x, y: y + x,
            "-": lambda x, y: y - x,
            "*": lambda x, y: y * x,
        }

        def calc() -> None:
            num_stack = []
            op_stack = []

            for token in stack:
                if token in op:
                    while len(op_stack) > 0:
                        if token == "*" and op_stack[-1] != "*":
                            break
                        else:
                            num_stack.append(op[op_stack.pop()](num_stack.pop(), num_stack.pop()))
                    op_stack.append(token)
                else:
                    num_stack.append(int(token))

            while op_stack:
                num_stack.append(op[op_stack.pop()](num_stack.pop(), num_stack.pop()))

            # print(stack, num_stack[0])
            if num_stack[0] == target:
                result.append("".join(stack))

        def possibility(i: int) -> None:
            if i == len(num):
                calc()
                return

            if i != 0:
                last = stack[-1]

                if last != "0":
                    stack.pop()
                    stack.append(last + num[i])
                    possibility(i + 1)
                    stack.pop()
                    stack.append(last)

                stack.append("+")
                stack.append(num[i])
                possibility(i + 1)
                stack.pop()
                stack.pop()

                stack.append("-")
                stack.append(num[i])
                possibility(i + 1)
                stack.pop()
                stack.pop()

                stack.append("*")
                stack.append(num[i])
                possibility(i + 1)
                stack.pop()
                stack.pop()
            else:
                stack.append(num[i])
                possibility(i + 1)
                stack.pop()

        possibility(0)
        return result
