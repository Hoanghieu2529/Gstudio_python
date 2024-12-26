import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class PhongBanForm:
    def __init__(self, master):
        self.frame = tk.Frame(master, bg="#f8f9fa")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.create_toolbar(self.frame)
        self.create_treeview(self.frame)

    def create_toolbar(self, parent_frame):
        toolbar = tk.Frame(parent_frame, bg="#f8f9fa")
        toolbar.pack(fill=tk.X, pady=10)

        create_btn = tk.Button(toolbar, text="Thêm mới", command=self.create_record, bg="#f8f9fa")
        read_btn = tk.Button(toolbar, text="Đọc", command=self.read_record, bg="#f8f9fa")
        update_btn = tk.Button(toolbar, text="Cập nhật", command=self.update_record, bg="#f8f9fa")
        delete_btn = tk.Button(toolbar, text="Xóa", command=self.delete_record, bg="#f8f9fa")

        create_btn.pack(side=tk.LEFT, padx=10)
        read_btn.pack(side=tk.LEFT, padx=10)
        update_btn.pack(side=tk.LEFT, padx=10)
        delete_btn.pack(side=tk.LEFT, padx=10)

    def create_treeview(self, parent_frame):
        columns_phongban = ("Số thứ tự", "Mã phòng ban", "Tên phòng ban", "Quản lý phòng ban", "Danh sách công việc")
        self.tree_phongban = ttk.Treeview(parent_frame, columns=columns_phongban, show="headings")

        for col in columns_phongban:
            self.tree_phongban.heading(col, text=col)
            self.tree_phongban.column(col, width=100)

        self.tree_phongban.pack(fill=tk.BOTH, expand=True)

        h_scroll = ttk.Scrollbar(parent_frame, orient="horizontal", command=self.tree_phongban.xview)
        self.tree_phongban.configure(xscrollcommand=h_scroll.set)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)

        self.auto_generate_stt = 1

    def create_record(self):
        form = tk.Toplevel(self.frame)
        form.title("Thêm mới phòng ban")

        labels = ["Mã phòng ban", "Tên phòng ban", "Quản lý phòng ban", "Danh sách công việc"]
        entries = self.generate_form_entries(form, labels)

        save_btn = tk.Button(form, text="Lưu", command=lambda: self.save_record(entries, form))
        save_btn.grid(row=len(labels) + 1, columnspan=2, pady=10)

    def update_record(self):
        selected_item = self.tree_phongban.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một phòng ban để cập nhật")
            return
        item = self.tree_phongban.item(selected_item)
        values = item["values"]

        form = tk.Toplevel(self.frame)
        form.title("Cập nhật thông tin phòng ban")

        labels = ["Mã phòng ban", "Tên phòng ban", "Quản lý phòng ban", "Danh sách công việc"]
        entries = self.generate_form_entries(form, labels, values)

        save_btn = tk.Button(form, text="Lưu thay đổi", command=lambda: self.save_changes(entries, selected_item, form))
        save_btn.grid(row=len(labels) + 1, columnspan=2, pady=10)

    def generate_form_entries(self, form, labels, values=None):
        entries = []
        for i, label in enumerate(labels):
            tk.Label(form, text=label).grid(row=i, column=0, padx=10, pady=5)
            if label == "Danh sách công việc":
                entry = tk.Listbox(form, selectmode="multiple")
                jobs = ["Lập trình", "Front end", "Back end", "Tester"]
                for job in jobs:
                    entry.insert(tk.END, job)
                if values:
                    selected_jobs = values[i + 1].split(", ")
                    for job in selected_jobs:
                        idx = jobs.index(job)
                        entry.select_set(idx)
            else:
                entry = tk.Entry(form)
                if values:
                    entry.insert(0, values[i + 1])
            entry.grid(row=i, column=1, padx=10, pady=5, sticky=tk.W)
            entries.append(entry)
        return entries

    def save_record(self, entries, form):
        new_record = [self.auto_generate_stt] + [self.get_entry_value(entry) for entry in entries]
        self.tree_phongban.insert("", "end", values=new_record)
        self.auto_generate_stt += 1
        form.destroy()

    def save_changes(self, entries, selected_item, form):
        new_values = [selected_item[0]] + [self.get_entry_value(entry) for entry in entries]
        self.tree_phongban.item(selected_item, values=new_values)
        form.destroy()

    def get_entry_value(self, entry):
        if isinstance(entry, tk.Listbox):
            return ", ".join(entry.get(idx) for idx in entry.curselection())
        return entry.get()

    def read_record(self):
        selected_item = self.tree_phongban.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một phòng ban để xem chi tiết")
            return
        item = self.tree_phongban.item(selected_item)
        values = item["values"]
        messagebox.showinfo("Thông tin phòng ban",
                            f"Mã phòng ban: {values[1]}\n"
                            f"Tên phòng ban: {values[2]}\n"
                            f"Quản lý phòng ban: {values[3]}\n"
                            f"Danh sách công việc: {values[4]}")

    def delete_record(self):
        selected_item = self.tree_phongban.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một phòng ban để xóa")
            return
        confirm = messagebox.askyesno("Xác nhận", "Bạn thật sự muốn xóa phòng ban này không?")
        if confirm:
            self.tree_phongban.delete(selected_item)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quản lý Phòng Ban")
    root.geometry("800x600")
    app = PhongBanForm(root)
    root.mainloop()
