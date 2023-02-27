print("Función print con cadena de texto")

variable = 1
print(f"Concatenando variables {variable}")

print("elementos", "separados")

print("elementos", "separados", "con", "sep", sep=",")

print("Primero", end=". ")
print("Segundo")


with open("print_ejemplo.txt", mode="w") as archivo:
    print("Hello World!", file=archivo)


import time


print("Inicio", flush=False)
time.sleep(2)
print("Fin")


print("Inicio", end="...", flush=True)
time.sleep(2)
print("Fin")
