from ctypes import c_double
# Variable
a = 10
b = 10
print(a + b)

firstName = "Ramadhan"
print(firstName)

# Tipe data
print("=============Tipe data=============")
# Integer
data_integer = 100
print("data: ", data_integer, "type: ", type(data_integer))

# String
data_string = "Kafka"
print("data: ", data_string, "type: ", type(data_string))

# Float
data_float = 10.10
print("data: ", data_float, "type: ", type(data_float))

# Boolean
data_bool = True
print("data: ", data_bool, "type: ", type(data_bool))

# bilangan kompleks
data_complex = complex(5,6)
print("data: ", data_complex, "type: ", type(data_complex))

# tipe data dari C
data_c_double = c_double(10.5)
print("data: ", data_c_double, "type: ", type(data_c_double))

# Casting tipe data
print("===============Casting tipe data==============")

# Integer
print("===Integer===")
data_int = 9
print("data = ", data_int, "type = ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)

print("Data = ", data_float, "type = ", type(data_float))
print("Data = ", data_str, "type = ", type(data_str))
print("Data = ", data_bool, "type = ", type(data_bool))

# FLOAT
print("===FLOAT===")
data_float = 9.9
print("data = ", data_float, "type = ", type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)

print("Data = ", data_int, "type = ", type(data_int))
print("Data = ", data_str, "type = ", type(data_str))
print("Data = ", data_bool, "type = ", type(data_bool))

# Bool
print("===Bool===")
data_bool = True
print("data = ", data_bool, "type = ", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)

print("Data = ", data_int, "type = ", type(data_int))
print("Data = ", data_str, "type = ", type(data_str))
print("Data = ", data_float, "type = ", type(data_float))


# String
print("===String===")
data_str = "9"
print("data = ", data_str, "type = ", type(data_str))

data_int = int(data_str)
data_bool = bool(data_str)
data_float = float(data_str)

print("Data = ", data_int, "type = ", type(data_int)) #harus string angka
print("Data = ", data_bool, "type = ", type(data_bool)) #harus string angka
print("Data = ", data_float, "type = ", type(data_float))


# Input User

data = input("Masukan data: ")
print(data)

