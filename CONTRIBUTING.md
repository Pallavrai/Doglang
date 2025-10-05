# Contributing to DogLang 🐕

First off, thank you for considering contributing to DogLang! We're building a fun, playful programming language with a dog theme, and we're excited to have you join the pack. 

Whether you're fixing a bug, adding a feature, improving documentation, or helping with tests, every contribution is valuable. This guide will help you get started.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Building the Package](#building-the-package)
- [Submitting Changes](#submitting-changes)
- [What to Contribute](#what-to-contribute)
- [Getting Help](#getting-help)

## 🤝 Code of Conduct

All contributors are expected to be respectful, inclusive, and professional. We're committed to providing a friendly, safe, and welcoming environment for everyone, regardless of experience level, background, or identity. Please:

- Be respectful and constructive in discussions
- Focus on what is best for the community
- Show empathy towards other community members
- Accept constructive criticism gracefully

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have:
- **Python 3.6 or higher** installed
- **Git** for version control
- A **GitHub account**
- Basic familiarity with Python and command-line tools

### Finding Something to Work On

The best way to start contributing:

1. **Browse open issues** on our [GitHub Issues page](https://github.com/Pallavrai/Doglang/issues)
2. Look for labels like:
   - `good first issue` - Perfect for newcomers
   - `help wanted` - Issues where we need assistance
   - `documentation` - Documentation improvements
   - `bug` - Bug fixes needed
   - `enhancement` - New features

3. **Have a new idea?** Open an issue first to discuss it with maintainers before starting work
4. **Comment on the issue** you want to work on to let others know you're tackling it

### Setting Up Your Development Environment

Follow these steps to get DogLang running locally:

#### 1. Fork and Clone the Repository

```bash
# Fork the repository on GitHub (click the "Fork" button)

# Clone your fork
git clone https://github.com/YOUR-USERNAME/doglang.git
cd doglang
```

#### 2. Create a Virtual Environment

Using a virtual environment keeps your dependencies isolated:

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

#### 3. Install in Development Mode

This is crucial! Installing in editable mode lets you modify the code and test changes immediately:

```bash
pip install -e .
```

#### 4. Verify Installation

Test that DogLang is working:

```bash
# Check the CLI is available
doglang --help

# Try running an example
doglang -e "bark('Hello, DogLang!');"

# Test with an example file (if available)
doglang -f examples/prog1.doggy
```

You're now ready to start contributing! 🎉

## 🔄 Development Workflow

### Creating a Feature Branch

Always create a new branch for your work:

```bash
# For a new feature
git checkout -b feat/add-howl-function

# For a bug fix
git checkout -b fix/parser-empty-file-error

# For documentation
git checkout -b docs/improve-readme
```

**Branch naming conventions:**
- `feat/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation changes
- `refactor/` - Code refactoring
- `test/` - Adding or modifying tests

### Making Changes

1. Make your code changes in the appropriate files
2. Test your changes frequently as you work
3. Keep commits focused and atomic (one logical change per commit)
4. Write clear commit messages (see [Commit Message Guidelines](#commit-message-guidelines))

### Testing Your Changes

**Important:** DogLang currently needs help building an automated test suite! This is a **high-priority contribution area**.

For now, please test manually:

```bash
# Test with example files
doglang -f examples/prog1.doggy
doglang -f examples/conditions.doggy

# Test direct code execution
doglang -e "a=10; bark(a);"
doglang -e "sniff(5 > 3) { bark('Five is greater!'); }"

# View tokens for debugging
doglang -f examples/conditions.doggy --tokens

# Test edge cases
doglang -e ""  # Empty input
doglang -e "bark('test');"  # Simple case
doglang -e "a=fetch('Enter: '); bark(a);"  # User input
```

**Test checklist before submitting:**
- [ ] Your changes work as expected
- [ ] Existing functionality still works
- [ ] Example programs still run correctly
- [ ] No new errors or warnings are introduced
- [ ] Edge cases are handled properly

## 🎨 Coding Standards

### Python Style Guidelines

We follow **PEP 8** style guidelines. Key points:

```python
# Good: Clear, descriptive names
def parse_expression(tokens):
    current_token = tokens[0]
    
# Avoid: Cryptic abbreviations
def p_expr(t):
    ct = t[0]
```

**Best practices:**
- Use **meaningful variable and function names**
- Keep functions **small and focused** on a single responsibility
- Add **docstrings** for functions and classes
- Use **comments** to explain complex logic, not obvious code
- Maximum line length: 79 characters (can extend to 99 for rare cases)
- Use 4 spaces for indentation (no tabs)

### Code Organization

```python
# Standard import order:
# 1. Standard library imports
import sys
from typing import List, Optional

# 2. Related third-party imports
import click

# 3. Local application imports
from doglang.tokenizer import Tokenizer
from doglang.parser import Parser
```

### Naming Conventions

- **Variables and functions:** `lowercase_with_underscores`
- **Classes:** `PascalCase`
- **Constants:** `UPPERCASE_WITH_UNDERSCORES`
- **Private methods:** `_leading_underscore`

### Commit Message Guidelines

Write clear, descriptive commit messages:

```bash
# Good commit messages:
git commit -m "Add support for boolean data types"
git commit -m "Fix parser error when handling empty files"
git commit -m "Update README with installation instructions"

# Avoid:
git commit -m "fixed stuff"
git commit -m "updates"
```

**Format:**
```
<type>: <subject>

<optional body>

<optional footer>
```

**Types:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, no logic change)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

**Example:**
```
feat: Add 'howl' keyword for uppercase output

Implements a new built-in function that converts strings
to uppercase before printing. This adds more variety to
output functions in DogLang.

Closes #42
```

## 🧪 Testing Guidelines

### Current Testing Status

DogLang is actively seeking contributors to build a comprehensive test suite! This is a **high-priority need**.

### Future Testing Framework

We plan to use **pytest** for testing. If you'd like to help set this up:

```bash
# Install pytest
pip install pytest pytest-cov

# Create tests in tests/ directory
# Run tests with:
pytest tests/
```

### What Tests We Need

1. **Unit Tests**
   - Tokenizer: Test lexical analysis of various inputs
   - Parser: Test syntax tree generation
   - Interpreter: Test code execution
   - Symbol Table: Test variable storage and retrieval

2. **Integration Tests**
   - End-to-end program execution
   - Error handling scenarios
   - CLI functionality

3. **Edge Cases**
   - Empty input
   - Invalid syntax
   - Undefined variables
   - Division by zero

### Manual Testing Checklist

Until automated tests exist, please verify:

- [ ] All example programs in `examples/` still work
- [ ] CLI commands execute without errors
- [ ] Error messages are clear and helpful
- [ ] New features work with existing functionality
- [ ] Edge cases don't cause crashes

## 📦 Building the Package

This section is for contributors interested in the package build process. You don't need to do this for typical contributions.

### Installing Build Dependencies

```bash
pip install --upgrade build twine setuptools wheel
```

### Building DogLang

1. **Clean previous builds:**
   ```bash
   rm -rf build/ dist/ *.egg-info/
   ```

2. **Build the package:**
   ```bash
   # Modern method (recommended)
   python -m build

   # Traditional method
   python setup.py sdist bdist_wheel
   ```

3. **Verify build artifacts:**
   ```bash
   ls -la dist/
   # Should show:
   # doglang-x.y.z-py3-none-any.whl
   # doglang-x.y.z.tar.gz
   ```

### Testing the Built Package

**Method 1: Fresh Virtual Environment**

```bash
# Create test environment
python -m venv test_env
source test_env/bin/activate  # Windows: test_env\Scripts\activate

# Install from wheel
pip install dist/doglang-*.whl

# Test it works
doglang --help
doglang -e "bark('Package test successful!');"

# Clean up
deactivate
rm -rf test_env/
```

**Method 2: Test Both Distributions**

```bash
# Test source distribution
python -m venv test_source
source test_source/bin/activate
pip install dist/doglang-*.tar.gz
doglang -e "bark('Source dist works!');"
deactivate

# Test wheel distribution
python -m venv test_wheel
source test_wheel/bin/activate
pip install dist/doglang-*.whl
doglang -e "bark('Wheel dist works!');"
deactivate

# Clean up
rm -rf test_source/ test_wheel/
```

### Build Validation Checklist

Before submitting package-related changes:

- [ ] Package builds without errors
- [ ] Both wheel and source distributions are created
- [ ] Package installs cleanly in fresh environment
- [ ] All example programs run correctly
- [ ] CLI commands work as expected
- [ ] Version number updated (if needed)
- [ ] MANIFEST.in includes all necessary files

### Common Build Issues

**Issue: ModuleNotFoundError during build**
```bash
# Solution: Install build dependencies
pip install --upgrade setuptools wheel build
```

**Issue: Package missing example files**
```bash
# Solution: Update MANIFEST.in
include examples/*.doggy
recursive-include examples *
```

**Issue: Command not found after install**
```bash
# Solution: Check setup.py entry_points
entry_points={
    "console_scripts": [
        "doglang=doglang.cli:main",
    ],
},
```

## 📤 Submitting Changes

### Pull Request Process

1. **Ensure your code is ready:**
   - All changes are committed
   - Code follows style guidelines
   - Manual testing is complete
   - Documentation is updated

2. **Push your branch:**
   ```bash
   git push origin your-branch-name
   ```

3. **Create a Pull Request:**
   - Go to the [DogLang repository](https://github.com/Pallavrai/Doglang)
   - Click "New Pull Request"
   - Select your branch
   - Fill out the PR template

### Pull Request Template

Use this format for your PR description:

```markdown
## Description
Brief description of what this PR does

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Test additions

## Related Issue
Closes #(issue number)

## Testing Done
- Tested with example files
- Tested CLI functionality
- Verified no regressions

## Checklist
- [ ] Code follows project style guidelines
- [ ] Changes have been tested manually
- [ ] Documentation updated if needed
- [ ] Commit messages are clear
```

### Review Process

1. A maintainer will review your PR
2. They may request changes or ask questions
3. Make requested changes and push updates
4. Once approved, your PR will be merged! 🎉

### After Your PR is Merged

- Your contribution will be acknowledged in the project
- Delete your feature branch (optional)
- Pull the latest changes from main:
  ```bash
  git checkout main
  git pull upstream main
  ```

## 🐾 What to Contribute

We welcome contributions in many areas:

### 1. New Language Features (High Priority)
- Implement new dog-themed keywords (see `examples/Ideas.md`)
- Add data types: booleans, floats, arrays
- Create built-in functions (string manipulation, math operations)
- Add support for functions and procedures
- Implement loops: `chase` (while), `dig` (for)

### 2. Testing Infrastructure (Highest Priority! 🌟)
- Set up pytest framework
- Write unit tests for tokenizer, parser, interpreter
- Create integration tests for end-to-end scenarios
- Add test coverage reporting
- Document testing procedures

### 3. Error Handling and Debugging
- Add line numbers to error messages
- Improve error message clarity
- Add better syntax error reporting
- Create helpful suggestions for common mistakes
- Add debug mode with verbose output

### 4. Documentation
- Improve README with more examples
- Create tutorial for language features
- Add API documentation
- Write guides for common tasks
- Translate documentation

### 5. Core Improvements
- Optimize interpreter performance
- Add support for code comments
- Improve parser error recovery
- Enhance symbol table management
- Add variable scoping

### 6. Tooling and Developer Experience
- Create syntax highlighting for editors (VS Code, Sublime, Vim)
- Build a language server protocol (LSP) implementation
- Add REPL mode for interactive coding
- Create a DogLang formatter
- Build a linter

### 7. Examples and Demos
- Add more `.doggy` example programs
- Create a showcase gallery
- Build demo applications
- Write code snippets for common patterns

## 📚 Project Structure

Understanding the codebase:

```
doglang/
├── doglang/                 # Main package directory
│   ├── __init__.py         # Package initialization
│   ├── Tokenizer.py        # Lexical analysis (converts code to tokens)
│   ├── SyntaxAnalyser.py   # Parsing (creates abstract syntax tree)
│   ├── SemanticAnalyser.py # Semantic analysis (validates meaning)
│   ├── main.py             # Interpreter (executes code)
│   ├── SymbolTable.py      # Variable storage and management
│   ├── cli.py              # Command-line interface
│   └── error.py            # Error handling and reporting
├── examples/               # Example DogLang programs
│   ├── prog1.doggy        # Basic examples
│   ├── conditions.doggy   # Conditional statements
│   └── Ideas.md           # Future feature ideas
├── tests/                  # Test suite (needs to be created!)
├── setup.py               # Package configuration
├── MANIFEST.in            # Package file inclusion rules
├── README.md              # Project overview
└── CONTRIBUTING.md        # This file
```

### Key Components

- **Tokenizer**: Breaks source code into tokens (keywords, operators, literals)
- **Parser**: Analyzes token structure and builds syntax tree
- **Semantic Analyzer**: Checks for logical errors and validates operations
- **Interpreter**: Executes the program by walking the syntax tree
- **Symbol Table**: Manages variable storage and scope

## ❓ Getting Help

### Where to Ask Questions

- **GitHub Issues**: For bug reports and feature requests
- **Pull Request Comments**: For questions about your PR
- **Issue Comments**: For questions about specific issues

### Before Asking

1. Check if your question is answered in this guide
2. Search existing issues and PRs
3. Review the README and documentation
4. Try to solve the problem yourself first

### How to Ask Good Questions

Include:
- What you're trying to do
- What you've already tried
- Complete error messages
- DogLang version, Python version, and OS
- Minimal code example that reproduces the issue

## 🎯 Current Priority Areas

Focus areas where we especially need help:

1. **Testing Framework** (Highest Priority!)
   - Set up pytest
   - Write comprehensive test suite
   - Add CI/CD pipeline

2. **Error Handling**
   - Add line numbers to errors
   - Improve error messages
   - Better error recovery

3. **Documentation**
   - More examples
   - Tutorials and guides
   - API documentation

4. **Language Features**
   - Functions and procedures
   - Arrays and data structures
   - Boolean and float types

5. **Performance**
   - Optimize interpreter
   - Profile and benchmark
   - Reduce memory usage

## 🏆 Recognition

Contributors are valued and recognized:

- All contributors are listed in the project README
- Significant contributions earn mentions in release notes
- Active contributors may be invited to be maintainers
- Your work helps build an awesome, fun programming language!

## 📄 License

By contributing to DogLang, you agree that your contributions will be licensed under the same license as the project.

---

## Ready to Contribute? 🚀

1. Find an issue or propose a new feature
2. Set up your development environment
3. Create a branch and make your changes
4. Test thoroughly
5. Submit a pull request

**Thank you for making DogLang better!** 🐕✨

Questions? Open an issue or reach out to the maintainers. We're here to help!

---

*Remember: Every expert was once a beginner. Don't be afraid to ask questions or make mistakes. We're all learning together!*
