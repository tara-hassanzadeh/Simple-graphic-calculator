import tkinter as tk

# ---------- عملیات ریاضی ----------
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "خطا: تقسیم بر صفر"

# ---------- متغیرهای مدیریت ----------
first_num = None
operation = None

# ---------- توابع دکمه‌ها ----------
def click_number(num):
    current = entry_text.get()
    entry_text.set(current + str(num))

def click_operation(op):
    global first_num, operation
    try:
        first_num = float(entry_text.get())
        operation = op
        entry_text.set("")
    except:
        entry_text.set("خطا")

def calculate():
    global first_num, operation
    try:
        second_num = float(entry_text.get())
        if operation == '+':
            result = add(first_num, second_num)
        elif operation == '-':
            result = subtract(first_num, second_num)
        elif operation == '*':
            result = multiply(first_num, second_num)
        elif operation == '/':
            result = divide(first_num, second_num)
        entry_text.set(result)
    except:
        entry_text.set("خطا")
    finally:
        first_num = None
        operation = None

def clear():
    global first_num, operation
    entry_text.set("")
    first_num = None
    operation = None

# ---------- ساخت پنجره ----------
root = tk.Tk()
root.title("ماشین حساب ساده")
root.geometry("300x400")  # حتما x بین اعداد باشد، نه *

# ---------- Entry برای نمایش ----------
entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 24), bd=5, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# ---------- فریم دکمه‌ها ----------
button_frame = tk.Frame(root)
button_frame.pack()

# ---------- تعریف دکمه‌ها ----------
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for i, row in enumerate(buttons):
    for j, button in enumerate(row):
        if button == '=':
            b = tk.Button(button_frame, text=button, font=("Arial", 18), width=5, height=2, command=calculate)
        elif button in ['+', '-', '*', '/']:
            b = tk.Button(button_frame, text=button, font=("Arial", 18), width=5, height=2,
                          command=lambda op=button: click_operation(op))
        else:
            b = tk.Button(button_frame, text=button, font=("Arial", 18), width=5, height=2,
                          command=lambda num=button: click_number(num))
        b.grid(row=i, column=j, padx=5, pady=5)

# ---------- دکمه پاک کردن ----------
clear_button = tk.Button(root, text="C", font=("Arial", 18), width=22, height=2, bg="#ff6666", fg="white", command=clear)
clear_button.pack(pady=5)

# ---------- اجرای برنامه ----------
root.mainloop()