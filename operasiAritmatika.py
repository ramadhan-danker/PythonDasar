# a = 10
# b = 10
# c = 10
# d = 2
# # tambah
# hasil = a + b
# print(a, '+', b, 'hasil = ', hasil)
# # pengurangan
# hasil = a - b
# print(a, '-', b, 'hasil = ', hasil)
# # perkalian
# hasil = a * b
# print(a, '*', b, 'hasil = ', hasil)
# # pembagian
# hasil = c / d
# print(a, '/', b, 'hasil = ', hasil)
# # eksponen
# hasil = 10 ** 3
# print(hasil)
# # modulus
# hasil = 10 % 3
# print(hasil)
# # floor divison
# hasil = 20 // 3
# print(hasil)

# prioritas operasi , operational precedence
"""
    1. ()ch
    2. exponen **
    3. perkalian dan teman-teman * / ** % //
    4. pertambahan / pengurangan

"""

# print("PROGRAM KONVERSI TEMPERATUR")
#
# # celsius
# celsius = float(input("Masukkan temperatur suhu = "))
# print("Celseius = ", celsius)
#
# # reamur
# reamur = (4/5) * celsius
# print("Reamur = ", reamur)
#
# # fahrenheit
# fahrenheit = ((9/5) * celsius) + 32
# print("Fahreinheit = ", fahrenheit)
#
# # kelvin
# kelvin = celsius + 273
# print("Kelvin = ", kelvin)

# OPERASI KOMPARASI

x = 5
y = 5
print(hex(id(x)))
print(hex(id(y)))
hasil = y is x
print(hasil)

x = 5
y = 4
print(hex(id(x)))
print(hex(id(y)))
hasil = y is not x
print(hasil)

a = 9
b = 5
#  Bitwise OR (|)
c = a | b
print("===OR===")
print("nilai : ", a, 'binary :', format(a, '08b'))
print("nilai : ", b, 'binary :', format(b, '08b'))
print("=============================== (|)")

print("nilai : ", c, 'binary :', format(c, '08b'))

#  Bitwise AND (&)
c = a & b
print("===AND===")
print("nilai : ", a, 'binary :', format(a, '08b'))
print("nilai : ", b, 'binary :', format(b, '08b'))
print("=============================== (&)")

print("nilai : ", c, 'binary :', format(c, '08b'))

#  Bitwise XOR (^)
c = a ^ b
print("===XOR===")
print("nilai : ", a, 'binary :', format(a, '08b'))
print("nilai : ", b, 'binary :', format(b, '08b'))
print("=============================== (^)")

print("nilai : ", c, 'binary :', format(c, '08b'))

#  Bitwise NOT (~)
c = ~a
print("===XOR===")
print("nilai : ", a, 'binary :', format(a, '08b'))
print("nilai : ", b, 'binary :', format(b, '08b'))
print("=============================== (~)")

d = 0b000001001
e = 0b111111111

print("nilai : ", c, 'binary :', format(c, '08b'))
print('nilai : ', a ^ b, 'binary: ', format(e ^ d, '08b'))

# shifting

# shift right
print("===Shift right===")
c = a >> 1
print("nilai : ", c, 'binary :', format(c, '08b'))

# shift left
print("===Shift right===")
c = a << 1
print("nilai : ", c, 'binary :', format(c, '08b'))

# operator assignment
a = 1
a += 10
print("nilai", a)

