from functools import reduce

tong = lambda x, y: x + y
in_ket_qua = lambda ht, diem: print(f"Ho ten: {ht}, Diem: {diem}", ht)
tong_diem = lambda ht, toan, tin: [ht, toan + tin]
doi_cho = lambda a, b: [b, a]
giai_thua = lambda n: reduce(lambda x, y: x * y, range(1, n + 1), 1)
to_hop = lambda n, k: int(giai_thua(n)/((giai_thua(k)) * giai_thua(n - k)))

def uoc(n):
    uoc_so = []
    for i in range(1, n):
        if n % i == 0:
            uoc_so.append(i)
    return uoc_so

def is_hoan_hao(n):
    sum = 0
    for i in uoc(n):
        sum += i
    if sum == n:
        return True
    return False

def average(arr: []):
    sum = 0
    for x in arr:
        sum += x;
    return sum / len(arr)
