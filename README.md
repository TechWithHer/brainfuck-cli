![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Repo Size](https://img.shields.io/github/repo-size/TechWithHer/brainfuck-cli)
![Last Commit](https://img.shields.io/github/last-commit/TechWithHer/brainfuck-cli)
![Language](https://img.shields.io/github/languages/top/TechWithHer/brainfuck-cli)
![GitHub stars](https://img.shields.io/github/stars/TechWithHer/brainfuck-cli?style=social)


# 🧠 Brainfuck CLI Interpreter

A minimalist yet powerful CLI-based interpreter for the [Brainfuck esoteric language](https://en.wikipedia.org/wiki/Brainfuck), built in Python. Designed to help developers understand how low-level interpreters work while offering a clean and professional tool for executing `.bf` programs.


---
You can learn more about this from: https://ambitious-yam-b71.notion.site/What-is-Brainfuck-20bdf188b81e8050a321e6efee10ca4d?source=copy_link 
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
