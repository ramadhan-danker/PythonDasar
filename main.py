# from ctypes import c_double
# # Variable
# a = 10
# b = 10
# print(a + b)
#
# firstName = "Ramadhan"
# print(firstName)
#
# # Tipe data
# print("=============Tipe data=============")
# # Integer
# data_integer = 100
# print("data: ", data_integer, "type: ", type(data_integer))
#
# # String
# data_string = "Kafka"
# print("data: ", data_string, "type: ", type(data_string))
#
# # Float
# data_float = 10.10
# print("data: ", data_float, "type: ", type(data_float))
#
# # Boolean
# data_bool = True
# print("data: ", data_bool, "type: ", type(data_bool))
#
# # bilangan kompleks
# data_complex = complex(5,6)
# print("data: ", data_complex, "type: ", type(data_complex))
#
# # tipe data dari C
# data_c_double = c_double(10.5)
# print("data: ", data_c_double, "type: ", type(data_c_double))
#
# # Casting tipe data
# print("===============Casting tipe data==============")
#
# # Integer
# print("===Integer===")
# data_int = 9
# print("data = ", data_int, "type = ", type(data_int))
#
# data_float = float(data_int)
# data_str = str(data_int)
# data_bool = bool(data_int)
#
# print("Data = ", data_float, "type = ", type(data_float))
# print("Data = ", data_str, "type = ", type(data_str))
# print("Data = ", data_bool, "type = ", type(data_bool))
#
# # FLOAT
# print("===FLOAT===")
# data_float = 9.9
# print("data = ", data_float, "type = ", type(data_float))
#
# data_int = int(data_float)
# data_str = str(data_float)
# data_bool = bool(data_float)
#
# print("Data = ", data_int, "type = ", type(data_int))
# print("Data = ", data_str, "type = ", type(data_str))
# print("Data = ", data_bool, "type = ", type(data_bool))
#
# # Bool
# print("===Bool===")
# data_bool = True
# print("data = ", data_bool, "type = ", type(data_bool))
#
# data_int = int(data_bool)
# data_str = str(data_bool)
# data_float = float(data_bool)
#
# print("Data = ", data_int, "type = ", type(data_int))
# print("Data = ", data_str, "type = ", type(data_str))
# print("Data = ", data_float, "type = ", type(data_float))
#
#
# # String
# print("===String===")
# data_str = "9"
# print("data = ", data_str, "type = ", type(data_str))
#
# data_int = int(data_str)
# data_bool = bool(data_str)
# data_float = float(data_str)
#
# print("Data = ", data_int, "type = ", type(data_int)) #harus string angka
# print("Data = ", data_bool, "type = ", type(data_bool)) #harus string angka
# print("Data = ", data_float, "type = ", type(data_float))
#
#
# # Input User
#
# data = input("Masukan data: ")
# print(data, "type", type(data))
#
# # casting input
# data_int = int(input("Masukkan angka: "))
# print("data = ", data_int, "type : ", type(data_int))
#
# biner = bool(int(input("Masukkan nilai boolean : ")))
#
# print("data = ", biner, "type = ", type(biner))

# XOR
# print("====XOR====")
# a = True
# b = False
# c = a ^ b
# print(c)

# # String method
# course = "ramadhan danker"
# length = len(course)
# print(course.title())
# print(course.capitalize())
# print(course.upper())
# print(course.lower())
# print(length)
# language = "danker"
# print(course.replace("danker", "Danker123"))
# print(language in course)

# firstName = "Ramadhan"
# lastName = "Danker"
# fullName = firstName + ' ' + lastName
# print(fullName)
#
# print(firstName not in lastName)
#
# # mengulang string
# print("wk" * 10)
#
# # indexing
# print("index ke 0 : " + firstName[0])
# print("index ke 1 : " + firstName[1])
# print("index ke 1 : " + firstName[-3])
# print("index ke 0-5 : " + firstName[0:10:2])
#
# # item paling kecil
# print(max(firstName))
#
# ascii_code = ord(" ")
# print("Ascii " + str(ascii_code))

# width and multiline

# Data
# data_nama = 'Ramadhan'
# data_umur = 18
# data_tinggi = 167.1
# data_nomor_sepatu = 37
#
# # string
# data_string = f"nama = {data_nama}, umur {data_umur}, tinggi {data_tinggi} , sepatu {data_nomor_sepatu}"
# print(5*"="+"Data String"+5*"=")
# print(data_string)
#
# # string multilane (\n)
# data_string = f"nama = {data_nama}, \numur {data_umur}, \ntinggi {data_tinggi} , \nsepatu {data_nomor_sepatu}"
# print("\n"+5*"="+"Data String"+5*"=")
# print(data_string)
#
# # String multiLine (kutip triplets)
#
#
#
# # mengatur lebar
# data_string = f"""
# nama     = {data_nama:>5}
# umur     = {data_umur:>5}
# tinggi   = {data_tinggi:>5}
# noSepatu = {data_nomor_sepatu:>5}
# """
# print("\n"+5*"="+"Data String"+5*"=")
# print(data_string)

# IF ELSE IFELSE

# name = input('Masukkan nama anda =')
#
# if name == "kafka":
#     print("mommy?")
# elif name == "azusa":
#     print("GYATTT")
# else:
#     print("Terserah")
#
# print(f"Terimakasih {name}")

# print(10*"=")
# print("Kalkulator")
# print(10*"=" + "\n")
#
# angka_1 = float(input("Masukkan angka 1 = "))
# operator = input("Masukkan operator (+,-,x,/) = ")
# angka_2 = float(input("Masukkan angka 2 = "))
#
# if operator == "+":
#     hasil = angka_1 + angka_2
#     print(hasil)
# elif operator == "-":
#     hasil = angka_1 - angka_2
#     print(hasil)
# elif operator == "*" or operator == "x":
#     hasil = angka_1 * angka_2
#     print(hasil)
# elif operator == "/":
#     hasil = angka_1 / angka_2
#     print(hasil)
# else:
#     print("Operator luh salah bang")
# print('selesai')

# Perulangan FOR
# a = "Kafka"
# for i in a:
#    print(i)
#
# b = ['apple', 'orange', 'watermelon']
# for i in b:
#     print(i)

# Perulangan While


