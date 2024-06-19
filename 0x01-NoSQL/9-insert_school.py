#!/usr/bin/env python3
"""
function inserts a new doc in a collection based on kwargs.
"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    parameters:
        mongo_collection: collection object that will contain the result.
        **kwargs: the keyword arguments rep the field value in doc
    returns:
        new _id of the inserted doc.
    """
    res = mongo_collection.insert_one(kwargs)

    return res.inserted_id
