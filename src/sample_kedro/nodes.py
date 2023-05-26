"""
This is a boilerplate pipeline 'main'
generated using Kedro 0.18.8
"""

import logging

from sklearn.datasets import load_iris


L = logging.getLogger(__name__)


def load_data():
    L.debug("# load_data")

    data_iris = load_iris(as_frame=True)
    df_iris = data_iris.data

    return df_iris
