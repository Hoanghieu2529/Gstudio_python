# import tkinter as tk
# from tkinter import ttk
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#
#
# class BaoCaoNhanSuForm(tk.Frame):
#     def __init__(self, master, controller):
#         super().__init__(master, bg="#f8f9fa")
#         self.controller = controller
#         self.pack(fill=tk.BOTH, expand=True)
#
#         # Tiêu đề
#         tk.Label(self, text="Báo Cáo Nhân Sự", font=("San Francisco", 16, "bold"), bg="#f8f9fa", fg="#333").pack(pady=10)
#
#         # Khung chứa biểu đồ treemap
#         self.frame_chart1 = tk.Frame(self, bg="#f8f9fa")
#         self.frame_chart1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
#
#         # Khung chứa biểu đồ cột
#         self.frame_chart2 = tk.Frame(self, bg="#f8f9fa")
#         self.frame_chart2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
#
#         # Nút tải lại
#         tk.Button(self, text="Tải báo cáo", command=self.controller.tai_lai_bao_cao).pack(pady=10)
#
#     def hien_thi_bieu_do_treemap(self, data):
#         """Hiển thị biểu đồ TreeMap."""
#         fig = Figure(figsize=(5, 4))
#         ax = fig.add_subplot(111)
#
#         labels = [f"{item['phong_ban']} ({item['so_luong']})" for item in data]
#         sizes = [item['so_luong'] for item in data]
#
#         ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
#         ax.set_title("Số lượng nhân viên theo phòng ban")
#
#         canvas = FigureCanvasTkAgg(fig, self.frame_chart1)
#         canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
#
#     def hien_thi_bieu_do_cot(self, data):
#         """Hiển thị biểu đồ cột cho thống kê lương."""
#         fig = Figure(figsize=(5, 4))
#         ax = fig.add_subplot(111)
#
#         categories = ['Cao nhất', 'Thấp nhất', 'Trung bình']
#         values = [data['max'], data['min'], data['avg']]
#
#         ax.bar(categories, values, color=['green', 'red', 'blue'])
#         ax.set_title("Thống kê lương cơ bản")
#         ax.set_ylabel("Lương (VNĐ)")
#
#         canvas = FigureCanvasTkAgg(fig, self.frame_chart2)
#         canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
import tkinter as tk
import squarify  # Đảm bảo bạn đã cài thư viện này
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.ticker import FuncFormatter

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
        fig = Figure(figsize=(6, 5))
        ax = fig.add_subplot(111)

        sizes = [item['so_luong'] for item in data]
        labels = [f"{item['phong_ban']} ({item['so_luong']})" for item in data]

        # Tạo treemap
        squarify.plot(sizes=sizes, label=labels, alpha=0.8, ax=ax)
        ax.set_title("Số lượng nhân viên theo phòng ban")
        ax.axis('off')  # Ẩn trục

        canvas = FigureCanvasTkAgg(fig, self.frame_chart1)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def hien_thi_bieu_do_luong(self, data):
        """Hiển thị biểu đồ cột cho thống kê lương (đơn vị: triệu đồng) với giá trị trên đầu cột."""
        fig = Figure(figsize=(5, 4))
        ax = fig.add_subplot(111)

        # Chuyển đổi đơn vị từ đồng sang triệu đồng
        categories = ['Cao nhất', 'Thấp nhất', 'Trung bình']
        values = [data['max'] / 1_000_000, data['min'] / 1_000_000, data['avg'] / 1_000_000]

        # Tạo biểu đồ cột
        bars = ax.bar(categories, values, color=['green', 'red', 'blue'])
        ax.set_title("Thống kê lương cơ bản (Triệu đồng)")
        ax.set_ylabel("Lương (Triệu đồng)")

        # Định dạng trục y để hiển thị giá trị có dấu phẩy ngăn cách
        from matplotlib.ticker import FuncFormatter
        formatter = FuncFormatter(lambda x, _: f'{int(x):,}')
        ax.yaxis.set_major_formatter(formatter)

        # Hiển thị giá trị trên đầu mỗi cột
        for bar, value in zip(bars, values):
            ax.text(
                bar.get_x() + bar.get_width() / 2,  # Vị trí ngang
                bar.get_height(),  # Vị trí dọc (cao hơn đỉnh cột)
                f'{value:.2f}',  # Giá trị hiển thị với 2 chữ số thập phân
                ha='center',  # Căn giữa
                va='bottom',  # Căn phía dưới
                fontsize=10,  # Kích thước chữ
                color='black'  # Màu chữ
            )

        # Tạo canvas Matplotlib cho giao diện Tkinter
        canvas = FigureCanvasTkAgg(fig, self.frame_chart2)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


