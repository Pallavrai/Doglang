from doglang.main import Interpreter
from doglang.error import SemanticError

code_to_run = """
a = 10;
c = a + 5;
sniff (c > 10) {
    bark(c);
} else {
    bark(0);
}
"""

try:
    Interpreter(code_to_run)
except SemanticError as e:
    print(f"Semantic Woof-ror: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
print("---------------------------------")