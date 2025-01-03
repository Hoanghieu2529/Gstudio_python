from models.models_BaoCaoNhanSu import ModelBaoCaoNhanSu
from View.View_BaoCaoNhanSu import BaoCaoNhanSuForm


class ControllerBaoCaoNhanSu:
    """
        Lớp điều khiển báo cáo nhân sự, kết nối dữ liệu từ model và giao diện view.

        - Chức năng:
            + Lấy dữ liệu từ model `ModelBaoCaoNhanSu`.
            + Hiển thị dữ liệu dưới dạng biểu đồ trên giao diện `BaoCaoNhanSuForm`.
        """
    def __init__(self, root):
        """
        Khởi tạo lớp điều khiển.

        - Đầu vào:
            + root: Cửa sổ chính của ứng dụng (tk.Tk hoặc tk.Frame).
        - Đầu ra:
            + Tạo đối tượng model `ModelBaoCaoNhanSu`.
            + Tạo giao diện `BaoCaoNhanSuForm` và liên kết với controller này.
        """
        self.model = ModelBaoCaoNhanSu()
        self.view = BaoCaoNhanSuForm(root, self)

    def tai_lai_bao_cao(self):
        """
        Tải lại dữ liệu báo cáo và cập nhật giao diện.
        - Đầu vào: Không có.
        - Đầu ra:
            + Lấy dữ liệu số lượng nhân viên từ model và hiển thị dưới dạng biểu đồ treemap.
            + Lấy dữ liệu thống kê lương từ model và hiển thị dưới dạng biểu đồ lương.
        """
        so_luong_data = self.model.lay_so_luong_nhan_vien()
        self.view.hien_thi_bieu_do_treemap(so_luong_data)

        thong_ke_luong = self.model.lay_thong_ke_luong()
        self.view.hien_thi_bieu_do_luong(thong_ke_luong)
