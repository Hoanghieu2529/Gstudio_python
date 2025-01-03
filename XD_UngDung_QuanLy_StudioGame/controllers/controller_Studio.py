import tkinter as tk
from tkinter import messagebox, simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class StudioFormController:
    """
    Lớp điều khiển quản lý giao diện thông tin và biểu đồ của Studio.
    Bao gồm:
    - Hiển thị thông tin cơ bản về Studio.
    - Hiển thị biểu đồ mẫu trên giao diện.
    """
    def __init__(self, view):
        """
        Khởi tạo lớp điều khiển Studio.

        - Đầu vào:
            + view: Đối tượng giao diện (View) liên kết với controller.
        - Đầu ra:
            + Khởi tạo thông tin cơ bản của Studio trong thuộc tính `studio_info`.
        """
        self.view = view

        self.studio_info = {
            "Tên Studio": "Studio Panda",
            "Địa chỉ": "123 Đường Nguyễn Thị Định, TP.HCM",
            "Số điện thoại": "0123456789",
            "Email": "panda.studio.uit@gmail.com",
        }

    def tao_thong_tin_cb(self, parent_frame):
        """
        Tạo và hiển thị phần thông tin cơ bản của Studio.

        - Đầu vào:
            + parent_frame: Frame cha nơi phần thông tin sẽ được hiển thị.
        - Đầu ra:
            + Thêm các thông tin về Studio (Tên, Địa chỉ, Số điện thoại, Email) vào giao diện.
            + Thông tin được trình bày trong một khung với định dạng rõ ràng.
        """
        info_frame = tk.Frame(parent_frame, bg="#f8f9fa", pady=10)
        info_frame.pack(fill=tk.X)

        studio_label = tk.Label(info_frame, text="Thông tin Studio", font=("Arial", 14, "bold"), bg="#f8f9fa")
        studio_label.pack(anchor=tk.W, padx=10, pady=5)

        for key, value in self.studio_info.items():
            label = tk.Label(info_frame, text=f"{key}: {value}", font=("Arial", 12), bg="#f8f9fa")
            label.pack(anchor=tk.W, padx=20)

    def tao_bieu_do_mau(self, parent_frame):
        """
       Tạo và hiển thị một biểu đồ mẫu trên giao diện.

       - Đầu vào:
           + parent_frame: Frame cha nơi biểu đồ sẽ được hiển thị.
       - Đầu ra:
           + Thêm một biểu đồ tuyến (line plot) mẫu vào giao diện.
           + Biểu đồ được hiển thị bằng thư viện matplotlib.
       - Chi tiết:
           1. Tạo một `Figure` mới bằng matplotlib.
           2. Thêm biểu đồ tuyến với dữ liệu mẫu `[1, 2, 3, 4, 5]`.
           3. Gắn biểu đồ vào giao diện thông qua `FigureCanvasTkAgg`.
       """
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