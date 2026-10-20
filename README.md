
# Estadística básica

Librería pequeña en Python con funciones de estadística básica, pruebas
unitarias con `pytest` e integración continua con GitHub Actions.

Proyecto de la Sesión Práctica #7 – Continuous Integration
(CC3047 Administración y Mantenimiento de Sistemas, UVG).

## Funciones

Todas reciben una lista (o tupla) de números y están en [`estadistica.py`](estadistica.py).

| Función | Descripción | Ejemplo |
|---|---|---|
| `media(datos)` | Media aritmética | `media([1, 2, 3, 4, 5])` → `3.0` |
| `mediana(datos)` | Valor central de los datos ordenados (promedio de los dos centrales si la cantidad es par) | `mediana([4, 1, 3, 2])` → `2.5` |
| `moda(datos)` | Lista ordenada de los valores que más se repiten (puede haber varias modas) | `moda([1, 1, 2, 2, 3])` → `[1, 2]` |
| `variance(datos)` | Varianza poblacional (divide entre *n*) | `variance([2, 4, 4, 4, 5, 5, 7, 9])` → `4.0` |
| `ds(datos)` | Desviación estándar poblacional (raíz de la varianza) | `ds([2, 4, 4, 4, 5, 5, 7, 9])` → `2.0` |

### Manejo de errores

En lugar de retornar un valor arbitrario, las funciones lanzan una excepción si la entrada no es válida:

| Entrada | Excepción |
|---|---|
| No es lista ni tupla (por ejemplo `123`) | `TypeError` |
| Lista vacía | `ValueError` |
| Contiene un valor no numérico o booleano (`"2"`, `None`, `True`) | `TypeError` |
| Contiene `NaN` | `ValueError` |

## Instalación

Requiere Python 3.12 o superior.

```bash
git clone https://github.com/Gerax5/ADMIN-PR7.git
cd ADMIN-PR7
pip install -r requirements.txt
```

## Uso

```python
from estadistica import media, mediana, moda, variance, ds

datos = [2, 4, 4, 4, 5, 5, 7, 9]
media(datos)     # 5.0
mediana(datos)   # 4.5
moda(datos)      # [4]
variance(datos)  # 4.0
ds(datos)        # 2.0
```

## Pruebas

Las pruebas están en [`test_estadistica.py`](test_estadistica.py). Cada función
tiene al menos dos casos exitosos y al menos un caso de error.

```bash
pytest -v
```

## Integración continua

El workflow [`.github/workflows/tests.yml`](.github/workflows/tests.yml) corre
`pytest` en cada Pull Request hacia `main` y en cada push a `main`.

La rama `main` está protegida con un ruleset:

- Solo se puede modificar mediante Pull Request.
- El check **`tests`** debe pasar para que se habilite el merge.

Por eso, si un cambio rompe alguna función, las pruebas fallan en el PR y el merge queda bloqueado hasta que se corrija.
