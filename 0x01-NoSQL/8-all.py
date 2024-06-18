#!/usr/bin/env python3
""" List all documents in a collection.
    
    :param mongo_collection: pymongo collection object
    :return: List of documents in the collection or an empty list if no documents are found
"""

from pymongo import MongoClient

def list_all(mongo_collection):
    """
    List all documents in a collection.
    
    :param mongo_collection: pymongo collection object
    :return: List of documents in the collection or an empty list if no documents are found
    """
    documents = list(mongo_collection.find())
    return documents
