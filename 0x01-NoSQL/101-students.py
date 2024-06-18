#!/usr/bin/env python3
""" Returns all students sorted by average score.
    
    :param mongo_collection: pymongo collection object
    :return: List of students sorted by average score
"""

def top_students(mongo_collection):
    """
    Returns all students sorted by average score.
    
    :param mongo_collection: pymongo collection object
    :return: List of students sorted by average score
    """
    # Calculate average score for each student and sort them
    students = mongo_collection.aggregate([
        {
            "$addFields": {
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ])
    return list(students)
