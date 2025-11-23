from stack import Stack

class InfixToPostfixConverter:
    def __init__(self):
        self.precedence = {'+':1, '-':1, '*':2, '/':2}

    def convert(self, expression):
        stack = Stack()
        output = []
        tokens = expression.split()

        for token in tokens:
            if token.isalnum():
                output.append(token)
            elif token == '(':
                stack.push(token)
            elif token == ')':
                while not stack.is_empty() and stack.peek() != '(':
                    output.append(stack.pop())
                stack.pop()
            else:
                while (not stack.is_empty() and stack.peek() != '(' and
                       self.precedence.get(stack.peek(), 0) >= self.precedence.get(token, 0)):
                    output.append(stack.pop())
                stack.push(token)

        while not stack.is_empty():
            output.append(stack.pop())

        return " ".join(output)
