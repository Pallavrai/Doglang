class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Utility function to check if a string is an operator (arithmetic or comparison)
def is_operator(c):
    return c in ['+', '-', '*', '/', '^', '<', '<=', '>', '>=', '==', '!=']

# Function to perform operation based on the node's value (arithmetic or comparison)
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
    # Comparison operators (returning 1 for True, 0 for False)
    elif operator == '<':
        return 1 if left_val < right_val else 0
    elif operator == '<=':
        return 1 if left_val <= right_val else 0
    elif operator == '>':
        return 1 if left_val > right_val else 0
    elif operator == '>=':
        return 1 if left_val >= right_val else 0
    elif operator == '==':
        return 1 if left_val == right_val else 0
    elif operator == '!=':
        return 1 if left_val != right_val else 0

# Function to build the parse tree from a postfix expression
def build_parse_tree(postfix_expr):
    stack = []
    for token in postfix_expr:
        if token.isdigit():  # If operand, create node and push it onto the stack
            node = Node(int(token))
            stack.append(node)
        elif is_operator(token):  # If operator, pop two nodes, create an operator node
            if len(stack) < 2:
                raise ValueError("Insufficient operands for operator '{}'".format(token))
            node = Node(token)
            node.right = stack.pop()  # The right child is the last operand
            node.left = stack.pop()   # The left child is the second last operand
            stack.append(node)
    if len(stack) != 1:
        raise ValueError("Invalid expression, too many operands left")
    return stack.pop()  # The final node on the stack is the root of the tree

# Function to evaluate the expression tree
def evaluate_parse_tree(node):
    # Base case: If it's a leaf node (an operand), return its value
    if node.left is None and node.right is None:
        return node.value

    # Recursively evaluate the left and right subtrees
    left_val = evaluate_parse_tree(node.left)
    right_val = evaluate_parse_tree(node.right)

    # Evaluate the current node (operator node)
    return evaluate_operator(node.value, left_val, right_val)

# Function to convert an infix expression to a postfix expression (for easier tree building)
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '<': 0, '<=': 0, '>': 0, '>=': 0, '==': 0, '!=': 0}
    output = []
    operators = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            num = ''
            # Collect the full number (may contain multiple digits)
            while i < len(expression) and expression[i].isdigit():
                num += expression[i]
                i += 1
            output.append(num)
            continue  # Skip incrementing 'i' since it was already moved by the inner loop
        elif expression[i] == '(':
            operators.append(expression[i])
        elif expression[i] == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # Remove '(' from the stack
        
        elif i < len(expression) - 1 and expression[i:i+2] in precedence:
            op = expression[i:i+2]
            while (operators and operators[-1] != '(' and
                   precedence.get(operators[-1], 0) >= precedence[op]):
                output.append(operators.pop())
            operators.append(op)
            i += 2
            continue
        elif expression[i] in precedence:
            while (operators and operators[-1] != '(' and
                   precedence.get(operators[-1], 0) >= precedence[expression[i]]):
                output.append(operators.pop())
            operators.append(expression[i])
        i += 1
    
    while operators:
        output.append(operators.pop())
    
    return output  # Return as a list to keep multiple-digit numbers intact

# Example usage:
# expression = "(34+5) > 20 and (80/4) != 2"

# # Let's focus on each comparison without logical operators like "and" for now
# sub_expressions = expression.split('and')

# # Convert each subexpression to postfix and evaluate
# for expr in sub_expressions:
#     postfix_expr = infix_to_postfix(expr.strip())
#     print(f"Postfix Expression for '{expr.strip()}':", ' '.join(postfix_expr))
    
#     # Build the parse tree from the postfix expression
#     root = build_parse_tree(postfix_expr)

#     # Evaluate the parse tree
#     result = evaluate_parse_tree(root)
#     print("Evaluation Result (1 for True, 0 for False):", result)
