from tkinter import messagebox, filedialog
import subprocess
import customtkinter as tk
import os

def check_sudo():
    return os.geteuid() == 0

tk.set_appearance_mode('dark')
tk.set_default_color_theme('green')

def main():
    if not check_sudo():
        messagebox.showwarning("Susemation Warning", "Please run Susemation with sudo permissions.")

    root = tk.CTk()
    root.title("Susemation")

    window_width = 400
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    label = tk.CTkLabel(root, text="Welcome to Susemation!", font=("Helvetica", 16))
    label.pack(pady=20)

    button = tk.CTkButton(root, text="Select File", command=select_file)
    button.pack()

    root.mainloop()

def handle_file(file):
    if file.endswith('.exe'):
        print('Found')
        try:
            # Run the .exe file with Wine
            subprocess.run(['wine', file])
        except Exception as e:
            messagebox.showerror('Susemation Error!', e)
    elif file.endswith('.tar.xz'):
        print('Found')
        try:
            file_directory = os.path.dirname(file)

            # Define the destination directory and extract tar.xz 
            subprocess.run(['tar', '--extract', '-xJf', file, '-C', file_directory])
            messagebox.showinfo('Susemation Info', 'tar.xz file extracted to dir: ' + file_directory)
        except Exception as e:
            messagebox.showerror('Susemation Error!', str(e))
    else:
        print('None')

def select_file():
    file_path = filedialog.askopenfilename(title="Select a file on your System", filetypes=[("tar.xz files", ".tar.xz"), ("exe Files", ".exe")])
    if file_path:
        handle_file(file_path)

if __name__ == "__main__":
    main()
