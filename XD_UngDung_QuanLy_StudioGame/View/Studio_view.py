from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class QuanLyDuAn(QMainWindow):
    def __init__(self):
        """Tạo Giao Diện Quản lÝ dự án"""
        super().__init__()
        self.setWindowTitle("Quản lý dự án")
        self.setGeometry(100, 100, 1920, 1080)

        # Thiết kế bố cục
        layout = QVBoxLayout()

        # Nút thêm dự án
        self.nut_them_du_an = QPushButton("Thêm dự án")
        layout.addWidget(self.nut_them_du_an, alignment=Qt.AlignCenter)

        # Các nút khác (nếu cần)
        self.nut_xem_bao_cao = QPushButton("Xem báo cáo")
        layout.addWidget(self.nut_xem_bao_cao, alignment=Qt.AlignCenter)

        self.nut_quan_ly_nhan_su = QPushButton("Quản lý nhân sự")
        layout.addWidget(self.nut_quan_ly_nhan_su, alignment=Qt.AlignCenter)

        # Cấu hình giao diện chính
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

# Khởi chạy ứng dụng
if __name__ == "__main__":
    ung_dung = QApplication([])
    cua_so = QuanLyDuAn()
    cua_so.show()
    ung_dung.exec()
