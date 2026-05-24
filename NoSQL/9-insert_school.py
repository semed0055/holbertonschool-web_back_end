#!/usr/bin/env python3
"""
Module for task 9.
Contains a function that inserts a new document in a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.
    Returns the new _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
