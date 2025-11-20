"""Data cleaning utilities commonly needed in data science projects.

This module defines the :class:`DataCleaner` class, which groups simple
DataFrame transformations that are independent from any specific model.
These functions are ideal for teaching classic unit testing in a data
science context.
"""

from typing import Iterable
import pandas as pd
from pandas.api import types as pdt


class DataCleaner:
    """Utility class for common :class:`pandas.DataFrame` cleaning operations.

    The methods in this class are intentionally small and focused so they
    can be tested independently. None of them rely on a trained model or
    on external services, which makes them good candidates for unit tests.
    """

    def drop_invalid_rows(self, df: pd.DataFrame, cols: Iterable[str]) -> pd.DataFrame:
        """Return a copy of ``df`` without rows that have missing values.

        Parameters
        ----------
        df:
            Input DataFrame to clean.
        cols:
            Iterable of column names. Any row that has a missing value
            (NaN or None) in *any* of these columns will be removed.

        Returns
        -------
        cleaned_df:
            A new DataFrame with the same columns as ``df`` but with
            fewer rows if some contained missing values in the selected
            columns.

        Raises
        ------
        KeyError
            If any of the requested columns is not present in ``df``.

        Notes
        -----
        This method does not modify the input DataFrame in-place.
        """
        missing = [c for c in cols if c not in df.columns]
        if missing:
            raise KeyError(f"Columns not found in DataFrame: {missing}")

        return df.dropna(subset=list(cols))

    def trim_strings(self, df: pd.DataFrame, cols: Iterable[str]) -> pd.DataFrame:
        """Strip leading and trailing whitespace from string columns.

        Parameters
        ----------
        df:
            Input DataFrame.
        cols:
            Iterable of column names that are expected to contain text.

        Returns
        -------
        trimmed_df:
            A new DataFrame where the specified columns have their
            string values stripped using :meth:`str.strip`.

        Raises
        ------
        KeyError
            If any of the requested columns is not present in ``df``.
        TypeError
            If any requested column is not of a string dtype.

        Notes
        -----
        The original DataFrame is not modified; a copy is returned.
        """
        cols = list(cols)
        missing = [c for c in cols if c not in df.columns]
        if missing:
            raise KeyError(f"Columns not found in DataFrame: {missing}")

        non_string = [c for c in cols if not pdt.is_string_dtype(df[c])]
        if non_string:
            raise TypeError(f"Columns are not string dtype: {non_string}")

        result = df.copy()
        for c in cols:
            result[c] = result[c].str.strip()
        return result

    def remove_outliers_iqr(
        self,
        df: pd.DataFrame,
        col: str,
        factor: float = 1.5,
    ) -> pd.DataFrame:
        """Remove rows considered outliers in a numeric column using the IQR rule.

        The interquartile range (IQR) is defined as Q3 - Q1, where Q1 and Q3
        are the 25th and 75th percentiles. Values are considered outliers if
        they are below ``Q1 - factor * IQR`` or above ``Q3 + factor * IQR``.

        Parameters
        ----------
        df:
            Input DataFrame.
        col:
            Name of the numeric column on which to detect outliers.
        factor:
            Multiplier for the IQR. The traditional boxplot rule uses 1.5.

        Returns
        -------
        filtered_df:
            A new DataFrame with the same columns as ``df`` but with rows
            containing outliers in ``col`` removed.

        Raises
        ------
        KeyError
            If ``col`` is not present in ``df``.
        TypeError
            If ``col`` is not numeric.
        """
        if col not in df.columns:
            raise KeyError(f"Column '{col}' not found in DataFrame")

        if not pdt.is_numeric_dtype(df[col]):
            raise TypeError(f"Column '{col}' must be numeric to compute IQR")

        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - factor * iqr
        upper = q3 + factor * iqr

        mask = (df[col] >= lower) & (df[col] <= upper)
        return df.loc[mask].copy()
