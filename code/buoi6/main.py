from ham import viTriTonTai, kiemTraTangDan, locLe

a = list(map(int, input("Nhap day so: ").split()))

# 2
if kiemTraTangDan(a):
    print("tang dan")
else:
    print("khong tang dan")
    
# 3
print(locLe(a))


