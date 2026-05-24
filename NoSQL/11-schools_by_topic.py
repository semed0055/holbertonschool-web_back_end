#!/usr/bin/env python3
"""
Module for task 11.
Contains a function that returns the list of schools having a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools (documents) that contain a specific topic
    in their topics list.
    """
    if mongo_collection is None:
        return []

    return list(mongo_collection.find({"topics": topic}))
