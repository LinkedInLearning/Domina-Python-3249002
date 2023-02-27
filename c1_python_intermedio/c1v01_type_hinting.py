from typing import Union


def calular_perimetro_cuadrado(lado: Union[int, float]) -> Union[int, float]:
    return 4 * lado


print(calular_perimetro_cuadrado(lado=5.1))
