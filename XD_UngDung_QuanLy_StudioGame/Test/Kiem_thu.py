from models.models_nguoi_dung import model_nguoi_dung

def kiem_thu_them_nguoi_dung():
    """Kiểm thử thêm người dùng mới."""
    print("Thêm người dùng mới để kiểm thử...")
    model_nguoi_dung.them_nguoi_dung("hieund", "123456", "quan tri vien")
    model_nguoi_dung.them_nguoi_dung("ducna", "abcdef", "lap trinh vien")
    print("Đã thêm người dùng thành công.")


def kiem_thu_dang_nhap():
    """Kiểm thử chức năng đăng nhập."""
    print("Kiểm tra đăng nhập...")
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
    ten_dang_nhap = input("Tên đăng nhập để kiểm tra vai trò: ")
    print("Kiểm tra vai trò người dùng...")
    vai_tro = model_nguoi_dung.kiem_tra_vai_tro(ten_dang_nhap)

    if vai_tro:
        print(f"Vai trò của người dùng '{ten_dang_nhap}': {vai_tro}")
        return vai_tro
    else:
        print("Không tìm thấy vai trò của người dùng!")
        return None


if __name__ == "__main__":
    print("Chọn chế độ kiểm thử:")
    print("1. Kiểm thử thêm người dùng")
    print("2. Kiểm thử đăng nhập")
    print("3. Kiểm thử kiểm tra vai trò")

    lua_chon = input("Nhập lựa chọn của bạn (1-3): ")

    if lua_chon == "1":
        kiem_thu_them_nguoi_dung()
    elif lua_chon == "2":
        nguoi_dung = kiem_thu_dang_nhap()
        if nguoi_dung:
            print(f"Người dùng '{nguoi_dung['ten_dang_nhap']}' đã đăng nhập thành công.")
    elif lua_chon == "3":
        kiem_thu_kiem_tra_vai_tro()
    else:
        print("Lựa chọn không hợp lệ!")
