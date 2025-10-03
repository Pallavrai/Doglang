import pytest
from doglang.Tokenizer import Tokenizer
from doglang.SyntaxAnalyser import SyntaxAnalyser, SyntaxErrorDogLang


def parse_code(code):
    tokenizer = Tokenizer(code)
    tokens = tokenizer.tokenize()
    parser = SyntaxAnalyser(tokens)
    return parser.parse()

def test_missing_semicolon():
    code = "x = 5"
    with pytest.raises(SyntaxErrorDogLang, match=";"):
        parse_code(code)

def test_unexpected_keyword():
    code = "bark wagtail;"
    with pytest.raises(SyntaxErrorDogLang, match="wagtail"):
        parse_code(code)

def test_unclosed_brace():
    code = "wagtail 5 { bark 10;"
    with pytest.raises(SyntaxErrorDogLang, match="}"):
        parse_code(code)