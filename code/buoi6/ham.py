def viTriTonTai():
    try:
        a = list(map(int, input("Nhap day so: ").split()))
        x = int(input("Nhap x: "))
    except:
        a = [1, 4, 6, 2, 7, 8, 3]
        x = 2

    rs = []
    for i in range(len(a)):
        if a[i] == x:
            rs.append(i)
            print(f"{x}", end=" ")
            
    if x not in a:
        rs.append(-1)
        print("-1")

def kiemTraTangDan(a):
    cur = a[0]
    for x in a:
        if x < cur:
            return False
        cur = x
    return True

# su dung 1 danh sach de loc cac so le
def locLe(a):
    arr = []
    for x in a:
        if (x % 2 != 0) and (x not in arr):
            arr.append(x)
    return arr