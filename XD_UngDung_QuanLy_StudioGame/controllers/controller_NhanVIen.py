import tkinter as tk
from tkinter import ttk, messagebox

class NhanVienFormController:
    """
    Lớp điều khiển xử lý các sự kiện và logic liên quan đến form quản lý nhân viên.
    """
    def __init__(self, view):
        self.view = view
        self.auto_generate_stt = 1

    def tao_ban_ghi(self):
        """
       Tạo mới một bản ghi nhân viên.
       - Đầu ra: Hiển thị form thêm mới nhân viên. Sau khi nhập thông tin và nhấn "Lưu",
         bản ghi nhân viên mới sẽ được thêm vào bảng danh sách.
       """
        form = tk.Toplevel(self.view.frame)
        form.title("Thêm mới nhân viên")

        labels = ["Mã nhân viên", "Tên nhân viên", "Vai trò", "Phòng ban", "Email"]
        entries = []

        for i, label in enumerate(labels):
            tk.Label(form, text=label).grid(row=i, column=0, padx=10, pady=5)

            if "Vai trò" in label:
                entry = ttk.Combobox(form, values=["Lập trình viên", "Nhà thiết kế", "Quản trị"])
            elif "Phòng ban" in label:
                entry = ttk.Combobox(form,
                                     values=["Phòng lập trình", "Phòng thiết kế", "Phòng Giám Đốc", "Phòng nhân sự"])
                entry.current(0)
            else:
                entry = tk.Entry(form)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky=tk.W)
            entries.append(entry)

        def luu_ban_ghi():
            """Hàm Lưu bản ghi """
            new_record = [self.auto_generate_stt] + [entry.get() for entry in entries]
            self.view.tree_nhanvien.insert("", "end", values=new_record)
            self.auto_generate_stt += 1  # Tăng số thứ tự tự động
            form.destroy()

        save_btn = tk.Button(form, text="Lưu", command=luu_ban_ghi)
        save_btn.grid(row=len(labels), columnspan=2, pady=10)

    def doc_ban_ghi(self):
        """Hàm đọc các bản ghi được chọn
        - Đầu ra: Hiển thị một hộp thoại với các thông tin chi tiết về nhân viên được chọn.
        - Lưu ý: Nếu không có bản ghi nào được chọn, hiển thị cảnh báo cho người dùng.
        """
        selected_item = self.view.tree_nhanvien.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một nhân viên để xem chi tiết")
            return
        item = self.view.tree_nhanvien.item(selected_item)
        values = item["values"]
        messagebox.showinfo("Thông tin nhân viên",
                            f"Mã nhân viên: {values[1]}\n"
                            f"Tên nhân viên: {values[2]}\n"
                            f"Vai trò: {values[3]}\n"
                            f"Phòng ban: {values[4]}\n"
                            f"Email: {values[5]}")

    def cap_nhat_ban_ghi(self):
        """Hàm cập nhật lại bản ghi khi lựa chọn tính năng cập nhật
        - Đầu ra: Hiển thị form cập nhật thông tin nhân viên. Sau khi thay đổi và nhấn "Lưu thay đổi",
          thông tin bản ghi sẽ được cập nhật trong bảng danh sách.
        - Lưu ý: Nếu không có bản ghi nào được chọn, hiển thị cảnh báo cho người dùng.
        """
        selected_item = self.view.tree_nhanvien.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một nhân viên để cập nhật")
            return
        item = self.view.tree_nhanvien.item(selected_item)
        values = item["values"]

        # Tạo form cập nhật
        form = tk.Toplevel(self.view.frame)
        form.title("Cập nhật thông tin nhân viên")

        labels = ["Mã nhân viên", "Tên nhân viên", "Vai trò", "Phòng ban", "Email"]
        entries = []

        for i, label in enumerate(labels):
            tk.Label(form, text=label).grid(row=i, column=0, padx=10, pady=5)

            if "Vai trò" in label:
                entry = ttk.Combobox(form, values=["Lập trình viên", "Nhà thiết kế", "Quản trị"])
                entry.set(values[3])
            elif "Phòng ban" in label:
                entry = ttk.Combobox(form,
                                     values=["Phòng lập trình", "Phòng thiết kế", "Phòng Giám Đốc", "Phòng nhân sự"])
                entry.set(values[4])
            else:
                entry = tk.Entry(form)
                entry.insert(0, values[i + 1])
            entry.grid(row=i, column=1, padx=10, pady=5, sticky=tk.W)
            entries.append(entry)

        def luu_thay_doi():
            """
            Hàm lưu các giá trị sau khi thay đổi thông tin nhân viên trong form cập nhật.

                - Đầu vào:
                    + Không có tham số đầu vào trực tiếp.
                    + Sử dụng các giá trị hiện tại được lấy từ `entries` (các trường nhập liệu trong form)
                      và `values` (giá trị ban đầu của bản ghi được chọn).
                    + `selected_item`: Bản ghi đang được chọn trong `tree_nhanvien`.

                - Đầu ra:
                    + Cập nhật lại bản ghi nhân viên trong `tree_nhanvien` với các giá trị mới nhập.
                    + Đóng form cập nhật sau khi lưu thành công.

                - Chi tiết hoạt động:
                    1. Thu thập các giá trị mới từ các trường nhập liệu trong form cập nhật.
                    2. Kết hợp số thứ tự (STT) cũ với các giá trị mới để tạo danh sách `new_values`.
                    3. Cập nhật bản ghi được chọn trong `tree_nhanvien` bằng các giá trị mới.
                    4. Đóng form cập nhật.
            """
            new_values = [values[0]] + [entry.get() for entry in entries]
            self.view.tree_nhanvien.item(selected_item, values=new_values)
            form.destroy()

        save_btn = tk.Button(form, text="Lưu thay đổi", command=luu_thay_doi)
        save_btn.grid(row=len(labels), columnspan=2, pady=10)

    def xoa_ban_ghi(self):
        """Hàm xử lý Xóa bản ghi nhân viên sau khi chọn xóa
            - Đầu ra: Xóa bản ghi khỏi bảng danh sách sau khi người dùng xác nhận
            - Lưu ý: Nếu không có bản ghi nào được chọn, hiển thị cảnh báo cho người dùng"""
        selected_item = self.view.tree_nhanvien.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một nhân viên để xóa")
            return
        confirm = messagebox.askyesno("Xác nhận", "Bạn thật sự muốn xóa nhân viên này không?")
        if confirm:
            self.view.tree_nhanvien.delete(selected_item)
