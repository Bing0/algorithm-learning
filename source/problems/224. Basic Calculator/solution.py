class Solution:
    def calculate(self, s: str) -> int:
        num_stack = []
        op_stack = []

        num = None

        op = {
            "+": lambda x, y: y + x,
            "-": lambda x, y: y - x,
            "*": lambda x, y: y * x,
            "/": lambda x, y: y / x,
        }

        # 5+(2+3
        # 3+5*6-3
        pri = {
            "+": 2,
            "-": 2,
            "*": 1,
            "/": 1,
            "(": 3,
        }

        num_pushed = False
        for token in s:

            if "0" <= token <= "9":
                if num:
                    num = num * 10 + int(token)
                else:
                    num = int(token)
                continue
            if num is not None:
                num_stack.append(num)
                num_pushed = True
                num = None

            if token == " ":
                continue

            if token == "(":
                op_stack.append(token)
                continue
            if token == ")":
                while op_stack[-1] != "(":
                    num_stack.append(op[op_stack.pop()](num_stack.pop(), num_stack.pop()))
                op_stack.pop()
                continue
            while len(op_stack) > 0:
                if pri[token] >= pri[op_stack[-1]]:
                    num_stack.append(op[op_stack.pop()](num_stack.pop(), num_stack.pop()))
                else:
                    break
            if not num_pushed:
                num_stack.append(0)
            num_pushed = False
            op_stack.append(token)

        if num is not None:
            num_stack.append(num)

        while len(op_stack) > 0:
            num_stack.append(op[op_stack.pop()](num_stack.pop(), num_stack.pop()))
        return num_stack[0]
