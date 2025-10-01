"""
Integration tests for Doglang with the new ExpressionParser.
Tests the complete pipeline from tokenization to execution.
"""

import unittest
import sys
import io
from doglang.main import Interpreter


class TestDoglangIntegration(unittest.TestCase):
    """Integration tests for Doglang interpreter with ExpressionParser."""
    
    def capture_output(self, code):
        """
        Helper method to capture print output from Doglang code.
        
        Args:
            code: Doglang source code string
            
        Returns:
            Captured output as string
        """
        old_stdout = sys.stdout
        sys.stdout = captured_output = io.StringIO()
        
        try:
            Interpreter(code)
            output = captured_output.getvalue()
        finally:
            sys.stdout = old_stdout
        
        return output.strip()
    
    def test_simple_arithmetic(self):
        """Test simple arithmetic expression"""
        code = """
        x = 5 + 3;
        bark(x);
        """
        output = self.capture_output(code)
        self.assertEqual(output, "8")
    
    def test_operator_precedence(self):
        """Test operator precedence: 2 + 3 * 4"""
        code = """
        result = 2 + 3 * 4;
        bark(result);
        """
        output = self.capture_output(code)
        self.assertEqual(output, "14")
    
    def test_parentheses(self):
        """Test parentheses override precedence: (2 + 3) * 4"""
        code = """
        result = (2 + 3) * 4;
        bark(result);
        """
        output = self.capture_output(code)
        self.assertEqual(output, "20")
    
    def test_modulo_operation(self):
        """Test modulo operation for even number check"""
        code = """
        a = 10;
        sniff(a % 2 == 0){
            bark("Even");
        }else{
            bark("Odd");
        }
        """
        output = self.capture_output(code)
        self.assertEqual(output, "Even")
    
    def test_comparison_operators(self):
        """Test comparison operators in conditionals"""
        code = """
        x = 15;
        sniff(x > 10){
            bark("Greater");
        }else{
            bark("Smaller");
        }
        """
        output = self.capture_output(code)
        self.assertEqual(output, "Greater")
    
    def test_logical_operators(self):
        """Test logical operators"""
        code = """
        a = 5;
        b = 10;
        sniff(a < 10 && b > 5){
            bark("Both true");
        }else{
            bark("Not both true");
        }
        """
        output = self.capture_output(code)
        self.assertEqual(output, "Both true")
    
    def test_loop_with_expression(self):
        """Test loop with arithmetic in condition"""
        code = """
        counter = 0;
        sum = 0;
        wagtail(counter < 3){
            sum = sum + 2;
            counter = counter + 1;
        }
        bark(sum);
        """
        output = self.capture_output(code)
        self.assertEqual(output, "6")
    
    def test_complex_expression(self):
        """Test complex expression with multiple operators"""
        code = """
        result = 10 + 5 * 2 - 8 / 4;
        bark(result);
        """
        output = self.capture_output(code)
        self.assertEqual(output, "18")
    
    def test_variable_arithmetic(self):
        """Test arithmetic with variables"""
        code = """
        a = 10;
        b = 5;
        c = a + b * 2;
        bark(c);
        """
        output = self.capture_output(code)
        self.assertEqual(output, "20")
    
    def test_nested_expressions(self):
        """Test nested expressions with parentheses"""
        code = """
        x = ((10 + 5) * 2) - 3;
        bark(x);
        """
        output = self.capture_output(code)
        self.assertEqual(output, "27")
    
    def test_comparison_in_loop(self):
        """Test comparison operators in loop condition"""
        code = """
        i = 0;
        wagtail(i < 5){
            i = i + 1;
        }
        bark(i);
        """
        output = self.capture_output(code)
        self.assertEqual(output, "5")
    
    def test_inequality_check(self):
        """Test inequality operator"""
        code = """
        x = 5;
        sniff(x != 10){
            bark("Not equal");
        }else{
            bark("Equal");
        }
        """
        output = self.capture_output(code)
        self.assertEqual(output, "Not equal")
    
    def test_multiple_operations(self):
        """Test multiple operations in sequence"""
        code = """
        a = 5;
        b = a + 10;
        c = b * 2;
        d = c - 5;
        bark(d);
        """
        output = self.capture_output(code)
        self.assertEqual(output, "25")
    
    def test_complex_conditional(self):
        """Test complex conditional with arithmetic and comparison"""
        code = """
        x = 10;
        y = 5;
        sniff(x + y > 12 && x - y < 10){
            bark("Condition met");
        }else{
            bark("Condition not met");
        }
        """
        output = self.capture_output(code)
        self.assertEqual(output, "Condition met")


if __name__ == '__main__':
    unittest.main()
