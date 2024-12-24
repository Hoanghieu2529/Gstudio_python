from abc import ABC, abstractmethod
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

# Lớp trừu tượng
class dichvu_email(ABC):
    @abstractmethod
    def gui_otp(self, recipient_email, otp):
        """Phương thức trừu tượng để gửi OTP"""
        pass

    @abstractmethod
    def tao_otp(self):
        """Phương thức trừu tượng để tạo OTP"""
        pass

# Lớp triển khai cho Gmail
class dich_vu_Gmail(dichvu_email):
    def __init__(self):
        """Khởi tạo dịch vụ email với Gmail"""
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.sender_email = "panda.studio.uit@gmail.com"
        self.sender_password = "edxn ojwl rjjo fpxu"  # Mật khẩu ứng dụng Gmail

    def tao_otp(self):
        """Tạo mã OTP ngẫu nhiên gồm 6 chữ số."""
        return str(random.randint(100000, 999999))

    def gui_otp(self, recipient_email, otp):
        """Gửi email chứa mã OTP đến người nhận."""
        try:
            # Nội dung email
            subject = "Xác thực tài khoản của bạn"
            body = f"Mã OTP của bạn là: {otp}. Mã này sẽ hết hạn sau 5 phút."

            # Tạo email
            msg = MIMEMultipart()
            msg["From"] = self.sender_email
            msg["To"] = recipient_email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            # Gửi email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Khởi động mã hóa TLS
                server.login(self.sender_email, self.sender_password)  # Đăng nhập
                server.sendmail(self.sender_email, recipient_email, msg.as_string())  # Gửi email

            print("Email đã được gửi thành công!")
            return True
        except Exception as e:
            print("Lỗi khi gửi email:", e)
            return False
