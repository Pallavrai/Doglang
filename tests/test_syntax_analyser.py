import pytest
from doglang.Tokenizer import Tokenizer
from doglang.SyntaxAnalyser import SyntaxAnalyser
from doglang.error import DogLangSyntaxError

def test_parser_handles_valid_code():
    """Tests that a simple, valid program parses without errors."""
    code = 'bark "hello";'
    tokens = Tokenizer(code)
    analyser = SyntaxAnalyser(tokens)
    # This should run without raising any exceptions
    analyser.parse()

def test_parser_raises_error_for_unknown_keyword():
    """
    This is the main test.
    It checks that a typo like 'wagdog' raises a specific syntax error.
    """
    # This code contains an invalid keyword on the second line
    code_with_typo = 'bark "hello";\nwagdog'
    
    tokens = Tokenizer(code_with_typo)
    analyser = SyntaxAnalyser(tokens)
    
    # Use pytest.raises to check that the correct exception is thrown
    with pytest.raises(DogLangSyntaxError) as excinfo:
        analyser.parse() # This line should trigger the error
        
    # Assert that the error message is exactly what the issue requires
    assert str(excinfo.value) == "Syntax Error: Unknown keyword 'wagdog' at line 2"

def test_parser_raises_error_for_unexpected_token():
    """Tests that the parser fails on other invalid syntax."""
    code_with_bad_token = '"hello";' # A string cannot start a statement
    
    tokens = Tokenizer(code_with_bad_token)
    analyser = SyntaxAnalyser(tokens)
    
    with pytest.raises(DogLangSyntaxError):
        analyser.parse()