angka = int(input("masukkan nilai"))
if angka <0 :
    index = "nilai tidak valid"
elif angka >= 90:
    index =("A")
elif angka >= 80:
    index =("B")
elif angka >= 70: 
    index =("C")
elif angka >= 60:
    index =("D")
elif angka >= 40:
    index =("E")
elif angka < 40:
    index =("F")


print("nilai", angka, "=", index)

n = int(input("masukkan n"))
if n%3 == 0:
    print("ping")
if n%5 == 0:
    print("pong")

