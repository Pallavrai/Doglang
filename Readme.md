# DogLang Programming Language

# 🐕 Welcome to DogLang!

DogLang is a fun, interpreted programming language I created with syntax inspired by our canine friends. With keywords like `bark` for printing and `wagtail` for loops, it brings a playful approach to coding.

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
- Arithmetic operations
- Loop constructs (wagtail)
- Print statements (bark)
- Comparison operators

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

## Examples

### Basic Example
```
a = 0;
wagtail(a<100) { 
    bark(a);
    a = a+10;
}
```
This program initializes a variable `a` to 0, then loops while `a` is less than 100, printing the value of `a` and incrementing it by 10 each iteration.

## How to Use DogLang

### Installation
Clone this repository to your local machine:
```
git clone https://github.com/yourusername/doglang.git
cd doglang
```

### Running a DogLang Program
DogLang provides two ways to execute code:

1. From a file:
   ```
   python doglang.py -f your_program.doggy
   ```

2. Directly from the command line:
   ```
   python doglang.py -e "a=10; bark(a)"
   ```

### Additional Options
- To view the tokens generated from your code:
  ```
  python doglang.py -f your_program.doggy --tokens
  ```

## File Extensions
DogLang programs use the `.doggy` file extension.

## Language Reference

### Keywords
- `bark`: Print a value
- `wagtail`: Loop construct

### Operators
- Arithmetic: `+`, `-`, `*`, `/`, `%`
- Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Assignment: `=`

## Tips for Writing DogLang Programs
1. Each statement should end with a semicolon (optional in some contexts)
2. Blocks of code are enclosed in curly braces `{}`
3. Variables don't need type declarations - they're inferred automatically

## Limitations
- Currently only supports integer data type
- No function definitions
- Limited error reporting

## Project Structure
- `doglang.py`: Main entry point for the interpreter
- `Tokenizer.py`: Lexical analyzer
- `SyntaxAnalyser.py`: Parser
- `SemanticAnalyser.py`: Semantic analyzer
- `main.py`: Interpreter implementation
- `SymbolTable.py`: Symbol table for variable management
- `evaluator.py`: Expression evaluation