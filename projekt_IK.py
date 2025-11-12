import tkinter as tk
from tkinter import colorchooser, messagebox, simpledialog
import random
import os


def get_random_color_IK():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'#{r:02x}{g:02x}{b:02x}'


class RajzoloApp_IK:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Rajzoló - IK")
        self.root.geometry("800x600")

        self.brush_color = "black"
        self.brush_size = 2
        self.last_x = None
        self.last_y = None

        self.control_frame = tk.Frame(self.root, padx=5, pady=5)
        self.control_frame.pack(side=tk.TOP, fill=tk.X)

        self.color_button = tk.Button(self.control_frame, text="Szín választás", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT, padx=5)

        self.random_color_button = tk.Button(self.control_frame, text="Véletlen szín", command=self.use_random_color)
        self.random_color_button.pack(side=tk.LEFT, padx=5)

        self.size_button = tk.Button(self.control_frame, text="Ecsetméret", command=self.set_brush_size)
        self.size_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(self.control_frame, text="Törlés", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        self.info_button = tk.Button(self.control_frame, text="OS Info", command=self.show_os_info)
        self.info_button.pack(side=tk.LEFT, padx=5)

        self.canvas = tk.Canvas(self.root, bg="white", relief=tk.SUNKEN, borderwidth=2)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Válassz színt")
        if color_code[1]:
            self.brush_color = color_code[1]

    def use_random_color(self):
        self.brush_color = get_random_color_IK()

    def set_brush_size(self):
        new_size = simpledialog.askinteger("Ecsetméret", "Add meg az új ecsetméretet (1-20):", minvalue=1, maxvalue=20)
        if new_size:
            self.brush_size = new_size

    def clear_canvas(self):
        self.canvas.delete("all")

    def start_drawing(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                    width=self.brush_size, fill=self.brush_color,
                                    capstyle=tk.ROUND, smooth=tk.TRUE)
            self.last_x = event.x
            self.last_y = event.y

    def stop_drawing(self, event):
        self.last_x = None
        self.last_y = None

    def show_os_info(self):
        current_dir = os.getcwd()
        cpu_cores = os.cpu_count()
        this_file_name = os.path.basename(__file__)

        info_text = f"'OS' Modul:\n\n"
        info_text += f"1. os.getcwd():\n{current_dir}\n\n"
        info_text += f"2. os.cpu_count():\n{cpu_cores} CPU mag\n\n"
        info_text += f"3. os.path.basename(__file__):\n{this_file_name}"

        messagebox.showinfo("Rendszer Információ", info_text)

