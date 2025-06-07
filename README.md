# 🧠 Brainfuck CLI Interpreter

A minimalist yet powerful CLI-based interpreter for the [Brainfuck esoteric language](https://en.wikipedia.org/wiki/Brainfuck), built in Python. Designed to help developers understand how low-level interpreters work while offering a clean and professional tool for executing `.bf` programs.

> Built with ❤️ by [Ayushi Singh](https://github.com/TechWithHer) — empowering SMEs through code, AI & automation.

---

## ✨ Features

- ✅ Full Brainfuck language support (`+`, `-`, `<`, `>`, `[`, `]`, `.`, `,`)
- 🔁 Loop stack handling
- 🖥️ Command-line execution of `.bf` files
- 💡 Clean, readable output
- 🧪 Simple examples to test functionality

---

## 📂 Project Structure

brainfuck-cli/
│
├── brainfuck.py # Interpreter logic
├── cli.py # Command-line interface
├── examples/ # Sample .bf programs
│ └── hello_world.bf
├── README.md # You're here
├── LICENSE # Open source MIT license
└── requirements.txt # Dependencies (optional)


---

## 🚀 How to Use

 🐍 Run from Python CLI
```bash 
python cli.py examples/hello_world.bf

Example Output:
Hello World!

📥 Installation (Optional if you want to make it pip-installable)

git clone git@github.com:TechWithHer/brainfuck-cli.git
cd brainfuck-cli
python cli.py examples/hello_world.bf
