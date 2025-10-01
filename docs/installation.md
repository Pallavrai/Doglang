# Installation and setup instructions

Welcome to Doglang! Follow the instructions below to get started quickly with installing and running Doglang on your machine.

## Option 1: Install from PyPI (Recommended)

The easiest way to install Doglang is via Python's package manager `pip`. This option installs Doglang globally so you can run it from the command line anywhere.

### Requirements
- Python 3.7 or higher
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

## Option 2: Clone from GitHub

You can also clone the Doglang source repository to your local machine and run it directly.

### Steps

1. Clone the repository:
```bash
git clone https://github.com/Pallavrai/Doglang.git
```

2. Change into the project directory:
```bash
cd Doglang
```

3. (Optional) It is recommended to use a Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```

4. Install required dependencies:
```bash
pip install -r requirements.txt
```

---

## Running Doglang Programs

### Running a program from a file

If you cloned the repo, run:
```bash
python doglang.py -f your_program.doggy
```

If installed via PyPI:
```bash
doglang -f your_program.doggy
```

### Running code directly from command line

Execute inline commands:

If cloned:
```bash
python doglang.py -e "a = 10; bark(a);"
```

---

## Additional Options

- To see the tokens generated from your code (for debugging):
```bash
doglang -f your_program.doggy --tokens
```

---

## Notes

- Doglang source files use the `.doggy` extension.
- Make sure your Python environment is set up correctly for the above commands to work.
- If you encounter issues, check your Python and pip versions or raise an issue in the GitHub repo.

---

Enjoy coding with Doglang!




