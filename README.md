# 🧮 Scientific & Chain Calculator (Python CLI)

A command-line scientific and continuous-chain calculator built in Python using `match / case` pattern matching and the built-in `math` module.

## ✨ Features
- **Continuous Chaining:** Chain unlimited operations (`10 + 5 * 2 =`) using the running total until pressing `=` or `c` (Clear).
- **Basic Operations:** Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), Floor Division (`//`), Modulus (`%`), and Power (`**`).
- **Scientific Operations:** Square Root (`sqrt`), Factorial (`fact`), Base-10 Logarithm (`log`), and Degree-Based Trigonometry (`sin`, `cos`, `tan`).
- **Crash-Proof Validation:** Guards against non-numeric text (`ValueError`), `nan`/`inf`, division by zero, negative square roots, and non-integer factorials.

## 🚀 How to Run
```bash
git clone https://github.com
cd cli-calculator
python main.py
```
