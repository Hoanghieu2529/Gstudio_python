import os
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from fpdf import FPDF
from fpdf.enums import XPos, YPos
import pandas as pd
from models.models_tinh_luong import ModelTinhLuong

class ControllerTinhLuong:
    """
    Lớp điều khiển quản lý tính lương nhân viên, chịu trách nhiệm:
    - Hiển thị dữ liệu lương từ model lên view.
    - Xuất dữ liệu lương ra file Excel và PDF.
    - Cập nhật thông tin ngày công của nhân viên.
    """
    def __init__(self, view):
        """
        Khởi tạo lớp điều khiển tính lương.

        - Đầu vào:
            + view: Đối tượng giao diện (View) để hiển thị dữ liệu lương.
        - Đầu ra:
            + Kết nối với model `ModelTinhLuong` để lấy dữ liệu lương.
            + Hiển thị dữ liệu lương lên view nếu có view được truyền vào.
        """
        self.view = view
        self.model = ModelTinhLuong()
        self.du_lieu = self.model.lay_danh_sach_luong()  # Lấy dữ liệu từ model
        if self.view:
            self.view.hien_thi_du_lieu(self.du_lieu)

    def hien_thi_du_lieu(self):
        """
        Lấy dữ liệu từ model và hiển thị trên view.
        - Đầu ra:
            + Cập nhật dữ liệu lương từ model.
            + Hiển thị dữ liệu lên giao diện view.
        """
        if self.view:
            self.du_lieu = self.model.lay_danh_sach_luong()
            self.view.hien_thi_du_lieu(self.du_lieu)

    def xuat_excel(self):
        """
        Xuất dữ liệu lương nhân viên ra file Excel.
        - Đầu ra:
            + Xuất file Excel chứa dữ liệu lương với các thông tin:
                * Mã NV, Họ Tên, Chức Vụ, Lương Cơ Bản, Ngày Công, Tổng Lương.
            + Hiển thị thông báo khi xuất thành công hoặc lỗi khi xuất thất bại.
        """
        duong_dan = asksaveasfilename(defaultextension=".xlsx",
                                      filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if not duong_dan:
            return

        # Chuẩn bị dữ liệu cho Excel
        data_for_excel = [
            {
                "Mã NV": nv["manv"],
                "Họ Tên": nv["ho_ten"],
                "Chức Vụ": nv["chuc_vu"],
                "Lương Cơ Bản": f'{nv["luong_cb"]:,} VNĐ',
                "Ngày Công": nv["ngay_cong"],
                "Tổng Lương": f'{int(nv["luong_cb"] * nv["ngay_cong"] / 22):,} VNĐ'
            }
            for nv in self.du_lieu
        ]

        # Tạo DataFrame từ dữ liệu
        df = pd.DataFrame(data_for_excel)

        # Xuất dữ liệu ra file Excel
        try:
            df.to_excel(duong_dan, index=False, engine='openpyxl')
            messagebox.showinfo("Thành công", "Dữ liệu đã được xuất ra file Excel.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể xuất file Excel: {e}")

    def xuat_pdf(self):
        """
        Xuất dữ liệu lương nhân viên ra file PDF.
        - Đầu ra:
            + Xuất file PDF chứa dữ liệu lương với các thông tin:
                * Mã NV, Họ Tên, Chức Vụ, Lương Cơ Bản, Ngày Công, Tổng Lương.
            + Hiển thị thông báo khi xuất thành công hoặc lỗi khi xuất thất bại.
        """
        try:
            # Đường dẫn lưu file PDF
            duong_dan = asksaveasfilename(defaultextension=".pdf",
                                          filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")])
            if not duong_dan:
                return

            pdf = FPDF()
            pdf.add_page()

            # Thêm font DejaVu
            font_path = os.path.join("fonts", "DejaVuSans.ttf")
            pdf.add_font("DejaVu", "", font_path, uni=True)
            pdf.set_font("DejaVu", size=12)

            # Tiêu đề
            pdf.cell(200, 10, txt="Bảng Lương Nhân Viên", ln=True, align="C")

            # Tạo bảng
            pdf.set_font("DejaVu", size=10)
            col_widths = [30, 50, 50, 30, 30, 30]  # Định nghĩa độ rộng của các cột
            headers = ["Mã NV", "Họ Tên", "Chức Vụ", "Lương Cơ Bản", "Ngày Công", "Tổng Lương"]

            # In tiêu đề cột
            for header, width in zip(headers, col_widths):
                pdf.cell(width, 10, header, border=1, align="C")
            pdf.ln()  # Xuống dòng

            # In dữ liệu
            for nv in self.du_lieu:
                tong_luong = nv["luong_cb"] * nv["ngay_cong"] / 22
                row = [
                    str(nv["manv"]),  # Chuyển số thành chuỗi
                    str(nv["ho_ten"]),
                    str(nv["chuc_vu"]),
                    f"{nv['luong_cb']:,} VNĐ",  # Định dạng tiền tệ
                    str(nv["ngay_cong"]),  # Chuyển số thành chuỗi
                    f"{tong_luong:,.0f} VNĐ"  # Định dạng tiền tệ
                ]
                for cell, width in zip(row, col_widths):
                    pdf.cell(width, 10, str(cell), border=1, align="C")  # Đảm bảo tất cả dữ liệu đều là chuỗi
                pdf.ln()  # Xuống dòng

            # Xuất file PDF
            pdf.output(duong_dan)
            messagebox.showinfo("Thành công", "Dữ liệu đã được xuất ra file PDF.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể xuất file PDF: {e}")

    def cap_nhat_ngay_cong(self, manv, ngay_cong_moi):
        """Cập nhật số ngày công của một nhân viên.

        - Đầu vào:
            + manv: Mã nhân viên cần cập nhật.
            + ngay_cong_moi: Số ngày công mới.
        - Đầu ra:
            + Cập nhật thông tin ngày công vào cơ sở dữ liệu qua model.
            + Hiển thị thông báo khi cập nhật thành công.
        """
        self.model.cap_nhat_ngay_cong(manv, ngay_cong_moi)
        messagebox.showinfo("Thành công", "Ngày công đã được cập nhật.")
