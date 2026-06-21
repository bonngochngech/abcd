name = input("Tên học sinh: ")

math = float(input("Điểm Toán: "))
literature = float(input("Điểm Văn: "))
english = float(input("Điểm Anh: "))

average = (math + literature + english) / 3

if average >= 8:
    rank = "Giỏi"
elif average >= 6.5:
    rank = "Khá"
elif average >= 5:
    rank = "Trung bình"
else:
    rank = "Yếu"

print(f"\nHọc sinh: {name}")
print(f"Điểm trung bình: {average:.2f}")
print(f"Xếp loại: {rank}")