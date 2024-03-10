import tkinter as tk
def convert():
    try:
        temp = float(entry_temp.get())
        if var.get() == "Celsius to Fahrenheit":
            result = (temp * 9/5) + 32
            show_result(f"{temp}°C = {result}°F")
        elif var.get() == "Fahrenheit to Celsius":
            result = (temp - 32) * 5/9
            show_result(f"{temp}°F = {result}°C")
        else:
            show_result("Please select an option")
    except ValueError:
        show_result("Invalid input")
def show_result(text):
    result_window = tk.Toplevel(root)
    result_window.title("Conversion Result")
    lbl_result = tk.Label(result_window, text=text)
    lbl_result.pack(pady=10)
root = tk.Tk()
root.title("Temperature Converter")
entry_temp = tk.Entry(root)
entry_temp.pack(pady=10)
var = tk.StringVar()
var.set("Celsius to Fahrenheit")
option_menu = tk.OptionMenu(root, var, "Celsius to Fahrenheit", "Fahrenheit to Celsius")
option_menu.pack(pady=5)
btn_convert = tk.Button(root, text="Convert", command=convert)
btn_convert.pack(pady=5)
root.mainloop()
