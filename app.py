import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

data = {
    "Họ và tên": [
        "Nguyễn Văn 1", "Nguyễn Thị 2", "Trần Văn 3",
        "Trần Thị 4", "Ngô Văn 5", "Ngô Thị 6",
        "Bùi Văn 7", "Bùi Thị 8", "Lê Văn 9", "Lê Thị 10"
    ],
    "Điểm chuyên cần": [7, 8, 9, 8, 7, 9, 10, 6, 8, 9],
    "Điểm giữa kỳ": [8, 9, 9, 9, 8, 8, 10, 9, 8, 9],
    "Điểm cuối kỳ": [6, 7, 5, 8, 6, 9, 10, 6, 8, 9]
}

df = pd.DataFrame(data)

# Tính điểm tổng kết
df["Tong_ket"] = (
    0.2 * df["Điểm chuyên cần"]
    + 0.3 * df["Điểm giữa kỳ"]
    + 0.5 * df["Điểm cuối kỳ"]
)

# Xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 1. Hiển thị bảng điểm
st.subheader("1. Bảng điểm sinh viên")
st.dataframe(df, use_container_width=True)

# 2. Thống kê
st.subheader("2. Thống kê điểm")
diem_trung_binh = df["Tong_ket"].mean()
sv_cao_nhat = df.loc[df["Tong_ket"].idxmax()]
sv_thap_nhat = df.loc[df["Tong_ket"].idxmin()]
so_sinh_vien_dat = (df["Tong_ket"] >= 5).sum()

st.metric("Điểm trung bình của lớp", round(diem_trung_binh, 2))
st.write("Sinh viên có điểm cao nhất:", sv_cao_nhat["Họ và tên"], "-", round(sv_cao_nhat["Tong_ket"], 2))
st.write("Sinh viên có điểm thấp nhất:", sv_thap_nhat["Họ và tên"], "-", round(sv_thap_nhat["Tong_ket"], 2))
st.write("Số sinh viên đạt (điểm >= 5):", int(so_sinh_vien_dat))

# 3. Tra cứu sinh viên
st.subheader("3. Tra cứu sinh viên")
ten_sv = st.selectbox("Chọn sinh viên", df["Họ và tên"])
sv = df[df["Họ và tên"] == ten_sv].iloc[0]
st.write("Điểm chuyên cần:", sv["Điểm chuyên cần"])
st.write("Điểm giữa kỳ:", sv["Điểm giữa kỳ"])
st.write("Điểm cuối kỳ:", sv["Điểm cuối kỳ"])
st.write("Điểm tổng kết:", round(sv["Tong_ket"], 2))
st.write("Xếp loại:", sv["Xep_loai"])

# 4. Biểu đồ điểm tổng kết
st.subheader("4. Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df["Họ và tên"], df["Tong_ket"])
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Họ và tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
st.pyplot(fig)

# Sửa tên và MSSV trước khi nộp
st.caption("Người thực hiện: [Tên của bạn] - MSSV: [MSSV của bạn]")
