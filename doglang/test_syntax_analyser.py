import pytest
from doglang.Tokenizer import Tokenizer
from doglang.SyntaxAnalyser import SyntaxAnalyser
from doglang.error import DogLangSyntaxError

def test_parser_raises_error_for_unknown_keyword():
    """Checks that a typo like 'wagdog' raises a syntax error."""

    code_with_typo = "wagdog" # A simple case with just the typo

    tokens = Tokenizer(code_with_typo)
    analyser = SyntaxAnalyser(tokens)

    with pytest.raises(DogLangSyntaxError) as excinfo:
        analyser.parse() # Run the parser

    # Check that the error message is exactly as required
    assert str(excinfo.value) == "Syntax Error: Unknown keyword 'wagdog' at line 1"