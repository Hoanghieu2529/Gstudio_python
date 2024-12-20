from datetime import datetime

class CongViec:
    def __init__(self, ma_cong_viec: int, ten_congviec: str, mota_congviec: str,
                 cv_giaocho: str, han_cuoi: str, cv_trang_thai: str = "Chưa bắt đầu"):
        self.ma_congviec = ma_cong_viec
        self.ten_congviec = ten_congviec
        self.mota_congviec = mota_congviec
        self.cv_giaocho = cv_giaocho
        self.han_cuoi = self.parsed_han_cuoi(han_cuoi)
        self.trang_thai = cv_trang_thai

    @staticmethod
    def parsed_han_cuoi(han_cuoi: str):
        """Chuyển từ string sang format datetime."""
        try:
            return datetime.strptime(han_cuoi, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Sai han_cuoi format, hãy dùng 'YYYY-MM-DD'.")

    def update_cv_trang_thai(self, trang_thai_moi: str):
        """Cập nhật trạng thái công việc."""
        cac_trang_thai = ["Chưa bắt đầu", "Đang tiến hành", "Hoàn thành", "Quá hạn"]
        if trang_thai_moi not in cac_trang_thai:
            raise ValueError(f"Sai trạng thái. Những trạng thái có sẵn là: {', '.join(cac_trang_thai)}.")
        self.trang_thai = trang_thai_moi
        print(f"Trạng thái công việc {self.ma_congviec} đã được cập nhật thành '{trang_thai_moi}'.")

    def __str__(self):
        """String thể hiện công việc."""
        han_cuoi_str = self.han_cuoi.strftime("%Y-%m-%d") if isinstance(self.han_cuoi, datetime) else self.han_cuoi
        return (f"Công Việc ID: {self.ma_congviec}\n"
                f"Tên: {self.ten_congviec}\n"
                f"Mô tả: {self.mota_congviec}\n"
                f"Giao cho: {self.cv_giaocho}\n"
                f"han_cuoi: {han_cuoi_str}\n"
                f"Trạng thái: {self.trang_thai}\n")
