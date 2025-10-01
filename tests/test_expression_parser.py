"""
Unit tests for the ExpressionParser module.
Tests operator precedence, evaluation, and error handling.
"""

import unittest
from doglang.ExpressionParser import ExpressionParser, parse_and_evaluate
from doglang.Tokenizer import Token, Tokens
from doglang.SymbolTable import SymbolTable


class MockAST:
    """Mock AST node for testing."""
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value


class TestExpressionParser(unittest.TestCase):
    """Test cases for the ExpressionParser class."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Clear the global symbols list to ensure test isolation
        from doglang.SymbolTable import symbols
        symbols.clear()
        self.symbol_table = SymbolTable()
    
    def create_tokens(self, token_list):
        """
        Helper method to create AST-like tokens from a list of (type, value) tuples.
        
        Args:
            token_list: List of tuples (token_type, value)
            
        Returns:
            List of MockAST objects
        """
        return [MockAST(t, v) for t, v in token_list]
    
    # ===== Basic Arithmetic Tests =====
    
    def test_simple_addition(self):
        """Test simple addition: 5 + 3"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '5'),
            (Tokens.ARITHMETIC_OP, '+'),
            (Tokens.INT_LITERAL, '3')
        ])
        result = parse_and_evaluate(tokens)
        self.assertEqual(result, 8)
    
    def test_simple_subtraction(self):
        """Test simple subtraction: 10 - 4"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '10'),
            (Tokens.ARITHMETIC_OP, '-'),
            (Tokens.INT_LITERAL, '4')
        ])
        result = parse_and_evaluate(tokens)
        self.assertEqual(result, 6)
    
    def test_simple_multiplication(self):
        """Test simple multiplication: 6 * 7"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '6'),
            (Tokens.ARITHMETIC_OP, '*'),
            (Tokens.INT_LITERAL, '7')
        ])
        result = parse_and_evaluate(tokens)
        self.assertEqual(result, 42)
    
    def test_simple_division(self):
        """Test simple division: 20 / 5"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '20'),
            (Tokens.ARITHMETIC_OP, '/'),
            (Tokens.INT_LITERAL, '5')
        ])
        result = parse_and_evaluate(tokens)
        self.assertEqual(result, 4)
    
    def test_simple_modulo(self):
        """Test modulo operation: 10 % 3"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '10'),
            (Tokens.ARITHMETIC_OP, '%'),
            (Tokens.INT_LITERAL, '3')
        ])
        result = parse_and_evaluate(tokens)
        self.assertEqual(result, 1)
    
    # ===== Operator Precedence Tests =====
    
    def test_multiplication_before_addition(self):
        """Test precedence: 2 + 3 * 4 = 14 (not 20)"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '2'),
            (Tokens.ARITHMETIC_OP, '+'),
            (Tokens.INT_LITERAL, '3'),
            (Tokens.ARITHMETIC_OP, '*'),
            (Tokens.INT_LITERAL, '4')
        ])
        result = parse_and_evaluate(tokens)
        self.assertEqual(result, 14)
    
    def test_division_before_subtraction(self):
        """Test precedence: 20 - 8 / 4 = 18 (not 3)"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '20'),
            (Tokens.ARITHMETIC_OP, '-'),
            (Tokens.INT_LITERAL, '8'),
            (Tokens.ARITHMETIC_OP, '/'),
            (Tokens.INT_LITERAL, '4')
        ])
        result = parse_and_evaluate(tokens)
        self.assertEqual(result, 18)
    
    def test_complex_precedence(self):
        """Test complex precedence: 10 + 2 * 3 - 4 / 2 = 14"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '10'),
            (Tokens.ARITHMETIC_OP, '+'),
            (Tokens.INT_LITERAL, '2'),
            (Tokens.ARITHMETIC_OP, '*'),
            (Tokens.INT_LITERAL, '3'),
            (Tokens.ARITHMETIC_OP, '-'),
            (Tokens.INT_LITERAL, '4'),
            (Tokens.ARITHMETIC_OP, '/'),
            (Tokens.INT_LITERAL, '2')
        ])
        result = parse_and_evaluate(tokens)
        self.assertEqual(result, 14)
    
    # ===== Parentheses Tests =====
    
    def test_parentheses_override_precedence(self):
        """Test parentheses: (2 + 3) * 4 = 20"""
        tokens = self.create_tokens([
            (Tokens.PARENTHESIS, '('),
            (Tokens.INT_LITERAL, '2'),
            (Tokens.ARITHMETIC_OP, '+'),
            (Tokens.INT_LITERAL, '3'),
            (Tokens.PARENTHESIS, ')'),
            (Tokens.ARITHMETIC_OP, '*'),
            (Tokens.INT_LITERAL, '4')
        ])
        result = parse_and_evaluate(tokens)
        self.assertEqual(result, 20)
    
    def test_nested_parentheses(self):
        """Test nested parentheses: ((2 + 3) * 4) - 5 = 15"""
        tokens = self.create_tokens([
            (Tokens.PARENTHESIS, '('),
            (Tokens.PARENTHESIS, '('),
            (Tokens.INT_LITERAL, '2'),
            (Tokens.ARITHMETIC_OP, '+'),
            (Tokens.INT_LITERAL, '3'),
            (Tokens.PARENTHESIS, ')'),
            (Tokens.ARITHMETIC_OP, '*'),
            (Tokens.INT_LITERAL, '4'),
            (Tokens.PARENTHESIS, ')'),
            (Tokens.ARITHMETIC_OP, '-'),
            (Tokens.INT_LITERAL, '5')
        ])
        result = parse_and_evaluate(tokens)
        self.assertEqual(result, 15)
    
    # ===== Comparison Operators Tests =====
    
    def test_less_than(self):
        """Test less than: 5 < 10"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '5'),
            (Tokens.COMPARISON_OP, '<'),
            (Tokens.INT_LITERAL, '10')
        ])
        result = parse_and_evaluate(tokens)
        self.assertTrue(result)
    
    def test_greater_than(self):
        """Test greater than: 15 > 10"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '15'),
            (Tokens.COMPARISON_OP, '>'),
            (Tokens.INT_LITERAL, '10')
        ])
        result = parse_and_evaluate(tokens)
        self.assertTrue(result)
    
    def test_less_than_or_equal(self):
        """Test less than or equal: 5 <= 5"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '5'),
            (Tokens.COMPARISON_OP, '<='),
            (Tokens.INT_LITERAL, '5')
        ])
        result = parse_and_evaluate(tokens)
        self.assertTrue(result)
    
    def test_greater_than_or_equal(self):
        """Test greater than or equal: 10 >= 8"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '10'),
            (Tokens.COMPARISON_OP, '>='),
            (Tokens.INT_LITERAL, '8')
        ])
        result = parse_and_evaluate(tokens)
        self.assertTrue(result)
    
    def test_equality(self):
        """Test equality: 7 == 7"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '7'),
            (Tokens.COMPARISON_OP, '=='),
            (Tokens.INT_LITERAL, '7')
        ])
        result = parse_and_evaluate(tokens)
        self.assertTrue(result)
    
    def test_inequality(self):
        """Test inequality: 5 != 3"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '5'),
            (Tokens.COMPARISON_OP, '!='),
            (Tokens.INT_LITERAL, '3')
        ])
        result = parse_and_evaluate(tokens)
        self.assertTrue(result)
    
    def test_comparison_with_arithmetic(self):
        """Test comparison with arithmetic: 2 + 3 > 4"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '2'),
            (Tokens.ARITHMETIC_OP, '+'),
            (Tokens.INT_LITERAL, '3'),
            (Tokens.COMPARISON_OP, '>'),
            (Tokens.INT_LITERAL, '4')
        ])
        result = parse_and_evaluate(tokens)
        self.assertTrue(result)
    
    # ===== Logical Operators Tests =====
    
    def test_logical_and_true(self):
        """Test logical AND (true): 5 > 3 && 10 > 8"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '5'),
            (Tokens.COMPARISON_OP, '>'),
            (Tokens.INT_LITERAL, '3'),
            (Tokens.LOGICAL_OP, '&&'),
            (Tokens.INT_LITERAL, '10'),
            (Tokens.COMPARISON_OP, '>'),
            (Tokens.INT_LITERAL, '8')
        ])
        result = parse_and_evaluate(tokens)
        self.assertTrue(result)
    
    def test_logical_and_false(self):
        """Test logical AND (false): 5 > 3 && 10 < 8"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '5'),
            (Tokens.COMPARISON_OP, '>'),
            (Tokens.INT_LITERAL, '3'),
            (Tokens.LOGICAL_OP, '&&'),
            (Tokens.INT_LITERAL, '10'),
            (Tokens.COMPARISON_OP, '<'),
            (Tokens.INT_LITERAL, '8')
        ])
        result = parse_and_evaluate(tokens)
        self.assertFalse(result)
    
    def test_logical_or_true(self):
        """Test logical OR (true): 5 < 3 || 10 > 8"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '5'),
            (Tokens.COMPARISON_OP, '<'),
            (Tokens.INT_LITERAL, '3'),
            (Tokens.LOGICAL_OP, '||'),
            (Tokens.INT_LITERAL, '10'),
            (Tokens.COMPARISON_OP, '>'),
            (Tokens.INT_LITERAL, '8')
        ])
        result = parse_and_evaluate(tokens)
        self.assertTrue(result)
    
    def test_logical_or_false(self):
        """Test logical OR (false): 5 < 3 || 10 < 8"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '5'),
            (Tokens.COMPARISON_OP, '<'),
            (Tokens.INT_LITERAL, '3'),
            (Tokens.LOGICAL_OP, '||'),
            (Tokens.INT_LITERAL, '10'),
            (Tokens.COMPARISON_OP, '<'),
            (Tokens.INT_LITERAL, '8')
        ])
        result = parse_and_evaluate(tokens)
        self.assertFalse(result)
    
    # ===== Unary Operators Tests =====
    
    def test_unary_minus(self):
        """Test unary minus: -5 + 10 = 5"""
        tokens = self.create_tokens([
            (Tokens.ARITHMETIC_OP, '-'),
            (Tokens.INT_LITERAL, '5'),
            (Tokens.ARITHMETIC_OP, '+'),
            (Tokens.INT_LITERAL, '10')
        ])
        result = parse_and_evaluate(tokens)
        self.assertEqual(result, 5)
    
    def test_unary_minus_in_expression(self):
        """Test unary minus in expression: 10 * -2 = -20"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '10'),
            (Tokens.ARITHMETIC_OP, '*'),
            (Tokens.ARITHMETIC_OP, '-'),
            (Tokens.INT_LITERAL, '2')
        ])
        result = parse_and_evaluate(tokens)
        self.assertEqual(result, -20)
    
    def test_logical_not(self):
        """Test logical NOT: !(5 > 10)"""
        tokens = self.create_tokens([
            (Tokens.LOGICAL_OP, '!'),
            (Tokens.PARENTHESIS, '('),
            (Tokens.INT_LITERAL, '5'),
            (Tokens.COMPARISON_OP, '>'),
            (Tokens.INT_LITERAL, '10'),
            (Tokens.PARENTHESIS, ')')
        ])
        result = parse_and_evaluate(tokens)
        self.assertTrue(result)
    
    # ===== Variables Tests =====
    
    def test_variable_lookup(self):
        """Test variable lookup: x + 5 where x = 10"""
        self.symbol_table.insert("x", "int", "local", 10)
        tokens = self.create_tokens([
            (Tokens.IDENTIFIER, 'x'),
            (Tokens.ARITHMETIC_OP, '+'),
            (Tokens.INT_LITERAL, '5')
        ])
        result = parse_and_evaluate(tokens, self.symbol_table)
        self.assertEqual(result, 15)
    
    def test_multiple_variables(self):
        """Test multiple variables: x + y * z where x=2, y=3, z=4"""
        self.symbol_table.insert("x", "int", "local", 2)
        self.symbol_table.insert("y", "int", "local", 3)
        self.symbol_table.insert("z", "int", "local", 4)
        tokens = self.create_tokens([
            (Tokens.IDENTIFIER, 'x'),
            (Tokens.ARITHMETIC_OP, '+'),
            (Tokens.IDENTIFIER, 'y'),
            (Tokens.ARITHMETIC_OP, '*'),
            (Tokens.IDENTIFIER, 'z')
        ])
        result = parse_and_evaluate(tokens, self.symbol_table)
        self.assertEqual(result, 14)
    
    def test_variable_comparison(self):
        """Test variable comparison: a < b where a=5, b=10"""
        self.symbol_table.insert("a", "int", "local", 5)
        self.symbol_table.insert("b", "int", "local", 10)
        tokens = self.create_tokens([
            (Tokens.IDENTIFIER, 'a'),
            (Tokens.COMPARISON_OP, '<'),
            (Tokens.IDENTIFIER, 'b')
        ])
        result = parse_and_evaluate(tokens, self.symbol_table)
        self.assertTrue(result)
    
    # ===== Error Handling Tests =====
    
    def test_division_by_zero(self):
        """Test division by zero error"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '10'),
            (Tokens.ARITHMETIC_OP, '/'),
            (Tokens.INT_LITERAL, '0')
        ])
        with self.assertRaises(Exception) as context:
            parse_and_evaluate(tokens)
        self.assertIn("Division by zero", str(context.exception))
    
    def test_modulo_by_zero(self):
        """Test modulo by zero error"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '10'),
            (Tokens.ARITHMETIC_OP, '%'),
            (Tokens.INT_LITERAL, '0')
        ])
        with self.assertRaises(Exception) as context:
            parse_and_evaluate(tokens)
        self.assertIn("Modulo by zero", str(context.exception))
    
    def test_undefined_variable(self):
        """Test undefined variable error"""
        tokens = self.create_tokens([
            (Tokens.IDENTIFIER, 'undefined_var'),
            (Tokens.ARITHMETIC_OP, '+'),
            (Tokens.INT_LITERAL, '5')
        ])
        with self.assertRaises(Exception) as context:
            parse_and_evaluate(tokens, self.symbol_table)
        self.assertIn("not declared", str(context.exception))
    
    def test_missing_closing_parenthesis(self):
        """Test missing closing parenthesis error"""
        tokens = self.create_tokens([
            (Tokens.PARENTHESIS, '('),
            (Tokens.INT_LITERAL, '5'),
            (Tokens.ARITHMETIC_OP, '+'),
            (Tokens.INT_LITERAL, '3')
        ])
        with self.assertRaises(Exception) as context:
            parse_and_evaluate(tokens)
        self.assertIn("Missing closing parenthesis", str(context.exception))
    
    # ===== Complex Expression Tests =====
    
    def test_complex_expression_1(self):
        """Test complex expression: (10 + 5) * 2 - 8 / 4 + 3 = 31"""
        tokens = self.create_tokens([
            (Tokens.PARENTHESIS, '('),
            (Tokens.INT_LITERAL, '10'),
            (Tokens.ARITHMETIC_OP, '+'),
            (Tokens.INT_LITERAL, '5'),
            (Tokens.PARENTHESIS, ')'),
            (Tokens.ARITHMETIC_OP, '*'),
            (Tokens.INT_LITERAL, '2'),
            (Tokens.ARITHMETIC_OP, '-'),
            (Tokens.INT_LITERAL, '8'),
            (Tokens.ARITHMETIC_OP, '/'),
            (Tokens.INT_LITERAL, '4'),
            (Tokens.ARITHMETIC_OP, '+'),
            (Tokens.INT_LITERAL, '3')
        ])
        result = parse_and_evaluate(tokens)
        self.assertEqual(result, 31)
    
    def test_complex_expression_2(self):
        """Test complex expression with comparisons and logic"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '10'),
            (Tokens.ARITHMETIC_OP, '+'),
            (Tokens.INT_LITERAL, '5'),
            (Tokens.COMPARISON_OP, '>'),
            (Tokens.INT_LITERAL, '12'),
            (Tokens.LOGICAL_OP, '&&'),
            (Tokens.INT_LITERAL, '20'),
            (Tokens.ARITHMETIC_OP, '/'),
            (Tokens.INT_LITERAL, '4'),
            (Tokens.COMPARISON_OP, '=='),
            (Tokens.INT_LITERAL, '5')
        ])
        result = parse_and_evaluate(tokens)
        self.assertTrue(result)
    
    def test_modulo_even_check(self):
        """Test modulo for even number check: 10 % 2 == 0"""
        tokens = self.create_tokens([
            (Tokens.INT_LITERAL, '10'),
            (Tokens.ARITHMETIC_OP, '%'),
            (Tokens.INT_LITERAL, '2'),
            (Tokens.COMPARISON_OP, '=='),
            (Tokens.INT_LITERAL, '0')
        ])
        result = parse_and_evaluate(tokens)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
