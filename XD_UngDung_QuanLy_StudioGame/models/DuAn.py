class DuAn:
    def __init__(self, duan_id: int, duan_name: str, duan_mota: str, duan_start: str, duan_end: str, duan_status: str):
        self.duan_id = duan_id
        self.duan_name = duan_name
        self.duan_mota = duan_mota
        self.duan_start = duan_start
        self.duan_end = duan_end
        self.duan_status = duan_status
        self.congviec = []
        self.thanhvien = []

    def add_congviec(self, congviec):
        self.congviec.append(congviec)

    def add_thanhvien(self, thanhvien):
        self.thanhvien.append(thanhvien)

    def tinh_tien_do(self):
        pass



