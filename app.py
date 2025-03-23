import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# CSV File Path
CSV_FILE = os.path.join(os.path.dirname(__file__), "university_events.csv")

# Function to load events
def load_events():
    try:
        df = pd.read_csv(CSV_FILE)
        return df
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load events: {e}")
        print("error at read")
        return pd.DataFrame()

# Display events
def display_events():
    df = load_events()

    # Clear previous content
    for widget in result_frame.winfo_children():
        widget.destroy()

    if df.empty:
        messagebox.showinfo("No Events", "No events available.")
        return

    # Display events with index numbering
    for idx, (_, row) in enumerate(df.iterrows(), start=1):
        frame = tk.Frame(result_frame, bg="#f0f0f0", bd=2, relief=tk.GROOVE)
        frame.pack(pady=10, fill=tk.X, padx=10)

        # Display event index as ID
        index_label = tk.Label(frame, text=f"🔹 Event ID: {idx}", font=("Helvetica", 12, "bold"), bg="#f0f0f0")
        index_label.pack(anchor="w", padx=5)

        date_label = tk.Label(frame, text=f"📅 Date: {row['Date']}", font=("Helvetica", 12, "bold"), bg="#f0f0f0")
        date_label.pack(anchor="w", padx=5)

        dept_label = tk.Label(frame, text=f"🏫 Department: {row['Department']}", font=("Helvetica", 12, "italic"), bg="#f0f0f0")
        dept_label.pack(anchor="w", padx=5)

        title_label = tk.Label(frame, text=f"📌 Title: {row['Title']}", font=("Helvetica", 12, "bold"), bg="#f0f0f0")
        title_label.pack(anchor="w", padx=5)

        desc_label = tk.Label(frame, text=f"{row['Description']}", font=("Arial", 10), wraplength=750, bg="#f0f0f0", justify="left")
        desc_label.pack(anchor="w", padx=5) 
    # Display statistics
    plot_event_statistics(df)

# Plot event statistics
def plot_event_statistics(df):
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Count events by department
    event_count = df['Department'].value_counts()
    ax.bar(event_count.index, event_count.values, color='skyblue')

    ax.set_title("Event Count by Department")
    ax.set_ylabel("Number of Events")

    canvas = FigureCanvasTkAgg(fig, master=result_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# GUI Setup
root = tk.Tk()
root.title("University Notice Board")
root.geometry("500x600") 

# Header
header = tk.Label(root, text="University Notices and Events", font=("Helvetica", 18, "bold"), bg="#4CAF50", fg="white", pady=15)
header.pack(fill=tk.X)

# Result Frame
result_frame = tk.Frame(root, bg="white", bd=2, relief=tk.SUNKEN)
result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

display_events()

# Start GUI
root.mainloop()
