import sys
import argparse
from doglang.main import Interpreter
from doglang.Tokenizer import Tokenizer

#!/usr/bin/env python3

def main():
    parser = argparse.ArgumentParser(description='DogLang Interpreter')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-e', '--execute', metavar='CODE', help='Execute DogLang code directly')
    group.add_argument('-f', '--file', metavar='FILE', help='Execute DogLang code from file')
    parser.add_argument('--tokens', action='store_true', help='Print tokens instead of executing')
    
    args = parser.parse_args()
    
    if args.execute:
        code = args.execute
    elif args.file:
        try:
            with open(args.file, 'r') as file:
                code = file.read()
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found")
            sys.exit(1)
        except Exception as e:
            print(f"Error reading file: {e}")
            sys.exit(1)
    
    try:
        if args.tokens:
            tokens = Tokenizer(code)
            print("Tokens:")
            for token in tokens:
                print(token)
        else:
            Interpreter(code)
    except Exception as e:
        print(f"Execution error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()