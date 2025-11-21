import pandas as pd
import unittest

from src.data_cleaner import DataCleaner


def make_sample_df() -> pd.DataFrame:
    """Create a small DataFrame for testing.

    The DataFrame intentionally contains missing values, extra whitespace
    in a text column, and an obvious numeric outlier.
    """
    return pd.DataFrame(
        {
            "name": [" Alice ", "Bob", None, " Carol  "],
            "age": [25, None, 35, 120],  # 120 is a likely outlier
            "city": ["SCL", "LPZ", "SCL", "LPZ"],
        }
    )


class TestDataCleaner(unittest.TestCase):
    """Test suite for DataCleaner class."""

    def test_drop_invalid_rows_removes_rows_with_missing_values(self):
        """Test que verifica que el método drop_invalid_rows elimina correctamente las filas
        que contienen valores faltantes (NaN o None) en las columnas especificadas.
        
        Escenario esperado:
        - Crear un DataFrame con valores faltantes usando make_sample_df()
        - Llamar a drop_invalid_rows con las columnas "name" y "age"
        - Verificar que el DataFrame resultante no tiene valores faltantes en esas columnas
        - Verificar que el DataFrame resultante tiene menos filas que el original
        """

    def test_drop_invalid_rows_raises_keyerror_for_unknown_column(self):
        """Test que verifica que el método drop_invalid_rows lanza un KeyError cuando
        se llama con una columna que no existe en el DataFrame.
        
        Escenario esperado:
        - Crear un DataFrame usando make_sample_df()
        - Llamar a drop_invalid_rows con una columna que no existe (ej: "does_not_exist")
        - Verificar que se lanza un KeyError (usar self.assertRaises)
        """

    def test_trim_strings_strips_whitespace_without_changing_other_columns(self):
        """Test que verifica que el método trim_strings elimina correctamente los espacios
        en blanco al inicio y final de los valores en las columnas especificadas, sin modificar
        el DataFrame original ni las columnas no especificadas.
        
        Escenario esperado:
        - Crear un DataFrame con espacios en blanco usando make_sample_df()
        - Llamar a trim_strings con la columna "name"
        - Verificar que el DataFrame original no fue modificado (mantiene los espacios)
        - Verificar que en el DataFrame resultante los valores de "name" no tienen espacios al inicio/final
        - Verificar que las columnas no especificadas (ej: "city") permanecen sin cambios
        """

    def test_trim_strings_raises_typeerror_for_non_string_column(self):
        """Test que verifica que el método trim_strings lanza un TypeError cuando
        se llama con una columna que no es de tipo string.
        
        Escenario esperado:
        - Crear un DataFrame usando make_sample_df()
        - Llamar a trim_strings con una columna numérica (ej: "age")
        - Verificar que se lanza un TypeError (usar self.assertRaises)
        """

    def test_remove_outliers_iqr_removes_extreme_values(self):
        """Test que verifica que el método remove_outliers_iqr elimina correctamente los
        valores extremos (outliers) de una columna numérica usando el método del rango
        intercuartílico (IQR).
        
        Escenario esperado:
        - Crear un DataFrame con valores extremos usando make_sample_df() (contiene edad=120)
        - Llamar a remove_outliers_iqr con la columna "age" y factor=1.5
        - Verificar que el valor extremo (120) fue eliminado del resultado
        - Verificar que al menos uno de los valores no extremos (25 o 35) permanece en el resultado
        """

    def test_remove_outliers_iqr_raises_keyerror_for_missing_column(self):
        """Test que verifica que el método remove_outliers_iqr lanza un KeyError cuando
        se llama con una columna que no existe en el DataFrame.
        
        Escenario esperado:
        - Crear un DataFrame usando make_sample_df()
        - Llamar a remove_outliers_iqr con una columna que no existe (ej: "salary")
        - Verificar que se lanza un KeyError (usar self.assertRaises)
        """

    def test_remove_outliers_iqr_raises_typeerror_for_non_numeric_column(self):
        """Test que verifica que el método remove_outliers_iqr lanza un TypeError cuando
        se llama con una columna que no es de tipo numérico.
        
        Escenario esperado:
        - Crear un DataFrame usando make_sample_df()
        - Llamar a remove_outliers_iqr con una columna de texto (ej: "city")
        - Verificar que se lanza un TypeError (usar self.assertRaises)
        """


if __name__ == "__main__":
    unittest.main()
