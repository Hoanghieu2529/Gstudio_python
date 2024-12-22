from models import *
from controllers import StudioController
hethong_controller = StudioController.HeThongController()


def main():
    # Tạo Controller cho hệ thống
    hethong_controller = StudioController.HeThongController()

    # 1. Thêm dự án mới
    print("=== TẠO DỰ ÁN ===")
    duan1 = hethong_controller.tao_duan(
        ma_duan=1,
        ten_duan="Dự án Alpha",
        mota_duan="Phát triển hệ thống CRM",
        ng_batdau_duan="2024-01-01",
        ng_ketthuc_duan="2024-12-31",
        trang_thai_duan="Đang tiến hành"
    )
    print(f"Tạo thành công: {duan1.ten_duan}\n")

    # 2. Thêm phòng ban
    print("=== TẠO PHÒNG BAN ===")
    phongban1 = hethong_controller.tao_phongban(
        ma_phongban=101,
        ten_phongban="Phòng Phát Triển",
        quanly_phongban="Nguyễn Văn A"
    )
    print(f"Tạo thành công: {phongban1.ten_phongban}\n")

    phongban2 = hethong_controller.tao_phongban(
        ma_phongban=102,
        ten_phongban="Phòng Kiểm Thử",
        quanly_phongban="Trần Thị B"
    )
    print(f"Tạo thành công: {phongban2.ten_phongban}\n")

    # 3. Thêm nhân viên vào phòng ban
    print("=== THÊM NHÂN VIÊN ===")
    nhanvien1 = hethong_controller.them_nhanvien(
        phongban_id=101,
        ma_nhanvien=201,
        ten_nhanvien="Phạm Văn C",
        vaitro="Lập Trình Viên",
        email_nhanvien="phamvanc@company.com"
    )
    print(f"Nhân viên {nhanvien1._ten_nhanvien} đã được thêm vào phòng ban {phongban1.ten_phongban}.\n")

    nhanvien2 = hethong_controller.them_nhanvien(
        phongban_id=102,
        ma_nhanvien=202,
        ten_nhanvien="Lê Thị D",
        vaitro="Kiểm Thử Viên",
        email_nhanvien="lethid@company.com"
    )
    print(f"Nhân viên {nhanvien2._ten_nhanvien} đã được thêm vào phòng ban {phongban2.ten_phongban}.\n")

    # 4. Liệt kê dự án và phòng ban
    print("=== LIỆT KÊ DỰ ÁN VÀ PHÒNG BAN ===")
    print("Danh sách dự án:")
    for duan in hethong_controller.lietke_duan():
        print(f" - {duan}")

    print("\nDanh sách phòng ban:")
    for pb in hethong_controller.lietke_phongban():
        print(f" - {pb}")

    # 5. Gán công việc cho dự án
    print("\n=== GÁN CÔNG VIỆC CHO DỰ ÁN ===")
    congviec1 = CongViec(
        ma_cong_viec=301,
        ten_congviec="Xây dựng API",
        mota_congviec="Phát triển các API backend",
        cv_giaocho="Phạm Văn C",
        han_cuoi="2024-05-01"
    )
    duan1.them_congviec(congviec1)
    print(f"Đã giao công việc '{congviec1.ten_congviec}' cho dự án '{duan1.ten_duan}'.\n")

    # 6. Tính tiến độ dự án
    print("=== TIẾN ĐỘ DỰ ÁN ===")
    tiendo = duan1.tinh_tien_do()
    print(f"Tiến độ dự án '{duan1.ten_duan}': {tiendo}%\n")

    # 7. Liệt kê công việc trong dự án
    print("=== CÁC CÔNG VIỆC TRONG DỰ ÁN ===")
    print(f"Danh sách công việc trong dự án '{duan1.ten_duan}':")
    for cv in duan1.lietke_congviec():
        print(f" - {cv}")

    print("\n=== KẾT THÚC ===")


# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()
