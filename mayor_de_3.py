a = int(input("Dame el primer numero: "))
b = int(input("Dame el segundo numero: "))
c = int(input("Dame el tercer numero: "))
if a > b and a > c:
    print(f"{a} es el numero mas grande")
if b > a and b > c:
    print(f"{b} es el numero mas grande")
if c > a and c > b:
    print(f"{c} es el numero mas grande")
