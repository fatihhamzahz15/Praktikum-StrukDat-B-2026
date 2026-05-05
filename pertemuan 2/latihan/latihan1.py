angka = [10,20,30,40,50]

angka.append(60)
print(angka)
angka.remove(20)
print(angka)
tertinggi = max(angka)
terendah = min(angka)

print(f'angka tertinggi = {tertinggi}')
print(f'angka terendah = {terendah}')

total = 0

for x in angka:
    print(x)
    total = total + x
rata_rata = total/5
print(rata_rata)



