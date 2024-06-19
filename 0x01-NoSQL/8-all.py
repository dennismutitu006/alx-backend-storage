#!/usr/bin/env python3
"""
a function that lists all docs in a collection.
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    parameters:
    mongo_collection - collection object.
    returns:
        empty list.
    """
    doc = list(mongo_collection.find())

    return doc
