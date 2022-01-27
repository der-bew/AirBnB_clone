#!/usr/bin/python3
""" module for State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """A class representation of state """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
