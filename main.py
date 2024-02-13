import tkinter as tk
from tkinter import messagebox, filedialog
import os
import subprocess

def check_sudo():
    return os.geteuid() == 0

def main():
    if not check_sudo():
        messagebox.showwarning("Susemation Warning", "Please run Susemation with sudo permissions.")

    root = tk.Tk()
    root.title("Susemation")

    # Dracula colors
    dracula_bg = "#282a36"
    dracula_fg = "#f8f8f2"
    dracula_button_bg = "#44475a"
    dracula_button_fg = "#f8f8f2"

    root.configure(bg=dracula_bg)

    window_width = 400
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    label = tk.Label(root, text="Welcome to Susemation!", font=("Helvetica", 16), bg=dracula_bg, fg=dracula_fg)
    label.pack(pady=20)

    button = tk.Button(root, text="Select File", command=select_file, bg=dracula_button_bg, fg=dracula_button_fg)
    button.pack()

    root.mainloop()


def handle_file(file):
    if file.endswith('.exe'):
        print('Found')
        try:
            # Run the .exe file with Wine
            subprocess.run(['wine', file])
        except Exception as e:
            tk.messagebox.showerror('Susemation Error!', e)
    elif file.endswith('.tar.xz'):
        print('Found')
        try:
            file_directory = os.path.dirname(file)

            # Define the destination directory and extract tar.xz 
            subprocess.run(['tar', '--extract', '-xJf', file, '-C', file_directory])
        except Exception as e:
            tk.messagebox.showerror('Susemation Error!', str(e))
    else:
        print('None')

def select_file():
    file_path = filedialog.askopenfilename(title="Select a file on your System", filetypes=[("tar.xz files", ".tar.xz"), ("exe Files", ".exe")])
    if file_path:
        handle_file(file_path)

if __name__ == "__main__":
    main()
