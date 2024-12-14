
# **UIT-PythonProject**

Dự án của nhóm tại trường **UIT**  
**GV hướng dẫn**: Phạm Thế Sơn  
**Thành viên thực hiện**:  
- Nguyễn Duy Hiếu  
- Nguyễn Anh Đức  
- Hồ Thị Ngọc Định  

---

## **Mô tả**

Ứng dụng quản lý dự án phát triển game, hỗ trợ:
- **Quản lý các dự án game** từ ý tưởng đến phát hành.
- **Theo dõi nhân sự**, nhiệm vụ, và tài nguyên trong dự án.
- **Quản lý chi phí và doanh thu** từ từng dự án.
- **Xuất báo cáo** chi tiết về tiến độ và tài chính.

Ứng dụng được phát triển dưới dạng **Desktop Application** sử dụng mô hình **MVC (Model-View-Controller)**.

---

## **Yêu cầu chương trình**
- **Python**: >= 3.8  
- **MySQL**: >= 5.7  
- **IDE**: PyCharm  
- **Công cụ hỗ trợ**: `MySQL Workbench` hoặc `DataGrip`

---

## **Ngôn ngữ lập trình**
```plaintext
Python
```

## **Mô hình sử dụng**
```plaintext
MVC
```

---

## **Thư viện sử dụng**

### **Thư viện chính**
| Thư viện                  | Mục đích                                                        |
|---------------------------|-----------------------------------------------------------------|
| `mysql-connector-python`  | Kết nối và thao tác với cơ sở dữ liệu MySQL.                   |
| `tkinter`                 | Tạo giao diện desktop (Mặc định trong Python).                 |
| `pyqt5`                   | Tạo giao diện desktop chuyên nghiệp (Tùy chọn thay thế Tkinter). |
| `sqlalchemy`              | ORM mạnh mẽ để quản lý cơ sở dữ liệu (Tùy chọn).               |

### **Thư viện hỗ trợ**
| Thư viện                  | Mục đích                                                        |
|---------------------------|-----------------------------------------------------------------|
| `pandas`                  | Xử lý dữ liệu và tạo báo cáo.                                   |
| `matplotlib`              | Vẽ biểu đồ trực quan hóa dữ liệu.                              |
| `reportlab`               | Xuất báo cáo PDF.                                              |
| `pytest`                  | Kiểm thử tự động cho ứng dụng.                                 |
| `bcrypt`                  | Mã hóa và bảo mật mật khẩu.                                    |

---

## **Cấu trúc dự án**

```plaintext
project-name/
├── controllers/         # Xử lý logic ứng dụng (MVC Controller)
│   ├── project_controller.py
│   ├── employee_controller.py
│   ├── task_controller.py
├── models/              # Tương tác cơ sở dữ liệu (MVC Model)
│   ├── database.py
│   ├── project_model.py
│   ├── employee_model.py
│   ├── task_model.py
├── views/               # Giao diện người dùng (MVC View)
│   ├── project_view.py
│   ├── employee_view.py
│   ├── task_view.py
├── main.py              # Tập lệnh khởi động ứng dụng desktop
├── libary_requirements.txt     # Danh sách thư viện cần thiết
```

---

## **Cài đặt**
###1. Cài đặt các thư viện
```bash
pip install -r requirements.txt
```

---

## **Tính năng chính**
- **Quản lý dự án**: Hiển thị danh sách dự án, thêm mới, chỉnh sửa và xóa.
- **Quản lý nhân sự**: Phân công nhân sự cho các dự án và nhiệm vụ cụ thể.
- **Theo dõi nhiệm vụ**: Quản lý tiến độ và trạng thái nhiệm vụ.
- **Xuất báo cáo**:
  - Tạo báo cáo tài chính.
  - Biểu đồ tiến độ dự án.
  - Xuất báo cáo dạng PDF hoặc biểu đồ.
  - 
---
Theo dõi checklist:
```
https://www.notion.so/Checklist-ph-t-tri-n-d-n-153a6ca75001809fb86fe55387d2ecd9
```
```
https://tinyurl.com/Checklistpython
```
---

![Checklistpython-400](https://github.com/user-attachments/assets/1d27931d-3183-4b22-8863-29e4c8e244f6)

---

## **Liên hệ**
- **Tác giả**: 
  - Nguyễn Duy Hiếu:  23210111@ms.uit.edu.vn 
  - Nguyễn Anh Đức:   23210102@ms.uit.edu.vn  
  - Hồ Thị Ngọc Định: 23210099@ms.uit.edu.vn 
