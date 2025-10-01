# DogLang Feature Ideas 🐕

## Completed Features ✅
- **fetch** – for input (`a = fetch("Enter the number")`) - ✅ Implemented in [`doglang/main.py`](doglang/main.py)
- **sniff** – for checking conditions (like if-else, `sniff (x == 5) { ... }`) - ✅ Implemented in [`doglang/SyntaxAnalyser.py`](doglang/SyntaxAnalyser.py)
- **bark** – for printing output - ✅ Implemented in [`doglang/main.py`](doglang/main.py)
- **wagtail** – for loops - ✅ Implemented in [`doglang/SyntaxAnalyser.py`](doglang/SyntaxAnalyser.py)
- **else** – for alternative conditions - ✅ Implemented in [`doglang/SyntaxAnalyser.py`](doglang/SyntaxAnalyser.py)

## New Procedural Programming Ideas 💡

### Function-like Constructs (No OOP)
- **sit** – for defining reusable code blocks/procedures (`sit greet() { bark("Hello"); }`)
- **rollover** – for returning values from procedures (`rollover result;`)

### Loop Control
- **heel** – for breaking out of loops (`heel;`)
- **stay** – for continuing to next iteration (`stay;`)

### Data Structures
- **pack** – for creating arrays/lists (`numbers = pack[1, 2, 3, 4];`)
- **dig** – for accessing array elements (`value = dig numbers[0];`)
- **bury** – for storing values in arrays (`bury numbers[0] = 10;`)

### String Operations
- **chew** – for string concatenation (`result = chew("Hello", " World");`)
- **wag** – for string length (`length = wag("DogLang");`)
- **nose** – for finding substrings (`found = nose("DogLang", "Lang");`)

### Math Operations  
- **treat** – for random numbers (`lucky = treat(1, 100);`)
- **chase** – for absolute value (`positive = chase(-42);`)

### File Operations
- **scratch** – for reading files (`content = scratch("data.txt");`)
- **mark** – for writing to files (`mark("output.txt", "Hello World");`)

### Error Handling
- **howl** – for throwing errors/exceptions (`howl "Something went wrong!";`)
- **rescue** – for catching errors (`rescue { /* error handling */ }`)

### Advanced Features
- **whistle** – for calling external system commands (`whistle("ls -la");`)
- **leash** – for importing other .doggy files (`leash "utilities.doggy";`)
- **collar** – for creating named scopes/namespaces

### Example Usage
```doggy
// Procedure definition
sit calculate_sum(a, b) {
    result = a + b;
    rollover result;
}

// Array operations
numbers = pack[10, 20, 30];
first = dig numbers[0];
bury numbers[1] = 25;

// String operations
message = chew("Hello", " DogLang");
len = wag(message);

// File operations
data = scratch("input.txt");
mark("output.txt", data);

// Error handling
howl "Division by zero!" sniff(b == 0);
```

## Implementation Priority 📋
1. **sit/rollover** - Procedure definitions and returns
2. **pack/dig/bury** - Array support  
3. **heel/stay** - Loop control
4. **chew/wag** - String operations
5. **howl/rescue** - Error handling
6. **leash** - Module system

## Notes 📝
- Maintaining procedural paradigm - no classes or objects
- All new keywords follow dog theme
- Avoiding redundancy with existing features
- Focus on practical programming constructs
