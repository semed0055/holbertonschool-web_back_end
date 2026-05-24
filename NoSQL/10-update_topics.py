#!/usr/bin/env python3
"""
Module for task 10.
Contains a function that updates all topics of a school document based on the name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.
    Updates multiple documents if they match the name criteria.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
