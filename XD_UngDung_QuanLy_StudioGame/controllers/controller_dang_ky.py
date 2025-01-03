from models.models_nguoi_dung import model_nguoi_dung
from Scrips.dich_vu_email import dich_vu_Gmail
import random

class controller_dang_ky:
    """
        Lớp điều khiển đăng ký người dùng, xử lý các tác vụ liên quan đến:
        - Gửi mã OTP qua email để xác thực.
        - Lưu thông tin người dùng mới vào cơ sở dữ liệu.
        """
    def __init__(self):
        """
           Khởi tạo lớp điều khiển đăng ký.
           - Đầu ra:
               + Tạo đối tượng `dich_vu_Gmail` để gửi email.
           """
        self.email_service = dich_vu_Gmail()

    def gui_otp_gui(self, email):
        """
        Gửi mã OTP qua email để xác thực.

        - Đầu vào:
            + email: Địa chỉ email của người dùng cần xác thực.
        - Đầu ra:
            + Trả về mã OTP nếu gửi thành công.
            + Trả về `None` nếu xảy ra lỗi hoặc gửi thất bại.
        - Quy trình:
            1. Tạo mã OTP bằng phương thức `tao_otp` của dịch vụ email.
            2. Gửi mã OTP tới email người dùng.
            3. Trả về mã OTP nếu gửi thành công, ngược lại trả về `None`.
        """
        try:
            otp = self.email_service.tao_otp()  # Tạo OTP
            if self.email_service.gui_otp(email, otp):  # Gửi OTP
                return otp  # Trả về OTP nếu gửi thành công
            return None
        except Exception as e:
            print(f"Lỗi khi gửi OTP: {e}")
            return None

    def xu_ly_dang_ky(self, ten_dang_nhap, mat_khau, email, vai_tro="nguoi dung"):
        """
        Xử lý logic đăng ký người dùng mới.
        - Đầu vào:
            + ten_dang_nhap: Tên đăng nhập của người dùng.
            + mat_khau: Mật khẩu của người dùng.
            + email: Địa chỉ email của người dùng.
            + vai_tro: Vai trò của người dùng (mặc định là "nguoi dung").
        - Đầu ra:
            + Trả về `True` nếu đăng ký thành công.
            + Trả về `False` nếu xảy ra lỗi hoặc gửi email thất bại.
        - Quy trình:
            1. Tạo mã OTP ngẫu nhiên.
            2. Gửi mã OTP đến email người dùng qua dịch vụ email.
            3. Nếu gửi thành công, lưu thông tin người dùng (bao gồm tên đăng nhập, mật khẩu, email, và vai trò) vào cơ sở dữ liệu.
        """
        try:
            # Sinh mã OTP ngẫu nhiên
            otp = str(random.randint(100000, 999999))

            # Gửi email xác thực
            if not self.email_service.gui_otp(email, otp):
                print("Không thể gửi email xác thực.")
                return False

            # Lưu thông tin người dùng vào cơ sở dữ liệu
            return model_nguoi_dung.them_nguoi_dung(ten_dang_nhap, mat_khau, email, vai_tro)
        except Exception as e:
            print(f"Lỗi khi xử lý đăng ký: {e}")
            return False
