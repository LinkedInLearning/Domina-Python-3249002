# Binarios en formato string
bin_5 = 0b101  # 5
bin_10 = 0b1010 # 10

resultado = bin_5 + bin_10

print("bin_5", bin_5)
print("bin_10", bin_10)
print("resultado", resultado)

print("resultado binario", bin(resultado))

# Binarios en formato string
bin_7 = "0b111"  # 7
bin_12 = "0b1100" # 12

resultado_string = int(bin_7, 2) + int(bin_12, 2)

print("bin_7", bin_7)
print("bin_12", bin_12)
print(resultado_string)
