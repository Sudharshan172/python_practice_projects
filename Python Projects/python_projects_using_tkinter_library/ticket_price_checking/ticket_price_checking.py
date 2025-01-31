import tkinter as tk
from tkinter import messagebox

boarding_place = ['Bangalore', 'Chennai', 'Hyderabad', 'Delhi']
dropping_place = ['Bangalore', 'Chennai', 'Hyderabad', 'Delhi']
transport_mode = ['Bus', 'Train', 'Flight']

price_chart = {
    ("Bangalore", "Chennai", "Bus"): 565,
    ("Bangalore", "Chennai", "Train"): 400,
    ("Bangalore", "Chennai", "Flight"): 2500,
    ("Bangalore", "Hyderabad", "Bus"): 980,
    ("Bangalore", "Hyderabad", "Train"): 700,
    ("Bangalore", "Hyderabad", "Flight"): 3200,
    ("Bangalore", "Delhi", "Bus"): 1400,
    ("Bangalore", "Delhi", "Train"): 1100,
    ("Bangalore", "Delhi", "Flight"): 6000,
    ("Chennai", "Hyderabad", "Bus"): 750,
    ("Chennai", "Hyderabad", "Train"): 500,
    ("Chennai", "Hyderabad", "Flight"): 2800,
    ("Chennai", "Delhi", "Bus"): 1950,
    ("Chennai", "Delhi", "Train"): 1500,
    ("Chennai", "Delhi", "Flight"): 5000,
    ("Hyderabad", "Delhi", "Bus"): 900,
    ("Hyderabad", "Delhi", "Train"): 700,
    ("Hyderabad", "Delhi", "Flight"): 4000
}

def check_price():
    boarding = boarding_var.get()
    dropping = dropping_var.get()
    transport = transport_var.get()

    if boarding == "Select" or dropping == "Select":
        messagebox.showerror("Input Error", "Please select both boarding and dropping points.")
        return
    if transport == "Select":
        messagebox.showerror("Input Error", "Please select a mode of transport.")
        return
    if boarding == dropping:
        messagebox.showerror("Input Error", "Boarding and dropping points cannot be the same.")
        return
    if (boarding, dropping, transport) in price_chart:
        route = (boarding, dropping, transport)
    else:
        route = (dropping, boarding, transport)
    price = price_chart.get(route, 0)

    if price == 0:
        messagebox.showerror("Route Error", "Route not available for the selected transport.")
        return
    messagebox.showinfo("Price Details", f"Price from {boarding} to {dropping} via {transport} is ₹{price}.")

root = tk.Tk()
root.title("Ticket Price Checking")
root.geometry('500x500')

title_label = tk.Label(root, text="Ticket Price Checking", font=("Times New Roman", 20, "bold"))
title_label.pack(pady=10)

boarding_point = tk.Label(root, text="Select Boarding Point", font=("Times New Roman", 15))
boarding_point.pack()
boarding_var = tk.StringVar()
boarding_var.set("Select")
boarding_dropdown = tk.OptionMenu(root, boarding_var, *boarding_place)
boarding_dropdown.pack()

dropping_point = tk.Label(root, text="Select Dropping Point", font=("Times New Roman", 15))
dropping_point.pack()
dropping_var = tk.StringVar()
dropping_var.set("Select")
dropping_dropdown = tk.OptionMenu(root, dropping_var, *dropping_place)
dropping_dropdown.pack()

transport_label = tk.Label(root, text="Select Mode of Transport", font=("Times New Roman", 15))
transport_label.pack()
transport_var = tk.StringVar()
transport_var.set("Select")
transport_dropdown = tk.OptionMenu(root, transport_var, *transport_mode)
transport_dropdown.pack()

check_price_button = tk.Button(root, text="Check Price", command=check_price, bg="blue", fg="white",
                                font=("Times New Roman", 15))
check_price_button.pack(pady=20)

root.mainloop()
