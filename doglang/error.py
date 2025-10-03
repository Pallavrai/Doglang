class DogLangError(Exception):
    """Base class for all language errors."""
    pass

class SemanticError(DogLangError):
    """For errors found by the semantic analyser."""
    pass