def show_tutorial():
    tutorial = """
🐕 Welcome to Doglang! 🐕

Doglang is a fun, dog-themed programming language. Here's how to use it:

📝 Basic Syntax:
----------------
1. Variables:
   a = 5;  # Assign value 5 to variable 'a'

2. Print Statement:
   bark("Hello World");  # Prints to console

3. Input:
   name = fetch("What's your name? ");  # Gets user input

4. Conditional Statements:
   sniff(condition) {
       # code to execute if condition is true
   }

5. Loops:
   wagtail(condition) {
       # code to repeat while condition is true
   }

6. Comments:
   # This is a comment

📚 Example Programs:
-------------------
1. Hello World:
   bark("Woof! Hello World!");

2. Simple Counter:
   a = 0;
   wagtail(a < 10) {
       bark(a);
       a = a + 1;
   }

3. Even Numbers:
   a = 0;
   wagtail(a < 10) {
       sniff(a % 2 == 0) {
           bark(a);
       }
       a = a + 1;
   }

4. User Input:
   name = input("What's your name? ");
   bark("Hello " + name + "!");

🐾 Keywords:
-----------
- bark: Print to console
- sniff: If statement
- wagtail: While loop
- input: Get user input

For more examples, check the examples/ directory in the package.
"""
    print(tutorial) 