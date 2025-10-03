# doglang/error.py

class DogLangError(Exception):
    """Base exception class for all errors in DogLang."""
    pass

class DogLangSyntaxError(DogLangError):
    """Exception raised for syntax errors found during parsing."""
    pass

# You can add other specific error types here in the future, like:
# class DogLangSemanticError(DogLangError):
#     pass
    