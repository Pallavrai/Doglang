import pytest
from doglang.Tokenizer import Tokenizer, Token, Tokens

def test_tokenize_single_keyword():
    """
    Tests if the tokenizer can correctly identify a single keyword.
    """
    code = "bark"
    tokens = Tokenizer(code)
    
    assert len(tokens) == 1
    token = tokens[0]
    assert token.token_type == Tokens.KEYWORD
    assert token.value == "bark"
    assert token.line == 1

def test_tokenize_simple_assignment():
    """
    Tests if the tokenizer can handle a simple variable assignment.
    """
    code = "my_var = 10"
    tokens = Tokenizer(code)

    assert len(tokens) == 3
    assert tokens[0].token_type == Tokens.IDENTIFIER
    assert tokens[0].value == "my_var"
    assert tokens[1].token_type == Tokens.ASSIGNMENT_OP
    assert tokens[2].token_type == Tokens.INT_LITERAL
    assert tokens[2].value == "10"
