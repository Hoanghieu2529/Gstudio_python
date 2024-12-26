import tkinter as tk
from tkinter import messagebox, simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class StudioFormController:
    def __init__(self, view):
        self.view = view

        self.studio_info = {
            "Tên Studio": "Studio Panda",
            "Địa chỉ": "123 Đường Nguyễn Thị Định, TP.HCM",
            "Số điện thoại": "0123456789",
            "Email": "panda.studio.uit@gmail.com",
        }

    def create_info_section(self, parent_frame):
        info_frame = tk.Frame(parent_frame, bg="#f8f9fa", pady=10)
        info_frame.pack(fill=tk.X)

        studio_label = tk.Label(info_frame, text="Thông tin Studio", font=("Arial", 14, "bold"), bg="#f8f9fa")
        studio_label.pack(anchor=tk.W, padx=10, pady=5)

        for key, value in self.studio_info.items():
            label = tk.Label(info_frame, text=f"{key}: {value}", font=("Arial", 12), bg="#f8f9fa")
            label.pack(anchor=tk.W, padx=20)

    def create_graph_section(self, parent_frame):
        graph_frame = tk.Frame(parent_frame, bg="#f8f9fa")
        graph_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        data = [1, 2, 3, 4, 5]
        ax.plot(data, 'r-')
        ax.set_title('Biểu đồ mẫu')

        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)