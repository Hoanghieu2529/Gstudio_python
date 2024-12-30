from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from fpdf import FPDF
import pandas as pd
from models.models_tinh_luong import ModelTinhLuong

class ControllerTinhLuong:
    def __init__(self, view):
        self.view = view
        self.model = ModelTinhLuong()
        self.du_lieu = self.model.lay_danh_sach_luong()  # Lấy dữ liệu từ model
        if self.view:
            self.view.hien_thi_du_lieu(self.du_lieu)

    def hien_thi_du_lieu(self):
        """Lấy dữ liệu từ model và hiển thị trên view."""
        if self.view:
            self.du_lieu = self.model.lay_danh_sach_luong()
            self.view.hien_thi_du_lieu(self.du_lieu)

    def xuat_excel(self):
        """Xuất dữ liệu ra file Excel."""
        duong_dan = asksaveasfilename(defaultextension=".xlsx",
                                       filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if not duong_dan:
            return

        df = pd.DataFrame(self.du_lieu)
        df.to_excel(duong_dan, index=False)
        messagebox.showinfo("Thành công", "Dữ liệu đã được xuất ra file Excel.")

    def xuat_pdf(self):
        """Xuất dữ liệu ra file PDF."""
        duong_dan = asksaveasfilename(defaultextension=".pdf",
                                       filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")])
        if not duong_dan:
            return

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Bảng Lương Nhân Viên", ln=True, align="C")

        col_widths = [30, 50, 50, 30, 30]
        headers = ["Mã NV", "Họ Tên", "Phòng Ban", "Lương Cơ Bản", "Ngày Công"]

        for i, header in enumerate(headers):
            pdf.cell(col_widths[i], 10, header, border=1, align="C")
        pdf.ln()

        for nv in self.du_lieu:
            pdf.cell(col_widths[0], 10, nv["manv"], border=1)
            pdf.cell(col_widths[1], 10, nv["ho_ten"], border=1)
            pdf.cell(col_widths[2], 10, nv["ten_phong_ban"], border=1)
            pdf.cell(col_widths[3], 10, str(nv["luong_co_ban"]), border=1)
            pdf.cell(col_widths[4], 10, str(nv["ngay_cong"]), border=1)
            pdf.ln()

        pdf.output(duong_dan)
        messagebox.showinfo("Thành công", "Dữ liệu đã được xuất ra file PDF.")

    def cap_nhat_ngay_cong(self, manv, ngay_cong_moi):
        """Cập nhật số ngày công."""
        self.model.cap_nhat_ngay_cong(manv, ngay_cong_moi)
        messagebox.showinfo("Thành công", "Ngày công đã được cập nhật.")
