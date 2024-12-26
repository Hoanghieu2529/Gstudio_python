from models.models_nguoi_dung import model_nguoi_dung
from controllers.controller_dang_ky import controller_dang_ky
from Services.dich_vu_email  import dich_vu_Gmail

# ================= KIỂM THỬ NGƯỜI DÙNG =================
def kiem_thu_them_nguoi_dung():
    """Kiểm thử thêm người dùng mới."""
    print("\nThêm người dùng mới để kiểm thử...")
    model_nguoi_dung.them_nguoi_dung("hieund", "123456", "quan tri vien")
    model_nguoi_dung.them_nguoi_dung("ducna", "abcdef", "lap trinh vien")
    print("Đã thêm người dùng thành công.")

def kiem_thu_dang_nhap():
    """Kiểm thử chức năng đăng nhập."""
    print("\nKiểm tra đăng nhập...")
    ten_dang_nhap = input("Tên đăng nhập: ")
    mat_khau = input("Mật khẩu: ")
    nguoi_dung = model_nguoi_dung.kiem_tra_dang_nhap(ten_dang_nhap, mat_khau)

    if nguoi_dung:
        print("Đăng nhập thành công!")
        print("Thông tin người dùng:", nguoi_dung)
        return nguoi_dung
    else:
        print("Tên đăng nhập hoặc mật khẩu không chính xác!")
        return None

def kiem_thu_kiem_tra_vai_tro():
    """Kiểm thử kiểm tra vai trò của người dùng."""
    print("\nKiểm tra vai trò người dùng...")
    ten_dang_nhap = input("Tên đăng nhập để kiểm tra vai trò: ")
    vai_tro = model_nguoi_dung.kiem_tra_vai_tro(ten_dang_nhap)

    if vai_tro:
        print(f"Vai trò của người dùng '{ten_dang_nhap}': {vai_tro}")
        return vai_tro
    else:
        print("Không tìm thấy vai trò của người dùng!")
        return None

# ================= KIỂM THỬ EMAIL =================
def kiem_thu_gui_otp():
    """Chức năng kiểm thử gửi OTP"""
    dich_vu = dich_vu_Gmail()

    print("\nGửi OTP kiểm thử...")
    recipient_email = input("Nhập email của bạn: ")
    otp = dich_vu.tao_otp()

    if dich_vu.gui_otp(recipient_email, otp):
        print("Mã OTP đã được gửi đến email của bạn.")

        # Nhập OTP để xác thực
        user_otp = input("Nhập mã OTP: ")
        if user_otp == otp:
            print("Xác thực thành công!")
        else:
            print("Mã OTP không chính xác.")
    else:
        print("Không thể gửi email. Vui lòng thử lại sau.")

# ================= MENU CHÍNH =================
def hien_menu_nguoi_dung():
    """Hiển thị menu kiểm thử người dùng"""
    print("\n=== MENU KIỂM THỬ NGƯỜI DÙNG ===")
    print("1. Thêm người dùng")
    print("2. Đăng nhập")
    print("3. Kiểm tra vai trò")
    print("0. Thoát")

def hien_menu_email():
    """Hiển thị menu kiểm thử email"""
    print("\n=== MENU KIỂM THỬ EMAIL ===")
    print("1. Gửi OTP")
    print("0. Thoát")

def main():
    while True:
        print("\n=== MENU CHÍNH ===")
        print("1. Kiểm thử người dùng")
        print("2. Kiểm thử email")
        print("0. Thoát")
        lua_chon = input("Nhập lựa chọn của bạn (0-2): ")

        if lua_chon == "1":
            while True:
                hien_menu_nguoi_dung()
                nguoi_dung_chon = input("Nhập lựa chọn của bạn (0-3): ")

                if nguoi_dung_chon == "1":
                    kiem_thu_them_nguoi_dung()
                elif nguoi_dung_chon == "2":
                    kiem_thu_dang_nhap()
                elif nguoi_dung_chon == "3":
                    kiem_thu_kiem_tra_vai_tro()
                elif nguoi_dung_chon == "0":
                    break
                else:
                    print("Lựa chọn không hợp lệ!")

        elif lua_chon == "2":
            while True:
                hien_menu_email()
                email_chon = input("Nhập lựa chọn của bạn (0-1): ")

                if email_chon == "1":
                    kiem_thu_gui_otp()
                elif email_chon == "0":
                    break
                else:
                    print("Lựa chọn không hợp lệ!")

        elif lua_chon == "0":
            print("Thoát chương trình kiểm thử.")
            break

        else:
            print("Lựa chọn không hợp lệ!")

def kiem_thu_dang_ky():
    controller = controller_dang_ky()
    print("Kiểm thử đăng ký:")
    if controller.xu_ly_dang_ky("testuser", "password123", "testemail@example.com"):
        print("Đăng ký thành công!")
    else:
        print("Đăng ký thất bại!")

if __name__ == "__main__":
    main()
    kiem_thu_dang_ky()
    model_nguoi_dung.them_nguoi_dung("test_user", "password123", "test_email@gmail.com", "nguoi dung")
