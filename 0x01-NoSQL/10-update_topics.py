#!/usr/bin/env python3
"""  Update the topics of a school document based on the name.

    :param mongo_collection: pymongo collection object
    :param name: string, the school name to update
    :param topics: list of strings, the list of topics to set
"""

import pymongo

def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school document based on the name.

    :param mongo_collection: pymongo collection object
    :param name: string, the school name to update
    :param topics: list of strings, the list of topics to set
    """
    mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
