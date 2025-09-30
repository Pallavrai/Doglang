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

### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused on a single responsibility

## 🐕 Types of Contributions

### 1. New Language Features
- Add new dog-themed keywords (see `examples/Ideas` for inspiration)
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

3. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

4. Open a Pull Request on GitHub

### Commit Message Guidelines
- Use present tense ("Add feature" not "Added feature")
- Keep the first line under 50 characters
- Reference issues if applicable

### Pull Request Checklist
- [ ] Code follows the project's style guidelines
- [ ] Changes have been tested manually
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