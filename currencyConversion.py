import tkinter as tk

from AlvarezCristianM6A1 import resultLabel

window = tk.Tk()
window.geometry("400x300")

label = tk.Label(text="Money Conversion Program",
                 font=("Arial", 20, "bold"),
                 bg="pink",
                 fg="white")
label.pack(pady=5)

weightEntry = tk.Entry(window)
weightEntry.pack(pady=10)

def poundsToUSD():
    pounds = weightEntry.get()
    pounds = float(pounds)
    usd = pounds * 1.36
    resultLabel.config(text=f"${usd:.2f}")

def USDToPounds():
    usd = weightEntry.get()
    usd = float(usd)
    pounds = usd * .71
    resultLabel.config(text=f"£{pounds:.2f}")

button = tk.Button(window, text="Convert to USD", command=poundsToUSD)
button.pack(pady=5)

toPoundsButton = tk.Button(window, text="Convert to Pounds", command=USDToPounds)
toPoundsButton.pack(pady=5)


resultLabel = tk.Label(text="")
resultLabel.pack(pady=5)

window.mainloop()


