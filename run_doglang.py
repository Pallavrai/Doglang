from doglang.main import Interpreter
from doglang.error import SemanticError

def run_test(name, code):
    """Runs a single test case and prints the outcome."""
    print(f"--- Running Test: {name} ---")
    try:
        # This calls your full pipeline: Tokenize -> Parse -> Analyze
        interpreter = Interpreter(code)
        # This executes the code if analysis passes
        interpreter.run()
    except SemanticError as e:
        print(f"Semantic Woof-ror: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("------------------------------------")

# --- Test Cases ---
if __name__ == "__main__":
    valid_code = """
    a = 10;
    c = a + 5;
    sniff (c > 10) {
        bark(c);
    }
    """

    undeclared_variable_code = """
    a = 10 + x;
    """

    type_error_code = """
    a = 10;
    sniff (a) {
        bark("This should not work.");
    }
    """

    run_test("Valid Code", valid_code)
    run_test("Undeclared Variable Error", undeclared_variable_code)
    run_test("Type Error in Condition", type_error_code)