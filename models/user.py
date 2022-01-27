#!/usr/bin/python3
""" module for a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """A class representation of a user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
