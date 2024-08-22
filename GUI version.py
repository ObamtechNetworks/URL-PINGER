import tkinter as tk
import requests

def ping_url():
    url = url_entry.get()
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            result_label.config(text="Success: OK")
        else:
            result_label.config(text=f"Failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Error: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("URL Pinger")

# Create the input field
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

# Create the button
ping_button = tk.Button(root, text="Ping URL", command=ping_url)
ping_button.pack(pady=10)

# Create the result label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the application
root.mainloop()
