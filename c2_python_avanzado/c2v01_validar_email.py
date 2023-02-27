import re


def email_valido(email):

    formato_valido = r"^([a-z0-9]+[.-_])*[a-z0-9]+@[a-z0-9-]+(\.[a-z]{2,})+$"
    if re.match(formato_valido, email, re.IGNORECASE):
        return True
    return False

valido = email_valido("anaPPPP@email.edu.co")
print("Email valido:", valido)
