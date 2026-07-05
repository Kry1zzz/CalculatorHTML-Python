# In Python
import tkinter as tk
from tkinter import font

total = None
current_number = None

def process_input():
    global total, current_number
    error_label.config(text="")
    
    if number_entry.winfo_viewable():
        num_input = number_entry.get().strip()
        
        if num_input == "=":
            if total is None:
                display_label.config(text="Final result: null")
            else:
                display_label.config(text=f"Final result: {total}")
            number_frame.pack_forget()
            operator_frame.pack_forget()
            return
            
        try:
            if "." in num_input:
                number = float(num_input)
            else:
                number = int(num_input)
        except ValueError:
            error_label.config(text="This does not look like a number. Try again.")
            number_entry.delete(0, tk.END)
            return

        if total is None:
            total = number
            display_label.config(text=f"Current result: {total}")
            number_label.config(text="Enter a number (or '=' to exit):")
            number_entry.delete(0, tk.END)
        else:
            current_number = number
            number_frame.pack_forget()
            operator_frame.pack(anchor="w", pady=5)
            operator_entry.delete(0, tk.END)
            operator_entry.focus()

    elif operator_frame.winfo_viewable():
        op = operator_entry.get().strip()
        
        if op not in ["+", "-", "*", "/"]:
            error_label.config(text="Invalid operator! Use only +, -, * or /")
            operator_entry.delete(0, tk.END)
            return
            
        if op == "+":
            total += current_number
        elif op == "-":
            total -= current_number
        elif op == "*":
            total *= current_number
        elif op == "/":
            if current_number == 0:
                error_label.config(text="Division by zero!")
                operator_frame.pack_forget()
                number_frame.pack(anchor="w", pady=5)
                number_entry.delete(0, tk.END)
                number_entry.focus()
                return
            total /= current_number

        display_label.config(text=f"Result: {total}")
        
        operator_frame.pack_forget()
        number_frame.pack(anchor="w", pady=5)
        number_entry.delete(0, tk.END)
        number_entry.focus()

root = tk.Tk()
root.title("Sequential Calculator")
root.configure(bg="#000000")
root.geometry("500x580")

bold_font = font.Font(family="Arial", size=11, weight="bold")
title_font = font.Font(family="Arial", size=13, weight="bold")
author_font = font.Font(family="Arial", size=16, weight="bold")

# Авторская надпись в самом верху (Исправленная строка 88)
author_label = tk.Label(
    root, text="By Kry1zz", font=author_font, 
    bg="#000000", fg="#FF8C00"
)
author_label.pack(pady=(15, 0))

instruction_text = (
    "1. Enter the first number and press Enter.\n"
    "2. Enter the second number, then enter the operation sign\n"
    "   (+, -, *, /) that will apply to this number.\n"
    "3. Repeat this step as much as you want: each time a new\n"
    "   number is entered first, and then a sign for it.\n"
    "4. To complete the calculations and get the final result,\n"
    "   just enter = instead of a number."
)

instruction_box = tk.Label(
    root, text=instruction_text, justify="left", font=bold_font,
    bg="#000000", fg="#FF8C00", bd=2, relief="solid", highlightthickness=2,
    highlightbackground="#FF8C00", padx=10, pady=10
)
instruction_box.pack(fill="x", padx=20, pady=15)

display_label = tk.Label(
    root, text="Current result: Not entered yet", font=title_font,
    bg="#000000", fg="#FF8C00", bd=2, relief="solid", height=2, anchor="w", padx=10
)
display_label.pack(fill="x", padx=20, pady=5)

error_label = tk.Label(root, text="", font=bold_font, bg="#000000", fg="#FF0000")
error_label.pack(fill="x", padx=20, pady=5)

number_frame = tk.Frame(root, bg="#000000")
number_frame.pack(anchor="w", padx=20, pady=5)

number_label = tk.Label(
    number_frame, text="Enter the first number (or '=' to exit):",
    font=bold_font, bg="#000000", fg="#FF8C00"
)
number_label.pack(anchor="w")

number_entry = tk.Entry(
    number_frame, font=title_font, bg="#000000", fg="#FF8C00",
    insertbackground="#FF8C00", bd=2, relief="solid", width=30
)
number_entry.pack(anchor="w", pady=5)
number_entry.focus()
number_entry.bind("<Return>", lambda event: process_input())

number_button = tk.Button(
    number_frame, text="Submit Number", font=bold_font,
    bg="#FF8C00", fg="#000000", activebackground="#000000",
    activeforeground="#FF8C00", bd=2, relief="raised", command=process_input
)
number_button.pack(anchor="w", pady=5)

operator_frame = tk.Frame(root, bg="#000000")

operator_label = tk.Label(
    operator_frame, text="Enter operator (+, -, *, /):",
    font=bold_font, bg="#000000", fg="#FF8C00"
)
operator_label.pack(anchor="w")

operator_entry = tk.Entry(
    operator_frame, font=title_font, bg="#000000", fg="#FF8C00",
    insertbackground="#FF8C00", bd=2, relief="solid", width=30
)
operator_entry.pack(anchor="w", pady=5)
operator_entry.bind("<Return>", lambda event: process_input())

operator_button = tk.Button(
    operator_frame, text="Submit Operator", font=bold_font,
    bg="#FF8C00", fg="#000000", activebackground="#000000",
    activeforeground="#FF8C00", bd=2, relief="raised", command=process_input
)
operator_button.pack(anchor="w", pady=5)

root.mainloop()
