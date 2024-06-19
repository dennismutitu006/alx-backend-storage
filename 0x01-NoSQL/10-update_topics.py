#!/usr/bin/env python3
"""
function will change all topics of a school doc based on the name.
"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    parameters:
        mongo_collection: the collection object in pymongo.
        name: a str that will be the name to update.
        topics: list of topics approched in the school.
    returns:
        updated doc based on the name.
    """
    res = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
        )
    return res
