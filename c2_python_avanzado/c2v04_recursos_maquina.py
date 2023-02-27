import psutil


def recursos_usados():

    nucleos = psutil.cpu_count(logical=False)
    print("Cantidad de núcleos:", nucleos)

    carga = psutil.getloadavg()
    print("Carga promedio:", carga)

    uso = psutil.cpu_percent(interval=5, percpu=True)
    print("Porcentaje de uso de la CPU:", uso)


recursos_usados()
