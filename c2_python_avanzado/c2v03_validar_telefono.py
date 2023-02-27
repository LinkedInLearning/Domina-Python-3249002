import phonenumbers


def validar_telefono(telefono_str, codigo_pais=None):
        
    try:
        telefono = phonenumbers.parse(telefono_str, codigo_pais)
        return phonenumbers.is_valid_number(telefono)
    except Exception as e:
        print("Teléfono inválido:", e)
        return False


valido = validar_telefono("3003401030")
print(valido)
