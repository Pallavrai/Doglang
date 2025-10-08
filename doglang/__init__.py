from .main import Interpreter
from .error import DogLangError, SemanticError

__version__ = "1.0.0-alpha"
__all__ = ["Interpreter", "DogLangError", "SemanticError"]