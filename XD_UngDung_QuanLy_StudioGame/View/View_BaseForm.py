import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class KhungCoSo(tk.Frame):
    """Lớp cơ sở để kế thừa"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.goc = master

    def mo_cua_so(self, tieu_de, truong_du_lieu, ham_gui):
        """Cửa sổ động với các trường linh hoạt"""
        cua_so = tk.Toplevel(self.goc)
        cua_so.title(tieu_de)

        # Căn giữa cửa sổ
        rong, cao = 400, 300
        rong_man_hinh = self.goc.winfo_screenwidth()
        cao_man_hinh = self.goc.winfo_screenheight()
        x = (rong_man_hinh // 2) - (rong // 2)
        y = (cao_man_hinh // 2) - (cao // 2)
        cua_so.geometry(f"{rong}x{cao}+{x}+{y}")

        # Tạo các trường nhập liệu
        o_nhap = {}
        do_rong = 25

        for i, (ten_truong, loai_truong, lua_chon) in enumerate(truong_du_lieu):
            tk.Label(cua_so, text=f"{ten_truong}:", anchor="e").grid(row=i, column=0, padx=10, pady=5, sticky="e")
            if loai_truong == "nhap":
                o = tk.Entry(cua_so, width=do_rong)
            elif loai_truong == "ngay":
                o = DateEntry(cua_so, date_pattern='dd/mm/yyyy', width=do_rong)
            elif loai_truong == "chon":
                o = ttk.Combobox(cua_so, values=lua_chon, width=do_rong - 2)
                o.current(0)
            else:
                o = tk.Entry(cua_so, width=do_rong)
            o.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            o_nhap[ten_truong] = o

        nut_gui = tk.Button(cua_so, text="Lưu", command=lambda: ham_gui(o_nhap))
        nut_gui.grid(row=len(truong_du_lieu), column=0, columnspan=2, pady=10)
