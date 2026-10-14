
import pandas as pd
import matplotlib.pyplot as plt

# 1. Tạo DataFrame
data = {
    "Họ và tên": [
        "Nguyễn Văn 1", "Nguyễn Thị 2", "Trần Văn 3", "Trần Thị 4",
        "Ngô Văn 5", "Ngô Thị 6", "Bùi Văn 7", "Bùi Thị 8",
        "Lê Văn 9", "Lê Thị 10"
    ],
    "Điểm chuyên cần": [7, 8, 9, 8, 7, 9, 10, 6, 8, 9],
    "Điểm giữa kỳ": [8, 9, 9, 9, 8, 8, 10, 9, 8, 9],
    "Điểm cuối kỳ": [6, 7, 5, 8, 6, 9, 10, 6, 8, 9]
}

df = pd.DataFrame(data)
print("BẢNG ĐIỂM SINH VIÊN")
print(df)

# 2. Tính điểm tổng kết
df["Tong_ket"] = (
    0.2 * df["Điểm chuyên cần"]
    + 0.3 * df["Điểm giữa kỳ"]
    + 0.5 * df["Điểm cuối kỳ"]
)

# 3. Xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7:
        return "Kha"
    elif diem >= 5:
        return "Trung binh"
    else:
        return "Yeu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)
print("\nBẢNG ĐIỂM VÀ XẾP LOẠI")
print(df.round({"Tong_ket": 2}))

# 4. Thống kê
diem_trung_binh = df["Tong_ket"].mean()
print("\nTHỐNG KÊ")
print("Diem trung binh cua lop:", round(diem_trung_binh, 2))

sv_cao_nhat = df.loc[df["Tong_ket"].idxmax()]
print("Sinh vien cao nhat:", sv_cao_nhat["Họ và tên"])
print("Diem cao nhat:", round(sv_cao_nhat["Tong_ket"], 2))

sv_thap_nhat = df.loc[df["Tong_ket"].idxmin()]
print("Sinh vien thap nhat:", sv_thap_nhat["Họ và tên"])
print("Diem thap nhat:", round(sv_thap_nhat["Tong_ket"], 2))

so_sinh_vien_dat = (df["Tong_ket"] >= 5).sum()
print("So sinh vien dat:", int(so_sinh_vien_dat))

# 5. Vẽ biểu đồ cột
plt.figure(figsize=(12, 6))
plt.bar(df["Họ và tên"], df["Tong_ket"])
plt.title("Diem tong ket cua 10 sinh vien")
plt.xlabel("Ho va ten sinh vien")
plt.ylabel("Diem tong ket")
plt.xticks(rotation=45, ha="right")
plt.ylim(0, 10)
plt.tight_layout()
plt.show()

# Người thực hiện: Nguyễn Vũ Quốc Mạnh - STT 26
