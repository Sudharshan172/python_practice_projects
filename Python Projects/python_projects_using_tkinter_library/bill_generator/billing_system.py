import tkinter as tk
from tkinter import messagebox

product_price = {
    "Milk (250ml)": 20,
    "Bread": 40,
    "Eggs": 7.5,
    "Jam (200gm)": 75
}

cart = {}
total_cost = 0

def add_to_cart():
    global total_cost
    product = product_var.get()
    try:
        quantity = int(quantity_entry.get())
        if quantity <= 0:
            raise ValueError
        if product in cart:
            cart[product] += quantity
        else:
            cart[product] = quantity
        total_cost += product_price[product] * quantity
        update_cart_display()
        total_label.config(text=f"Total Cost: ₹{total_cost}")
        quantity_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive integer for quantity.")

def update_cart_display():
    cart_text.config(state="normal")
    cart_text.delete(1.0, tk.END)
    for product, quantity in cart.items():
        cart_text.insert(tk.END, f"{product}: {quantity} x ₹{product_price[product]} = ₹{quantity * product_price[product]}\n")
    cart_text.config(state="disabled")

def generate_bill():
    global total_cost
    if not cart:
        messagebox.showwarning("Empty Cart", "Your cart is empty. Add some products before generating a bill.")
        return
    bill_window = tk.Toplevel(root)
    bill_window.title("Final Bill")
    bill_window.geometry("400x400")

    bill_title = tk.Label(bill_window, text="Total Bill", font=("Times New Roman", 20, "bold"))
    bill_title.pack(pady=10)

    bill_text = tk.Text(bill_window, height=20, width=40, bg="lightyellow")
    bill_text.pack()

    bill_text.insert(tk.END, "Product Details:\n")
    bill_text.insert(tk.END, "-" * 40 + "\n")
    for product, quantity in cart.items():
        cost = product_price[product] * quantity
        bill_text.insert(tk.END, f"{product}: {quantity} x ₹{product_price[product]} = ₹{cost}\n")

    bill_text.insert(tk.END, "-" * 40 + "\n")
    bill_text.insert(tk.END, f"Total Cost: ₹{total_cost}\n")
    bill_text.config(state="disabled")

    close_button = tk.Button(bill_window, text="Close", command=bill_window.destroy, bg="red", fg="white")
    close_button.pack(pady=10)

root = tk.Tk()
root.title("Billing System")
root.geometry("500x600")

title_label = tk.Label(root, text="Billing System", font=("Times New Roman", 20, "bold"))
title_label.pack(pady=10)

product_label = tk.Label(root, text="Select Product", font=("Times New Roman", 15))
product_label.pack()

product_var = tk.StringVar()
product_var.set("Select")
product_dropdown = tk.OptionMenu(root, product_var, *product_price.keys())
product_dropdown.pack()

quantity_label = tk.Label(root, text="Enter Quantity", font=("Times New Roman", 15))
quantity_label.pack()

quantity_entry = tk.Entry(root)
quantity_entry.pack()

add_button = tk.Button(root, text="Add to Cart", command=add_to_cart, bg="green", fg="white")
add_button.pack(pady=10)

cart_label = tk.Label(root, text="Cart", font=("Times New Roman", 15, "bold"))
cart_label.pack(pady=10)

cart_text = tk.Text(root, height=10, width=40, bg="lightyellow")
cart_text.pack()

total_label = tk.Label(root, text="Total Cost: ₹0", font=("Times New Roman", 15, "bold"))
total_label.pack(pady=10)

generate_bill_button = tk.Button(root, text="Generate Bill", command=generate_bill, bg="blue", fg="white")
generate_bill_button.pack(pady=10)

root.mainloop()
