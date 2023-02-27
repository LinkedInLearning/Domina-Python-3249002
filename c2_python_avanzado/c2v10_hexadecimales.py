# Binarios en formato string
hex_1997 = 0x7CD # 1997
hex_2023 = 0x7E7 # 2023

resultado_int = hex_2023 - hex_1997

print("hex_1997", hex_1997)
print("hex_2023", hex_2023)
print(resultado_int)

print(hex(resultado_int))

# Binarios en formato string
hex_15 = "0xf"  # 15
hex_10 = "0xa" # 10

resultado = int(hex_15, 16) + int(hex_10, 16)

print("hex_15", hex_15)
print("hex_10", hex_10)
print(resultado)
