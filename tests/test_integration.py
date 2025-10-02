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
    
    def test_temperature_conversion(self):
        """Test temperature conversion formula"""
        code = """
        fahrenheit = 212;
        celsius = (fahrenheit - 32) * 5 / 9;
        bark(celsius);
        """
        output = self.capture_output(code)
        self.assertEqual(output, "100")
    
    def test_average_calculation(self):
        """Test average of three numbers"""
        code = """
        a = 10;
        b = 20;
        c = 30;
        average = (a + b + c) / 3;
        bark(average);
        """
        output = self.capture_output(code)
        self.assertEqual(output, "20")
    
    def test_discount_calculator(self):
        """Test discount calculation"""
        code = """
        price = 100;
        discount = 20;
        final_price = price - (price * discount / 100);
        bark(final_price);
        """
        output = self.capture_output(code)
        self.assertEqual(output, "80")
    
    def test_range_validation(self):
        """Test value within range"""
        code = """
        value = 50;
        min = 10;
        max = 100;
        sniff(value >= min && value <= max){
            bark("In range");
        }else{
            bark("Out of range");
        }
        """
        output = self.capture_output(code)
        self.assertEqual(output, "In range")
    
    def test_complex_loop_with_calculation(self):
        """Test loop with complex calculation"""
        code = """
        sum = 0;
        i = 1;
        wagtail(i <= 5){
            sum = sum + (i * 2);
            i = i + 1;
        }
        bark(sum);
        """
        output = self.capture_output(code)
        self.assertEqual(output, "30")  # 2 + 4 + 6 + 8 + 10 = 30
    
    def test_nested_conditionals(self):
        """Test nested conditional statements"""
        code = """
        score = 85;
        sniff(score >= 90){
            bark("A");
        }else{
            sniff(score >= 80){
                bark("B");
            }else{
                bark("C");
            }
        }
        """
        output = self.capture_output(code)
        self.assertEqual(output, "B")
    
    def test_factorial_like_calculation(self):
        """Test factorial-like calculation"""
        code = """
        n = 5;
        result = 1;
        counter = 1;
        wagtail(counter <= n){
            result = result * counter;
            counter = counter + 1;
        }
        bark(result);
        """
        output = self.capture_output(code)
        self.assertEqual(output, "120")  # 5! = 120
    
    def test_fibonacci_like_sequence(self):
        """Test fibonacci-like sequence generation"""
        code = """
        a = 0;
        b = 1;
        count = 0;
        wagtail(count < 5){
            temp = a + b;
            a = b;
            b = temp;
            count = count + 1;
        }
        bark(b);
        """
        output = self.capture_output(code)
        self.assertEqual(output, "8")  # 5th Fibonacci number
    
    def test_power_calculation(self):
        """Test power calculation (2^5 = 32)"""
        code = """
        base = 2;
        exponent = 5;
        result = 1;
        counter = 0;
        wagtail(counter < exponent){
            result = result * base;
            counter = counter + 1;
        }
        bark(result);
        """
        output = self.capture_output(code)
        self.assertEqual(output, "32")
    
    def test_prime_check(self):
        """Test prime number check for 17"""
        code = """
        num = 17;
        is_prime = 1;
        divisor = 2;
        wagtail(divisor < num && is_prime == 1){
            sniff(num % divisor == 0){
                is_prime = 0;
            }
            divisor = divisor + 1;
        }
        sniff(is_prime == 1){
            bark("Prime");
        }else{
            bark("Not Prime");
        }
        """
        output = self.capture_output(code)
        self.assertEqual(output, "Prime")
    
    def test_gcd_like_calculation(self):
        """Test GCD-like calculation using subtraction"""
        code = """
        a = 48;
        b = 18;
        wagtail(a != b){
            sniff(a > b){
                a = a - b;
            }else{
                b = b - a;
            }
        }
        bark(a);
        """
        output = self.capture_output(code)
        self.assertEqual(output, "6")  # GCD(48, 18) = 6
    
    def test_sum_of_squares(self):
        """Test sum of squares: 1^2 + 2^2 + 3^2 + 4^2"""
        code = """
        sum = 0;
        i = 1;
        wagtail(i <= 4){
            sum = sum + (i * i);
            i = i + 1;
        }
        bark(sum);
        """
        output = self.capture_output(code)
        self.assertEqual(output, "30")  # 1 + 4 + 9 + 16 = 30


if __name__ == '__main__':
    unittest.main()
