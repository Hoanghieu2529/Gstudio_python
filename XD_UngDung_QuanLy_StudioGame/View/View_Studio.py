import tkinter as tk
from tkinter import messagebox, simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from controllers import StudioFormController
from View.View_BaseForm import KhungCoSo


class StudioForm(KhungCoSo):
    """
   Lớp giao diện quản lý studio, kế thừa từ KhungCoSo.

   - Chức năng:
       + Hiển thị thông tin cơ bản của studio.
       + Hiển thị biểu đồ mẫu.
       + Tạo tiêu đề cho giao diện.
   """
    def __init__(self, master, **kwargs):
        """
        Khởi tạo giao diện StudioForm.

        - Đầu vào:
            + master (tk.Tk): Cửa sổ hoặc frame cha.
            + kwargs: Các tham số bổ sung.
        - Đầu ra:
            + Tạo khung giao diện chính.
            + Kết nối với controller để tạo nội dung và biểu đồ.
        """
        super().__init__(master, **kwargs)
        self.frame = tk.Frame(master, bg="#f8f9fa")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.controllers = StudioFormController(self)
        self.controllers.tao_thong_tin_cb(self.frame)
        self.controllers.tao_bieu_do_mau(self.frame)
        # Thêm tiêu đề
        self.tao_tieu_de("Quản lý studio")

    def tao_tieu_de(self, tieu_de_text):
        """
        Tạo tiêu đề ở phía trên giao diện.

        - Đầu vào:
            + tieu_de_text (str): Chuỗi tiêu đề cần hiển thị.
        - Đầu ra:
            + Hiển thị tiêu đề ở phía trên giao diện với định dạng font và màu sắc.
        """
        tieu_de = tk.Label(self, text=tieu_de_text, font=("San Francisco", 16, "bold"), bg="#f8f9fa", fg="#333")
        tieu_de.pack(pady=10)





if __name__ == "__main__":
    """
    Khởi chạy giao diện StudioForm để kiểm tra độc lập.

    - Tạo cửa sổ chính (root).
    - Tạo một instance của StudioForm và hiển thị trên cửa sổ chính.
    """
    root = tk.Tk()
    root.title("Quản lý Studio")
    root.geometry("800x600")
    app = StudioForm(root)
    root.mainloop()
