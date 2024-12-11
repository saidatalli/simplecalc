import tkinter as tk

def do_calculation(a, b, operand):
    if operand == '+':
        return a + b
    elif operand == '-':
        return a - b
    elif operand == '*':
        return a * b
    elif operand == '/':
        if b == 0:
            raise ZeroDivisionError("Error: You can't divide by zero!")
        else:
            return a / b

def calculate():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        operator = operator_var.get()

        result = do_calculation(num1, num2, operator)
        result_label.config(text=f"{num1} {operator} {num2} = {result}")

    except ZeroDivisionError:
        result_label.config(text="Error: Division by zero")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers only.")

def clear_fields():
    # Clear the input fields and reset the result label
    num1_entry.delete(0, tk.END)  # Clears the first number entry field
    num2_entry.delete(0, tk.END)  # Clears the second number entry field
    result_label.config(text="")  # Resets the result label

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create input fields and labels
num1_label = tk.Label(window, text="Enter first number:")
num1_entry = tk.Entry(window)

num2_label = tk.Label(window, text="Enter second number:")
num2_entry = tk.Entry(window)

operator_label = tk.Label(window, text="Choose operation:")
operator_var = tk.StringVar(window)
operator_var.set("+")
operator_dropdown = tk.OptionMenu(window, operator_var, "+", "-", "*", "/")

calculate_button = tk.Button(window, text="Calculate", command=calculate)
clear_button = tk.Button(window, text="Clear", command=clear_fields)
result_label = tk.Label(window, text="")

# Grid layout
num1_label.grid(row=0, column=0)
num1_entry.grid(row=0, column=1)

num2_label.grid(row=1, column=0)
num2_entry.grid(row=1, column=1)

operator_label.grid(row=2, column=0)
operator_dropdown.grid(row=2, column=1)

calculate_button.grid(row=3, column=0)
clear_button.grid(row=3, column=1)
result_label.grid(row=4, columnspan=2)

window.mainloop()