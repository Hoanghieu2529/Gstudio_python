from models.models_nguoi_dung import model_nguoi_dung
from Scrips.dich_vu_email import dich_vu_Gmail
import random

class controller_dang_ky:
    def __init__(self):
        self.email_service = dich_vu_Gmail()

    def gui_otp_gui(self, email):
        """Gửi OTP qua email và trả về mã OTP nếu thành công."""
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
        Xử lý logic đăng ký người dùng:
        1. Tạo mã OTP.
        2. Gửi email xác thực.
        3. Lưu thông tin người dùng vào cơ sở dữ liệu.
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
