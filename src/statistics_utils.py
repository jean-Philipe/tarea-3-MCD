"""Small numerical utilities for data science workflows.

The :class:`StatisticsUtils` class provides pure numerical helpers that
do not depend on machine learning models. They are designed to be simple
enough for unit testing while still reflecting real-world needs.
"""

from typing import Sequence
import numpy as np


class StatisticsUtils:
    """Collection of basic statistical helper functions.

    Each method performs a single task, using NumPy arrays internally.
    All methods validate their inputs and raise clear exceptions when
    the arguments are invalid, so that tests can verify both normal and
    error behaviour.
    """

    def moving_average(self, arr: Sequence[float], window: int) -> np.ndarray:
        """Compute a simple moving average over a one-dimensional sequence.

        Parameters
        ----------
        arr:
            Input sequence of numbers (list, tuple or NumPy array).
        window:
            Size of the sliding window. Must be a positive integer and
            not larger than the length of ``arr``.

        Returns
        -------
        ma:
            One-dimensional NumPy array containing the moving average
            values. Its length is ``len(arr) - window + 1``.

        Raises
        ------
        ValueError
            If ``window`` is not positive or is larger than ``len(arr)``.
        """
        if window <= 0:
            raise ValueError("window must be a positive integer")

        arr = np.asarray(arr, dtype=float)
        if arr.ndim != 1:
            raise ValueError("moving_average only supports 1D sequences")

        if len(arr) < window:
            raise ValueError("window must not be larger than the array size")

        kernel = np.ones(window, dtype=float) / window
        return np.convolve(arr, kernel, mode="valid")

    def zscore(self, arr: Sequence[float]) -> np.ndarray:
        """Return the z-score of each value in a numeric sequence.

        The z-score is defined as ``(x - mean) / std``. This method uses
        the population standard deviation as computed by ``numpy.ndarray.std()``
        with the default parameters.

        Parameters
        ----------
        arr:
            Input sequence of numbers.

        Returns
        -------
        z:
            NumPy array of the same shape as the input sequence,
            containing the z-score of each element.

        Raises
        ------
        ValueError
            If the standard deviation of the input is zero, which would
            lead to a division by zero.
        """
        arr = np.asarray(arr, dtype=float)
        std = arr.std()
        if std == 0:
            raise ValueError("Standard deviation is zero; z-scores are undefined")
        mean = arr.mean()
        return (arr - mean) / std

    def min_max_scale(self, arr: Sequence[float]) -> np.ndarray:
        """Scale a numeric sequence to the [0, 1] range.

        The transformation is ``(x - min) / (max - min)``. All operations
        are done in floating point.

        Parameters
        ----------
        arr:
            Input sequence of numbers.

        Returns
        -------
        scaled:
            NumPy array with the same length as the input and all values
            between 0 and 1 inclusive.

        Raises
        ------
        ValueError
            If all values in ``arr`` are equal, making the scaling
            undefined.
        """
        arr = np.asarray(arr, dtype=float)
        min_val = arr.min()
        max_val = arr.max()
        if min_val == max_val:
            raise ValueError("All values are equal; min-max scaling is undefined")
        return (arr - min_val) / (max_val - min_val)
