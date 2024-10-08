class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_operator(c):
    return c in ['+', '-', '*', '/', '^']


def evaluate_operator(operator, left_val, right_val):
    if operator == '+':
        return left_val + right_val
    elif operator == '-':
        return left_val - right_val
    elif operator == '*':
        return left_val * right_val
    elif operator == '/':
        return left_val / right_val
    elif operator == '^':
        return left_val ** right_val


def build_parse_tree(postfix_expr):
    stack = []
    for token in postfix_expr:
        if token.isdigit():  
            node = Node(int(token))
            stack.append(node)
        elif is_operator(token):  
            node = Node(token)
            node.right = stack.pop()  
            node.left = stack.pop()   
            stack.append(node)
    return stack.pop()  


def evaluate_parse_tree(node):
    
    if node.left is None and node.right is None:
        return node.value


    left_val = evaluate_parse_tree(node.left)
    right_val = evaluate_parse_tree(node.right)

    return evaluate_operator(node.value, left_val, right_val)

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    operators = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            num = ''
          
            while i < len(expression) and expression[i].isdigit():
                num += expression[i]
                i += 1
            output.append(num)
            continue  
        elif expression[i] == '(':
            operators.append(expression[i])
        elif expression[i] == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # Remove '(' from the stack
        elif expression[i] in precedence:
            while (operators and operators[-1] != '(' and
                   precedence.get(operators[-1], 0) >= precedence[expression[i]]):
                output.append(operators.pop())
            operators.append(expression[i])
        i += 1
    
    while operators:
        output.append(operators.pop())
    
    return output  # Return as a list to keep multiple-digit numbers intact


# expression = "(34+5)*20-(80/4)^2"
# postfix_expr = infix_to_postfix(expression)
# print("Postfix Expression:", ' '.join(postfix_expr))

# root = build_parse_tree(postfix_expr)

# result = evaluate_parse_tree(root)
# print("Evaluation Result:", result)
