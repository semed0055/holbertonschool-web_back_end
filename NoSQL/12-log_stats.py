#!/usr/bin/env python3
"""
Module for task 12.
Provides some stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


def log_stats():
    """
    Connects to local MongoDB and prints stats about nginx logs.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Toplam log sayı
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Metodların statistikası
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Xüsusi filtr: GET metodu və /status path olanların sayı
    status_checks = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_checks} status check")


if __name__ == "__main__":
    log_stats()
