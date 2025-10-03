# Installation and setup instructions

Welcome to Doglang! Follow the instructions below to get started quickly with installing and running Doglang on your machine.

## Option 1: Install from PyPI (Recommended)

The easiest way to install Doglang is via Python's package manager `pip`. This option installs Doglang globally so you can run it from the command line anywhere.

### Requirements
- Python 3.6 or higher
- pip installed (usually included with Python)

### Installation Command

Open your terminal or command prompt and run:
```bash
pip install doglang
```

### Verify Installation

To verify Doglang was installed successfully, run:
```bash
doglang --help
```

This should display the Doglang command line usage information.

---

## Option 2: Install from GitHub Repository

You can install Doglang directly from the GitHub repository.

### Method A: Direct Install from GitHub

Install directly using pip:
```bash
pip install git+https://github.com/Pallavrai/Doglang.git
```

### Method B: Clone and Install Locally

1. Clone the repository:
```bash
git clone https://github.com/Pallavrai/Doglang.git
```

2. Change into the project directory:
```bash
cd doglang
```

3. Install the package:
```bash
pip install .
```

**For development (editable install):**
```bash
pip install -e .
```

This allows you to make changes to the source code and see them reflected immediately without reinstalling.

### Verify Installation

After installation, verify it works:
```bash
doglang --help
```

---

## Running Doglang Programs

Once installed (via any method above), use the `doglang` command:

### Running a program from a file

```bash
doglang -f your_program.doggy
```

### Running code directly from command line

Execute inline commands:
```bash
doglang -e "a = 10; bark(a);"
```

### Example with sample files

Try the included examples:
```bash
doglang -f examples/prog1.doggy
doglang -f examples/conditions.doggy
```

---

## Additional Options

### View Tokens (for debugging)

To see the tokens generated from your code:
```bash
doglang -f your_program.doggy --tokens
```

### Help Command

View all available options:
```bash
doglang --help
```

---

## Using a Virtual Environment (Recommended)

It's good practice to use a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install Doglang
pip install doglang
# OR install from local clone
pip install .

# When done, deactivate
deactivate
```

---

## Troubleshooting

### Command Not Found

If `doglang` command is not found after installation:

1. Make sure pip's bin directory is in your PATH
2. Try using the full path:
   ```bash
   python -m doglang.cli -f your_program.doggy
   ```

3. Or reinstall with:
   ```bash
   pip install --force-reinstall doglang
   ```

### Permission Errors

On some systems, you might need to use `pip install --user`:
```bash
pip install --user doglang
```

Or use `sudo` (not recommended):
```bash
sudo pip install doglang
```

### Import Errors

If you get import errors, ensure you're in the correct directory and the package is properly installed:
```bash
pip show doglang  # Check if installed
pip install --upgrade doglang  # Upgrade to latest version
```

---

## Notes

- Doglang source files use the `.doggy` extension
- Make sure your Python version is 3.6 or higher: `python --version`
- The `doglang` command is available globally after installation
- No need to run `python doglang.py` - that file doesn't exist as an entry point
- If you encounter issues, check your Python and pip versions or raise an issue in the [GitHub repo](https://github.com/Pallavrai/Doglang)

---

## Uninstalling

To remove Doglang:
```bash
pip uninstall doglang
```

---

Enjoy coding with Doglang! 🐾




