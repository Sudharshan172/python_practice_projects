import tkinter as tk
from tkinter import messagebox

boarding_places = ['Bangalore', 'Chennai', 'Hyderabad', 'Delhi']
dropping_places = ['Bangalore', 'Chennai', 'Hyderabad', 'Delhi']
gender_options=['Male','Female','Others']
price_chart = {
    ("Bangalore", "Chennai"): 565,
    ("Bangalore", "Hyderabad"): 980,
    ("Bangalore", "Delhi"): 1400,
    ("Chennai", "Hyderabad"): 750,
    ("Chennai", "Delhi"): 1950,
    ("Hyderabad", "Delhi"): 900
}


def generate_ticket():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    boarding = boarding_var.get()
    dropping = dropping_var.get()
    if not name.strip():
        messagebox.showerror("Input Error", "Please enter your name.")
        return
    if not age.isdigit() or int(age) <= 0:
        messagebox.showerror("Input Error", "Please enter a valid positive age.")
        return
    if boarding == "Select" or dropping == "Select":
        messagebox.showerror("Input Error", "Please select both boarding and dropping points.")
        return
    if boarding == dropping:
        messagebox.showerror("Input Error", "Boarding and dropping points cannot be the same.")
        return

    if (boarding, dropping) in price_chart:
        route = (boarding, dropping)
    else:
        route = (dropping, boarding)
    price = price_chart.get(route, 0)

    if price == 0:
        messagebox.showerror("Route Error", "Route not available.")
        return

    ticket_window = tk.Toplevel(root)
    ticket_window.title("Your Ticket")
    ticket_window.geometry('400x300')

    ticket_title = tk.Label(ticket_window, text="Ticket Details", font=("Times New Roman", 20, "bold"))
    ticket_title.pack(pady=10)

    ticket_info = tk.Text(ticket_window, height=15, width=50, bg="lightyellow")
    ticket_info.pack(pady=10)

    ticket_info.insert(tk.END, f"Name: {name}\n")
    ticket_info.insert(tk.END, f"Age: {age}\n")
    ticket_info.insert(tk.END, f"Gender: {gender}\n")
    ticket_info.insert(tk.END, f"Boarding Point: {boarding}\n")
    ticket_info.insert(tk.END, f"Dropping Point: {dropping}\n")
    ticket_info.insert(tk.END, f"Amount: ₹{price}\n")
    ticket_info.config(state="disabled")

    close_button = tk.Button(ticket_window, text="Close", command=ticket_window.destroy, bg="red", fg="white")
    close_button.pack(pady=10)

root = tk.Tk()
root.title("Ticket Generator")
root.geometry('500x600')

# Title Label
title_label = tk.Label(root, text="Ticket Generator", font=("Times New Roman", 20, "bold"))
title_label.pack(pady=10)

# Name Entry
name_label = tk.Label(root, text="Enter Your Name:", font=("Times New Roman", 15))
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Age Entry
age_label = tk.Label(root, text="Enter Your Age:", font=("Times New Roman", 15))
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack(pady=5)

gender_label = tk.Label(root, text="Select your Gender:", font=("Times New Roman", 15))
gender_label.pack()
gender_var = tk.StringVar()
gender_var.set("Select")
gender_dropdown = tk.OptionMenu(root, gender_var,*gender_options)
gender_dropdown.pack()

# Boarding Point Dropdown
boarding_point = tk.Label(root, text="Select Boarding Point:", font=("Times New Roman", 15))
boarding_point.pack()
boarding_var = tk.StringVar()
boarding_var.set("Select")
boarding_dropdown = tk.OptionMenu(root, boarding_var, *boarding_places)
boarding_dropdown.pack()

# Dropping Point Dropdown
dropping_point = tk.Label(root, text="Select Dropping Point:", font=("Times New Roman", 15))
dropping_point.pack()
dropping_var = tk.StringVar()
dropping_var.set("Select")
dropping_dropdown = tk.OptionMenu(root, dropping_var, *dropping_places)
dropping_dropdown.pack()

generate_ticket_button = tk.Button(root, text="Generate Ticket", command=generate_ticket, bg="blue", fg="white",
                                   font=("Times New Roman", 15))
generate_ticket_button.pack(pady=20)

root.mainloop()
