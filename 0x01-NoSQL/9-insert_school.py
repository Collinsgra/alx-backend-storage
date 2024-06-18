#!/usr/bin/env python3
"""  Insert a new document in a collection based on kwargs.
    
    :param mongo_collection: pymongo collection object
    :param kwargs: key-value pairs representing the document to be inserted
    :return: The new document's _id
"""

def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a collection based on kwargs.
    
    :param mongo_collection: pymongo collection object
    :param kwargs: key-value pairs representing the document to be inserted
    :return: The new document's _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
