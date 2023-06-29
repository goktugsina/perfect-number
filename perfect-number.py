print("""
Mükemmel Sayı Nedir?

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. 
Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)

""")

sayi = int(input("Bir Sayı Giriniz:"))
x = range(1,1000)
toplam = 0

for i in x:
    if (sayi % i == 0):
        toplam = toplam + i
    else:
        continue
if ((toplam - sayi)== sayi):
    print("{} Bir Mükemmel Sayıdır!".format(sayi))
else:
    print("{} Bir Mükemmel Sayı Değildir!".format(sayi))
"""

İkinci Kodlama Yöntemi


sayı = int(input("Sayı:"))

i = 1
toplam = 0
while (i < sayı):
    if (sayı % i == 0):
        toplam += i
    i += 1

if (toplam == sayı):
    print(sayı,"mükemmel bir sayıdır.")
else:
    print(sayı,"mükemmel bir sayı değildir.")
"""