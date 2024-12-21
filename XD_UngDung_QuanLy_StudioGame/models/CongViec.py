from datetime import datetime

class CongViec:
    def __init__(self, ma_cong_viec: int, ten_congviec: str, mota_congviec: str, cv_giaocho: str, han_cuoi: str, trang_thai_congviec: str = "Chưa bắt đầu"):
        self.ma_congviec = ma_cong_viec
        self.ten_congviec = ten_congviec
        self.mota_congviec = mota_congviec
        self.cv_giaocho = cv_giaocho
        self.han_cuoi = self.parsed_han_cuoi(han_cuoi)
        self.trang_thai = trang_thai_congviec

    @staticmethod
    def parsed_han_cuoi(han_cuoi: str):
        try:
            return datetime.strptime(han_cuoi, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Sai han_cuoi format, hãy dùng 'YYYY-MM-DD'.")

    def update_trangthai_congviec(self, trang_thai_moi: str):
        cac_trang_thai = ["Chưa bắt đầu", "Đang tiến hành", "Hoàn thành", "Quá hạn"]
        if trang_thai_moi not in cac_trang_thai:
            raise ValueError(f"Trạng thái không hợp lệ. Các trạng thái hợp lệ: {', '.join(cac_trang_thai)}.")
        self.trang_thai = trang_thai_moi

    def __str__(self):
        return (f"Công việc: {self.ten_congviec} (ID: {self.ma_congviec}), "
                f"Trạng thái: {self.trang_thai}, Hạn cuối: {self.han_cuoi.strftime('%Y-%m-%d')}")
