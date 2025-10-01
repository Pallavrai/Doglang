# Contributing to DogLang 🐕

Thank you for your interest in contributing to DogLang! This project welcomes contributions from developers of all experience levels.

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- Git

### Setting Up Development Environment

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/doglang.git
   cd doglang
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the package in development mode:
   ```bash
   pip install -e .
   ```

## 🛠️ Development Workflow

### Running Tests
Currently, the project doesn't have automated tests, but you can test manually:

```bash
# Test with example files
doglang -f examples/prog1.doggy

# Test direct execution
doglang -e "a=10; bark(a);"

# View tokens
doglang -f examples/conditions.doggy --tokens
```

## 📦 Building and Testing the Package

### Installing Build Dependencies

Before building, install the necessary build tools:

```bash
# Install/upgrade build tools
pip install --upgrade build twine setuptools wheel
```

### Building the Package

1. **Clean previous build artifacts:**
   ```bash
   rm -rf build/ dist/ *.egg-info/
   ```

2. **Build the package:**
   ```bash
   # Modern way (recommended)
   python -m build

   # Or using the traditional method
   python setup.py sdist bdist_wheel
   ```

3. **Verify the build:**
   ```bash
   ls -la dist/
   # You should see files like:
   # doglang-0.1.0-py3-none-any.whl
   # doglang-0.1.0.tar.gz
   ```

### Testing the Package Locally

#### Method 1: Test in a Fresh Virtual Environment

```bash
# Create a test environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install your built package
pip install dist/doglang-*.whl

# Test the installation
doglang --help
doglang -e "bark('Hello from packaged DogLang!');"

# Test with example files
doglang -f examples/prog1.doggy

# Clean up
deactivate
rm -rf test_env/
```

#### Method 2: Test with pip install from local directory

```bash
# In a new virtual environment
python -m venv test_local
source test_local/bin/activate

# Install from local directory
pip install .

# Run tests
doglang -f examples/conditions.doggy
doglang -e "a=fetch('Enter number: '); bark(a);"

# Clean up
deactivate
rm -rf test_local/
```

#### Method 3: Test both source and wheel distributions

```bash
# Test the source distribution
python -m venv test_source
source test_source/bin/activate
pip install dist/doglang-*.tar.gz
doglang -e "bark('Testing source distribution');"
deactivate

# Test the wheel distribution
python -m venv test_wheel
source test_wheel/bin/activate
pip install dist/doglang-*.whl
doglang -e "bark('Testing wheel distribution');"
deactivate

# Clean up
rm -rf test_source/ test_wheel/
```

### Quick Build and Test Script

Create this handy one-liner for quick testing:

```bash
# Clean, build, and test in one command
rm -rf build/ dist/ *.egg-info/ && python -m build && python -m venv quick_test && source quick_test/bin/activate && pip install dist/doglang-*.whl && doglang -e "bark('Package works!');" && deactivate && rm -rf quick_test/
```

### Package Validation Checklist

Before submitting your changes, ensure:

- [ ] Package builds without errors: `python -m build`
- [ ] Both wheel and source distributions are created
- [ ] Package installs cleanly in a fresh environment
- [ ] All example programs run correctly
- [ ] CLI commands work as expected
- [ ] Version number is updated if needed (in `setup.py` and `__init__.py`)
- [ ] All necessary files are included (check `MANIFEST.in`)

### Common Build Issues and Solutions

**Issue: ModuleNotFoundError during build**
```bash
# Solution: Ensure all dependencies are installed
pip install --upgrade setuptools wheel build
```

**Issue: Package doesn't include example files**
```bash
# Solution: Check MANIFEST.in includes the files
# Add to MANIFEST.in:
include examples/*.doggy
```

**Issue: Command not found after installation**
```bash
# Solution: Check entry_points in setup.py
# Should have:
entry_points={
    "console_scripts": [
        "doglang=doglang.cli:main",
    ],
},
```

**Issue: Import errors in installed package**
```bash
# Solution: Check __init__.py files exist and imports are correct
```

### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused on a single responsibility

## 🐕 Types of Contributions

### 1. New Language Features
- Add new dog-themed keywords (see [`examples/Ideas.md`](examples/Ideas.md) for inspiration)
- Implement data types (arrays, booleans, floats)
- Add built-in functions

### 2. Core Improvements
- Enhance error messages and reporting
- Improve the parser or interpreter
- Add support for comments in DogLang code
- Optimize performance

### 3. Documentation
- Improve README examples
- Add more example programs
- Write tutorials or guides
- Fix typos and clarify explanations

### 4. Testing
- Create unit tests for components
- Add integration tests
- Test edge cases and error conditions

### 5. Tooling
- IDE syntax highlighting
- Language server protocol support
- Better CLI interface

## 📝 Submitting Changes

### Pull Request Process

1. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them:
   ```bash
   git add .
   git commit -m "Add feature: brief description"
   ```

3. **Test your changes:**
   ```bash
   # Build and test the package
   rm -rf build/ dist/ *.egg-info/
   python -m build
   python -m venv test_changes
   source test_changes/bin/activate
   pip install dist/doglang-*.whl
   doglang -f examples/prog1.doggy
   deactivate
   rm -rf test_changes/
   ```

4. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

5. Open a Pull Request on GitHub

### Commit Message Guidelines
- Use present tense ("Add feature" not "Added feature")
- Keep the first line under 50 characters
- Reference issues if applicable

### Pull Request Checklist
- [ ] Code follows the project's style guidelines
- [ ] Changes have been tested manually
- [ ] Package builds and installs correctly
- [ ] Documentation has been updated if needed
- [ ] Commit messages are clear and descriptive

## 🐛 Reporting Issues

When reporting bugs, please include:
- DogLang version
- Python version
- Operating system
- Complete error message
- Minimal code example that reproduces the issue

## 💡 Suggesting Features

For new features:
- Check if it fits the "dog theme"
- Explain the use case
- Provide examples of how it would work
- Consider implementation complexity

## 🎯 Current Priority Areas

1. **Error Handling**: Improve error messages and add line numbers
2. **Testing**: Create a comprehensive test suite
3. **Documentation**: More examples and tutorials
4. **Language Features**: Functions, arrays, better data types
5. **Performance**: Optimize the interpreter

## 📚 Project Structure

```
doglang/
├── doglang/           # Main package
│   ├── Tokenizer.py   # Lexical analysis
│   ├── SyntaxAnalyser.py  # Parsing
│   ├── SemanticAnalyser.py  # Semantic analysis
│   ├── main.py        # Interpreter
│   ├── SymbolTable.py # Variable management
│   ├── cli.py         # Command line interface
│   └── error.py       # Error handling
├── examples/          # Example DogLang programs
├── setup.py           # Package configuration
└── README.md          # Project documentation
```

## 🤝 Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help newcomers learn and contribute
- Keep discussions focused on the project

## ❓ Questions?

- Open an issue for questions about contributing
- Check existing issues and pull requests first
- Don't hesitate to ask for help or clarification

## 🏆 Recognition

Contributors will be acknowledged in the project README. Significant contributions may earn you a mention in release notes!

---

Happy coding! 🐕✨