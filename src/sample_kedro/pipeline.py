"""
This is a boilerplate pipeline 'main'
generated using Kedro 0.18.8
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import *


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=test_step,
            inputs=None,
            outputs="test",
        )
    ])
