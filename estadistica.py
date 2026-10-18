"""Librería de estadística básica.

Funciones: media, mediana, moda, variance y ds (desviación estándar).
Todas validan la entrada y lanzan excepciones claras en lugar de
retornar valores arbitrarios.
"""

import math
from collections import Counter


def _validar(datos):
    """Valida que `datos` sea una lista/tupla no vacía de números."""
    if not isinstance(datos, (list, tuple)):
        raise TypeError("Los datos deben ser una lista o tupla de números")
    if len(datos) == 0:
        raise ValueError("La lista de datos no puede estar vacía")
    for x in datos:
        # bool es subclase de int, pero no es un dato numérico válido aquí
        if isinstance(x, bool) or not isinstance(x, (int, float)):
            raise TypeError(f"Valor no numérico en los datos: {x!r}")
        if isinstance(x, float) and math.isnan(x):
            raise ValueError("Los datos no pueden contener NaN")



def media(datos):
    """Retorna la media aritmética de un listado de números."""
    _validar(datos)
    return sum(datos) / len(datos)


def mediana(datos):
    """Retorna la mediana de un listado de números."""
    _validar(datos)
    ordenados = sorted(datos)
    n = len(ordenados)
    medio = n // 2
    if n % 2 == 1:
        return ordenados[medio]
    return (ordenados[medio - 1] + ordenados[medio]) / 2


def moda(datos):
    """Retorna la lista (ordenada) de valores que más se repiten.

    Se retorna siempre una lista, porque puede haber más de una moda.
    """
    _validar(datos)
    conteo = Counter(datos)
    maximo = max(conteo.values())
    return sorted(valor for valor, veces in conteo.items() if veces == maximo)