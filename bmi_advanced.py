import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv
import datetime
import os

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and Height must be positive")
            return
        
        bmi = weight / (height ** 2)
        category = get_bmi_category(bmi)
        
        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")
        
        # Save to CSV
        save_to_csv(weight, height, bmi, category)
        
        # Update graph
        update_graph(bmi)
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def save_to_csv(weight, height, bmi, category):
    file_exists = os.path.isfile('bmi_history.csv')
    with open('bmi_history.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Date', 'Weight', 'Height', 'BMI', 'Category'])
        writer.writerow([datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), weight, height, f"{bmi:.2f}", category])

def update_graph(bmi):
    ax.clear()
    categories = ['Underweight', 'Normal', 'Overweight', 'Obese']
    values = [18.5, 24.9, 29.9, 35]
    colors = ['blue', 'green', 'orange', 'red']
    
    ax.bar(categories, values, color=colors, alpha=0.3)
    ax.axhline(y=bmi, color='black', linestyle='--', label=f'Your BMI: {bmi:.2f}')
    ax.set_ylabel('BMI Value')
    ax.set_title('BMI Categories')
    ax.legend()
    canvas.draw()

# GUI Window
root = tk.Tk()
root.title("BMI Calculator Advanced")
root.geometry("600x500")

frame = ttk.Frame(root, padding=10)
frame.pack()

ttk.Label(frame, text="Weight (kg):").grid(row=0, column=0, pady=5)
weight_entry = ttk.Entry(frame)
weight_entry.grid(row=0, column=1)

ttk.Label(frame, text="Height (m):").grid(row=1, column=0, pady=5)
height_entry = ttk.Entry(frame)
height_entry.grid(row=1, column=1)

calc_btn = ttk.Button(frame, text="Calculate BMI", command=calculate_bmi)
calc_btn.grid(row=2, column=0, columnspan=2, pady=10)

result_label = ttk.Label(frame, text="", font=("Arial", 12, "bold"))
result_label.grid(row=3, column=0, columnspan=2)

# Graph
fig, ax = plt.subplots(figsize=(5, 3))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()