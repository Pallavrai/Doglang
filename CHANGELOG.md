# Changelog

All notable changes to the Doglang project will be documented in this file.

## [Unreleased] - 2025-10-01

### Added
- **Operator Precedence Parser**: Implemented a custom Pratt parser for expression evaluation
  - Replaces Python's `eval()` for improved security and control
  - Supports all arithmetic, comparison, and logical operators
  - Proper operator precedence (multiplication before addition, etc.)
  - Support for parentheses to override precedence
  - Support for unary operators (`-` for negation, `!` for logical NOT)
- **ExpressionParser Module** (`doglang/ExpressionParser.py`)
  - `ExpressionParser` class implementing precedence climbing algorithm
  - `parse_and_evaluate()` convenience function
  - Comprehensive error handling with clear error messages
- **Unit Tests** (`tests/test_expression_parser.py`)
  - 34 test cases covering all operators and precedence rules
  - Tests for arithmetic, comparison, logical operators
  - Tests for parentheses and operator precedence
  - Tests for unary operators
  - Tests for variable lookup
  - Tests for error conditions (division by zero, undefined variables, etc.)
- **Integration Tests** (`tests/test_integration.py`)
  - 14 integration tests for complete Doglang programs
  - Tests for conditionals, loops, and complex expressions
  - End-to-end testing of the interpreter with the new parser
- **Documentation**
  - `docs/OPERATOR_PRECEDENCE.md`: Comprehensive documentation of the parser
  - Updated `Readme.md` with information about the new parser
  - Detailed operator precedence table
  - Usage examples and best practices

### Changed
- **main.py**: Updated `expression_stmt()` method to use ExpressionParser instead of `eval()`
- **SemanticAnalyser.py**: Updated `check()` method to use ExpressionParser instead of `eval()`
- **README.md**: 
  - Added section about expression parsing and security improvements
  - Updated operator documentation with precedence information
  - Added testing section
  - Updated project structure

### Improved
- **Security**: Eliminated use of `eval()`, preventing arbitrary code execution
- **Error Handling**: More informative error messages for expression evaluation
- **Performance**: Direct evaluation without string conversion overhead
- **Maintainability**: Clear, well-documented code with comprehensive tests

### Technical Details

#### Operator Precedence Levels
1. Parentheses: `()`
2. Unary operators: `!`, `-` (unary)
3. Multiplicative: `*`, `/`, `%`
4. Additive: `+`, `-`
5. Comparison: `<`, `>`, `<=`, `>=`
6. Equality: `==`, `!=`
7. Logical AND: `&&`
8. Logical OR: `||`

#### Example Expression Evaluations
- `2 + 3 * 4` → `14` (multiplication first)
- `(2 + 3) * 4` → `20` (parentheses override)
- `10 % 2 == 0` → `true` (modulo then equality)
- `5 > 3 && 10 < 20` → `true` (comparisons then AND)

### Testing
- All 34 unit tests passing
- All 14 integration tests passing
- All example programs (prog.doggy, conditions.doggy, prog1.doggy) working correctly

### Breaking Changes
None. This change is fully backward compatible with existing Doglang programs.

### Migration Guide
No migration needed. All existing Doglang programs will continue to work as before.

### Future Enhancements
- Support for floating-point numbers
- String concatenation with `+` operator
- Bitwise operators
- Ternary conditional operator
- Function calls in expressions
- Type checking for expressions
- Constant folding optimization
