#!/usr/bin/env python3
""" Logs
"""

from pymongo import MongoClient

def log_stats():
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    # Total number of logs
    total_logs = nginx_collection.count_documents({})

    # Number of logs for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: nginx_collection.count_documents({"method": method}) for method in methods}

    # Number of status checks
    status_check_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})

    # Print results
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check_count} status check")
