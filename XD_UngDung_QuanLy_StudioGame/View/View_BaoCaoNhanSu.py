import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class BaoCaoNhanSuForm(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#f8f9fa")
        self.controller = controller
        self.pack(fill=tk.BOTH, expand=True)

        # Tiêu đề
        tk.Label(self, text="Báo Cáo Nhân Sự", font=("San Francisco", 16, "bold"), bg="#f8f9fa", fg="#333").pack(pady=10)

        # Khung chứa biểu đồ treemap
        self.frame_chart1 = tk.Frame(self, bg="#f8f9fa")
        self.frame_chart1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Khung chứa biểu đồ cột
        self.frame_chart2 = tk.Frame(self, bg="#f8f9fa")
        self.frame_chart2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Nút tải lại
        tk.Button(self, text="Tải báo cáo", command=self.controller.tai_lai_bao_cao).pack(pady=10)

    def hien_thi_bieu_do_treemap(self, data):
        """Hiển thị biểu đồ TreeMap."""
        fig = Figure(figsize=(5, 4))
        ax = fig.add_subplot(111)

        labels = [f"{item['phong_ban']} ({item['so_luong']})" for item in data]
        sizes = [item['so_luong'] for item in data]

        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.set_title("Số lượng nhân viên theo phòng ban")

        canvas = FigureCanvasTkAgg(fig, self.frame_chart1)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def hien_thi_bieu_do_cot(self, data):
        """Hiển thị biểu đồ cột cho thống kê lương."""
        fig = Figure(figsize=(5, 4))
        ax = fig.add_subplot(111)

        categories = ['Cao nhất', 'Thấp nhất', 'Trung bình']
        values = [data['max'], data['min'], data['avg']]

        ax.bar(categories, values, color=['green', 'red', 'blue'])
        ax.set_title("Thống kê lương cơ bản")
        ax.set_ylabel("Lương (VNĐ)")

        canvas = FigureCanvasTkAgg(fig, self.frame_chart2)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
