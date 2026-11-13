import tkinter as tk


root = tk.Tk()
root.title("Discount Calculator")
root.geometry("400x300")


# Original Price
price_label = tk.Label(root, text="Original Price:")
price_label.pack()

price_entry = tk.Entry(root)
price_entry.pack()


# Discount
discount_label = tk.Label(root, text="Discount (%):")
discount_label.pack()

discount_entry = tk.Entry(root)
discount_entry.pack()


# Result
result_label = tk.Label(root, text="Final Price: Rp. 0.00")
result_label.pack(pady=10)


# Calculation function
def calculate_discount():
    price = float(price_entry.get())
    discount = float(discount_entry.get())

    final_price = price * (1 - discount / 100)

    result_label.config(
        text=f"Final Price: Rp. {final_price:,.2f}"
    )


# Calculate button
calculate_button = tk.Button(
    root,
    text="Calculate",
    command=calculate_discount
)
calculate_button.pack()


root.mainloop()