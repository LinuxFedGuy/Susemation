from tkinter import messagebox, filedialog, ttk
import subprocess
import customtkinter as tk
import os
import zipfile
import rarfile
import threading

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
    elif file.endswith(('.tar.xz', '.zip', '.rar')):
        print('Found')
        try:
            file_directory = os.path.dirname(file)

            if file.endswith('.tar.xz'):
                # Extract tar.xz file
                subprocess.run(['tar', '--extract', '-xJf', file, '-C', file_directory])
            elif file.endswith('.zip'):
                # Extract zip file
                with zipfile.ZipFile(file, 'r') as zip_ref:
                    zip_ref.extractall(file_directory)
            elif file.endswith('.rar'):
                # Extract rar file
                with rarfile.RarFile(file, 'r') as rar_ref:
                    rar_ref.extractall(file_directory)

            messagebox.showinfo('Susemation Info', f'File extracted to dir: {file_directory}')
        except Exception as e:
            messagebox.showerror('Susemation Error!', str(e))
    else:
        print('None')

def select_file():
    file_path = filedialog.askopenfilename(title="Select a file on your System", filetypes=[("tar.xz files", ".tar.xz"), ("zip files", ".zip"), ("rar files", ".rar"), ("exe Files", ".exe")])
    if file_path:
        # Start a new thread for handling the file
        thread = threading.Thread(target=handle_file, args=(file_path,))
        thread.start()

if __name__ == "__main__":
    main()
