# Overview of language features

Doglang combines a fun dog-inspired syntax with core programming constructs to make coding enjoyable and easy to learn. Below is an overview of its main features:

---

## Core Language Constructs

- **Variable Assignment**  
  Assign values to variables without explicit type declarations:
```bash
a = 10;
```

- **Print Statement (`bark`)**  
Print values or messages to the console:
```bash
bark("Hello, Doglang!");
bark(a);
```

- **Loops (`wagtail`)**  
Loop while a condition is true:
```bash
wagtail(a < 5) {
bark(a);
a = a + 1;
}
```

- **Conditionals (`sniff` / `else`)**  
Branch execution based on conditions:
```bash
sniff(a == 10) {
bark("Ten!");
} else {
bark("Not ten.");
}
```

- **Input (`fetch`)**  
Get user input during program execution:
```bash
name = fetch("Enter your name: ");
```

---

## Supported Operators

- Arithmetic:  
`+`, `-`, `*`, `/`, `%`

- Comparison:  
`==`, `!=`, `<`, `>`, `<=`, `>=`

- Assignment:  
`=`

---

## File Extension

- Doglang source files use the `.doggy` extension.

---

## Limitations

- Currently supports only integer and string data types.
- No functions or user-defined procedures yet.
- Basic error reporting without detailed debug info.

---

## Tips for Writing Doglang Code

- End each statement with a semicolon (`;`).
- Enclose code blocks in curly braces `{}`.
- Variables are dynamically typed (no need to declare type).

---

Doglang is actively evolving, and new features are planned. Contributions and suggestions are always welcome!

