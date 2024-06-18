#!/usr/bin/env python3
""" Log stats - new version  """
from pymongo import MongoClient
from collections import Counter

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

    # Top 10 IPs
    ip_counts = Counter([log['ip'] for log in nginx_collection.find({}, {"ip": 1})])
    top_10_ips = ip_counts.most_common(10)

    # Print results
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check_count} status check")
    print("IPs:")
    for ip, count in top_10_ips:
        print(f"\t{ip}: {count}")
