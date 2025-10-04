import pytest


class TestBasicOperations:
    """Test basic DogLang operations"""
    
    def test_variable_assignment(self, run_code):
        """Test simple variable assignment and printing"""
        assert run_code("a = 10; bark(a);") == "10"
    
    @pytest.mark.parametrize("code,expected", [
        ("a = 5 + 3; bark(a);", "8"),
        ("b = 10 * 2; bark(b);", "20"),
        ("c = 20 - 5; bark(c);", "15"),
        ("d = 100 / 4; bark(d);", "25.0"),
    ])
    def test_arithmetic_operations(self, run_code, code, expected):
        """Test various arithmetic expressions"""
        assert run_code(code) == expected
    
    def test_string_literal(self, run_code):
        """Test string printing"""
        assert run_code('bark("Hello DogLang");') == "Hello DogLang"
    
    @pytest.mark.parametrize("value,expected", [
        (10, "Equal"),
        (5, "Not Equal"),
        (15, "Not Equal"),
    ])
    def test_comparison_operators(self, run_code, value, expected):
        """Test comparison in conditionals"""
        code = f"""
        a = {value};
        sniff(a == 10) {{
            bark("Equal");
        }} else {{
            bark("Not Equal");
        }}
        """
        assert run_code(code) == expected
    
    def test_conditional_else(self, run_code):
        """Test if-else branching"""
        code = """
        a = 5;
        sniff(a > 10) {
            bark("Greater");
        } else {
            bark("Smaller");
        }
        """
        assert run_code(code) == "Smaller"
    
    @pytest.mark.parametrize("limit,expected", [
        (3, "0\n1\n2"),
        (5, "0\n1\n2\n3\n4"),
        (1, "0"),
    ])
    def test_loop_basic(self, run_code, limit, expected):
        """Test basic loop with different limits"""
        code = f"""
        a = 0;
        wagtail(a < {limit}) {{
            bark(a);
            a = a + 1;
        }}
        """
        assert run_code(code) == expected
    
    def test_modulo_operator(self, run_code):
        """Test modulo operation"""
        assert run_code("a = 10; b = a % 2; bark(b);") == "0"
        assert run_code("a = 11; b = a % 2; bark(b);") == "1"
    
    def test_variable_update(self, run_code):
        """Test variable modification"""
        code = """
        a = 5;
        bark(a);
        a = 10;
        bark(a);
        """
        assert run_code(code) == "5\n10"
    
    @pytest.mark.parametrize("var_name", ["undefined_var", "x", "y", "missing"])
    def test_undeclared_variable_error(self, expect_error, var_name):
        """Test that using undeclared variable raises error"""
        code = f"bark({var_name});"
        with expect_error(code, "Variable not declared"):
            from doglang.main import Interpreter
            Interpreter(code)


@pytest.mark.symbol_table
class TestSymbolTableIsolation:
    """Test that symbol table is properly isolated between interpreter instances"""
    
    def test_isolated_symbol_tables(self, run_code, expect_error):
        """Test that separate interpreter instances don't share variables"""
        # First interpreter instance
        assert run_code("a = 30; bark(a);") == "30"
        
        # Second interpreter instance - should NOT have access to 'a'
        with expect_error("bark(a);", "Variable not declared"):
            from doglang.main import Interpreter
            Interpreter("bark(a);")
    
    @pytest.mark.parametrize("programs", [
        [
            ("x = 10; bark(x);", "10"),
            ("y = 20; bark(y);", "20"),
            ("z = 30; bark(z);", "30"),
        ]
    ])
    def test_multiple_programs_independence(self, run_code, expect_error, programs):
        """Test that multiple programs run independently"""
        variables = []
        
      
        for code, expected_output in programs:
            assert run_code(code) == expected_output
            # Extract variable name from code
            var_name = code.split('=')[0].strip()
            variables.append(var_name)
        
      
        for var_name in variables:
            with expect_error(f"bark({var_name});", "Variable not declared"):
                from doglang.main import Interpreter
                Interpreter(f"bark({var_name});")
    
    @pytest.mark.parametrize("var_name,values", [
        ("value", [42, 99, 123]),
        ("counter", [1, 2, 3]),
        ("result", [100, 200, 300]),
    ])
    def test_same_variable_different_programs(self, run_code, expect_error, var_name, values):
        """Test that same variable name in different programs doesn't conflict"""
        # Run programs with same variable name but different values
        for value in values:
            assert run_code(f"{var_name} = {value}; bark({var_name});") == str(value)
        
        # Verify variable doesn't persist
        with expect_error(f"bark({var_name});", "Variable not declared"):
            from doglang.main import Interpreter
            Interpreter(f"bark({var_name});")


class TestComplexPrograms:
    """Test more complex DogLang programs"""
    
    def test_nested_conditions(self, run_code):
        """Test nested conditional statements"""
        code = """
        a = 10;
        sniff(a > 5) {
            sniff(a == 10) {
                bark("Perfect");
            }
        }
        """
        assert run_code(code) == "Perfect"
    
    def test_loop_with_condition(self, run_code):
        """Test loop with conditional inside"""
        code = """
        a = 0;
        wagtail(a < 5) {
            sniff(a % 2 == 0) {
                bark(a);
            }
            a = a + 1;
        }
        """
        assert run_code(code) == "0\n2\n4"
    
    @pytest.mark.parametrize("x,y,expected", [
        (10, 20, "30"),
        (5, 15, "20"),
        (100, 50, "150"),
    ])
    def test_multiple_variables(self, run_code, x, y, expected):
        """Test multiple variable operations"""
        code = f"""
        x = {x};
        y = {y};
        z = x + y;
        bark(z);
        """
        assert run_code(code) == expected
    
    def test_fibonacci_like(self, run_code):
        """Test fibonacci-like sequence"""
        code = """
        a = 0;
        b = 1;
        count = 0;
        wagtail(count < 5) {
            bark(a);
            temp = a + b;
            a = b;
            b = temp;
            count = count + 1;
        }
        """
        assert run_code(code) == "0\n1\n1\n2\n3"
    
    @pytest.mark.slow
    def test_larger_fibonacci(self, run_code):
        """Test larger fibonacci sequence"""
        code = """
        a = 0;
        b = 1;
        count = 0;
        wagtail(count < 10) {
            bark(a);
            temp = a + b;
            a = b;
            b = temp;
            count = count + 1;
        }
        """
        expected = "0\n1\n1\n2\n3\n5\n8\n13\n21\n34"
        assert run_code(code) == expected



@pytest.mark.parametrize("code,expected", [
    ("a = 5; bark(a);", "5"),
    ("a = 10 + 5; bark(a);", "15"),
    ("a = 20 * 2; bark(a);", "40"),
    ('bark("Test");', "Test"),
    ("a = 100 / 5; bark(a);", "20.0"),
    ("a = 7 % 3; bark(a);", "1"),
])
def test_simple_operations(run_code, code, expected):
    """Parametrized test for simple operations"""
    assert run_code(code) == expected


@pytest.mark.parametrize("condition,expected", [
    ("10 > 5", "True"),
    ("5 > 10", "False"),
    ("10 == 10", "True"),
    ("10 != 5", "True"),
])
def test_boolean_expressions(run_code, condition, expected):
    """Test boolean expression evaluation"""
    code = f"""
    sniff({condition}) {{
        bark("True");
    }} else {{
        bark("False");
    }}
    """
    assert run_code(code) == expected