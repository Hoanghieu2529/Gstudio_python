import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage


class StudioForm:
    def __init__(self, master):
        self.frame = tk.Frame(master, bg="#f8f9fa")
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.root.iconphoto(False, PhotoImage(file="Images/Logo_studio.png"))

        self.studio_info = {
            "Tên Studio": "Studio A",
            "Địa chỉ": "123 Đường ABC, TP.HCM",
        }

        self.departments = ["Phòng Thiết kế", "Phòng Lập trình"]
        self.projects = ["Dự án Game A", "Dự án Game B"]

        self.create_info_section(self.frame)
        self.create_management_section(self.frame)

    def create_info_section(self, parent_frame):
        info_frame = tk.Frame(parent_frame, bg="#f8f9fa", pady=10)
        info_frame.pack(fill=tk.X)

        studio_label = tk.Label(info_frame, text="Thông tin Studio", font=("Arial", 14, "bold"), bg="#f8f9fa")
        studio_label.pack(anchor=tk.W, padx=10, pady=5)

        for key, value in self.studio_info.items():
            label = tk.Label(info_frame, text=f"{key}: {value}", font=("Arial", 12), bg="#f8f9fa")
            label.pack(anchor=tk.W, padx=20)

    def create_management_section(self, parent_frame):
        management_frame = tk.Frame(parent_frame, bg="#f8f9fa")
        management_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Tabs
        tab_control = ttk.Notebook(management_frame)

        # Departments Tab
        self.department_tab = tk.Frame(tab_control, bg="#f8f9fa")
        tab_control.add(self.department_tab, text="Phòng ban")
        self.create_department_section(self.department_tab)

        # Projects Tab
        self.project_tab = tk.Frame(tab_control, bg="#f8f9fa")
        tab_control.add(self.project_tab, text="Dự án")
        self.create_project_section(self.project_tab)

        tab_control.pack(fill=tk.BOTH, expand=True)

    def create_department_section(self, parent_frame):
        self.department_tree = ttk.Treeview(parent_frame, columns=("department"), show="headings")
        self.department_tree.heading("department", text="Phòng ban")
        self.department_tree.pack(fill=tk.BOTH, expand=True, pady=10)

        for department in self.departments:
            self.department_tree.insert("", "end", values=(department,))

        self.create_buttons(parent_frame, self.department_tree, self.departments, "phòng ban")

    def create_project_section(self, parent_frame):
        self.project_tree = ttk.Treeview(parent_frame, columns=("project"), show="headings")
        self.project_tree.heading("project", text="Dự án")
        self.project_tree.pack(fill=tk.BOTH, expand=True, pady=10)

        for project in self.projects:
            self.project_tree.insert("", "end", values=(project,))

        self.create_buttons(parent_frame, self.project_tree, self.projects, "dự án")

    def create_buttons(self, parent_frame, treeview, data_list, entity_name):
        button_frame = tk.Frame(parent_frame, bg="#f8f9fa")
        button_frame.pack(fill=tk.X, pady=5)

        add_btn = tk.Button(button_frame, text=f"Thêm {entity_name}", command=lambda: self.add_item(treeview, data_list, entity_name))
        edit_btn = tk.Button(button_frame, text=f"Sửa {entity_name}", command=lambda: self.edit_item(treeview, data_list, entity_name))
        delete_btn = tk.Button(button_frame, text=f"Xóa {entity_name}", command=lambda: self.delete_item(treeview, data_list, entity_name))

        add_btn.pack(side=tk.LEFT, padx=5)
        edit_btn.pack(side=tk.LEFT, padx=5)
        delete_btn.pack(side=tk.LEFT, padx=5)

    def add_item(self, treeview, data_list, entity_name):
        item_name = tk.simpledialog.askstring("Thêm", f"Nhập tên {entity_name} mới:")
        if item_name:
            data_list.append(item_name)
            treeview.insert("", "end", values=(item_name,))

    def edit_item(self, treeview, data_list, entity_name):
        selected_item = treeview.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", f"Vui lòng chọn một {entity_name} để sửa")
            return

        current_values = treeview.item(selected_item, "values")
        new_value = tk.simpledialog.askstring("Sửa", f"Nhập tên mới cho {entity_name}:", initialvalue=current_values[0])

        if new_value:
            index = data_list.index(current_values[0])
            data_list[index] = new_value
            treeview.item(selected_item, values=(new_value,))

    def delete_item(self, treeview, data_list, entity_name):
        selected_item = treeview.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", f"Vui lòng chọn một {entity_name} để xóa")
            return

        current_values = treeview.item(selected_item, "values")
        confirm = messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa {entity_name} '{current_values[0]}' không?")

        if confirm:
            data_list.remove(current_values[0])
            treeview.delete(selected_item)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quản lý Studio")
    root.geometry("800x600")
    app = StudioForm(root)
    root.mainloop()
