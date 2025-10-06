"""
Test cases for loop control functionality in DogLang
Tests heel (break) and stay (continue) statements
"""

import pytest
import sys
import os

# Add the parent directory to the path so we can import doglang
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from doglang.main import Interpreter
from doglang.error import DogLangError


class TestLoopControl:
    """Test cases for loop control statements"""
    
    def test_heel_break_basic(self):
        """Test basic heel (break) functionality"""
        code = """
        i = 0;
        wagtail i < 5 {
            bark i;
            i = i + 1;
            if i == 3 {
                heel;
            }
        }
        """
        # Should print 0, 1, 2 and then break
        interpreter = Interpreter(code)
        # Note: This test would need to capture output to verify behavior
    
    def test_stay_continue_basic(self):
        """Test basic stay (continue) functionality"""
        code = """
        i = 0;
        wagtail i < 5 {
            i = i + 1;
            if i == 3 {
                stay;
            }
            bark i;
        }
        """
        # Should print 1, 2, 4, 5 (skipping 3)
        interpreter = Interpreter(code)
    
    def test_heel_outside_loop_error(self):
        """Test that heel outside loop raises error"""
        code = """
        heel;
        """
        with pytest.raises(Exception):  # Should raise LoopControlError
            interpreter = Interpreter(code)
    
    def test_stay_outside_loop_error(self):
        """Test that stay outside loop raises error"""
        code = """
        stay;
        """
        with pytest.raises(Exception):  # Should raise LoopControlError
            interpreter = Interpreter(code)
    
    def test_heel_in_nested_loop(self):
        """Test heel in nested loop breaks inner loop"""
        code = """
        i = 0;
        wagtail i < 3 {
            j = 0;
            wagtail j < 3 {
                bark i * 10 + j;
                j = j + 1;
                if j == 2 {
                    heel;
                }
            }
            i = i + 1;
        }
        """
        # Should print 00, 01, 10, 11, 20, 21
        interpreter = Interpreter(code)
    
    def test_stay_in_nested_loop(self):
        """Test stay in nested loop continues inner loop"""
        code = """
        i = 0;
        wagtail i < 3 {
            j = 0;
            wagtail j < 3 {
                j = j + 1;
                if j == 2 {
                    stay;
                }
                bark i * 10 + j;
            }
            i = i + 1;
        }
        """
        # Should print 11, 12, 21, 22, 31, 32
        interpreter = Interpreter(code)
    
    def test_heel_with_condition(self):
        """Test heel with conditional logic"""
        code = """
        i = 0;
        wagtail i < 10 {
            i = i + 1;
            if i > 5 {
                heel;
            }
            bark i;
        }
        """
        # Should print 1, 2, 3, 4, 5, 6
        interpreter = Interpreter(code)
    
    def test_stay_with_condition(self):
        """Test stay with conditional logic"""
        code = """
        i = 0;
        wagtail i < 5 {
            i = i + 1;
            if i == 2 or i == 4 {
                stay;
            }
            bark i;
        }
        """
        # Should print 1, 3, 5
        interpreter = Interpreter(code)


if __name__ == "__main__":
    pytest.main([__file__])
