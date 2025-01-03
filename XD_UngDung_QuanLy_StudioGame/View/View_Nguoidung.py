import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk, messagebox
from models.database import Database
import bcrypt


class NguoiDungForm:
    def __init__(self, master,controller):
        """Khởi tạo giao diện người dùng"""
        self.master = master  # Lưu trữ tham chiếu đến master
        self.controller = controller
        self.frame = tk.Frame(master, bg="#f8f9fa")
        self.frame.pack(fill=tk.BOTH, expand=True)


        try:
            master.iconphoto(False, PhotoImage(file="Images/Logo_studio.png"))  # Đặt icon
        except Exception as e:
            print(f"Lỗi khi tải logo: {e}")

        self.tao_tieude(self.frame)
        self.create_toolbar(self.frame)
        self.create_treeview(self.frame)

    def tao_tieude(self, parent_frame):
        """Tạo tiêu đề cho giao diện"""
        title = tk.Label(parent_frame, text="Quản lý Người Dùng", font=("San Francisco", 16, "bold"), bg="#f8f9fa", fg="#333")
        title.pack(pady=10)

    def create_toolbar(self, parent_frame):
        """Tạo thanh công cụ CRUD"""
        toolbar = tk.Frame(parent_frame, bg="#f8f9fa")
        toolbar.pack(fill=tk.X, pady=10)

        create_btn = tk.Button(toolbar, text="Thêm mới", command=self.create_record, bg="#007bff", fg="white")
        read_btn = tk.Button(toolbar, text="Xem", command=self.read_record, bg="#28a745", fg="white")
        update_btn = tk.Button(toolbar, text="Cập nhật", command=self.update_record, bg="#ffc107", fg="black")
        delete_btn = tk.Button(toolbar, text="Xóa", command=self.delete_record, bg="#dc3545", fg="white")

        create_btn.pack(side=tk.LEFT, padx=10)
        read_btn.pack(side=tk.LEFT, padx=10)
        update_btn.pack(side=tk.LEFT, padx=10)
        delete_btn.pack(side=tk.LEFT, padx=10)

    def create_treeview(self, parent_frame):
        """Tạo bảng hiển thị danh sách người dùng"""
        columns_nguoidung = ("ID", "Tên", "Email", "Điện thoại")
        self.tree_nguoidung = ttk.Treeview(parent_frame, columns=columns_nguoidung, show="headings")

        # Định dạng các cột
        for col in columns_nguoidung:
            self.tree_nguoidung.heading(col, text=col, anchor="center")
            self.tree_nguoidung.column(col, anchor="center", width=150)

        self.tree_nguoidung.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Thêm thanh cuộn ngang
        h_scroll = ttk.Scrollbar(parent_frame, orient="horizontal", command=self.tree_nguoidung.xview)
        self.tree_nguoidung.configure(xscrollcommand=h_scroll.set)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)

    def create_record(self):
        """Thêm một bản ghi mới vào cơ sở dữ liệu và cập nhật Treeview"""
        # Dữ liệu mới
        new_id = "1"  # Có thể tạo ID tự động nếu cần
        new_name = "Nguyễn Văn A"
        new_email = "nguyenvana@example.com"
        new_phone = "0123456789"

        # Kết nối đến cơ sở dữ liệu
        db = Database()

        try:
            # Thêm bản ghi mới vào cơ sở dữ liệu
            query = """
                INSERT INTO nguoi_dung (mand, ten_dang_nhap, email, mat_khau, vai_tro)
                VALUES (%s, %s, %s, %s, %s)
            """
            mat_khau_default = "123"  # Mật khẩu mặc định
            vai_tro_default = "nguoi dung"  # Vai trò mặc định

            # Mã hóa mật khẩu
            hashed_password = bcrypt.hashpw(mat_khau_default.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            db.execute_query(query, (new_id, new_name, new_email, hashed_password, vai_tro_default))
            self.tree_nguoidung.insert("", "end", values=(new_id, new_name, new_email, new_phone))

            # Hiển thị thông báo
            tk.messagebox.showinfo("Thành công", "Bản ghi mới đã được thêm vào cơ sở dữ liệu.")
        except Exception as e:
            tk.messagebox.showerror("Lỗi", f"Không thể thêm bản ghi: {e}")
        finally:
            del db

    def read_record(self):
        """Xem thông tin bản ghi được chọn"""
        selected_item = self.tree_nguoidung.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một người dùng để xem chi tiết")
            return
        item = self.tree_nguoidung.item(selected_item)
        values = item["values"]
        messagebox.showinfo("Thông tin người dùng", f"ID: {values[0]}\nTên: {values[1]}\nEmail: {values[2]}\nĐiện thoại: {values[3]}")

    def update_record(self):
        """Cập nhật thông tin bản ghi được chọn"""
        selected_item = self.tree_nguoidung.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một người dùng để cập nhật")
            return
        item = self.tree_nguoidung.item(selected_item)
        values = item["values"]
        new_values = (values[0], "Jane Doe", values[2], values[3])  # Giá trị mới
        self.tree_nguoidung.item(selected_item, values=new_values)

    def delete_record(self):
        """Xóa bản ghi được chọn"""
        selected_item = self.tree_nguoidung.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một người dùng để xóa")
            return
        self.tree_nguoidung.delete(selected_item)
