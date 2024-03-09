import tkinter as tk
def add_to_expression(char):
    entry_expression.insert(tk.END, char)
def clear_expression():
    entry_expression.delete(0, tk.END)
def calculate():
    try:
        expression = entry_expression.get()
        result = eval(expression)
        show_result(result)
    except Exception as e:
        show_result("Error")
def show_result(result):
    result_window = tk.Toplevel(root)
    result_window.title("Calculator Result")
    lbl_result = tk.Label(result_window, text=result)
    lbl_result.pack(pady=10)
root = tk.Tk()
root.title("Calculator")
entry_expression = tk.Entry(root)
entry_expression.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, columnspan=4)
for i in range(1, 10):
    tk.Button(button_frame, text=str(i), command=lambda i=i: add_to_expression(str(i))).grid(row=(i-1)//3, column=(i-1)%3, padx=5, pady=5)
tk.Button(button_frame, text="0", command=lambda: add_to_expression("0")).grid(row=3, column=1, padx=5, pady=5)
operators = ["+", "-", "*", "/"]
for i, operator in enumerate(operators):
    tk.Button(button_frame, text=operator, command=lambda operator=operator: add_to_expression(operator)).grid(row=i, column=3, padx=5, pady=5)
tk.Button(button_frame, text="C", command=clear_expression).grid(row=3, column=0, padx=5, pady=5, sticky="ew")
tk.Button(button_frame, text="=", command=calculate).grid(row=3, column=2, padx=5, pady=5, sticky="ew")
root.mainloop()