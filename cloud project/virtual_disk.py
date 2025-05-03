import tkinter as tk
from tkinter import messagebox
import subprocess
import os


def open_create_virtual_disk(root):
    win = tk.Toplevel(root)
    win.title("Create Virtual Disk")
    win.geometry("400x300")
    win.configure(bg="#f4f4f4")

    tk.Label(win, text="Create Virtual Disk", font=(
        "Segoe UI", 14, "bold"), bg="#f4f4f4", fg="#007acc").pack(pady=10)

    # Disk Name
    tk.Label(win, text="Disk Name (with .qcow2/.img):", bg="#f4f4f4").pack()
    disk_name_entry = tk.Entry(win, width=30)
    disk_name_entry.pack(pady=5)

    # Format
    tk.Label(win, text="Disk Format:", bg="#f4f4f4").pack()
    format_var = tk.StringVar(value="qcow2")
    formats = ["qcow2", "raw", "vdi", "vmdk"]
    format_menu = tk.OptionMenu(win, format_var, *formats)
    format_menu.pack(pady=5)

    # Size
    tk.Label(win, text="Disk Size (e.g. 10G, 500M):", bg="#f4f4f4").pack()
    disk_size_entry = tk.Entry(win, width=30)
    disk_size_entry.pack(pady=5)

    def create_disk():
        disk_name = disk_name_entry.get()
        disk_format = format_var.get()
        disk_size = disk_size_entry.get()

        if not disk_name or not disk_size:
            messagebox.showerror("Error", "Please enter all fields.")
            return

       
        windows_dir = "C:\Users\Ibrahim\Desktop\cloud project\Virtual Disks"
        os.makedirs(windows_dir, exist_ok=True)  
        windows_full_path = os.path.join(windows_dir, disk_name)

        # تحويله لمسار Unix-style علشان bash يفهمه
        bash_path = windows_full_path.replace("\\", "/").replace("C:", "/c")

        # بناء الأمر الكامل اللي هيتنفذ
        bash_command = f'qemu-img create -f {disk_format} {bash_path} {disk_size}'

        try:
            subprocess.run([
                'cmd', '/c',
                f'start "" "C:\Users\Ibrahim\Desktop\MSYS2 MINGW64.lnk" /bin/bash -c "{bash_command}"'
            ], shell=True)
            messagebox.showinfo(
                "Success", f"Disk '{disk_name}' created successfully in:\n{windows_dir}")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to create disk:\n{e}")
        except FileNotFoundError:
            messagebox.showerror(
                "Error", "MSYS2 shortcut not found. Make sure the path is correct.")

    tk.Button(win, text="Create Disk", bg="#0096c7", fg="white", font=("Segoe UI", 10),
              command=create_disk).pack(pady=15)
