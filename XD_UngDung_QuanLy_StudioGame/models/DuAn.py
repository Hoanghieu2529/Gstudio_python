class DuAn:
    def __init__(self, ma_duan: int, ten_duan: str, mota_duan: str, ng_batdau_duan: str, ng_ketthuc_duan: str, trang_thai_duan: str):
        self.ma_duan = ma_duan
        self.ten_duan = ten_duan
        self.mota_duan = mota_duan
        self.ng_batdau_duan = ng_batdau_duan
        self.ng_ketthuc_duan = ng_ketthuc_duan
        self.trang_thai_duan = trang_thai_duan
        self.congviec = []  # Danh sách các công việc thuộc dự án

    def them_congviec(self, congviec):
        """Thêm công việc vào dự án."""
        self.congviec.append(congviec)

    def tinh_tien_do(self):
        """Tính tiến độ dự án dựa trên trạng thái các công việc."""
        if not self.congviec:
            return 0  # Nếu không có công việc, tiến độ là 0%
        cong_viec_hoan_thanh = sum(1 for cv in self.congviec if cv.trang_thai == "Hoàn thành")
        return round((cong_viec_hoan_thanh / len(self.congviec)) * 100, 2)

    def lietke_congviec(self):
        """Liệt kê tên các công việc thuộc dự án."""
        return [cv.ten_congviec for cv in self.congviec]

    def __str__(self):
        """Hiển thị thông tin dự án."""
        return (f"Dự án: {self.ten_duan} (ID: {self.ma_duan})\n"
                f"Mô tả: {self.mota_duan}\n"
                f"Ngày bắt đầu: {self.ng_batdau_duan}\n"
                f"Ngày kết thúc: {self.ng_ketthuc_duan}\n"
                f"Trạng thái: {self.trang_thai_duan}\n"
                f"Tiến độ: {self.tinh_tien_do()}%\n"
                f"Công việc: {', '.join(self.lietke_congviec())}")
