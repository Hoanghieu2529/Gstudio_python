import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class CongViecFormController:
    """
       Lớp điều khiển quản lý công việc, bao gồm các chức năng: thêm, xem, cập nhật và xóa công việc.
       """
    def __init__(self, view):
        """
           Khởi tạo lớp điều khiển.
           - Đầu vào:
               + view: Đối tượng giao diện (view) liên kết với controller.
           - Đầu ra:
               + Khởi tạo biến `auto_generate_stt` để tự động tạo số thứ tự.
           """
        self.view = view
        self.auto_generate_stt = 1  # Tự động tạo số thứ tự

    def tao_ban_ghi(self):
        """
           Tạo mới một công việc.
           - Đầu vào: Không có.
           - Đầu ra:
               + Hiển thị form thêm mới công việc.
               + Lưu công việc mới vào `tree_congviec` với các thông tin:
                   * Mã công việc
                   * Tên công việc
                   * Mô tả công việc
                   * Giao cho
                   * Hạn cuối
                   * Trạng thái
               + Tăng số thứ tự tự động sau khi lưu.
           """
        form = tk.Toplevel(self.view.frame)
        form.title("Thêm mới công việc")

        labels = ["Mã công việc", "Tên công việc", "Mô tả công việc", "Giao cho", "Hạn cuối", "Trạng thái"]
        entries = []

        for i, label in enumerate(labels):
            tk.Label(form, text=label).grid(row=i, column=0, padx=10, pady=5)
            if "Hạn cuối" in label:
                entry = DateEntry(form, date_pattern='dd/mm/yyyy')
            elif "Trạng thái" in label:
                entry = ttk.Combobox(form, values=["Đang thực hiện", "Hoàn thành", "Hủy bỏ"])
                entry.current(0)
            else:
                entry = tk.Entry(form)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky=tk.W)
            entries.append(entry)

        def luu_ban_ghi():
            """Lưu bản ghi"""
            new_record = [self.auto_generate_stt] + [entry.get() for entry in entries]
            self.view.tree_congviec.insert("", "end", values=new_record)
            self.auto_generate_stt += 1  # Tăng số thứ tự tự động
            form.destroy()

        save_btn = tk.Button(form, text="Lưu", command=luu_ban_ghi)
        save_btn.grid(row=len(labels), columnspan=2, pady=10)

    def doc_ban_ghi(self):
        """
            Đọc chi tiết thông tin của công việc được chọn.
            - Đầu vào: Không có.
            - Đầu ra:
                + Hiển thị hộp thoại thông tin chi tiết của công việc, bao gồm:
                    * Mã công việc
                    * Tên công việc
                    * Mô tả công việc
                    * Giao cho
                    * Hạn cuối
                    * Trạng thái
                + Nếu không có công việc nào được chọn, hiển thị cảnh báo.
                """
        selected_item = self.view.tree_congviec.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một công việc để xem chi tiết")
            return
        item = self.view.tree_congviec.item(selected_item)
        values = item["values"]
        messagebox.showinfo("Thông tin công việc",
                            f"Mã công việc: {values[1]}\n"
                            f"Tên công việc: {values[2]}\n"
                            f"Mô tả công việc: {values[3]}\n"
                            f"Giao cho: {values[4]}\n"
                            f"Hạn cuối: {values[5]}\n"
                            f"Trạng thái: {values[6]}")

    def cap_nhat_ban_ghi(self):
        """
            Cập nhật trạng thái của công việc được chọn thành "Hoàn thành".

            - Đầu vào: Không có.
            - Đầu ra:
                + Thay đổi trạng thái của công việc được chọn trong `tree_congviec` thành "Hoàn thành".
                + Nếu không có công việc nào được chọn, hiển thị cảnh báo.
            """
        selected_item = self.view.tree_congviec.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một công việc để cập nhật")
            return
        item = self.view.tree_congviec.item(selected_item)
        values = item["values"]
        new_values = (values[0], values[1], values[2], values[3], values[4], values[5], "Hoàn thành")
        self.view.tree_congviec.item(selected_item, values=new_values)

    def xoa_ban_ghi(self):
        """
            Xóa công việc được chọn.

            - Đầu vào: Không có.
            - Đầu ra:
                + Xóa công việc khỏi `tree_congviec` sau khi người dùng xác nhận.
                + Nếu không có công việc nào được chọn, hiển thị cảnh báo.
            """
        selected_item = self.view.tree_congviec.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một công việc để xóa")
            return
        messagebox.showwarning("Cảnh báo", "Bạn có chắc chắn muốn xóa?")
        self.view.tree_congviec.delete(selected_item)
