import tkinter as tk


def calculate(*args):
    try:
        value = f'{dns1.get()}\n{dns2.get()}'
        response.set(value)
    except ValueError:
        pass

root = tk.Tk()
root.title("Feet to Meters")
root.geometry("800x400")

# to make the GUI dimensions fixed
root.resizable(False, False)

dns1 = tk.StringVar()
dns_one = tk.Entry(root, width=20, textvariable=dns1, justify=tk.CENTER)
dns_one.grid(column=1, row=1, padx=10, pady=10)

dns2 = tk.StringVar()
dns_two = tk.Entry(root, width=20, textvariable=dns2, justify=tk.CENTER)
dns_two.grid(column=1, row=2, padx=10, pady=10)

response = tk.StringVar()
tk.Label(root, textvariable=response, bg='green', fg="white").grid(column=0, row=3)

tk.Button(root, text="OK", command=calculate).grid(column=0, row=4)

tk.Label(root, text="First DNS").grid(column=0, row=1)
tk.Label(root, text="Second DNS").grid(column=0, row=2)


dns_one.focus_force()
root.bind("<Return>\n", calculate)
root.mainloop()