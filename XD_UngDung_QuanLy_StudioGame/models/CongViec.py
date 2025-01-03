from datetime import datetime

class CongViec:
    """
    Lớp đại diện cho thông tin một công việc.

    Bao gồm các thuộc tính:
    - Mã công việc (ma_congviec)
    - Tên công việc (ten_congviec)
    - Mô tả công việc (mota_congviec)
    - Người được giao công việc (cv_giaocho)
    - Hạn cuối (han_cuoi)
    - Trạng thái công việc (trang_thai)
    """
    def __init__(self, ma_cong_viec: int, ten_congviec: str, mota_congviec: str, cv_giaocho: str, han_cuoi: str, trang_thai_congviec: str = "Chưa bắt đầu"):
        """
        Khởi tạo một công việc mới.

        - Đầu vào:
            + ma_cong_viec (int): Mã định danh duy nhất của công việc.
            + ten_congviec (str): Tên của công việc.
            + mota_congviec (str): Mô tả chi tiết công việc.
            + cv_giaocho (str): Người được giao công việc.
            + han_cuoi (str): Ngày hạn cuối của công việc, định dạng 'YYYY-MM-DD'.
            + trang_thai_congviec (str, tùy chọn): Trạng thái hiện tại của công việc (mặc định là "Chưa bắt đầu").
        - Đầu ra:
            + Tạo một đối tượng `CongViec` với các thuộc tính đã khởi tạo.
        - Lưu ý:
            + Nếu `han_cuoi` không đúng định dạng 'YYYY-MM-DD', sẽ ném lỗi `ValueError`.
        """
        self.ma_congviec = ma_cong_viec
        self.ten_congviec = ten_congviec
        self.mota_congviec = mota_congviec
        self.cv_giaocho = cv_giaocho
        self.han_cuoi = self.parsed_han_cuoi(han_cuoi)
        self.trang_thai = trang_thai_congviec

    @staticmethod
    def parsed_han_cuoi(han_cuoi: str):
        """
        Chuyển đổi chuỗi ngày hạn cuối sang đối tượng datetime.

        - Đầu vào:
            + han_cuoi (str): Chuỗi ngày hạn cuối, định dạng 'YYYY-MM-DD'.
        - Đầu ra:
            + Đối tượng `datetime` tương ứng với chuỗi ngày.
        - Lưu ý:
            + Nếu `han_cuoi` không đúng định dạng, sẽ ném lỗi `ValueError`.
        """
        try:
            return datetime.strptime(han_cuoi, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Sai han_cuoi format, hãy dùng 'YYYY-MM-DD'.")

    def update_trangthai_congviec(self, trang_thai_moi: str):
        """
        Cập nhật trạng thái của công việc.

        - Đầu vào:
            + trang_thai_moi (str): Trạng thái mới cần cập nhật.
              Các trạng thái hợp lệ bao gồm:
              * "Chưa bắt đầu"
              * "Đang tiến hành"
              * "Hoàn thành"
              * "Quá hạn"
        - Đầu ra:
            + Cập nhật giá trị `trang_thai` của công việc.
        - Lưu ý:
            + Nếu `trang_thai_moi` không hợp lệ, sẽ ném lỗi `ValueError`.
        """
        cac_trang_thai = ["Chưa bắt đầu", "Đang tiến hành", "Hoàn thành", "Quá hạn"]
        if trang_thai_moi not in cac_trang_thai:
            raise ValueError(f"Trạng thái không hợp lệ. Các trạng thái hợp lệ: {', '.join(cac_trang_thai)}.")
        self.trang_thai = trang_thai_moi

    def __str__(self):
        """
            Chuỗi biểu diễn của đối tượng công việc.
            - Đầu ra:
                + Trả về chuỗi chứa thông tin công việc bao gồm:
                  * Tên công việc
                  * Mã công việc
                  * Trạng thái
                  * Hạn cuối
            """
        return (f"Công việc: {self.ten_congviec} (ID: {self.ma_congviec}), "
                f"Trạng thái: {self.trang_thai}, Hạn cuối: {self.han_cuoi.strftime('%Y-%m-%d')}")
