# main.py

import tkinter as tk
from tkinter import messagebox
from virtual_disk import open_create_virtual_disk

# Colors and style
PRIMARY_COLOR = "#007acc"
SECONDARY_COLOR = "#00b4d8"
BACKGROUND_COLOR = "#f0f8ff"
SECTION_BG = "#ffffff"
BUTTON_COLOR = "#007acc"
BUTTON_HOVER = "#005f99"
TEXT_COLOR = "#222222"
FONT_TITLE = ("Segoe UI", 20, "bold")
FONT_HEADER = ("Segoe UI", 14, "bold")
FONT_BUTTON = ("Segoe UI", 11)


def styled_button(parent, text, command):
    btn = tk.Button(parent, text=text, font=FONT_BUTTON, bg=BUTTON_COLOR, fg="white",
                    activebackground=BUTTON_HOVER, activeforeground="white", relief="flat",
                    cursor="hand2", height=2, width=35, command=command)
    btn.pack(pady=5)
    return btn


# Placeholder for future windows
def open_window(title):
    win = tk.Toplevel(root)
    win.title(title)
    win.configure(bg=BACKGROUND_COLOR)
    tk.Label(win, text=f"🛠️ {title}", font=FONT_HEADER,
             bg=BACKGROUND_COLOR, fg=PRIMARY_COLOR).pack(pady=20)


# Main window
root = tk.Tk()
root.title("MSA Cloud Management System")
root.geometry("600x750")
root.configure(bg=BACKGROUND_COLOR)

# Title
tk.Label(root, text="☁️ MSA Cloud Management System", bg=BACKGROUND_COLOR,
         fg=PRIMARY_COLOR, font=FONT_TITLE).pack(pady=15)

# QEMU Section
qemu_frame = tk.LabelFrame(root, text="🔧 Virtual Machine Management (QEMU)", bg=SECTION_BG,
                           fg=TEXT_COLOR, font=FONT_HEADER, padx=15, pady=10, bd=2, relief="groove")
qemu_frame.pack(fill="x", padx=25, pady=10)

styled_button(qemu_frame, "🗂️ Create Virtual Disk",
              lambda: open_create_virtual_disk(root))
styled_button(qemu_frame, "🖥️ Create Virtual Machine",
              lambda: open_window("Create Virtual Machine"))

# Docker Section
docker_frame = tk.LabelFrame(root, text="🐳 Docker Management", bg=SECTION_BG,
                             fg=TEXT_COLOR, font=FONT_HEADER, padx=15, pady=10, bd=2, relief="groove")
docker_frame.pack(fill="x", padx=25, pady=10)

styled_button(docker_frame, "📝 Create Dockerfile",
              lambda: open_window("Create Dockerfile"))
styled_button(docker_frame, "🏗️ Build Docker Image",
              lambda: open_window("Build Docker Image"))
styled_button(docker_frame, "🧱 List Docker Images",
              lambda: open_window("List Docker Images"))
styled_button(docker_frame, "📦 List Running Containers",
              lambda: open_window("List Running Containers"))
styled_button(docker_frame, "🛑 Stop Container",
              lambda: open_window("Stop Container"))

# Search & Pull Section
search_frame = tk.LabelFrame(root, text="🌐 Search & Pull Docker Images", bg=SECTION_BG,
                             fg=TEXT_COLOR, font=FONT_HEADER, padx=15, pady=10, bd=2, relief="groove")
search_frame.pack(fill="x", padx=25, pady=10)

styled_button(search_frame, "🔍 Search Local Docker Image",
              lambda: open_window("Search Local Docker Image"))
styled_button(search_frame, "🌎 Search Image on DockerHub",
              lambda: open_window("Search Image on DockerHub"))
styled_button(search_frame, "⬇️ Pull Image from DockerHub",
              lambda: open_window("Pull Image from DockerHub"))

# Footer
tk.Label(root, text="Developed for the Cloud Computing Course at MSA University", bg=BACKGROUND_COLOR,
         fg=PRIMARY_COLOR, font=("Segoe UI", 10, "italic")).pack(pady=15)

root.mainloop()
