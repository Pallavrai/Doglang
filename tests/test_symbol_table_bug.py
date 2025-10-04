"""Specific tests to verify the symbol table bug is fixed using pytest"""
import pytest
from doglang.SymbolTable import SymbolTable


@pytest.mark.bug
@pytest.mark.symbol_table
class TestSymbolTableBugFix:
    """Tests specifically for the symbol table isolation bug"""
    
    def test_original_bug_scenario(self, run_code, expect_error):
        """
        Original bug: Running testfile1.doggy then testfile2.doggy
        testfile2 would incorrectly access variables from testfile1
        """

        assert run_code("a = 30; bark(30);") == "30", "First program should execute correctly"
        

        with expect_error("bark(a);", "Variable not declared"):
            from doglang.main import Interpreter
            Interpreter("bark(a);")
    
    @pytest.mark.parametrize("programs,check_vars", [
        (
            [("x = 10; bark(x);", "10"), ("y = 20; bark(y);", "20"), ("z = 30; bark(z);", "30")],
            ["x", "y", "z"]
        ),
        (
            [("a = 1; bark(a);", "1"), ("b = 2; bark(b);", "2")],
            ["a", "b"]
        ),
    ])
    def test_sequential_program_execution(self, run_code, expect_error, programs, check_vars):
        """Test that sequential program executions don't leak variables"""
        # Run all programs
        for code, expected_output in programs:
            assert run_code(code) == expected_output
        
       
        for var_name in check_vars:
            with expect_error(f"bark({var_name});", "Variable not declared"):
                from doglang.main import Interpreter
                Interpreter(f"bark({var_name});")
    
    def test_interpreter_instance_isolation(self, expect_error):
        """Test that each Interpreter instance has isolated symbol table"""
        from doglang.main import Interpreter
        import sys
        from io import StringIO
        
        # Create first interpreter with variable
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            Interpreter("var1 = 100;")
        finally:
            sys.stdout = old_stdout
        
        # Create second interpreter - should not have var1
        with expect_error("bark(var1);"):
            Interpreter("bark(var1);")
    
    @pytest.mark.parametrize("var_name,value1,value2", [
        ("name", 111, 222),
        ("counter", 1, 2),
        ("value", 999, 888),
    ])
    def test_cross_program_variable_conflict(self, run_code, expect_error, var_name, value1, value2):
        """Test that same variable names in different programs don't conflict"""
        # Program 1
        assert run_code(f"{var_name} = {value1}; bark({var_name});") == str(value1)
        
        # Program 2 - different value for same variable name
        assert run_code(f"{var_name} = {value2}; bark({var_name});") == str(value2)
        
        # Program 3 - variable should not exist
        with expect_error(f"bark({var_name});"):
            from doglang.main import Interpreter
            Interpreter(f"bark({var_name});")
    
    def test_loop_program_isolation(self, run_code, expect_error):
        """Test programs with loops maintain isolation"""
        code = """
        counter = 0;
        wagtail(counter < 3) {
            counter = counter + 1;
        }
        bark(counter);
        """
        assert run_code(code) == "3"
        
        # Second program should not have access to counter
        with expect_error("bark(counter);", "Variable not declared"):
            from doglang.main import Interpreter
            Interpreter("bark(counter);")


@pytest.mark.symbol_table
class TestSymbolTableInternalBehavior:
    """Test the SymbolTable class directly"""
    
    @pytest.mark.parametrize("var1,val1,var2,val2", [
        ("var1", 100, "var2", 200),
        ("x", 10, "y", 20),
        ("counter", 1, "total", 99),
    ])
    def test_symbol_table_instance_isolation(self, var1, val1, var2, val2):
        """Test that SymbolTable instances are truly independent"""
       
        st1 = SymbolTable()
        st1.insert(var1, "int", "local", val1)
        
       
        st2 = SymbolTable()
        st2.insert(var2, "int", "local", val2)
        
        # Verify isolation
        assert st1.lookup(var1) is not None
        assert st1.lookup(var2) is None
        
        assert st2.lookup(var2) is not None
        assert st2.lookup(var1) is None
    
    def test_symbol_table_cleanup(self):
        """Test that symbol tables don't persist between creations"""
        # Create and populate first instance
        st1 = SymbolTable()
        st1.insert("temp", "int", "local", 42)
        assert st1.lookup("temp") is not None
        
        # Delete first instance
        del st1
        
        # Create new instance - should not have 'temp'
        st2 = SymbolTable()
        assert st2.lookup("temp") is None
    
    @pytest.mark.parametrize("operations", [
        [("x", 10), ("y", 20), ("z", 30)],
        [("a", 1), ("b", 2), ("c", 3), ("d", 4)],
    ])
    def test_symbol_table_multiple_variables(self, operations):
        """Test symbol table with multiple variables"""
        st = SymbolTable()
        
        # Insert all variables
        for var_name, value in operations:
            st.insert(var_name, "int", "local", value)
        
        # Verify all are present with correct values
        for var_name, expected_value in operations:
            entry = st.lookup(var_name)
            assert entry is not None
            assert entry['value'] == expected_value
    
    def test_symbol_table_modify(self):
        """Test modifying symbol table entries"""
        st = SymbolTable()
        st.insert("counter", "int", "local", 0)
        
        # Modify multiple times
        for i in range(1, 6):
            st.modify("counter", i)
            assert st.lookup("counter")['value'] == i


# Parametrized edge case tests
@pytest.mark.parametrize("var_name", ["undefined", "missing", "not_declared", "random"])
def test_undeclared_variables(expect_error, var_name):
    """Parametrized test for undeclared variable errors"""
    with expect_error(f"bark({var_name});", "Variable not declared"):
        from doglang.main import Interpreter
        Interpreter(f"bark({var_name});")