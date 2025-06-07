import argparse
from brainfuck import run_brainfuck

def main():
    parser = argparse.ArgumentParser(description="Brainfuck CLI Interpreter")
    parser.add_argument("file", help="Path to Brainfuck code file")
    args = parser.parse_args()

    with open(args.file, 'r') as f:
        code = f.read()

    result = run_brainfuck(code)
    print("\nOutput:\n", result)

if __name__ == "__main__":
    main()

