import math

import pytest

from estadistica import media, mediana, moda


# ---------- media ----------
class TestMedia:
    def test_enteros(self):
        assert media([1, 2, 3, 4, 5]) == 1

    def test_decimales_y_negativos(self):
        assert media([-2, 0, 2.5, 3.5]) == pytest.approx(1.0)

    def test_un_solo_dato(self):
        assert media([7]) == 7

    def test_lista_vacia(self):
        with pytest.raises(ValueError):
            media([])

    def test_valor_no_numerico(self):
        with pytest.raises(TypeError):
            media([1, "2", 3])


# ---------- mediana ----------
class TestMediana:
    def test_cantidad_impar(self):
        assert mediana([3, 1, 2]) == 2

    def test_cantidad_par(self):
        assert mediana([4, 1, 3, 2]) == 2.5

    def test_no_modifica_la_lista_original(self):
        datos = [3, 1, 2]
        mediana(datos)
        assert datos == [3, 1, 2]

    def test_lista_vacia(self):
        with pytest.raises(ValueError):
            mediana([])

    def test_entrada_no_es_lista(self):
        with pytest.raises(TypeError):
            mediana(123)


# ---------- moda ----------
class TestModa:
    def test_una_moda(self):
        assert moda([1, 2, 2, 3]) == [2]

    def test_multiples_modas(self):
        assert moda([1, 1, 2, 2, 3]) == [1, 2]

    def test_todos_distintos_son_moda(self):
        assert moda([1, 2, 3]) == [1, 2, 3]

    def test_lista_vacia(self):
        with pytest.raises(ValueError):
            moda([])

    def test_booleanos_no_validos(self):
        with pytest.raises(TypeError):
            moda([True, False, True])