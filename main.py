import tkinter as tk
from tkinter import ttk
import subprocess
from tkinter import messagebox


def set_dns(dns1, dns2):
    """
    Set the primary and secondary DNS servers for the active network interface.
    """
    try:
        # Get the name of the active network interface
        interface_name = subprocess.check_output(
            'netsh interface show interface | findstr "Connected"',
            shell=True, text=True
        ).split()[-1]

        # Set the primary DNS
        subprocess.run(f'netsh interface ip set dns "{interface_name}" static {dns1}', shell=True, check=True)

        # Set the secondary DNS
        subprocess.run(f'netsh interface ip add dns "{interface_name}" {dns2} index=2', shell=True, check=True)

        messagebox.showinfo("Success", "DNS settings updated successfully!")
    except subprocess.CalledProcessError as e:
        # Show an error message if the command fails
        messagebox.showerror("Error", f"Failed to set DNS:\n{e.stderr}")


def reset_dns():
    """
    Reset the DNS settings to default (Dynamic or DHCP).
    """
    try:
        # Get the name of the active network interface
        interface_name = subprocess.check_output(
            'netsh interface show interface | findstr "Connected"',
            shell=True, text=True
        ).split()[-1]

        # Reset DNS to DHCP
        subprocess.run(f'netsh interface ip set dns "{interface_name}" dhcp', shell=True, check=True)
        messagebox.showinfo("Success", "DNS settings reset to default (DHCP).")
    except subprocess.CalledProcessError as e:
        # Show an error message if the command fails
        messagebox.showerror("Error", f"Failed to reset DNS:\n{e.stderr}")


def on_ok_click():
    """
    Handle the OK button click event to set the DNS servers.
    """
    dns_one = dns_one_entry.get()
    dns_two = dns_two_entry.get()

    if not dns_one or not dns_two:
        # Show a warning if any DNS field is empty
        messagebox.showwarning("Input Error", "Both DNS fields must be filled!")
        return

    set_dns(dns_one, dns_two)


def on_dropdown_change(event):
    """
    Handle the dropdown change event to prefill DNS fields.
    """
    selected = dropdown.get()
    if selected == "Shekan":
        dns_one_entry.delete(0, tk.END)
        dns_two_entry.delete(0, tk.END)
        dns_one_entry.insert(0, "178.22.122.100")
        dns_two_entry.insert(0, "185.51.200.2")


# Create the main application window
root = tk.Tk()
root.title("DNS Setter")
root.geometry("400x300")
root.resizable(False, False)

# Label and input field for DNS One
dns_one_label = tk.Label(root, text="DNS One:", font=("Helvetica", 12))
dns_one_label.grid(row=0, column=0, padx=10, pady=10)

dns_one_entry = tk.Entry(root, width=30, font=("Helvetica", 10))
dns_one_entry.grid(row=0, column=1, padx=10, pady=10)

# Label and input field for DNS Two
dns_two_label = tk.Label(root, text="DNS Two:", font=("Helvetica", 12))
dns_two_label.grid(row=1, column=0, padx=10, pady=10)

dns_two_entry = tk.Entry(root, width=30, font=("Helvetica", 10))
dns_two_entry.grid(row=1, column=1, padx=10, pady=10)

# Dropdown for predefined DNS servers
dropdown_label = tk.Label(root, text="Select Preset DNS:", font=("Helvetica", 12))
dropdown_label.grid(row=2, column=0, padx=10, pady=10)

dns_presets = ["None", "Shekan"]
dropdown = ttk.Combobox(root, values=dns_presets, state="readonly", font=("Helvetica", 10))
dropdown.grid(row=2, column=1, padx=10, pady=10)
dropdown.set("None")  # Default value
dropdown.bind("<<ComboboxSelected>>", on_dropdown_change)

# Style for the buttons
style = ttk.Style()
style.configure("Rounded.TButton", font=("Helvetica", 12, "bold"), foreground="#000000", background="#d6d6d6", padding=10,
                borderwidth=3, relief="raised")

# OK button
ok_button = ttk.Button(root, text="Set DNS", command=on_ok_click, style="Rounded.TButton")
ok_button.grid(row=3, column=0, columnspan=2, pady=10, ipadx=20)

# Reset button
reset_button = ttk.Button(root, text="Reset DNS", command=reset_dns, style="Rounded.TButton")
reset_button.grid(row=4, column=0, columnspan=2, pady=10, ipadx=20)

# Run the application
root.mainloop()
