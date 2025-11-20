import numpy as np
import pytest

from src.statistics_utils import StatisticsUtils


def test_moving_average_basic_case():
    """Test que verifica que el método moving_average calcula correctamente la media móvil
    de una secuencia numérica para un caso básico.
    
    Escenario esperado:
    - Crear una lista de números (ej: [1, 2, 3, 4])
    - Llamar a moving_average con window=2
    - Verificar que el resultado es correcto (ej: [1.5, 2.5, 3.5] para el array dado)
    - Verificar que el resultado tiene la forma (shape) esperada
    """


def test_moving_average_raises_for_invalid_window():
    """Test que verifica que el método moving_average lanza un ValueError cuando
    se proporciona una ventana (window) inválida.
    
    Escenario esperado:
    - Crear una lista de números (ej: [1, 2, 3])
    - Intentar llamar a moving_average con window=0 (valor no positivo)
    - Verificar que se lanza un ValueError
    - Intentar llamar a moving_average con window mayor que la longitud del array
    - Verificar que se lanza un ValueError
    """


def test_moving_average_only_accepts_1d_sequences():
    """Test que verifica que el método moving_average lanza un ValueError cuando
    se intenta calcular la media móvil sobre una secuencia multidimensional.
    
    Escenario esperado:
    - Crear una secuencia bidimensional (ej: [[1, 2], [3, 4]])
    - Intentar llamar a moving_average con esa secuencia
    - Verificar que se lanza un ValueError indicando que solo se aceptan secuencias 1D
    """


def test_zscore_has_mean_zero_and_unit_std():
    """Test que verifica que el método zscore calcula correctamente los z-scores
    de una secuencia numérica, comprobando que el resultado tiene media cero y
    desviación estándar unitaria.
    
    Escenario esperado:
    - Crear una lista de números (ej: [10, 20, 30, 40])
    - Llamar a zscore para obtener los z-scores
    - Verificar que la media del resultado es aproximadamente 0
    - Verificar que la desviación estándar del resultado es aproximadamente 1
    """


def test_zscore_raises_for_zero_std():
    """Test que verifica que el método zscore lanza un ValueError cuando
    se intenta calcular z-scores de una secuencia con desviación estándar cero
    (todos los valores son iguales).
    
    Escenario esperado:
    - Crear una lista con todos los valores iguales (ej: [5, 5, 5])
    - Intentar llamar a zscore con esa secuencia
    - Verificar que se lanza un ValueError indicando que la desviación estándar es cero
    """


def test_min_max_scale_maps_to_zero_one_range():
    """Test que verifica que el método min_max_scale escala correctamente una secuencia
    numérica al rango [0, 1], donde el valor mínimo se mapea a 0 y el máximo a 1.
    
    Escenario esperado:
    - Crear una lista de números (ej: [2, 4, 6])
    - Llamar a min_max_scale para obtener los valores escalados
    - Verificar que el valor mínimo del resultado es 0.0
    - Verificar que el valor máximo del resultado es 1.0
    - Verificar que los valores transformados son correctos (ej: [0.0, 0.5, 1.0] para [2, 4, 6])
    """


def test_min_max_scale_raises_for_constant_values():
    """Test que verifica que el método min_max_scale lanza un ValueError cuando
    se intenta escalar una secuencia donde todos los valores son iguales (no hay variación).
    
    Escenario esperado:
    - Crear una lista con todos los valores iguales (ej: [3, 3, 3])
    - Intentar llamar a min_max_scale con esa secuencia
    - Verificar que se lanza un ValueError indicando que todos los valores son iguales
    """
