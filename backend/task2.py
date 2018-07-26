x = input('Masukkan array dengan tanda koma sebagai pemisah: \n ')
y = input('Pengali: ')
# mengubah string dari input user menjadi array
a = x.split(',')
# merotasi elemen array
for i in range(0, int(y)):
	a += a.pop(0)
print(a)

