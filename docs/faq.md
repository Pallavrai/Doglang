# Frequently Asked Questions (FAQ)

---

## What file extension do Doglang programs use?

Doglang source code files use the `.doggy` extension.

---

## How do I run a Doglang program?

After installing Doglang, run:
```bash
doglang -f your_program.doggy
```

You can also execute inline code with the `-e` option:
```bash
doglang -e "a = 10; bark(a);"
```

For more installation options, see the [Installation Guide](installation.md).

---

## What data types does Doglang support?

Currently, Doglang supports only **integers** and **strings**.

---

## Are functions supported in Doglang?

No, Doglang does not yet support user-defined functions or procedures. However, this is a planned feature! Check out [`examples/Ideas.md`](https://github.com/Pallavrai/Doglang/blob/main/examples/Ideas.md) for upcoming features.

---

## How does Doglang handle errors?

Doglang provides error messages for syntax, semantic, and runtime errors. Error handling is continuously being improved to provide better debugging information.

---

## Can I contribute to Doglang?

Absolutely! Contributions are welcome from users of all experience levels. You can:

- Improve or add features
- Fix bugs
- Enhance the documentation
- Suggest new dog-themed commands or capabilities

See the [Contributing Guide](CONTRIBUTING.md) for details on submitting pull requests and reporting issues.

---

## Where can I find more documentation?

Full documentation and usage examples are available online at:

[https://pallavrai.github.io/Doglang](https://pallavrai.github.io/Doglang)

---

## How do I view tokens for debugging?

Use the `--tokens` flag to see the tokenized output:
```bash
doglang -f your_program.doggy --tokens
```

---

## Can I use Doglang in a virtual environment?

Yes! It's recommended to use a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install doglang
```

---

## What Python version does Doglang require?

Doglang requires Python 3.6 or higher.

---

## Who created Doglang?

Doglang is a fun open-source project created by Pallav Rai to bring a playful spin to learning programming and language design.

---

## How do I uninstall Doglang?

Simply run:
```bash
pip uninstall doglang
```

---

If you have other questions, feel free to open an issue on the [GitHub repository](https://github.com/Pallavrai/Doglang).

