from threading import Thread
import tkinter as tk
from tkinter import scrolledtext, Button
import datetime
import requests

gui_running = True

def log(message):
    global gui
    gui.log(message)

# GUI for displaying logs
class APIGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("RestAPIConnectionTest v1.0")

        # Add a "Check" button to the GUI
        self.check_button = Button(self.root, text="Check", command=self.check_api_health)
        self.check_button.pack(pady=5)

        # area for logs
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=50, height=10)
        self.text_area.pack(padx=10, pady=10)
        self.text_area.config(state='disabled')

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def log(self, message):
        self.text_area.config(state='normal')
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.text_area.insert(tk.END, f"{timestamp} - {message}\n")
        self.text_area.config(state='disabled')
        self.text_area.yview(tk.END)
            
    def on_close(self):
        global gui_running
        gui_running = False  # Update the flag to indicate GUI is closing
        self.root.destroy()

    def check_api_health(self):
        # Perform the API call and log the result
        try:
            response = requests.get('http://localhost:8080/health')
            if response.status_code == 200:
                self.log(f"API Health Check: {response.json()}")
            else:
                self.log(f"API Health Check Failed: Status Code {response.status_code}")
        except Exception as e:
            self.log(f"API Health Check Error: {e}")

if __name__ == '__main__':
    gui = APIGui()
    gui.root.mainloop()