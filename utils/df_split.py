import numpy as np
import pandas as pd

def split(array, n=None, field=None, filter_list=None):
    """
    Plan for how it should work
    1.) pass in an array and if n is not None break into n parts
    2.) pass in an array and if filter_dict is not None break into each filter chunk
        --> is there a use case for having multiple dict entries? i dont think so.
    """

    if n is not None:
        parts = np.array_split(array, n)

    if field and filter_list is not None:
        parts = list()

        for f in filter_list:
            part = array.loc[array[field].isin([f])]
            parts.append(part)

    return parts