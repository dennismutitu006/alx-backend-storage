#!/usr/bin/env python3
"""
function will return the list of schools having specific topic
"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    parameters:
        mongo_collection: the mongo collection object.
        topic: topic to be searched.
    returns:
        list of schools with the searched topic.
    """
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
