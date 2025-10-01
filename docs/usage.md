# Usage examples with code snippets

This section provides basic examples to help you get started with writing Doglang programs.

---

## Variable Assignment

Assign a value to a variable using the equals sign (`=`):
```bash
a = 10 ;
```

---

## Print Statement (`bark`)

Use the `bark` command to print values or messages:
```bash
bark(a);
bark("Hello, Doglang!");
```

---

## Loop Statement (`wagtail`)

The `wagtail` keyword starts a loop which runs while the condition is true:
```bash
a = 0;
wagtail(a < 5) {
bark(a);
a = a + 1;
}
```

This loops from 0 to 4, printing each value.

---

## Conditional Statement (`sniff`)

Use `sniff` to check conditions and optionally `else` for alternate execution:
```bash
a = 10;
sniff(a % 2 == 0) {
bark("Even");
} else {
bark("Odd");
}
```

This prints "Even" if `a` is even, otherwise prints "Odd".

---

## Input Statement (`fetch`)

Prompt the user for input using `fetch`:
```bash
name = fetch("Enter your name: ");
bark("Hello, " + name + "!");
```

---

## Running Doglang Code from Command Line

### From File
```bash
doglang -f your_program.doggy
```

### Inline Code Execution
```bash
doglang -e "a = 10; bark(a);"
```

---

Explore these examples and start creating your own fun Doglang programs!

