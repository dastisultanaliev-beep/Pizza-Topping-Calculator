
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Pizza Topping Calculator")
app.geometry("400x350")

BASE_PRICE = 400

toppings = {
    "Cheese": 80,
    "Mushrooms": 60,
    "Jalapenos": 50,
    "Macadamia Nuts": 1000,
}

title_label = ctk.CTkLabel(
    app,
    text="Choose your toppings:",
    font=("Arial", 15, "bold")
)
title_label.pack()

checkboxes = {}


def calculate():
    total = BASE_PRICE

    for name, checkbox in checkboxes.items():
        if checkbox.get() == 1:
            total += toppings[name]

    price_label.configure(text=f"Total: {total} KGS")


for name, price in toppings.items():
    cb = ctk.CTkCheckBox(
        app,
        text=f"{name} (+{price} KGS)",
        command=calculate
    )
    cb.pack(anchor="w", padx=60, pady=6)
    checkboxes[name] = cb

price_label = ctk.CTkLabel(
    app,
    text=f"Total: {BASE_PRICE} KGS",
    font=("Arial", 20, "bold"),
)
price_label.pack(pady=20)

app.mainloop()
