kelas_A = {"Struktur Data", "Basis Data", "AI","Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI","Cloud Computing"}

matkul_keuda_kelas = kelas_A.intersection(kelas_B) 
print(matkul_keuda_kelas)

hanya_kelas_a = kelas_A.difference(kelas_B)#matkul unik kelas a
print('matkul unik kelas a = ',hanya_kelas_a)

hanya_kelas_b = kelas_B.difference(kelas_A)#matkul unik kelas b
print('matkul unik kelas b =',hanya_kelas_b)

matkul_unik_kedua_kelas = hanya_kelas_b|hanya_kelas_a
print('matkul unik kedua kelas = ',matkul_unik_kedua_kelas)


