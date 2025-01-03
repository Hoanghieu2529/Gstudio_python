from models.models_nguoi_dung import model_nguoi_dung
from models.database import Database

class controller_dang_nhap:
    """
        Lớp điều khiển xử lý đăng nhập người dùng, bao gồm các chức năng:
        - Kiểm tra thông tin đăng nhập.
        - Xác định vai trò của người dùng dựa trên thông tin đăng nhập.
        """
    def __init__(self):
        """
            Khởi tạo lớp điều khiển đăng nhập.

            - Đầu vào: Không có.
            - Đầu ra:
                + Khởi tạo kết nối cơ sở dữ liệu thông qua đối tượng `Database`.
            """
        self.db = Database()

    def xu_ly_dang_nhap(self, ten_dang_nhap, mat_khau):
        """
           Xử lý logic kiểm tra thông tin đăng nhập.

           - Đầu vào:
               + ten_dang_nhap: Tên đăng nhập của người dùng.
               + mat_khau: Mật khẩu của người dùng.
           - Đầu ra:
               + Trả về `True` nếu thông tin đăng nhập hợp lệ.
               + Trả về `False` nếu thông tin đăng nhập không hợp lệ.
           - Quy trình:
               1. Gọi phương thức `kiem_tra_dang_nhap` từ lớp `model_nguoi_dung` để kiểm tra thông tin đăng nhập.
               2. Nếu thông tin tồn tại trong cơ sở dữ liệu, trả về `True`, ngược lại trả về `False`.
           """
        return model_nguoi_dung.kiem_tra_dang_nhap(ten_dang_nhap, mat_khau) is not None

    def xac_dinh_vai_tro(self, ten_dang_nhap, mat_khau):
        """
            Xác định vai trò của người dùng sau khi đăng nhập thành công.

            - Đầu vào:
                + ten_dang_nhap: Tên đăng nhập của người dùng.
                + mat_khau: Mật khẩu của người dùng.
            - Đầu ra:
                + Trả về chuỗi `vai_tro` nếu thông tin đăng nhập hợp lệ.
                + Trả về `None` nếu thông tin đăng nhập không tồn tại hoặc không hợp lệ.
            - Quy trình:
                1. Thực hiện truy vấn SQL để lấy vai trò người dùng từ bảng `nguoi_dung`.
                2. Nếu thông tin tồn tại, trả về giá trị `vai_tro`, ngược lại trả về `None`.
            """
        query = "SELECT vai_tro FROM nguoi_dung WHERE ten_dang_nhap = %s AND mat_khau = %s"
        result = self.db.fetch_one(query, (ten_dang_nhap, mat_khau))
        return result['vai_tro'] if result else None

