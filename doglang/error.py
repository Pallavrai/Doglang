class DogLangError(Exception):
    """Base exception class for all errors in DogLang."""
    pass

class DogLangSyntaxError(DogLangError):
    """Exception raised for syntax errors found during parsing."""
    pass

class SemanticError(DogLangError):
    """For errors found by the semantic analyser."""
    pass