# NT101 — An toàn mạng máy tính

**Nhóm 16 · NT101.R11.2 · UIT**
- Hà Nguyễn Hiếu An — 24520043
- Nguyễn Hữu Nghĩa — 24521144

## Lab 1 — Mật mã học cổ điển

| Task | Nội dung | Notebook |
|---|---|---|
| 2.1 | Caesar | [Lab1_Task2.1.ipynb](Lab1/Lab1_Task2.1.ipynb) |
| 2.2 | Phân tích tần suất thay thế đơn bảng | [Lab1_Task2.2.ipynb](Lab1/Lab1_Task2.2.ipynb) |
| 2.3 | Tự động phá mã thay thế đơn bảng | [Lab1_Task2.3.ipynb](Lab1/Lab1_Task2.3.ipynb) |
| 2.4 | Playfair | [Lab1_Task2.4.ipynb](Lab1/Lab1_Task2.4.ipynb) |
| 2.5 | Vigenère | [Lab1_Task2.5.ipynb](Lab1/Lab1_Task2.5.ipynb) |
| 2.6 | Thám mã Vigenère | [Lab1_Task2.6.ipynb](Lab1/Lab1_Task2.6.ipynb) |
| 2.7 | Affine | [Lab1_Task2.7.ipynb](Lab1/Lab1_Task2.7.ipynb) |

## Lab 2 — Mật mã học hiện đại

| Task | Nội dung | Notebook |
|---|---|---|
| 2.1 | Cấu trúc Feistel và sự lan truyền thay đổi | [Lab2_Task2.1.ipynb](Lab2/Lab2_Task2.1.ipynb) |
| 2.2 | Các chế độ hoạt động của AES | [Lab2_Task2.2.ipynb](Lab2/Lab2_Task2.2.ipynb) |

Hai notebook độc lập, có lý thuyết, ví dụ, nhận xét, nhập liệu tùy chọn và kiểm thử. Hướng dẫn: [Lab 2](Lab2/README.md). Cài thư viện từ thư mục gốc:

```powershell
python -m pip install -r "Lab2/requirements.txt"
```

Lab2 dùng Python 3.10 trở lên; chọn kernel đã cài PyCryptodome rồi **Run All**. Nhập liệu mặc định tắt, không cần file dữ liệu hay mạng khi chạy. Khóa/IV/nonce cố định chỉ dùng thí nghiệm, không dùng cho dữ liệu thực tế.

## Lab 3 — Hàm băm và chữ ký số

| Task | Nội dung | Notebook |
|---|---|---|
| 2.1 | RSA: sinh khóa, mã hóa/giải mã số và chuỗi, Base64, giải bốn bản mã đề | [Lab3_Task2.1.ipynb](Lab3/Lab3_Task2.1.ipynb) |
| 2.2 | Đặc tính hàm băm: va chạm MD5 trên thông điệp và chương trình, SHA-1 trên hai PDF | [Lab3_Task2.2.ipynb](Lab3/Lab3_Task2.2.ipynb) |
| 2.4 | Xác minh chữ ký chứng chỉ X.509 bằng RSA | [Lab3_Task2.4.ipynb](Lab3/Lab3_Task2.4.ipynb) |

Task 2.1 dùng thư viện chuẩn Python 3.10 trở lên; nhập liệu mặc định tắt. Task 2.2 kèm dữ liệu mẫu và kết quả đã chạy; phần xem PDF cần `pypdfium2` và `Pillow`. Hướng dẫn và quy ước dữ liệu: [Lab 3](Lab3/README.md).

## Chạy notebook

Cần Python 3 và VS Code Python/Jupyter hoặc JupyterLab:

```powershell
python -m pip install jupyter ipykernel
```

Mở notebook, chọn kernel Python 3 và chạy các cell từ trên xuống. Riêng Task 2.2 của Lab1 chạy từ thư mục `Lab1`; giữ `cipher2.2.txt` và `task2_3_data/` để chạy offline. Một số cell Lab1 chờ nhập liệu; Lab2 mặc định tắt nhập liệu.

Chi tiết: [Hướng dẫn Lab 1](Lab1/Lab1_README.md), [Hướng dẫn Lab 2](Lab2/README.md). Repo lưu notebook, hướng dẫn, thư viện yêu cầu, dữ liệu cần thiết và cấu hình Git; báo cáo nộp riêng. Các mật mã cổ điển và cấu hình thí nghiệm chỉ phục vụ học tập, không dùng bảo vệ dữ liệu thực tế.
