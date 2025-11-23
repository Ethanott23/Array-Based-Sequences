from stack import Stack

class PostfixEvaluator:
    def evaluate(self, expression):
        stack = Stack()
        tokens = expression.split()

        for token in tokens:
            if token.isdigit() or token.replace('.', '', 1).isdigit():
                stack.push(float(token))
            else:
                right = stack.pop()
                left = stack.pop()

                if token == '+':
                    stack.push(left + right)
                elif token == '-':
                    stack.push(left - right)
                elif token == '*':
                    stack.push(left * right)
                elif token == '/':
                    stack.push(left / right)

        result = stack.pop()
        return int(result) if result.is_integer() else result
