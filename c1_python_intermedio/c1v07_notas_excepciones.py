try:
    print("Texto con formato {}".format())
except Exception as e:
    raise Exception("Ha ocurrido un error durante la ejecución")
# except Exception as e:
    # e.add_note("Ha ocurrido un error durante la ejecución")
    # print(e.__notes__)
