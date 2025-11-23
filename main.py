from postfix_evaluator import PostfixEvaluator
from infix_converter import InfixToPostfixConverter

postfix = ["5 3 +","8 2 - 3 +","5 3 8 * +","6 2 / 3 +","5 8 + 3 -",
           "5 3 + 8 *","8 2 3 * + 6 -","5 3 8 * + 2 /",
           "8 2 + 3 6 * -","5 3 + 8 2 / -"]

infix = ["A + B","A + B * C","( A + B ) * C","A * B + C / D",
         "( A + B ) * ( C - D )","A + B * C - D / E",
         "A * ( B + C ) / D","( A + B * C ) / ( D - E )",
         "A + ( B - C ) * D","( A + B * ( C - D ) ) / E"]

print("----- Postfix Evaluator -----")
pe = PostfixEvaluator()
for exp in postfix:
    print(f"[{exp}] = {pe.evaluate(exp)}")

print("\n----- Infix to Postfix Converter -----")
ic = InfixToPostfixConverter()
for exp in infix:
    print(f"[{exp}] -> [{ic.convert(exp)}]")
