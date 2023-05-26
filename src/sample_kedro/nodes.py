"""
This is a boilerplate pipeline 'main'
generated using Kedro 0.18.8
"""

import logging


L = logging.getLogger(__name__)


def test_step():
    L.debug("test_step")
    return "test"
