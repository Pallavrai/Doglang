
# DogLang Programming Language

# 🐕 Welcome to DogLang!

DogLang is a fun, interpreted programming language I created with syntax inspired by our canine friends. With keywords like `bark` for printing, `wagtail` for loops, and `sniff` for conditionals, it brings a playful approach to coding.

<p align="center">
<img width="200" height="200" alt="doglang" src="https://github.com/user-attachments/assets/44bd913d-d69b-4bfd-b12d-6a7cdc1f286b" />
</p>

## 🚀 Join the Pack!

This is an open-source hobby project that welcomes contributors of all experience levels. Whether you're a seasoned developer or just starting out:

- Experiment with the language
- Suggest new "dog-themed" features
- Help improve documentation
- Add new functionality
- Fix bugs

The goal is to create something enjoyable while learning about language design and interpretation. Pull requests and issues are very welcome on GitHub!

## Overview

DogLang is a programming language with the following components:
- Lexical analyzer (Tokenizer)
- Syntax analyzer (Parser)
- Semantic analyzer
- Symbol table for variable management
- Interpreter for code execution

## Language Features

- Variable assignments
- Arithmetic operations with proper operator precedence
- Conditional statements (sniff)
- Loop constructs (wagtail)
- Print statements (bark)
- Input (fetch)
- Comparison operators
- Logical operators (&&, ||, !)
- **Custom operator precedence parser** (replaces eval for improved security)

### Expression Parsing

DogLang now features a custom-built **operator precedence parser** that evaluates expressions safely and efficiently. This eliminates the use of Python's `eval()` function, providing:

- **Enhanced Security**: No arbitrary code execution
- **Better Error Handling**: Clear, informative error messages
- **Full Control**: Custom operator precedence and behavior
- **Improved Performance**: Direct evaluation without string conversion

For detailed information about operator precedence and expression parsing, see [OPERATOR_PRECEDENCE.md](docs/OPERATOR_PRECEDENCE.md).

## Syntax Guide

### Variables and Assignment
```
a = 10;
```

### Print Statement
```
bark(variable_name);
```

### Loop Statement
```
wagtail(condition) {
  // loop body
}
```

### Conditional Statement
```
sniff(condition) {
  // if true
} else {
  // if false
}
```

### Input Statement
```
a = fetch("Enter a value:");
```

## Examples

### Basic Loop Example
```
a = 0;
wagtail(a<100) { 
  bark(a);
  a = a+10;
}
```
This program initializes a variable `a` to 0, then loops while `a` is less than 100, printing the value of `a` and incrementing it by 10 each iteration.

### Conditional Example
```
a = 10;
sniff(a%2==0) {
  bark("Even");
} else {
  bark("Odd");
}
```
This program checks if variable `a` is even or odd and prints the result.

### Input Example
```
a = fetch("Enter the number");
wagtail(a<10) {
  bark(a);
  a = a+1;
}
```
This program asks the user for a number and then counts from that number up to 10.

## How to Use DogLang

### Installation

#### From GitHub
Clone this repository to your local machine:
```
git clone https://github.com/pallavrai/doglang.git
cd doglang
pip install .
```

#### From PyPI
Install DogLang directly using pip:
```
pip install doglang
```

### Running a DogLang Program

1. From a file:
   ```
   doglang -f your_program.doggy
   ```

2. Directly from the command line:
   ```
   doglang -e "a=10; bark(a);"
   ```

### Additional Options
- To view the tokens generated from your code:
  ```
  doglang -f your_program.doggy --tokens
  ```

## File Extensions
DogLang programs use the `.doggy` file extension.

## Language Reference

### Keywords
- `bark`: Print a value
- `wagtail`: Loop construct
- `sniff`: Conditional statement
- `fetch`: Input from user
- `else`: Alternative branch for conditionals

### Operators

#### Arithmetic Operators
- `+`: Addition
- `-`: Subtraction
- `*`: Multiplication
- `/`: Division
- `%`: Modulo

#### Comparison Operators
- `==`: Equal to
- `!=`: Not equal to
- `>`: Greater than
- `<`: Less than
- `>=`: Greater than or equal to
- `<=`: Less than or equal to

#### Logical Operators
- `&&`: Logical AND
- `||`: Logical OR
- `!`: Logical NOT

#### Assignment Operator
- `=`: Assignment

#### Operator Precedence
Operators follow standard precedence rules (see [documentation](docs/OPERATOR_PRECEDENCE.md)):
1. Parentheses `()`
2. Unary operators `!`, `-`
3. Multiplicative `*`, `/`, `%`
4. Additive `+`, `-`
5. Comparison `<`, `>`, `<=`, `>=`
6. Equality `==`, `!=`
7. Logical AND `&&`
8. Logical OR `||`

## Tips for Writing DogLang Programs
1. Each statement should end with a semicolon (optional in some contexts)
2. Blocks of code are enclosed in curly braces `{}`
3. Variables don't need type declarations - they're inferred automatically

## Limitations
- Currently only supports integer and string data types
- No function definitions
- Limited error reporting

## Project Structure
- `Tokenizer.py`: Lexical analyzer
- `SyntaxAnalyser.py`: Parser
- `SemanticAnalyser.py`: Semantic analyzer
- `ExpressionParser.py`: Operator precedence parser for expressions
- `main.py`: Interpreter implementation
- `SymbolTable.py`: Symbol table for variable management
- `tests/`: Unit and integration tests

## Testing

Run the test suite to verify everything works correctly:

```bash
# Run all tests
python tests/__init__.py

# Run specific test files
python -m unittest tests.test_expression_parser -v
python -m unittest tests.test_integration -v
```
