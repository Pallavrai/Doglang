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

## Loop Control (`heel` and `stay`)

### Break Statement (`heel`)
Use `heel` to exit a loop immediately:
```bash
i = 0;
wagtail(i < 10) {
    bark(i);
    i = i + 1;
    sniff i == 5 {
        heel;  # Exit loop when i equals 5
    }
}
```
This will print 0, 1, 2, 3, 4, 5 and then exit the loop.

### Continue Statement (`stay`)
Use `stay` to skip to the next iteration of a loop:
```bash
i = 0;
wagtail(i < 10) {
    i = i + 1;
    sniff i % 2 == 0 {
        stay;  # Skip even numbers
    }
    bark(i);
}
```
This will print only odd numbers: 1, 3, 5, 7, 9.

### Important Notes
- `heel` and `stay` can only be used inside loops
- Using them outside a loop will cause an error
- They work with both `wagtail` loops and nested loops

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

