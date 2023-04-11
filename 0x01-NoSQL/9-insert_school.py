#!/usr/bin/env python3
"""function that inserts a new document in a collection based on kwargs."""


def insert_school(mongo_collection, **kwargs):
    """returns new _id."""
    return mongo_collection.insert(kwargs)
