import os


def hacer_ping(hostname):

    respuesta = os.system(f"ping -c 1 {hostname}")
    if respuesta == 0:
        print (hostname, "está activo.")
    else:
        print (hostname, "está caído.")


hacer_ping("google.com")
