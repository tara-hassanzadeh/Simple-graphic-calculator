# 🧮 Simple Calculator with Tkinter

A simple **graphical calculator** built using Python's Tkinter library.  
This project demonstrates the basics of **GUI development**, **event handling**, and **arithmetic operations** in Python. Ideal for beginners who want to explore Python GUI applications and build interactive tools. ✨

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| ➕ **Basic Arithmetic** | Addition, subtraction, multiplication, and division |
| ⚠️ **Error Handling** | Prevents division by zero and invalid inputs |
| 🔢 **Decimal Support** | Allows decimal numbers in calculations |
| 🧹 **Clear Functionality** | Reset the input field with a clear ("C") button |
| 🖥️ **User-Friendly Interface** | Simple and intuitive layout using Tkinter's grid system |
| 📐 **Responsive Design** | Buttons resize and adjust layout for a clean appearance |

---

## 🛠 How It Works

1. The calculator has an **Entry widget** to display the current input and results.
2. **Number buttons** append digits (or decimal point) to the current input.
3. **Operation buttons** (`+`, `-`, `*`, `/`) store the first number and the chosen operation.
4. Pressing **equals ("=")** calculates the result based on the selected operation.
5. **Clear ("C")** resets the calculator to its default state.

> The program uses functions for each arithmetic operation and manages the current input, selected operation, and previous number with global variables.

---

## 🎯 Skills You Can Practice

- 🐍 **Python Basics:** Variables, functions, control flow, and error handling
- 🖱️ **Tkinter GUI Development:** Widgets, layout management (`pack` and `grid`), and event handling
- ✅ **User Input Validation:** Handling edge cases such as multiple decimal points or division by zero
- 🧩 **Program Logic:** Managing state between multiple inputs and operations
- 🗂️ **Code Organization:** Structuring code into functions and separating GUI and logic

---

## 🚀 How to Run

1. Make sure Python is installed on your system 🐍
2. Save the code as `calculator.py` (or your preferred filename)
3. Open a terminal and run:

```bash
python sc.py
