import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import os

# CSV File Path
CSV_FILE = "university_events.csv"

# Initialize CSV if it doesn't exist
if not os.path.exists(CSV_FILE):
    pd.DataFrame(columns=["Date", "Department", "Title", "Description"]).to_csv(CSV_FILE, index=False)


# Function to add event
def add_event():
    date = date_entry.get()
    department = dept_entry.get()
    title = title_entry.get()
    description = desc_text.get("1.0", tk.END).strip()

    if not (date and department and title and description):
        messagebox.showerror("Error", "All fields are required.")
        return

    # Add event to CSV
    df = pd.read_csv(CSV_FILE)
    new_event = {"Date": date, "Department": department, "Title": title, "Description": description}
    new_event_df = pd.DataFrame([new_event]) 
    df = pd.concat([df, new_event_df], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)

    messagebox.showinfo("Success", "Event added successfully!")
    clear_fields()

# Function to clear input fields
def clear_fields():
    date_entry.delete(0, tk.END)
    dept_entry.delete(0, tk.END)
    title_entry.delete(0, tk.END)
    desc_text.delete("1.0", tk.END)

# GUI Setup
admin_root = tk.Tk()
admin_root.title("Admin Panel - University Events")
admin_root.geometry("600x500")
admin_root.configure(bg="#f0f0f0")

# Header
header = tk.Label(admin_root, text="Admin Panel - Add Events", font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="white", pady=10)
header.pack(fill=tk.X)

# Form Fields
form_frame = tk.Frame(admin_root, bg="#f0f0f0")
form_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Date Field
tk.Label(form_frame, text="Date (YYYY-MM-DD):", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
date_entry = tk.Entry(form_frame, font=("Arial", 12))
date_entry.grid(row=0, column=1, pady=5)

# Department Field
tk.Label(form_frame, text="Department:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
dept_entry = tk.Entry(form_frame, font=("Arial", 12))
dept_entry.grid(row=1, column=1, pady=5)

# Title Field
tk.Label(form_frame, text="Event Title:", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=5)
title_entry = tk.Entry(form_frame, font=("Arial", 12))
title_entry.grid(row=2, column=1, pady=5)

# Description Field
tk.Label(form_frame, text="Description:", font=("Arial", 12), bg="#f0f0f0").grid(row=3, column=0, sticky="nw", pady=5)
desc_text = tk.Text(form_frame, height=5, width=40, font=("Arial", 12))
desc_text.grid(row=3, column=1, pady=5)

# Buttons
btn_frame = tk.Frame(admin_root, bg="#f0f0f0")
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="Add Event", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=add_event)
add_btn.pack(side=tk.LEFT, padx=5)

clear_btn = tk.Button(btn_frame, text="Clear", font=("Arial", 12, "bold"), bg="#f44336", fg="white", command=clear_fields)
clear_btn.pack(side=tk.LEFT, padx=5)

# Start Admin GUI
admin_root.mainloop()
