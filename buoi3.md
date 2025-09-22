```python
n = int(input("nhap n: "))
dk = True
so = 0
while dk:
    so += n % 10
    print(n % 10)
    n = n // 10
    if n == 0:
        dk = False

print(so)
```
