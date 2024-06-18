#!/usr/bin/env python3
"""    Return the list of schools having a specific topic.
    
    :param mongo_collection: pymongo collection object
    :param topic: string, topic searched
    :return: List of school documents having the specific topic
"""

import pymongo

def schools_by_topic(mongo_collection, topic):
    """
    Return the list of schools having a specific topic.
    
    :param mongo_collection: pymongo collection object
    :param topic: string, topic searched
    :return: List of school documents having the specific topic
    """
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
